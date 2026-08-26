<!--
README for wiener-gate-public. Branded for Legion Code Inc.
Brand source of truth: https://github.com/legioncodeinc/brands
Logo, palette, and typography pulled from legion-code-inc/. The verified-green
accent (#3DDC97) is used sparingly, per the brand scarcity rule.
Do not use em dashes or en dashes anywhere in this file (repo rule).

THIS FILE SHIPS. It is copied to the root of the public repository by
.github/workflows/public-repo-sync.yml, which appends a provenance footer
recording the sync time and source commit. Edit it here, never there.

Badges are static or point at the public repository. A badge pointing at a
private repository's workflow renders as a broken image for everyone who
cannot see that repository, which is every reader of this file.
-->

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/legioncodeinc/brands/main/legion-code-inc/logos/legion-logo-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/legioncodeinc/brands/main/legion-code-inc/logos/legion-logo-light.svg">
    <img src="https://raw.githubusercontent.com/legioncodeinc/brands/main/legion-code-inc/logos/legion-logo-dark.svg" alt="Legion Code Inc." width="300">
  </picture>
</p>

<p align="center"><em>The developer toolchain, for the time of AI.</em></p>

<p align="center">
  <img src="https://img.shields.io/badge/status-active%20investigation-E9C46A" alt="Active investigation">
  <img src="https://img.shields.io/badge/redaction%20contract-enforced%20in%20CI-3DDC97" alt="Redaction contract enforced in CI">
  <img src="https://img.shields.io/badge/every%20claim-referenced-3DDC97" alt="Every load-bearing claim is referenced">
  <img src="https://img.shields.io/badge/evidence-SHA--256%20hashed-264653" alt="Evidence SHA-256 hashed">
</p>

> [!IMPORTANT]
> **Several people whose names and faces appear in this material are victims of identity and image theft, not participants.**
>
> Before you read anything else, read **[Who is NOT a suspect](wiki/who-is-not-a-suspect.md)**. It is not an appendix. If you think you have identified a person in this material, do not act on it and do not publish it.

---

# Wiener Gate | Public Evidence Corpus

An evidence-bound investigation into a multi-brand online pet-purchase fraud network, documented as a criminal supply chain rather than a single suspect.

> **Compiled by:** Legion Code Inc. &nbsp;|&nbsp; **Principal:** Mario Aldayuz, CTO and co-founder
>
> **This is an evolving situation.** This corpus is a point-in-time snapshot synced from a private working repository. Findings marked `PROVISIONAL`, `UNVERIFIED` or `HYPOTHESIS` may change. See the [changelog](wiki/changelog.md).

## Start here

Six briefs, each written for a different reader. Pick yours.

| If you are | Read | Rendered |
|---|---|---|
| **Law enforcement** | [For law enforcement](briefs/BRIEF-01-law-enforcement.md) | [Web](https://legioncodeinc.github.io/wiener-gate-public/law-enforcement/) &middot; [PDF](docs/law-enforcement/BRIEF-01-law-enforcement.pdf) |
| **A victim, or you think you are being targeted** | [If you have been targeted](briefs/BRIEF-02-victims.md) | [Web](https://legioncodeinc.github.io/wiener-gate-public/victims/) &middot; [PDF](docs/victims/BRIEF-02-victims.pdf) |
| **A technical analyst** | [For technical analysts](briefs/BRIEF-03-technical-analysts.md) | [Web](https://legioncodeinc.github.io/wiener-gate-public/technical-analysts/) &middot; [PDF](docs/technical-analysts/BRIEF-03-technical-analysts.pdf) |
| **Intelligence or research** | [Analytic assessment](briefs/BRIEF-04-intelligence.md) | [Web](https://legioncodeinc.github.io/wiener-gate-public/intelligence/) &middot; [PDF](docs/intelligence/BRIEF-04-intelligence.pdf) |
| **Press, or simply reading** | [Why this matters](briefs/BRIEF-05-media-public.md) | [Web](https://legioncodeinc.github.io/wiener-gate-public/media-public/) &middot; [PDF](docs/media-public/BRIEF-05-media-public.pdf) |
| **Willing to help** | [How to help](briefs/BRIEF-06-how-to-help.md) | [Web](https://legioncodeinc.github.io/wiener-gate-public/contributors/) &middot; [PDF](docs/contributors/BRIEF-06-how-to-help.pdf) |

Everything in one document: **[MASTER-BRIEF.md](MASTER-BRIEF.md)** ([Web](https://legioncodeinc.github.io/wiener-gate-public/master/) &middot; [PDF](docs/master/MASTER-BRIEF.pdf)). The reference layer lives in the [wiki](wiki/index.md).

The **Web** links go to <https://legioncodeinc.github.io/wiener-gate-public/>, this corpus rendered as a site with every diagram drawn. It is published by GitHub Pages from the [`docs/`](docs/) folder on `main`, which carries its own landing page and a `.nojekyll` marker. A `docs/` link in this README opens the file listing rather than the page, which is why the rendered ones point at the site and the PDFs, which GitHub displays perfectly well, do not.

## The case in one paragraph

A multi-brand online pet-purchase fraud network solicits U.S. buyers for puppies, primarily miniature dachshunds, using stolen and AI-generated imagery across mass-produced Facebook pages and template websites. Buyers are "approved" for adoption, then walked up an escalating ladder of fees (a reservation deposit, then transport, insurance, and customs charges through a fake pet-courier) paid via hard-to-reverse peer-to-peer apps. The governing model is a **supply chain of rented services, not one perpetrator**: template and kit authoring, a Facebook page-farm and audience layer, a European payment leg, a family of fake-courier sites, and an operator layer. The storefronts are bought kits deployed without modification, and they prove it themselves: one publishes its template vendor's demonstration login credentials in plain text on a public page, ships the word "(demo)" in its own footer in two languages, and serves the vendor's demonstration shipment record from a live tracking database.

## What is in this repository

| Path | What is here |
|---|---|
| [`briefs/`](briefs/) | The six persona briefs, in markdown |
| [`wiki/`](wiki/) | The reference layer: network map, domain roster, indicators, methodology, glossary, changelog |
| [`docs/`](docs/) | The same briefs rendered as PDF and standalone HTML, diagrams included, with a landing page for GitHub Pages |
| [`MASTER-BRIEF.md`](MASTER-BRIEF.md) | Every brief and the full wiki compiled into one document |
| [`REDACTION_CONTRACT.md`](REDACTION_CONTRACT.md) | The binding rules this corpus holds itself to, published so you can audit them |

## What is not here, and why

The private working repository holds the evidence tree: the collected artifacts, the chain-of-custody log, victim identities, suspect-side financial detail, and images belonging to people who never consented to anything. **None of it ships**, and that is deliberate rather than incidental.

What ships instead is everything that can be checked without it: the infrastructure findings, the registry timeline, the template artifacts, the stolen-image provenance analysis described in words rather than reproduced, the methodology, and every hash needed to verify the work. The boundary is written down in [REDACTION_CONTRACT.md](REDACTION_CONTRACT.md) and enforced by a CI gate that fails the build rather than publishing a violation, because a redaction miss is not a bug you fix in the next release. It is permanent the moment it is public.

## How to check our work

This corpus is built to be attacked, and the reasoning is auditable rather than asserted.

- **Every load-bearing claim about the network carries a pointer** to the section of the private evidence log that supports it, in the form `(Z-7)`, `(U-4)`, `(R-1)`. Connective prose and descriptions of our own method carry none, because they assert nothing about the network.
- **Claims that outrun their evidence are labelled.** `UNVERIFIED`, `HYPOTHESIS`, `PROVISIONAL` and `ASSESSED` are used as terms of art, not decoration. A provisional finding stays provisional until the artifact that would settle it is filed.
- **Disproofs are retained.** Nine findings in the record make the case smaller or weaker, and they stay in the file: a shared-IP linkage downgraded once it turned out to be a hosting gateway with dozens of unrelated tenants, phone numbers abandoned as operator identifiers, an image-forensics indicator corrected after a real photograph displayed it, a hardware-serial route that turned out not to exist, and two entities affirmatively cleared. A file that only ever grows in one direction is a file nobody should trust.
- **The hashes are published.** [Verify our work](wiki/verify-our-work.md) explains what each manifest covers and how to check an artifact against it, including a discrepancy we already know about and have not hidden.

Found an error? That is the point. See [How to help](briefs/BRIEF-06-how-to-help.md).

## Reporting a problem

**If you find personal data that should have been redacted, report it privately.** Do not open a public issue, and do not repost it. Contact Legion Code Inc. through the security contact on the [organization profile](https://github.com/legioncodeinc), and describe the location without reproducing the content.

For anything else, including a factual correction or a broken claim pointer, a public issue is the right place.

## Provenance and license

This corpus is compiled and published by Legion Code Inc. It is synced from a private working repository; the footer below records the commit and time of the most recent sync.

No license is set. All rights reserved by Legion Code Inc. pending a deliberate licensing decision. The material is published so it can be read, checked, and acted on by the people it concerns, which is not the same as a grant to redistribute it.

<p align="center">
  <sub>Compiled under <strong>Legion Code Inc.</strong> &nbsp;|&nbsp; Brand assets: <a href="https://github.com/legioncodeinc/brands">legioncodeinc/brands</a></sub>
  <br>
  <sub>Read <a href="wiki/who-is-not-a-suspect.md">Who is NOT a suspect</a> before acting on anything here.</sub>
</p>

---

<sub>Synced from the private working repository on 2026-08-26T23:55:27Z.
Source commit `48c32a690b36bd4280572c78fb0f11cb7b3a2cda`.</sub>
