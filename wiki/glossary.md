# Glossary

> Category: Public Wiki | Version: 1.0 | Date: August 2026 | Status: Active

Every term a reader will hit in this corpus, defined in plain language: the investigation's own status vocabulary, the forensic and infrastructure terminology, the financial-crime and regulatory language, and the jargon the operation itself uses.

**Related:**
- [`index.md`](index.md) - the overview these terms describe
- [`methodology.md`](methodology.md) - where the classification vocabulary comes from and why
- [`indicators.md`](indicators.md) - the indicator sheet these status tokens appear in
- [`verify-our-work.md`](verify-our-work.md) - SHA-256, Object Lock and append-only in practice
- [`who-is-not-a-suspect.md`](who-is-not-a-suspect.md) - UNDETERMINED and CLEARED, applied to people
- [`../briefs/BRIEF-02-victims.md`](../briefs/BRIEF-02-victims.md) - the money-recovery terms, written for people who need them today
- [`../briefs/BRIEF-05-media-public.md`](../briefs/BRIEF-05-media-public.md) - the same vocabulary for a general audience

---

## 1. The corpus vocabulary

These are not generic words. They mean specific things in this record, and the difference between two of them is often the difference between a finding and a guess.

### Evidence-confidence labels

**UNVERIFIED**
A claim that outruns its evidence. It is recorded because it may matter, and labelled because nothing currently supports it. An unverified claim must never be quoted as a finding (CONTRIBUTING, A5.1).

**HYPOTHESIS**
An inference from circumstances, stated as an inference. Distinct from `UNVERIFIED` in that a hypothesis proposes a specific explanation and names what would confirm it. Example: the read that a particular bank account was opened remotely was relabelled from a finding to a hypothesis because no know-your-customer record supports it, and an in-person opening is not excluded by anything in the file (Z-13).

**PROVISIONAL**
A finding that is probably correct but rests on an artifact not yet filed and hashed. It is stated as provisional until the supporting artifact is in the corpus. Two findings in this case carry the label, along with a timing figure computed from one of them (Z-14, Z-8).

**ESTABLISHED**
Supported by a filed, hashed artifact or a registry-attested record. The default expectation for anything published without a qualifier.

**NEGATIVE RESULT**
A finding that weakens or shrinks the case. Retained deliberately. Some are *probative* negatives, meaning the absence itself proves something: a sweep across 98 photographs found zero image reuse between accounts, which proves large harvesting volume and deliberate detection avoidance rather than proving nothing (K-4, HANDOFF section 2d).

### Party status taxonomy

| Token | Meaning |
|---|---|
| **SCAM-INFRA** | Infrastructure attributable to the operation: a domain, a page, a handle, a template string |
| **STOLEN-CONTENT** | Material taken from a real person or business |
| **AI-ASSET** | Machine-generated content: a logo, a persona photograph, a testimonial |
| **UNDETERMINED** | The evidence genuinely does not distinguish between innocent and involved. **A real status, not a placeholder for "probably guilty"** |
| **LIKELY-VICTIM** | Assessed as harmed by the operation rather than part of it |
| **CLEARED** | Actively investigated and excluded. Not merely unexamined |

(CONTRIBUTING, HANDOFF section 2a)

### Interaction classification

Applied to every contact between the investigation and any surface in the case. The full decision procedure is in [`methodology.md`](methodology.md).

**PASSIVE**
Reading a publicly served page. No login, no form, no submission, **and login state positively known to be logged out**. That last precondition is strict: an interaction recorded as anonymous but not confirmed is `UNRESOLVED`, not `PASSIVE` (INTERACTION_LOG Amendments 2.1, 3.1).

**ACTIVE-OUT**
Something sent by the investigation **to** the operation: a form, a message, a cart, a login attempt, a payment. **This is investigator conduct, and it is what a defence can attack.**

**ACTIVE-IN**
Something sent by the operation **to** the investigator, in a channel the investigator is party to. **This is operator conduct, and it supports the case.** The distinction from `ACTIVE-OUT` is the whole reason a bare `ACTIVE` label was retired (INTERACTION_LOG Amendment 2.1).

**ACTIVE-3P**
Contact with a third party *about* the operation: an abuse desk, a registrar, a bank, a blocklist submission. Not contact with the operation.

**UNRESOLVED**
The facts needed to classify are not recoverable from the record. Six of the nine entries in the interaction log carry this label. **It is a final answer, not a to-do item**: where a fact is genuinely unrecoverable, guessing to close the field damages the record (INTERACTION_LOG Amendment 3.4).

### Corpus conventions

**Append-only**
No file in the evidence tree is ever edited, renamed, re-encoded, or re-saved. Corrections are appended as amendments so a reader can see what was believed at each point and what changed (CONTRIBUTING).

**Complainant A, Complainant B, Complainant C**
The three people who lost money and came forward. They consented to public attribution, and version 1 of this public corpus uses pseudonyms anyway. The mapping is held only in the private law-enforcement package (Y-1, Y-6, redaction contract section 3).

**Firewall**
The rule that a name never moves from the victim column to the suspect column without new evidence, and the exclusion list that enforces it (HANDOFF section 2a).

**Contamination**
Any interaction that puts investigator-originated traffic or data onto an operation's surface, creating both a signal to the operators and an argument that the record is polluted (W-1).

**Chain of custody**
The documented history of an artifact from capture onward: hashed before any move, moved without modification, re-hashed after, never altered (J, L).

## 2. Investigation and digital forensics

**SHA-256**
A cryptographic hash: a fixed-length fingerprint of a file's exact bytes. Change one byte and the fingerprint changes completely. Publishing a file's SHA-256 lets anyone confirm the file they hold is the file that was captured. It proves the bytes are unchanged; it proves nothing about what the bytes mean.

**Manifest**
A list pairing every file with its hash. This corpus has three, with different scopes. See [`verify-our-work.md`](verify-our-work.md).

**ELA (Error Level Analysis)**
A technique that re-saves a JPEG and visualises where compression error differs across the image, on the theory that edited regions compress differently. It produces suggestive pictures and is widely over-read. **In this corpus ELA is explicitly corroborative only, never probative** (M-2).

**Perceptual hashing (pHash) and difference hashing (dHash)**
Fingerprints designed to stay similar when an image is resized or re-encoded, unlike SHA-256 which changes completely. Used to find the same photograph reused across different accounts. A sweep across all 98 photographic files in this corpus found **zero** cross-account reuse (K-4).

**EXIF**
Metadata embedded in a photograph by the camera or software: date, camera model, sometimes location. Most platforms strip it on upload, which is why only three files out of 140 retained any (K-1). One retained intact camera metadata (K-2).

**C2PA (Coalition for Content Provenance and Authenticity)**
An open standard that cryptographically signs a media file with its origin and edit history, so a viewer can check where an image came from and what was done to it. Useful only on files that have not passed through a platform that strips metadata, which is why a provenance check in this case is limited to assets that never went through a social platform (HANDOFF section 5 item 18).

**Dork**
A precise search-engine query built from a distinctive string, used to enumerate every page containing it. The highest-yield candidate in this case is the published demonstration-credential string from a website template, which may enumerate every deployment of that template across every vertical (T-1, HANDOFF section 5 item 9).

**Red team / second-look review**
Deliberate adversarial review of an investigation's own conclusions by someone trying to break them. This record has been through six rounds, and the corrections are listed in [`changelog.md`](changelog.md).

## 3. Internet infrastructure

**WHOIS**
The long-standing protocol and record format for domain registration data: who registered a domain, when, through which registrar, and when it expires. Largely redacted for privacy since GDPR, but registration and expiry dates remain public.

**RDAP (Registration Data Access Protocol)**
The modern, structured replacement for WHOIS. Returns registration data as JSON over HTTPS, with proper support for access control. **RDAP records are registry-attested, meaning the registry itself vouches for them, which makes them higher-grade evidence than anything an operator writes on a website** (R). An RDAP response of HTTP 404 means the domain is not registered at all. Three domains in this case return 404 (R-2).

**Registrar**
The company a domain is bought through. Distinct from the host, which is where the website's files live. A single registrar can be a single point of leverage: one registrar in this case covers four of the network's domains and has one abuse desk (S-9).

**Nameserver**
The servers authoritative for a domain's DNS records. Hosting providers typically assign nameserver pairs per hosting plan, which is why three domains showing three *different* pairs argues for three separate hosting purchases rather than one account holding three domains (R-4).

**MX, SPF, DKIM, DMARC**
Mail records. `MX` says which servers receive mail for a domain. `SPF` declares which servers may send as it. `DKIM` signs outbound mail. `DMARC` states what to do when the first two fail. Their relevance here is direct: one domain's website is gone while its `MX` records are live, its `SPF` is published, and its certificate has been recently renewed. **That is a working mailbox, not a dead asset** (R-3).

**Co-tenancy**
Multiple unrelated domains sharing one server address. **Close to meaningless as evidence on its own**: the shared address in this case carries 48 or more tenants, and treating co-residency as linkage was formally withdrawn (R-4, S-6).

**FTP gateway**
A shared file-transfer endpoint provided by a hosting company, distinct from the servers that actually serve websites. Discovering that the "shared IP" in this case was a file-transfer gateway rather than a web host is what narrowed the linkage claim twice (S-6).

**Typosquat**
A domain registered as a near-miss of a real one, relying on misreading or mistyping. Several appear in the extracted domain list (D12).

**Sock page**
A low-follower social page created to impersonate or borrow credibility from a real business. One documented example points itself at a legitimate breeder's website while having two followers (A5c, B-13).

**Page recycling**
Creating or acquiring a social page for one purpose, then repeatedly renaming and repurposing it. The renamed page inherits the original's age and audience, which platforms and buyers both read as legitimacy. Documented as **standard operating practice** in this network, not an isolated case (N-1, B-15).

**Persona pool**
A reusable set of fabricated identities, names, testimonials, and photographs, drawn from repeatedly across different sites. **The persona pool is the durable linkage in this case**, because it survives every infrastructure correction (Q-5, S-3, U-7).

**Template artifact**
Text or an asset left in place from a purchased website template that the buyer never edited: demonstration credentials, a `(demo)` badge, a placeholder contact address, a statistics counter reading zero. **The single cleanest exhibit class in this case, because it requires no interpretation** (T-1, S-2, N-2).

**Shipper front**
A fake courier or pet-transport company, operated by the same people as the storefront, existing to justify escalating fees after a deposit is taken. This network has run two consecutively (Q-6, R-1, S-1).

**Impressum**
A legally mandated disclosure page identifying a website's operator: company form, registration number, VAT identification number, and a responsible person. **Under section 5 of the German Digital Services Act (DDG), providers of digital services offered commercially, and normally for payment, must publish one.** Not every site reachable from Germany is in scope; the obligation attaches to the commercial provision of the service.

Where it does apply, omitting or botching the disclosure is an administrative offence under section 33 DDG, carrying a fine of up to EUR 50,000. A competitor or a qualified association may also pursue it as a breach of market-conduct rules under section 3a UWG, but that civil route carries its own conditions, including that the breach noticeably impairs market participants and that the complainant has standing under section 8(3) UWG.

The reason it matters here is that it is a regulatory hook independent of the fraud: it needs no victim, no loss narrative, and no understanding of the wider network (T-5). Whether either route reaches a given site in this network is a question for German counsel, and this record does not answer it.

## 4. Money and financial crime

**Mule (money mule)**
A person whose bank account is used to receive and forward criminal proceeds. Mules range from knowing participants to people recruited under a false pretext, often a fake remote job, to identity-theft victims who never knew an account was opened in their name. **This is precisely why the holder of an account used by a fraud network cannot be assumed to be an operator** (Z-4). See [`who-is-not-a-suspect.md`](who-is-not-a-suspect.md) section 3j.

**Banking-as-a-service (BaaS)**
An arrangement where a chartered bank provides the regulated banking licence behind a consumer financial product built and operated by a separate technology company. The customer relationship may sit with the technology partner while the bank carries the legal obligations. Relevant here because a chartered bank's routing number paired with an overseas residential address suggests a sponsored program rather than a branch relationship. **That read is labelled a hypothesis, not a finding** (Z-3, Z-13).

**BSA/AML (Bank Secrecy Act / anti-money laundering)**
The United States regulatory framework requiring financial institutions to identify customers, monitor for suspicious activity, and report it. **The chartered institution carries the obligation regardless of which partner holds the front-end customer relationship**, which is what makes it the correct recipient of a fraud report either way (Z-3).

**Routing number**
A nine-digit code identifying a United States financial institution for wire and automated-clearing-house transfers. Publicly listed and verifiable against the Federal Reserve directory. The redaction contract clears the bank name and routing number for publication and forbids the account number (contract section 5, Z-2).

**Payment rail**
The specific mechanism money travelled on: wire, automated clearing house, a peer-to-peer payment app, a card, a gift card, cryptocurrency. **Recovery options differ completely by rail**, which is why a single generic "contact your bank" instruction is wrong and was corrected to a rail-specific table (Z-20).

**Recovery Asset Team (RAT)**
An FBI team that, on a qualifying report, contacts a receiving financial institution to attempt to freeze fraudulently transferred funds. **Eligibility runs on a clock that starts when the transfer happens.**

**Financial Fraud Kill Chain**
The FBI process for attempting to recall a fraudulent domestic wire transfer. Like the Recovery Asset Team, it is **time-bounded**, which is why transfer dates are recorded in this case as the single most urgent missing field (Z-5, Z-16).

**IC3 (Internet Crime Complaint Center)**
The FBI's public intake portal for internet crime complaints. **A victim-filed complaint is treated very differently from a third-party report**, and IC3 clusters related complaint numbers on its own side, so several linked victim complaints plus a supporting file is a materially stronger submission than one civilian report about several people (Y-3).

## 5. Platforms and legal process

**Page Transparency**
A Facebook panel disclosing a page's creation date, its full rename history, how many pages were merged into it, and its primary managing location. **Platform-attested rather than operator narrative**, which is what makes it usable evidence: it is how page recycling and a managing location were documented (N-1, B-15, A2-11).

**DYI export (Download Your Information)**
Meta's tool for exporting a user's own data, including a specific conversation thread. **A timestamped export is not comparable to a screenshot**, which is why victims are instructed to export their own threads immediately: if the operator blocks or deletes, the payment instructions in the operator's own words are gone permanently (Y-3).

**Preservation request**
A formal request asking a platform to retain records relating to an account. **Configuration changes do not delete underlying records.** When a network hardens its privacy settings mid-investigation, that is the argument for urgency rather than a reason to give up: friend lists, group history, administrator logs, address and device history, and message content all survive a settings change (X-2).

**DMCA takedown**
A copyright removal request. The only party with standing is the copyright holder, which is why image-theft victims are notified: **they can act where the investigation cannot** (Y-5, HANDOFF section 5 item 13).

**Abuse desk**
The channel a registrar, host, or platform maintains for reports of misuse. Often the fastest available remedy, and it requires no standing.

**Safe Browsing and blocklist submission**
Reporting a domain to browser and operating-system reputation services so users are warned. **The fastest harm reduction available and it requires no standing.** Worth noting that reputation services do not reliably catch this category: none of 91 engines flagged one of the network's domains (R-6).

## 6. Storage and archival

**Object Lock**
An object-storage feature preventing a stored file from being deleted or modified until a set date.

**Compliance mode**
The strict form of Object Lock. **It cannot be bypassed by any credential, including the account owner and the storage provider's own support staff**, until the retention date passes. This corpus is held in compliance mode until 2027-08-25.

**Retain-until timestamp**
The date an Object Lock expires. Checking only that the mode is "compliance" is insufficient, because a retention that had been shortened would pass a mode check while failing the custody requirement. The verification job therefore also enforces a minimum retention floor. See [`verify-our-work.md`](verify-our-work.md).

**age**
A modern file-encryption tool using public-key cryptography. The continuous-integration runner holds only the **public** key: it can encrypt and upload, and can never decrypt anything in the archive, including its own output.

## 7. The operation's own jargon

Terms a victim will have encountered, defined so that reading them in a message thread is recognisable rather than mysterious.

**Deposit / "secures your chosen puppy"**
The initial payment. One storefront's published copy asks $500 to reserve a puppy, with the balance due a week before pickup (U-8).

**Transport fee, crate fee, insurance**
The escalation ladder. After the deposit, a "shipping company" demands a transport fee, then a climate-controlled crate fee, then insurance, often described as refundable. Both ends of the ladder are the same operation on the same server (Q-6).

**Declared value**
The amount a buyer is induced to state the animal is worth. Insurance is then charged as a percentage of it, so the victim's own optimism sets the size of the next demand (T-8).

**Tracking number**
An operator-generated reference producing a live map, a moving aircraft position, a named coordinator, and a line reading "Payment Status: Paid". **This is the retention mechanism**: it is what keeps a victim believing and paying escalating fees for weeks instead of calling their bank on day three (T-3). Receiving one is an intake field, because it proves the shipper stage rather than merely the sale.

**IATA / IPATA**
Real bodies in the live-animal transport industry. One shipping front claims certification from one and accreditation with the other. **The certification badge ships with the word `(demo)` still attached, in both English and German** (T-2, T-9). Accreditation claims of this kind are checkable against public member directories, and a false claim is a discrete, provable misrepresentation independent of everything else (S-9, T-10).

**"Guardian Program"**
A second monetisation path advertised by one storefront, noted in the record as worth reviewing (U-9).
