# REDACTION CONTRACT

> Category: Public | Version: 1.0 | Date: August 2026 | Status: Active (BINDING)

**Every document in `library/knowledge/public/` and every artifact built from it
must satisfy this contract before it ships. No exceptions, no "just this once".**

This contract derives from `HANDOFF.md` section 2a, `EVIDENCE_LOG.md` Y-6a, and
Z-4. Those sections govern; where this file is ambiguous, they win. Y-6b
requires verification against the redaction table **every time, not once**.

---

## 1. The absolute prohibitions

These never appear in a public artifact, in any form, at any resolution,
however newsworthy.

| Never publish | Why | Ref |
|---|---|---|
| **Any image depicting minors** from the Red Dirt material | Consent belongs to their parents, not to anyone in this investigation | Y-6a |
| **Any image from the `fb_358582` persona album** | Harvested photo library of a real image-theft victim. Never contacted, no consent | G, M-1, W-3, Y-6a |
| **The unverified residential address associated with a domain registration** | Unverified. If a real person lives there they are a victim | U-2, Y-6a |
| **The solicited bank account number** | Suspect-side financial detail. Law enforcement and the bank only | Z-1, Z-26 |
| **The archived HTTP session capture of the checkout surface** | Carries 209 live `Cookie` and 2 `Authorization` headers | Z-26, A2.3 |
| **The unredacted solicitation screenshot** | Profile thumbnail is the `fb_358582` victim's likeness; also shows the account number | Z-9, Z-29 |

## 2. Named individuals: the firewall

**Nobody on this list is named as a suspect, participant, or person of
interest in any public document.** Several are confirmed victims. Several are
confirmed uninvolved.

| Party | Public posture | Ref |
|---|---|---|
| **The named holder of the solicited account** | **DO NOT NAME.** Status UNDETERMINED. Recruited mule, identity-theft victim, and operator all fit the evidence equally | Z-4, Z-12 |
| The individual associated with a stale published phone number | Do not name. Probable uninvolved third party | V-4 |
| The co-tenant technology business cleared at S-7 | Do not name. **CLEARED.** Publishing the co-tenancy would defame a working business | S-7 |
| The Arizona breeder whose website was appropriated | Do not name. Victim of website appropriation, not yet notified | A5c |
| Person depicted in `fb_026614` | Do not name or describe. May be operator or image-theft victim, indistinguishable | X-1b |
| Persons in `fb_358582` | Do not name, describe, or depict | G, M-1, W-3 |
| The eight breeder and rescue organisations whose imagery was stolen | Named only as **image-theft victims**, never as participants. Seven of eight are still unnotified (Y-5); check status before naming at all | H-1/H-3/H-4, A5-1, A5-2, Y-5 |
| Any third party inside a victim's message thread | Redact | Y-6a |

**The operator side of a published conversation is fair game. The victim side
belongs to the victim. Everyone else in the frame belongs to themselves.**

## 3. The three complainants: pseudonymous in v1

The three complainants consented to public attribution
(Y-6). **Version 1 of the public corpus does not use their names anyway.**

Use **Complainant A**, **Complainant B**, **Complainant C**. Consistently, with
the mapping held only in the private law-enforcement package.

The reasoning is recorded at Y-6: consent given in the first flush of anger
about losing money is real, but it is given without much sense of what it feels
like to be a searchable result attached to "puppy scam victim" for years.
Pseudonymity is reversible on their say-so. Publication is not.

**The investigator's own relationship disclosure (Y-2) still ships**, worded so
it does not identify which complainant is involved.

### 3a. The forwarder invariant

**Never attach the forwarding of the opening material to a complainant letter.**

Y-2's sanctioned sentence says the compiler is acquainted with one complainant
"who forwarded the initial material". That clause is safe **only** while no
public document says which lettered complainant forwarded anything. The moment
one does, the clause resolves, and it resolves retroactively across every brief
that carries it, all at once.

So the protection is not the wording. It is this:

| Safe | Never |
|---|---|
| "one of the complainants, who forwarded the initial material" | "Complainant B forwarded the opening images" |
| "the material that opened this investigation" | "Complainant A supplied the first screenshots" |
| "a complainant provided the initial thread" | any sentence pairing a letter with providing, forwarding, supplying or opening |

The standard disclosure, and the reference wording:

> The compiler of this file is personally acquainted with one of the named
> complainants, who forwarded the initial material. Which complainant is not
> stated here and is not derivable from anything published in this corpus. All
> infrastructure findings are independently verifiable from the captures and
> hashes provided (Y-2).

**Two elements are required. The exact words are not.** An earlier version of
this section demanded the sentence verbatim, which was a drafting error: it is
unenforceable without forcing bad prose, since a brief that is genuinely a
record should say "this record" and not "this file". Requiring words nobody can
enforce produces silent drift, which is precisely what happened.

| Required element | Why |
|---|---|
| **The acquaintance is disclosed** | An analyst who discovers an undisclosed relationship discounts everything around it (Y-2) |
| **Which complainant is stated to be unidentified and underivable** | This is the sentence doing the protective work. Without it the first element narrows the field |

Wording may vary. Both elements must be present in **every standalone brief**,
because each ships as its own PDF and a reader who sees only one document must
still get the disclosure.

**No brief may state the clause twice.** A duplicated "who forwarded the initial
material, who forwarded the initial material" reads as careless in a document
whose entire claim is care. The duplication spans a line break in practice, so
single-line greps miss it and the gate checks it across lines.

`scripts/redaction-check.sh` enforces the invariant, not the wording.

## 4. Claims discipline

Public documents inherit the same evidentiary standard as the private record.

| Rule | Detail | Ref |
|---|---|---|
| **No victim-payment claim** | It is **not established** that any victim paid the solicited account. Do not write, imply, or diagram otherwise | Z-12, Z-18 |
| **No dollar-scale figure** | The corpus does not support an aggregate loss estimate. Argue productization and measurable deployment count instead | D13, Z-18 |
| **Provisional stays provisional** | Z-8 and Z-9 conclusions are provisional pending the Meta export. Label them | Z-14, Z-29 |
| **Label opinion** | `BRIEF-04` and `BRIEF-05` may draw conclusions. Each must carry a visible marker that it is analysis or opinion, not evidence | |
| **Unverified is a word we use** | Anything outrunning its evidence is tagged `UNVERIFIED` or `HYPOTHESIS`, per `CONTRIBUTING.md` line 15 and A5.1 | |

## 5. What IS safe to publish

So this does not read as a wall of no. All of the following are cleared:

- Domain names, page IDs, TikTok handles, and the Tawk.to property ID
- The `(demo)` template artifacts and the published demo-credential string
- Stolen-image **provenance analysis**, described in words, without reproducing the images
- Registry timelines, WHOIS and RDAP dates, hosting relationships
- The persona-pool analysis, using the operator-side persona names
- Every SHA-256 in `MANIFEST.csv` and `EXPORT_MANIFEST.txt`
- Methodology, tooling, and contamination controls
- The page-recycling finding, including page `1179239581941044` and its rename history
- The bank **name and routing number** (institution-level, publicly listed), but **not the account number**

## 5a. Where the literals live

**This contract is published.** It therefore names categories, not the strings
themselves. An earlier version listed every forbidden literal inline, which made
the one document exempted from the gate the document that published what the
gate protects.

The exact strings and private mappings live in `scripts/redaction-fixtures.private.json`,
which is never copied into the public bundle. The gate loads them from there and
**refuses to run if that file is missing or any section is empty**, because a
gate that cannot load its own rules must not report PASS.

## 6. Verification gate

Before any public artifact ships:

1. Run `scripts/redaction-check.sh`. It fails closed on every literal in
   sections 1 and 2.
2. A human reads the diff against this contract. Automation catches literals;
   it does not catch a paraphrase that identifies someone.
3. The release PR on the sister repo is approved by the investigator.

**A redaction miss is not a bug you fix in the next release. It is permanent
the moment it is public.**
