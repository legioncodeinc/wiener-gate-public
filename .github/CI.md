# CI in this repository

Two workflows. Both run on merges into `main`, and both can also be started by
hand, which matters when a run has to be repeated without inventing a commit.

| Workflow | Fires on | Does |
|---|---|---|
| [`publish-wiki.yml`](workflows/publish-wiki.yml) | A push to `main` touching `wiki/**`, `.github/workflows/publish-wiki.yml`, or `.github/scripts/build_wiki.py`; or `workflow_dispatch` | Publishes `wiki/` to this repository's GitHub wiki |
| [`release.yml`](workflows/release.yml) | Any push to `main`; a pushed tag matching `v*`; or `workflow_dispatch` | Cuts a versioned release with the corpus bundled five ways |

Two details in that table are easy to miss and both change what a run does.

The wiki path filter covers the builder as well as the content. A change to
`build_wiki.py` alters every published page without touching `wiki/`, so a
filter that watched only `wiki/**` would leave the wiki built by the old script
until the next unrelated content edit.

`release.yml` answers to tags as well as to `main`. Pushing `v2026.08.26` cuts
that release directly, which is the path a release takes when it is being
published deliberately rather than as a consequence of a merge.
`workflow_dispatch` takes two inputs: `version`, a tag such as `v2026.08.26`,
defaulting to today's CalVer when left blank, and `draft`, which stops the run
at a draft release instead of publishing it.

Neither uses a third-party action. The only action referenced is `actions/checkout`; everything else is `git`, `python3`, and the `gh` CLI already present on the runner. For a repository whose whole claim is that the material can be verified, the build should not depend on code nobody here reviewed.

## Publishing the wiki

`wiki/` is the single source of truth. The workflow performs a full sync, so a page deleted from `wiki/` disappears from the published wiki, and a page edited in the wiki UI is overwritten on the next merge.

[`scripts/build_wiki.py`](scripts/build_wiki.py) does the translation, because a GitHub wiki is a flat namespace of pages and `wiki/` is authored as ordinary repository markdown:

- `wiki/index.md` becomes `Home.md`, the wiki landing page.
- A link to a sibling page loses its `.md` suffix and keeps its anchor, so `[glossary](glossary.md#labels)` becomes `[glossary](glossary#labels)`.
- A link that escapes `wiki/` becomes an absolute URL into this repository, so `../briefs/BRIEF-01-law-enforcement.md` resolves for someone reading inside the wiki.
- `_Sidebar.md` and `_Footer.md` are generated. Do not author them by hand. Sidebar order is the `SIDEBAR_ORDER` list in the script; a page missing from that list is appended alphabetically rather than dropped.

**Setup is done.** The wiki was initialised on 2026-08-26 and is populated. Nothing further is required. This is worth recording because GitHub offers no API to create a wiki and refuses a push to one that does not exist, so if the wiki is ever deleted, the first page has to be recreated by hand at `/wiki/_new` before this workflow can run again. The workflow detects that state and says so, and it distinguishes it from the Wiki feature simply being switched off.

To publish without a `wiki/` change, run the workflow manually from the Actions tab.

## Cutting a release

Readers are asked to cite a version, and this corpus is a point-in-time snapshot of a moving investigation, so every merge into `main` becomes a citable archive.

**Versions** are CalVer: `v2026.08.26`, then `v2026.08.26.1`, `v2026.08.26.2` for repeat syncs in one day. Three ways to set one:

- Merge into `main`. The date-based version is computed for you.
- Push a `v*` tag. That tag is used as-is.
- Run the workflow manually and pass a `version` input. There is also a `draft` input for rehearsing a release without publishing it.

To merge without cutting a release, put `[skip release]` in the commit subject.

**Assets**, for version `V`:

| Asset | Contents |
|---|---|
| `wiener-gate-public-V-full.zip` | Every tracked file |
| `wiener-gate-public-V-pdf.zip` | Rendered PDFs only |
| `wiener-gate-public-V-html.zip` | Rendered HTML only |
| `wiener-gate-public-V-markdown.zip` | Markdown sources only |
| `BRIEF-01` through `BRIEF-06`, `MASTER-BRIEF.md` | Loose, one file per brief, so a single audience can be linked on its own |
| `SHA256SUMS.txt` | Checksums for everything above |

All four bundles come out of `git archive` against the committed tree, so their contents are exactly what is under version control: no untracked scratch files, no build-host state. The subset bundles keep the repository layout, so `docs/victims/BRIEF-02-victims.pdf` sits where a reader expects it.

Before anything is published, the bundles are opened and checked: each must be a readable archive containing a known file. A corrupt or empty archive of an evidence corpus is worse than a failed release.

**Release notes** are composed by [`scripts/release_notes.py`](scripts/release_notes.py) and carry the standing not-a-suspect warning, the active-investigation caveat, a bundle table, the commits since the previous tag, the current entry from the corpus release log in `wiki/changelog.md`, and the SHA-256 of every asset.

Note that two different version numbers are in play and they are not meant to match. The release tag versions the *files*. The `Version:` header on each page versions the *findings*, and moves only when a finding does, under the rules in `wiki/changelog.md` section 2.

## Things worth knowing before you change any of this

**This repository receives a sync from a private working repository.** `README.md` says so in its own header comment: it is authored privately and copied here, and the same is true of `MASTER-BRIEF.md`, `REDACTION_CONTRACT.md`, `SECURITY.md`, `briefs/` and `wiki/`. Edit those in `wiener-gate-private` under `library/knowledge/public/`, never here, or the next sync reverts you.

**This directory is the exception, and it is a deliberate one.** The sync stages with `rsync --delete`, which makes the bundle authoritative over everything it does not exclude. `.github/`, `.gitignore` and `.gitattributes` are excluded by name, because they are the public repository's own infrastructure rather than published corpus. That exclusion was added in [wiener-gate-private#14](https://github.com/legioncodeinc/wiener-gate-private/pull/14). **Until that merges, the next sync deletes this entire directory.** If these workflows ever vanish after a sync, that is why: check the exclusion is still in `public-repo-sync.yml`.

**The redaction gate runs privately, and belongs there.** `README.md` says the contract is enforced by a CI gate that fails the build. It is: `scripts/redaction-check.sh` in the private repository runs three times before a sync PR is opened, against the source tree, the compiled master, and the assembled bundle. It cannot be moved here, because it loads its literals from a private fixture, and a gate that published the strings it protects would defeat itself. Nothing in this directory re-checks the contract, and neither workflow should be mistaken for one.

**Do not add a redaction gate here.** It would have to carry the protected literals to work, in public, in a repository that is mirrored and indexed.

## Testing a change locally

Both scripts run standalone against a checkout:

```bash
GITHUB_REPOSITORY=legioncodeinc/wiener-gate-public GITHUB_SHA=$(git rev-parse HEAD) python3 .github/scripts/build_wiki.py wiki /tmp/wiki-out
```
