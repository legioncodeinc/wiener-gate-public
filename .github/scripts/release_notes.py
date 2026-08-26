#!/usr/bin/env python3
"""Compose the release notes for a corpus snapshot.

A release here is a citable point-in-time archive of an active investigation, so
the notes carry four things a reader needs before quoting anything: the standing
not-a-suspect warning, what each bundle contains, the SHA-256 of every asset, and
the corpus's own release-log entry (which tracks findings, not files, and moves
on its own schedule).

Usage: release_notes.py <version> <dist-dir> <output-file> [previous-tag]
Environment: GITHUB_REPOSITORY, GITHUB_SHA
"""

from __future__ import annotations

import hashlib
import os
import posixpath
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

# Bundle filename suffix to the one-line description shown in the downloads table.
BUNDLE_BLURB = {
    "full.zip": "Every tracked file in the repository: briefs, wiki, rendered PDF and HTML, contracts.",
    "pdf.zip": "The rendered PDFs only: the master brief plus all six persona briefs.",
    "html.zip": "The rendered HTML only: the master brief plus all six persona briefs.",
    "markdown.zip": "The markdown sources only: master brief, six persona briefs, nine wiki pages, contracts.",
}

MAX_COMMITS = 40

RELEASE_LOG_RE = re.compile(r"^##\s+\d+\.\s+Release log\s*$(.*?)(?=^##\s|\Z)", re.M | re.S)
ENTRY_RE = re.compile(r"^###\s.*?(?=^###\s|\Z)", re.M | re.S)
LINK_RE = re.compile(r"\]\(\s*([^)\s]+)\s*\)")
EXTERNAL_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")


def absolutise_links(text: str, repo: str, ref: str = "main") -> str:
    """Turn wiki-relative markdown links into absolute repository URLs.

    Release notes are rendered on the releases page, which has no notion of the
    repository tree, so a relative link lifted out of wiki/changelog.md resolves
    nowhere unless it is rewritten here.
    """

    def replace(match: re.Match[str]) -> str:
        target = match.group(1)
        if not target or target.startswith("#") or EXTERNAL_RE.match(target):
            return match.group(0)
        path, sep, anchor = target.partition("#")
        if not path:
            return match.group(0)
        is_dir = path.endswith("/")
        resolved = posixpath.normpath(posixpath.join("wiki", path))
        while resolved.startswith("../"):
            resolved = resolved[3:]
        kind = "tree" if is_dir else "blob"
        url = f"https://github.com/{repo}/{kind}/{ref}/{resolved}{'/' if is_dir else ''}"
        return f"]({url}{sep}{anchor})"

    return LINK_RE.sub(replace, text)


def human_size(count: int) -> str:
    value = float(count)
    for unit in ("B", "KB", "MB", "GB"):
        if value < 1024 or unit == "GB":
            return f"{value:.0f} {unit}" if unit == "B" else f"{value:.1f} {unit}"
        value /= 1024
    return f"{value:.1f} GB"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1048576), b""):
            digest.update(chunk)
    return digest.hexdigest()


def git(*args: str) -> str:
    result = subprocess.run(
        ["git", *args], capture_output=True, text=True, check=False, encoding="utf-8"
    )
    return result.stdout.strip() if result.returncode == 0 else ""


def latest_release_log_entry(repo_root: Path) -> str:
    """Pull the topmost entry out of the wiki changelog's release log section."""
    changelog = repo_root / "wiki" / "changelog.md"
    if not changelog.is_file():
        return ""
    section = RELEASE_LOG_RE.search(changelog.read_text(encoding="utf-8"))
    if not section:
        return ""
    entry = ENTRY_RE.search(section.group(1))
    if not entry:
        return ""
    # Demote one level so the entry nests under a level-two heading in the notes.
    return re.sub(r"^###\s+", "#### ", entry.group(0).strip(), count=1)


def main() -> int:
    if len(sys.argv) not in (4, 5):
        print(
            "usage: release_notes.py <version> <dist-dir> <output-file> [previous-tag]",
            file=sys.stderr,
        )
        return 2

    version, dist_dir, output = sys.argv[1], Path(sys.argv[2]), Path(sys.argv[3])
    previous = sys.argv[4] if len(sys.argv) == 5 else ""

    repo = os.environ.get("GITHUB_REPOSITORY", "")
    sha = os.environ.get("GITHUB_SHA", "")
    if not repo:
        print("error: GITHUB_REPOSITORY is not set", file=sys.stderr)
        return 1

    repo_root = Path.cwd()
    blob = f"https://github.com/{repo}/blob/main"
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    short_sha = sha[:7] if sha else "unknown"

    assets = sorted(p for p in dist_dir.iterdir() if p.is_file())
    bundles = [p for p in assets if p.suffix == ".zip"]
    briefs = [p for p in assets if p.suffix == ".md"]

    lines: list[str] = []
    add = lines.append

    add(
        f"Point-in-time snapshot of the public evidence corpus, built from "
        f"[`{short_sha}`](https://github.com/{repo}/commit/{sha}) on {stamp}."
    )
    add("")
    add("> [!IMPORTANT]")
    add(
        "> **Several people whose names and faces appear in this material are victims "
        "of identity and image theft, not participants.** Read "
        f"[Who is NOT a suspect]({blob}/wiki/who-is-not-a-suspect.md) before you read, "
        "quote, or act on anything in these bundles."
    )
    add("")
    add(
        "> **This is an active investigation.** Findings marked `PROVISIONAL`, "
        "`UNVERIFIED` or `HYPOTHESIS` may change or be withdrawn. If you are citing "
        "this corpus in a filing, an article, or a report, cite this release tag and "
        f"check the [changelog]({blob}/wiki/changelog.md) before you publish."
    )
    add("")

    add("## Bundles")
    add("")
    add("| Bundle | Contents | Size |")
    add("|---|---|---|")
    for path in bundles:
        blurb = next(
            (text for suffix, text in BUNDLE_BLURB.items() if path.name.endswith(suffix)),
            "Bundle.",
        )
        add(f"| `{path.name}` | {blurb} | {human_size(path.stat().st_size)} |")
    add("")

    if briefs:
        add("## Individual briefs (markdown)")
        add("")
        add(
            "Attached loose, so a single brief can be linked or downloaded without "
            "taking the whole corpus."
        )
        add("")
        for path in briefs:
            add(f"- `{path.name}` ({human_size(path.stat().st_size)})")
        add("")

    if previous:
        add(f"## Changes since [{previous}](https://github.com/{repo}/releases/tag/{previous})")
        add("")
        log = git("log", "--no-merges", "--pretty=- %s (%h)", f"{previous}..HEAD")
        entries = [line for line in log.splitlines() if line.strip()]
        if entries:
            lines.extend(entries[:MAX_COMMITS])
            if len(entries) > MAX_COMMITS:
                add(
                    f"- ...and {len(entries) - MAX_COMMITS} further commits, listed in "
                    "the full comparison below."
                )
        else:
            add("No commits recorded between these tags.")
        add("")
        add(f"[Full comparison](https://github.com/{repo}/compare/{previous}...{version})")
        add("")
    else:
        add("## Changes")
        add("")
        add(
            "First archived snapshot of this corpus. There is no earlier release to "
            "compare against."
        )
        add("")

    entry = latest_release_log_entry(repo_root)
    if entry:
        entry = absolutise_links(entry, repo)
        add("## Corpus release log, latest entry")
        add("")
        add(
            "The corpus carries its own version, which tracks findings rather than "
            "files and moves on its own schedule. This is the current entry from "
            f"[`wiki/changelog.md`]({blob}/wiki/changelog.md)."
        )
        add("")
        add(entry)
        add("")

    add("## Verify these files")
    add("")
    add(
        "Every asset is listed with its SHA-256 in `SHA256SUMS.txt`. Download the "
        "assets and the sums file into the same directory, then:"
    )
    add("")
    add("```bash")
    add("sha256sum -c SHA256SUMS.txt")
    add("```")
    add("")
    add(
        "The wider integrity chain, including the hashes of the collected corpus "
        f"itself, is documented in [verify our work]({blob}/wiki/verify-our-work.md)."
    )
    add("")
    add("<details>")
    add("<summary>SHA-256 of every asset in this release</summary>")
    add("")
    add("```")
    for path in assets:
        if path.name == "SHA256SUMS.txt":
            continue
        add(f"{sha256(path)}  {path.name}")
    add("```")
    add("")
    add("</details>")
    add("")
    add("---")
    add("")
    add(
        "Compiled by Legion Code Inc. Published under the binding "
        f"[redaction contract]({blob}/REDACTION_CONTRACT.md). A redaction miss goes "
        "through the private reporting route, never a public issue."
    )

    output.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {output} ({len(lines)} lines, {len(assets)} assets)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
