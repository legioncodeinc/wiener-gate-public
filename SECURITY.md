# Security Policy

This repository is the public layer of an evidence-bound fraud investigation. "Security" here means two things: the integrity of the evidentiary record, and the protection of victim and third-party personal information.

The second one is the urgent one. **A redaction miss is not a bug that gets fixed in the next release. It is permanent the moment it is public.** That is why the reporting route below is private, and why it matters that you use it.

## Report these privately. Never in a public issue

Do not open a GitHub issue, discussion, or pull request for any of the following:

- **A redaction miss.** Personal information of a victim, a minor, or an uninvolved third party that should not be here
- **A person named or identifiable** who should be on the exclusion list. See [Who is NOT a suspect](wiki/who-is-not-a-suspect.md)
- **Content published beyond the scope of documented consent**
- **An evidence-integrity problem**, such as a file whose hash no longer matches its manifest entry
- **A leaked credential, token, or investigator personal information**

A public issue about a redaction miss republishes the miss to everyone watching this repository, and it does so in a place that is indexed and mirrored. It makes the exact problem you are reporting worse.

### How to report

**Preferred: [open a private security advisory](https://github.com/legioncodeinc/wiener-gate-public/security/advisories/new).** Private vulnerability reporting is enabled on this repository. The report stays private, stays attached to the repository, and does not become public unless and until a maintainer publishes it.

**Fallback: email <mario@legioncodeinc.com>.** Use this if you do not have a GitHub account, or if the advisory form will not accept what you need to say.

Everything else, a broken link, a typo, a factual correction, a question about method, belongs in a normal public issue. See [How to help](briefs/BRIEF-06-how-to-help.md).

### Do not put the sensitive material in the report

This holds for both routes. A private advisory is private, not encrypted at rest in your control, and email is not end-to-end encrypted at all. Send only what is needed to locate the problem, never the exposed material itself.

**Include** (non-sensitive metadata only):

- The affected file path, release tag, or commit SHA, and a line or section reference
- The category of problem (exposed personal data, consent-scope breach, hash mismatch, leaked credential)
- Why it is sensitive, and the potential impact, described in general terms
- Any suggested remediation, if you have one

**Do not include:**

- Names, images, contact details, or any other personal information of a victim, a minor, or a third party
- Quoted or pasted excerpts of the exposed content, screenshots of it, or attachments containing it
- Credential or token values. Report that a credential is exposed and where. Never paste the value

If a report cannot be made useful without transmitting sensitive content, say so in the email and wait for the maintainer to arrange a protected channel before sending anything further.

## What to expect

You can expect an acknowledgment within 3 business days. Confirmed exposure of victim or minor personal information is treated as the highest priority and is remediated before any other work continues.

A redaction miss is never quietly fixed. Per [`REDACTION_CONTRACT.md`](REDACTION_CONTRACT.md) section 6 and the correction policy in the [changelog](wiki/changelog.md), the repair is logged, and the log says a repair happened. The material itself is not reproduced in that entry.

## Supported versions

| Version | Supported |
| --- | --- |
| Latest release, and `main` | :white_check_mark: |
| Earlier release tags | Superseded. Findings may have been corrected or withdrawn since |

Releases are point-in-time snapshots of an active investigation. If you are citing this corpus, cite the release tag and check the [changelog](wiki/changelog.md) before you publish.

## Scope

This policy covers the contents of this repository and its releases. It is not a software vulnerability program: there is no application here to exploit. Reports about the GitHub Actions workflows in [`.github/`](.github/CI.md) are in scope and can be filed publicly, unless the report itself would disclose one of the categories listed above.
