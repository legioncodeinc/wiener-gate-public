# Public Indicator Reference

> Category: Public Wiki | Version: 1.0 | Date: August 2026 | Status: Active

The publishable subset of the investigation's indicator sheet, with the type, value, context, status and evidence-log reference for each entry, plus a full account of every category that was withheld and the reason.

**Related:**
- [`domain-roster.md`](domain-roster.md) - the domain indicators with registry detail
- [`network-at-a-glance.md`](network-at-a-glance.md) - how these indicators fit together
- [`who-is-not-a-suspect.md`](who-is-not-a-suspect.md) - the people behind the withheld rows
- [`glossary.md`](glossary.md) - status tokens, dork, persona pool, tracking format
- [`verify-our-work.md`](verify-our-work.md) - how to check any of this
- [`../briefs/BRIEF-03-technical-analysts.md`](../briefs/BRIEF-03-technical-analysts.md) - the analyst brief these indicators support
- [`../briefs/BRIEF-01-law-enforcement.md`](../briefs/BRIEF-01-law-enforcement.md) - where each indicator should be reported

---

## 1. This is a filtered subset. Read this section first.

The private indicator sheet carries every indicator the investigation holds, including the ones that identify people. **This page is a deliberate subset of it.**

Rows are withheld here for exactly three reasons, and every withheld category is itemised in [section 10](#10-what-was-withheld-and-why) rather than silently dropped. A gap you cannot see is worse than a gap that is labelled.

| Reason a row is withheld | Governing rule |
|---|---|
| It identifies a victim, a cleared party, or an undetermined individual | Redaction contract sections 1 and 2 |
| It is suspect-side financial detail belonging to law enforcement and a bank | Redaction contract section 1 |
| It is a claim the evidence does not support | Redaction contract section 4 |

**Every value on this page is either infrastructure the operation published about itself, or a registry fact anyone can re-derive.** Nothing here identifies a private individual, and nothing here should be used to try.

Status tokens follow the corpus vocabulary. `UNVERIFIED`, `HYPOTHESIS`, `PROVISIONAL` and `UNRESOLVED` mean specific things and are defined in [`glossary.md`](glossary.md).

## 2. Domains

| Type | Value | Context | Status | Ref |
|---|---|---|---|---|
| domain | `royalpawscompanions.com` | Storefront, Hostinger, created 2026-04-03 | CAPTURED AND HASHED | U, R-1 |
| domain | `evergreencompaniondogs.com` | Storefront, Hostinger, created 2026-07-09 | CAPTURED AND HASHED | U, R-1 |
| domain | `usapetsforhome.com` | Storefront, Vercel and Realtime Register, created 2026-08-18 | CAPTURED AND HASHED | U, R-1 |
| domain | `safepup-delivery.com` | Shipping front 2, Hostinger, created 2026-07-28 | CAPTURED AND HASHED | S, T |
| domain | `globaltransit-logistics.com` | Shipping front 1, web dark, mail live, created 2026-06-15 | MAIL ASSET ACTIVE | R-3 |
| domain | `smhomeraiseddachshunds.com` | Original brand | DEAD, RDAP 404 | R-2 |
| domain | `abkcamericanbullypuppies.com` | Cross-linked brand | DEAD, RDAP 404 | R-2 |
| domain | `pauldachshundhome.com` | Name-family storefront | DEAD, RDAP 404 | R-2 |
| domain | `safepupdelivery.com` | Unhyphenated form published as the shipping front's business email domain | PROVEN NON-EXISTENT | S-5 |

The full roster, including the card-harvest family and the unverified candidates, is in [`domain-roster.md`](domain-roster.md).

## 3. Social and platform identifiers

| Type | Value | Context | Status | Ref |
|---|---|---|---|---|
| fb_page_id | `1179239581941044` | Recycled shell page. Created 7 Jun 2026 as a product-category page, renamed the same day, renamed again 13 Aug 2026 to a personal name. 1 follower. Profile image is stolen | SCAM-INFRA, active solicitation | N-1, Z-7 |
| persona_name | "Connie Malone" | Display name assigned to the page above on 13 Aug 2026. **The page is a recycled shell, not a person** | SCAM-INFRA | N-1, Z-7 |
| fb_profile | `61583600066450` | Linked from a storefront. Capture priority | CAPTURE URGENT | U-1 |
| fb_profile | `100022087874969` | Account of investigative interest. **Not named here** | PRESERVATION REQUESTED | B-12 |
| fb_profile | `61592228827729` | Associated with the original brand cluster | OPEN | A-2a |
| fb_profile | `61590754176221` | Associated with the original brand cluster | OPEN | A-2a |
| fb_album_id | `144814298693276` | Successor-account album | PENDING CAPTURE | X-1 |
| fb_media_id | `144814252026614` | Successor-account media identifier root | CAPTURED | X-1b |
| tiktok | `@meyouqpbokz` | Peptide vertical. Publishes a phone number also published by a puppy storefront | LIVE, archive now | V-1 |
| tiktok | `@herman.walker90` | Peptide vertical, same number, ban-evasion language | LIVE, archive now | V-1 |
| tiktok | `@dimitripacks8` | Third account in the same cluster | ALREADY REMOVED | V-1 |
| shopify_shop_id | `77509984484` | Hosted-commerce shop, documented with redirect evidence | REPORT PENDING | A3g |
| tawkto_property | `6a68d4d16e813a1d4d6629ee/1juknukmm` | Live chat embedded on shipping front 2, tied to an operator mailbox. Reported; account preserved and terminated. **What the provider retained from before termination is UNVERIFIED** | REPORTED, retention UNVERIFIED | T-7, HANDOFF Amdt 2 B1 |

## 4. Contact channels published by the operation

| Type | Value | Context | Status | Ref |
|---|---|---|---|---|
| phone_whatsapp | `+1 702-208-4235` | Published by a storefront. Las Vegas NV area code | OPEN, line type unknown | U-1 |
| phone_whatsapp | `+1 534-626-0482` | Published by a storefront. Wisconsin area code | OPEN, line type unknown | U-1 |
| phone | `+1 724-860-4140` | Published by a storefront **and** by two peptide accounts on a different platform. Western Pennsylvania area code | HIGHEST PRIORITY, cross-vertical | V-1, Q-7 |
| phone_whatsapp | `+49 1521 7163344` | Published by shipping front 2. German mobile. The only working contact channel on that entire site | OPEN | S-1, S-5 |
| email | `hello@royalpawscompanions.com` | Storefront contact address | OPEN | U-1 |
| email | `hello@evergreencompaniondogs.com` | Storefront contact address | OPEN | U-1 |
| email | `contact@usapetsforhome.com` | Storefront contact address | OPEN | U-1 |
| email | `sales@safepupdelivery.com` | Published by shipping front 2 on an **unregistered** domain. Undeliverable | PROVEN NON-EXISTENT | S-5 |
| email | `brescueshelter@gmail.com` | Operator-side mailbox. 11 platform registrations, three of which independently place the account in Cameroon | KEY, attribution anchor | Q-1, A4-4 |

> **Standing caution, and it is not optional.** **Phone numbers are not clean operator identifiers** (V-5). One number in this network runs an entirely unrelated commercial vertical. Another, withheld from this page, reaches a probably-uninvolved private individual. Numbers in scam material can be spoofed, recycled, borrowed, or simply wrong. Report them; do not chase the person behind them. See [`who-is-not-a-suspect.md`](who-is-not-a-suspect.md) section 3h.

## 5. Template and content artifacts

These are the strongest exhibits in the case, because they require no interpretation and the operators cannot retract them: they are already captured and hashed.

| Type | Value | Context | Status | Ref |
|---|---|---|---|---|
| template_string | `Demo credentials: admin / Admin@12345` | Printed in plain text on a public admin login page of shipping front 2. **No login was attempted and none should be** | DORK CANDIDATE, highest yield | T-1 |
| template_string | `IATA Live Animal Certified (demo)` | Vendor demonstration text shipped live, in English and hand-translated into German with the placeholder intact | DORK CANDIDATE | T-2, T-9 |
| template_string | `Every Paw's Journey, Safely Home` | Shipping front 2 hero copy | DORK CANDIDATE | S-1 |
| template_string | `$500 secures your chosen puppy` | Storefront deposit copy | DORK CANDIDATE | U-8 |
| tracking_format | `PAW-` plus 8 digits | Shipping front 2 tracking numbers. **Ask victims for these**: receiving one proves the shipper stage, not merely the sale | INTAKE FIELD | T-3 |
| persona | "Priya" (K., N., Sharma) | 4 appearances across 3 domains on 2 hosting stacks | CONFIRMED SHARED POOL | Q-5, S-3, T-3, U-7 |
| persona | "James" (K., Whitfield) | 3 appearances | CONFIRMED SHARED POOL | Q-5, S-3, U-7 |
| persona | "Sarah M." | 2 appearances | CONFIRMED SHARED POOL | Q-5, U-7 |

The persona names above are **operator-side fabrications**, which the redaction contract explicitly clears for publication (contract section 5). They are not real people and must not be searched for as though they were.

## 6. Infrastructure observations

| Type | Value | Context | Status | Ref |
|---|---|---|---|---|
| ip | `77.37.34.75` | Shared Hostinger file-transfer gateway. Three domains web-serve from it while other tenants use it only for file transfer | **WEAK LINKAGE, see caution** | R-4, S-6 |
| address_claimed | `Flughafenstrasse 12, 60549 Frankfurt am Main, DE` | Shipping front 2 claimed head office, in the airport cargo district. **No Impressum is published anywhere on the site** | UNVERIFIED. Possible standalone section 5 DDG exposure, subject to scope and standing | T-5, S-4 |
| geo | Limbe, Southwest Region, Cameroon | Operator-layer attribution. Four corroborating signals plus one timestamped physical-presence indicator | ATTRIBUTION | Q-1, Q-8 |
| timing_metric | 12 days | Identity assignment to payment solicitation on one recycled page. Operational cycle time, testable against other pages | **PROVISIONAL** | Z-8, Z-14 |

**On the shared address:** do not cite it as proof of common control. It carries 48 or more tenants and the domains on it use three different nameserver pairs. The full narrowing is in [`domain-roster.md`](domain-roster.md) section 5.

**On the geolocation:** three of the four signals are metadata and all metadata is spoofable. The fourth is a dine-in review of a named beachfront business, which asserts bodily presence rather than a registration setting. The account's review prose is stylistically consistent with machine generation and the profile is consistent with points farming, so **the review text may be synthetic even if the visit occurred.** The city holds even if the prose does not, because it is independently corroborated by contributor coordinates and two separate platform registrations (Q-8).

## 7. Financial indicators

Only two rows here are publishable, and the framing around them is load-bearing.

| Type | Value | Context | Status | Ref |
|---|---|---|---|---|
| bank_institution | Lead Bank | Chartered institution, a major banking-as-a-service sponsor. The account is likely a sponsored fintech program rather than a branch account, which is a **HYPOTHESIS**, not a finding | REPORT PENDING | Z-3, Z-13 |
| bank_routing | `101019644` | Lead Bank, 1801 Main St, Kansas City MO 64108. Verified against the Federal Reserve routing directory | VERIFIED | Z-2 |
| intake_field | Transfer dates | **The most urgent missing field in the case.** Determines eligibility for the FBI Recovery Asset Team and the Financial Fraud Kill Chain, both of which run on clocks that have already started | OPEN, TIME CRITICAL | Z-5, Z-16 |

> **What is established, and what is not** (Z-18, governing):
>
> **ESTABLISHED:** on 2026-08-25 the operators sent bank account details to the **investigator** and solicited a wire transfer. The bank and routing number verify against the routing directory.
>
> **NOT ESTABLISHED:** that any victim ever sent money to that account; that the account received victim funds; that the named holder knowingly participated in anything. **The account that received victim money remains unidentified.**

The account number itself, the named holder, and the holder's address are suspect-side detail. They go to the bank's fraud and anti-money-laundering function and to law enforcement, and to nowhere else (Z-1, contract section 1).

## 8. Image provenance

The strongest provenance finding in the corpus, described in words rather than reproduced (contract section 5).

| Type | Detail | Status | Ref |
|---|---|---|---|
| image_provenance | One storefront **never renamed the photographs it took.** Its upload paths preserve a third-party listing site's own filename convention verbatim, including a brand string and eight listing identifiers: `21334`, `24287`, `20074`, `140935`, `160221`, `25171`, `26042`, `26091` | VICTIM IDENTIFICATION PENDING | U-3 |
| image_provenance | The 13-digit suffix on each upload path is a Unix millisecond timestamp. Eleven images were uploaded in a continuous 93-minute session **finishing 34 minutes before the domain was registered** | ESTABLISHED | U-4 |
| image_provenance | A second storefront yields 82 timestamped uploads. Two bulk sessions of 39 and 28 images built the inventory in the first week, then a slow trickle. 91 percent fall in a five-hour window incompatible with the first storefront's window | ESTABLISHED, behavioural not geographic | U-5 |
| image_provenance | A third storefront stores images under content-hash filenames. **No original filenames and no upload timestamps survive**, so this analysis cannot be repeated against it | NEGATIVE RESULT | U-6 |
| image_provenance | All 98 photographic files compared by perceptual and difference hashing. **Zero cross-account image reuse.** Each front is supplied with different stolen photographs | NEGATIVE RESULT, probative | K-4 |

**The brand string in the first row is withheld.** It identifies a listing marketplace that is itself an image-theft victim, and it has not been notified. The eight listing identifiers carry the forensic value and are published; the victim's name is not. See [`who-is-not-a-suspect.md`](who-is-not-a-suspect.md) section 3b.

**The upload-hour finding is a behavioural indicator, not a geolocation** (U-5). Upload timestamps reflect the server's clock. An operator targeting buyers in one region may deliberately work that region's hours. It must not be used to reinforce or walk back the attribution at Q-1, which rests on entirely separate account-level evidence.

## 9. Indicators that were tested and downgraded

Recorded here so nobody resurrects them. **Do not cite these as linkage** (HANDOFF section 4b).

| Downgraded claim | What replaced it | Ref |
|---|---|---|
| A shared address proves common control | It is a shared file-transfer gateway with 48 or more tenants. Three domains web-serve from it, which is narrower and is how it should be stated | R-4, S-6 |
| Phone numbers are clean operator identifiers | One runs an unrelated vertical; another reaches a probably-uninvolved private individual | V-5 |
| A 2048 by 2048 square image is an AI indicator | A confirmed-real photograph in the corpus is 2048 by 2048. Corroborative only | W-3 |
| Error level analysis is probative of manipulation | Corroborative only, never probative | M-2 |
| A camera serial number can be recovered | The camera model in question writes no body serial. Dead end | W-5 |
| Breach records mentioning a country corroborate the attribution | Substring matches on unrelated real freight companies. **Do not cite them** | R-5 |

## 10. What was withheld, and why

Nine categories of row exist in the private indicator sheet and do not appear on this page.

| Withheld | Reason | Governing rule |
|---|---|---|
| The solicited **bank account number** | Suspect-side financial detail. Law enforcement and the bank only | Contract 1, Z-1, Z-26 |
| The **named account holder** and their address | Status UNDETERMINED. Mule, identity-theft victim and operator all fit the evidence equally | Contract 2, Z-4 |
| One published **phone number** | Carries a stale association with a probably-uninvolved private individual | Contract 2, V-4, V-5 |
| A claimed **residential street address** | Unverified. If a real person lives there they are a victim | Contract 1, U-2 |
| The **names of the three complainants** | Pseudonymous in version 1 as Complainant A, B and C, notwithstanding their consent | Contract 3, Y-6 |
| The **eight image-theft victim entities** | Seven of eight are not yet notified | Contract 2, Y-5 |
| The **persona-album subject** and the **successor-account profile subject** | An image-theft victim, and an individual whose status is genuinely indistinguishable | Contract 2, G, M-1, X-1b |
| Two **cleared parties**: a technology business and a small breeder | Publishing either would defame or expose a party the record clears | Contract 2, S-7, A5c |
| A network capture file | Carries 209 live session cookie headers and 2 authorization headers | Contract 1, Z-26 |

Two claims are also absent by rule rather than by redaction: **no aggregate dollar-loss figure** appears anywhere in this corpus, because the evidence does not support one (D13, Z-18); and **no statement or diagram implies that a victim paid the solicited account**, because that is not established (Z-12, Z-18).

## 11. Contributing an indicator

New infrastructure is genuinely useful. New names are not.

Report a domain, page identifier, handle, template string, or tracking number, with where you saw it and when. Do not report a person, do not run reverse lookups on the numbers above, and do not submit anything to any of these surfaces. The contamination rules in [`methodology.md`](methodology.md) apply to readers exactly as they applied to the investigation. Routing is in [`../briefs/BRIEF-06-how-to-help.md`](../briefs/BRIEF-06-how-to-help.md).
