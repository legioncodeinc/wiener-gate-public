#!/usr/bin/env python3
"""Transform the repository's wiki/ folder into a GitHub wiki checkout.

The wiki/ folder is authored as ordinary repository markdown: pages link to each
other with relative `.md` paths and reach outside the folder with `../`. A GitHub
wiki is a flat namespace of pages with no `.md` suffix and no notion of the
repository tree, so every link has to be rewritten on the way in.

Rules applied here:
  * wiki/index.md becomes Home.md, the wiki landing page.
  * A link to a sibling wiki page loses its `.md` suffix and keeps its anchor.
  * A link that escapes wiki/ becomes an absolute URL into the repository at the
    commit being published, so it resolves for a reader who is inside the wiki.
  * _Sidebar.md and _Footer.md are generated, never authored by hand.

Usage: build_wiki.py <source-wiki-dir> <output-dir>
Environment: GITHUB_REPOSITORY, GITHUB_SHA, WIKI_SOURCE_REF (optional, default main)
"""

from __future__ import annotations

import os
import posixpath
import re
import shutil
import sys
from pathlib import Path

# Sidebar order. Pages not listed here are appended alphabetically, so adding a
# page to wiki/ never silently drops it out of the navigation.
SIDEBAR_ORDER = [
    "Home",
    "who-is-not-a-suspect",
    "network-at-a-glance",
    "domain-roster",
    "indicators",
    "verify-our-work",
    "methodology",
    "glossary",
    "changelog",
]

LINK_RE = re.compile(r"\]\(\s*(<[^>]*>|[^)\s]+)((?:\s+\"[^\"]*\")?)\s*\)")
EXTERNAL_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")
HEADING_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)


# Written by this script, so a source page may not claim either name.
GENERATED_PAGES = frozenset({"_Sidebar", "_Footer"})


def page_slug(stem: str) -> str:
    """Map a source filename stem to its wiki page name."""
    return "Home" if stem == "index" else stem


def rewrite_target(target: str, pages: set[str], blob_base: str, tree_base: str) -> str:
    """Rewrite a single markdown link target for the wiki namespace."""
    if not target or target.startswith("#") or EXTERNAL_RE.match(target):
        return target

    path, sep, anchor = target.partition("#")
    if not path:
        return target

    is_dir = path.endswith("/")
    # Resolve against wiki/, then clamp anything that climbed above the
    # repository root back down to the root. wiki/changelog.md carries a
    # `../../../../SECURITY.md` link that would otherwise resolve nowhere.
    resolved = posixpath.normpath(posixpath.join("wiki", path))
    while resolved.startswith("../"):
        resolved = resolved[3:]
    if resolved in (".", ".."):
        resolved = ""

    if resolved.startswith("wiki/"):
        inner = resolved[len("wiki/") :]
        if inner.endswith(".md") and "/" not in inner:
            slug = page_slug(inner[: -len(".md")])
            if slug in pages:
                return f"{slug}{sep}{anchor}" if sep else slug
        base = tree_base if is_dir else blob_base
        return f"{base}/{resolved}{'/' if is_dir else ''}{sep}{anchor}"

    base = tree_base if is_dir else blob_base
    return f"{base}/{resolved}{'/' if is_dir else ''}{sep}{anchor}"


def rewrite_links(text: str, pages: set[str], blob_base: str, tree_base: str) -> str:
    def replace(match: re.Match[str]) -> str:
        raw, title = match.group(1), match.group(2)
        bracketed = raw.startswith("<") and raw.endswith(">")
        target = raw[1:-1] if bracketed else raw
        new_target = rewrite_target(target, pages, blob_base, tree_base)
        if bracketed or " " in new_target:
            new_target = f"<{new_target}>"
        return f"]({new_target}{title})"

    return LINK_RE.sub(replace, text)


def page_title(text: str, fallback: str) -> str:
    match = HEADING_RE.search(text)
    return match.group(1).strip() if match else fallback


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: build_wiki.py <source-wiki-dir> <output-dir>", file=sys.stderr)
        return 2

    source = Path(sys.argv[1])
    output = Path(sys.argv[2])
    if not source.is_dir():
        print(f"error: {source} is not a directory", file=sys.stderr)
        return 1

    repo = os.environ.get("GITHUB_REPOSITORY", "")
    ref = os.environ.get("WIKI_SOURCE_REF", "main")
    sha = os.environ.get("GITHUB_SHA", "")
    if not repo:
        print("error: GITHUB_REPOSITORY is not set", file=sys.stderr)
        return 1

    blob_base = f"https://github.com/{repo}/blob/{ref}"
    tree_base = f"https://github.com/{repo}/tree/{ref}"

    sources = sorted(p for p in source.glob("*.md") if p.is_file())
    if not sources:
        print(f"error: no markdown pages found in {source}", file=sys.stderr)
        return 1

    # A set would hide a collision rather than report it. Two sources can map
    # to one page name (index.md and Home.md both become Home), and the write
    # loop below would then silently publish whichever ran last. The generated
    # _Sidebar and _Footer pages overwrite an authored page of the same name
    # for the same reason. Both are wrong quietly, which is the worst way for a
    # corpus that claims completeness to lose a page.
    by_slug: dict[str, list[str]] = {}
    for p in sources:
        by_slug.setdefault(page_slug(p.stem), []).append(p.name)

    problems = []
    for slug in sorted(by_slug):
        if len(by_slug[slug]) > 1:
            problems.append(
                f"{' and '.join(sorted(by_slug[slug]))} both map to {slug}.md"
            )
        if slug in GENERATED_PAGES:
            problems.append(
                f"{by_slug[slug][0]} maps to {slug}.md, which is generated"
            )
    if problems:
        for problem in problems:
            print(f"error: {problem}", file=sys.stderr)
        return 1

    pages = set(by_slug)

    # The sync below lists this directory, so it has to exist first. In CI the
    # wiki clone creates it, which is why this never surfaced there; the
    # standalone command in CI.md points at a fresh path and stopped on it.
    output.mkdir(parents=True, exist_ok=True)

    # Full sync: the wiki/ folder is the source of truth, so a page deleted
    # upstream must disappear from the wiki rather than linger.
    for existing in output.iterdir():
        if existing.name == ".git":
            continue
        if existing.is_dir():
            shutil.rmtree(existing)
        else:
            existing.unlink()

    titles: dict[str, str] = {}
    for path in sources:
        slug = page_slug(path.stem)
        text = path.read_text(encoding="utf-8")
        titles[slug] = page_title(text, slug)
        (output / f"{slug}.md").write_text(
            rewrite_links(text, pages, blob_base, tree_base), encoding="utf-8"
        )
        print(f"page: {path.name} -> {slug}.md")

    ordered = [s for s in SIDEBAR_ORDER if s in pages]
    ordered += sorted(pages - set(ordered))

    sidebar = ["### Wiener Gate", ""]
    for slug in ordered:
        sidebar.append(f"- [{titles[slug]}]({slug})")
    sidebar += [
        "",
        "### Briefs",
        "",
        f"- [All six briefs]({tree_base}/briefs/)",
        f"- [Redaction contract]({blob_base}/REDACTION_CONTRACT.md)",
        f"- [Repository]({tree_base})",
        "",
    ]
    (output / "_Sidebar.md").write_text("\n".join(sidebar), encoding="utf-8")

    # Deliberately no wall-clock stamp. The output is a function of the input
    # commit and nothing else, so re-running against an unchanged wiki/ produces
    # a byte-identical tree and the publish step commits nothing. When the sync
    # happened is already recorded, accurately, by the wiki commit itself.
    short_sha = sha[:7] if sha else "unknown"
    footer = (
        f"_Published from [`wiki/`]({tree_base}/wiki) at "
        f"[`{short_sha}`](https://github.com/{repo}/commit/{sha}). "
        "Edit the pages in the repository, never here: a change made in the wiki "
        "is overwritten by the next sync._\n"
    )
    (output / "_Footer.md").write_text(footer, encoding="utf-8")

    print(f"wrote {len(sources)} pages plus _Sidebar.md and _Footer.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
