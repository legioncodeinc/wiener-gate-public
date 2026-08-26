# Changelog

> Category: Public Wiki | Version: 1.0 | Date: August 2026 | Status: Active

This is an active matter, not a finished report: what this page records, what is expected to change, the corrections that have already reshaped the record, and how to watch for the next one.

**Related:**
- [`index.md`](index.md) - the overview, and the current state of the case
- [`verify-our-work.md`](verify-our-work.md) - the integrity chain, and where the investigators think the weak points are
- [`methodology.md`](methodology.md) - the append-only rule that makes corrections visible
- [`indicators.md`](indicators.md) - the findings most likely to move
- [`domain-roster.md`](domain-roster.md) - the section that will drift fastest
- [`glossary.md`](glossary.md) - PROVISIONAL, UNVERIFIED, HYPOTHESIS, defined
- [`../briefs/BRIEF-06-how-to-help.md`](../briefs/BRIEF-06-how-to-help.md) - how to submit a correction

---

## 1. Read this before citing anything here

**This is an active investigation.** The operation described in this corpus was still registering domains, still recycling pages, and still soliciting payments at the time of publication (R-1, Z-7). Anything written here describes a moving target.

**This public corpus is a point-in-time snapshot synced from a private working repository.** The private record is the evidentiary source; these pages are derived from it, filtered through a binding [redaction contract](../REDACTION_CONTRACT.md), and republished when the source changes materially. **The public pages will therefore lag the private record**, sometimes by days.

**Findings labelled `PROVISIONAL`, `UNVERIFIED` or `HYPOTHESIS` may change or be withdrawn.** Those labels are not hedging language. They mark specific claims whose supporting artifacts are not yet in hand, and at least one of them is expected to resolve in one direction or the other. See [`glossary.md`](glossary.md) for what each label commits to.

If you are quoting this corpus in a filing, an article, or a report: **cite the version and date in the page header, and check this page before you publish.**

## 2. Versioning

Every page carries a header of the form `Version: 1.0 | Date: August 2026 | Status: Active`.

| Change | Version effect |
|---|---|
| A typographical or link fix | No version change |
| New material that does not alter an existing finding | Minor version, `1.0` to `1.1` |
| **A finding is corrected, withdrawn, or downgraded** | Minor version on the affected page, plus an entry below stating what changed and why |
| A redaction miss is repaired | Minor version, plus an entry below. **A redaction miss is never quietly fixed** |
| Structural reorganisation of the public corpus | Major version across all pages |

The private record is **append-only**: corrections there are appended as amendments and never edited in place, so a reader can see what was believed at each point (CONTRIBUTING, [`methodology.md`](methodology.md)). The public pages are rewritten rather than appended, because a wiki that never removes a superseded claim becomes a hazard rather than a history. **This page is the append-only surface of the public corpus**, and it is where the history lives.

## 3. Release log

### 1.0 - August 2026 - Initial publication

First public release. Establishes the nine-page wiki reference layer and the six persona briefs.

**Published:**

- `index.md`, `who-is-not-a-suspect.md`, `network-at-a-glance.md`, `domain-roster.md`, `indicators.md`, `verify-our-work.md`, `methodology.md`, `glossary.md`, and this page.
- The six persona briefs at [`../briefs/`](../briefs/).

**State of the record at publication:**

| Item | State |
|---|---|
| Complaining victims | Three, identified, intake pending. Published pseudonymously as Complainant A, B and C (Y-1, Y-6, contract section 3) |
| Live network domains at last capture | Four sites fully captured and hashed, one shipping front web-dark with live mail (U, R-3) |
| Deregistered domains | Three (R-2) |
| Image-theft victim entities | Eight identified. **One notified, seven not.** None named publicly for that reason (Y-5) |
| Collected corpus integrity | 140 of 140 files verified against manifest, zero mismatches (L, EXPORT_MANIFEST header) |
| Off-site archive | Held under compliance-mode Object Lock until 2027-08-25 (HANDOFF Amendment 1 A3) |
| Adversarial review rounds completed | Six |
| Findings carrying `PROVISIONAL` | Two, plus one derived timing figure (Z-14, Z-8) |
| Interaction-log entries carrying `UNRESOLVED` | Six of nine (INTERACTION_LOG Amendment 3.1) |

**Known gaps at publication**, disclosed rather than deferred:

- The account that received **victim** money remains unidentified. What is established is a solicitation sent to the investigator (Z-12, Z-18).
- Transfer dates are uncollected for all three complainants. This is the single most time-critical missing field, because recovery mechanisms run on clocks that have already started (Z-5, Z-16).
- What a live-chat provider retained before terminating the operator's account is `UNVERIFIED` and must be established in writing (HANDOFF Amendment 2 B1).
- The enumerated in-corpus domain slice and the larger investigator-tracked total have not been reconciled (D12).
- Offline escrow of the archive's private key is incomplete (HANDOFF Amendment 1 A3).

## 4. Corrections carried into version 1

These predate public release. They are listed because **the corrections are the reason the surviving findings are worth anything**, and because a reader who encounters an older version of a claim elsewhere needs to know it was withdrawn.

Nine of these actively make the case smaller or weaker. They are retained by rule (HANDOFF section 2d).

| # | Original claim | What replaced it | Ref |
|---|---|---|---|
| 1 | A shared server address links three domains, therefore common control | The address carries 48 or more tenants and the domains use three different nameserver pairs, consistent with three separate hosting purchases. **Withdrawn as proof of control** | R-4 |
| 2 | (Following 1) The shared address is still a web-hosting linkage | It is a shared **file-transfer gateway**. Most co-tenants only use it for file transfer. The surviving observation is much narrower: three domains web-serve from it while others do not | S-6 |
| 3 | Published phone numbers identify operators | One runs an entirely unrelated commercial vertical; another reaches a probably-uninvolved private individual. **Downgraded** | V-5 |
| 4 | A technology business co-hosted with the network is of high interest | **CLEARED.** Its published client portfolio contains no pet, breeder, rescue, or logistics domain. Coincidental co-tenancy, no evidentiary value, and it is not named in this corpus | S-7 |
| 5 | A small breeder appears as a scam group co-administrator | **CLEARED.** The roster entry is a two-follower page impersonating her, not her account. She is a victim of website appropriation | A5c |
| 6 | A 2048 by 2048 square image indicates AI generation | A confirmed-real photograph in the corpus is 2048 by 2048. **Corroborative only** | W-3 |
| 7 | Error level analysis demonstrates image manipulation | **Corroborative only, never probative** | M-2 |
| 8 | A camera body serial number can be recovered from the metadata | The camera model in question writes no body serial. **Dead end** | W-5 |
| 9 | Perceptual hashing will link accounts through reused images | **Zero cross-account reuse across 98 files.** Retained as a probative negative: it proves large harvesting volume and deliberate detection avoidance | K-4 |
| 10 | Breach records mentioning a country corroborate the attribution | Substring matches on unrelated real freight companies. **Do not cite them.** Recorded specifically to stop a later reviewer rediscovering them | R-5 |
| 11 | The operator city is one coastal city | Corrected to a different city roughly 70 km away, on the longitude of the recorded coordinates | Q-8 |
| 12 | A phone number's associated mailbox identifies a party | **Refused.** Handled as a probable uninvolved third party and not enumerated | V-4 |
| 13 | A shipping domain is "already dark" | Dark on the web surface only. Live mail records, published sender policy, recently renewed certificate. **A working mailbox** | R-3 |
| 14 | The case has money movement | **Superseded.** What is established is a solicitation sent to the investigator. That any victim paid it is **not established** | Z-12, Z-18 |
| 15 | A bank account was opened remotely | Relabelled **HYPOTHESIS.** No know-your-customer record supports it, and an in-person opening is not excluded | Z-13 |
| 16 | A solicitation finding is "demonstrated" and "almost certainly correct" | Relabelled **PROVISIONAL**, and the confidence phrase removed, because no supporting artifact was filed at the time of writing | Z-14, Z-19 |
| 17 | A live-chat provider's preserved transcripts are "the complete set" | **Does not follow.** Termination ends the live channel; it says nothing about historical retention scope. **UNVERIFIED** pending written confirmation | HANDOFF Amdt 2 B1 |
| 18 | Unresolved log entries "should be completed before filing" | Corrected to **reviewed**, not necessarily completed. Pressuring an investigator to close a field under deadline is how a reconstructed-from-memory fact enters a record and later collapses | HANDOFF Amdt 2 B2 |
| 19 | Two interaction-log entries are `PASSIVE` | Reclassified **UNRESOLVED.** `PASSIVE` requires login state positively known to be logged out, and recording them as anonymous without confirming it presumed the answer | INTERACTION_LOG Amdt 3.1 |
| 20 | A checkout interaction was "inspected read-only" | Contradicted its own description of a populated form. Reclassified **ACTIVE-OUT** and disclosed, with the mechanism recorded as unrecoverable | HANDOFF Amdt 1 A4 |
| 21 | A single "contact your bank" recovery instruction | Corrected to a **payment-rail-specific** table. Recovery options differ completely by rail | Z-20 |
| 22 | A bare `ACTIVE` interaction class | **Retired.** Split into `ACTIVE-OUT`, `ACTIVE-IN` and `ACTIVE-3P`, because collapsing investigator conduct and operator conduct into one label defeats the log's purpose | INTERACTION_LOG Amdt 2.1 |

## 5. What is expected to change

Not speculation. These are specific, identified, and in most cases already in motion.

| Expected change | What it would affect |
|---|---|
| **Registry drift.** Domains go dead, new ones are registered. The burn cycle is four to ten weeks (R-1, R-2) | [`domain-roster.md`](domain-roster.md) sections 2 and 3. A domain going dead is itself a finding, not a broken link |
| **A pending platform data export arrives** | Would move two `PROVISIONAL` findings and one derived timing figure to established, or withdraw them (Z-14) |
| **Victim intake completes** | Payment rails, amounts, dates, and receiving account names. Would settle the open question of which account received victim money (Z-12, Y-3) |
| **Image-theft victims are notified** | Seven of eight are unnotified, which is the only reason they are unnamed here. Naming becomes possible **only after** notification, and only if appropriate (Y-5) |
| **Written confirmation from a live-chat provider** | Would resolve an `UNVERIFIED` retention scope (HANDOFF Amdt 2 B1) |
| **Domain enumeration reconciles** | Would let the scale claim be stated as one number instead of two (D12) |
| **Complainants revisit pseudonymity** | Pseudonymity is reversible on their say-so. **Publication is not** (Y-6, contract section 3) |
| **A finding is broken by a reader** | The most welcome item on this list. See [`verify-our-work.md`](verify-our-work.md) section 7 |

## 6. How to watch for updates

**Watch the repository.** On GitHub, use `Watch` and select `Custom` then `Releases` for version announcements only, or `All Activity` for every commit. Each public release is tagged.

**Follow the commit feed.** GitHub publishes an Atom feed per branch, at `https://github.com/<owner>/<repo>/commits/<branch>.atom`, which any feed reader can subscribe to without an account.

**Check the header.** Every page carries `Version` and `Date`. If the version on a page you are citing has moved past the one you read, come back here and read the entry for the difference.

**Check this page before publishing anything.** That is the whole request. Sections 1 and 5 exist so that a reporter, an analyst, or an investigator can tell in under a minute whether the claim they are about to repeat is still standing.

## 7. Correction policy

**Corrections are welcome, logged, and credited.** This record has been improved more by adversarial review than by additional collection, and the section 4 table is the evidence for that.

| What you found | Where it goes |
|---|---|
| A factual error, a broken link, a stale status | The repository's public issue tracker |
| **A redaction miss**: an identity, a minor, an unconfirmed suspect, a credential, or any sensitive data that should not be public | **The private route in [`../../../../SECURITY.md`](../../../../SECURITY.md). Never a public issue** |
| A finding you believe is unsupported | Public issue, with the specific claim and what breaks it. See [`verify-our-work.md`](verify-our-work.md) section 7 for the known soft spots |
| New infrastructure | See [`indicators.md`](indicators.md) section 11 and [`../briefs/BRIEF-06-how-to-help.md`](../briefs/BRIEF-06-how-to-help.md). **Report infrastructure, never a person** |

Two commitments govern how corrections are handled.

**A withdrawn claim is recorded as withdrawn, not deleted.** It goes in the section 4 table with what replaced it. Silent removal would make this corpus exactly as trustworthy as the material it investigates.

**A redaction miss is repaired immediately and disclosed here.** It is not a bug fixed in the next release. **It is permanent the moment it is public** (contract section 6), and the only honest response is to fix it fast and say so.
