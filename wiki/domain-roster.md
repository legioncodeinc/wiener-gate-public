# Domain Roster

> Category: Public Wiki | Version: 1.0 | Date: August 2026 | Status: Active

Every domain attributed to this operation, with registry dates, registrar, hosting and current status where those are known, plus an explicit account of which domains were deliberately left out of this page.

**Related:**
- [`network-at-a-glance.md`](network-at-a-glance.md) - how these domains relate to each other
- [`indicators.md`](indicators.md) - the same infrastructure in indicator form
- [`verify-our-work.md`](verify-our-work.md) - how to re-run these lookups yourself
- [`who-is-not-a-suspect.md`](who-is-not-a-suspect.md) - why the image-theft victim domains are not listed here
- [`glossary.md`](glossary.md) - RDAP, WHOIS, registrar, nameserver, typosquat
- [`../briefs/BRIEF-01-law-enforcement.md`](../briefs/BRIEF-01-law-enforcement.md) - the registrar and host abuse routes
- [`../briefs/BRIEF-03-technical-analysts.md`](../briefs/BRIEF-03-technical-analysts.md) - reproduction steps for the registry work

---

## 1. How to read this page

Classification is deliberately conservative. When a domain is ambiguous it is called a candidate or noise, not network (D12).

| Status | Meaning |
|---|---|
| **NETWORK** | Infrastructure attributable to the operation. Each still warrants independent confirmation |
| **CANDIDATE** | Matches the pattern, not yet fully verified. Treat as `UNVERIFIED` |
| **DEAD** | RDAP returns 404. The registration has lapsed or been deleted |
| **MAIL-ONLY** | The website is gone, the mail capability is live |

Registry dates come from Verisign RDAP lookups and live authoritative DNS queries run 2026-08-24 (R-1, R-2, R-3). **RDAP and authoritative DNS are registry-attested and operator-controlled respectively. Neither is user-editable narrative, so both are higher-grade evidence than anything written on a website** (R).

Everything on this page is a domain name, which the redaction contract clears for publication (contract section 5). No hosting relationship listed here identifies a person.

## 2. The registry timeline

This is the spine of the scale argument, and it is the one table to read if you read only one.

| Domain | Created (registry) | Expires | Registrar | Role | Status |
|---|---|---|---|---|---|
| `royalpawscompanions.com` | 2026-04-03 16:52:32Z | 2027-04-03 | HOSTINGER operations, UAB | Storefront | NETWORK, live at capture |
| `globaltransit-logistics.com` | 2026-06-15 17:01:13Z | 2027-06-15 | HOSTINGER operations, UAB | Shipping front 1 | NETWORK, MAIL-ONLY |
| `evergreencompaniondogs.com` | 2026-07-09 08:56:27Z | 2027-07-09 | HOSTINGER operations, UAB | Storefront | NETWORK, live at capture |
| `safepup-delivery.com` | 2026-07-28 21:53:10Z | 2027-07-28 | HOSTINGER operations, UAB | Shipping front 2 | NETWORK, live at capture |
| `usapetsforhome.com` | 2026-08-18 12:18:40Z | 2027-08-18 | Realtime Register B.V. | Storefront | NETWORK, live at capture |

**All five are one-year registrations, the standard disposable-asset term** (R-1).

Three findings sit in that table.

**Continuous replacement.** A storefront or a front is registered every four to ten weeks across a five-month window. The newest storefront was registered six days before the file was compiled (R-1).

**The shipper was stood up to serve a running storefront.** The first shipping domain was registered roughly ten weeks after the first storefront and roughly three weeks before the second, then survived into the next storefront's lifecycle. One shipper, two consecutive breeder brands (R-1).

**The build order is recoverable to the minute.** Eleven images were uploaded to the newest storefront in a continuous 93-minute session finishing **34 minutes before the domain was registered** (U-4). The content was harvested first and the domain bought second.

## 3. Deregistered domains

RDAP returns 404 (not registered) for these. Live DNS confirms no nameserver, no address, and no mail exchange records. These are not merely offline sites: **the registrations are gone** (R-2).

| Domain | Former role | Status |
|---|---|---|
| `smhomeraiseddachshunds.com` | Original brand storefront, the domain that opened this investigation | DEAD, RDAP 404 |
| `abkcamericanbullypuppies.com` | Cross-linked second brand, appeared in the original brand's footer | DEAD, RDAP 404 |
| `pauldachshundhome.com` | Name-family storefront | DEAD, RDAP 404 |

**Consequence, and it governs the whole collection posture:** the burn cycle on a brand domain is short enough that a domain named in the record on one day can be unregistered the next. Anything still resolving must be archived on sight, not scheduled (R-2).

## 4. Shipping and courier fronts

| Domain | Status | Detail |
|---|---|---|
| `safepup-delivery.com` | NETWORK, live at capture | 48 files captured and hashed. Publishes its template vendor's demonstration credentials on a public admin login page, and ships the string `(demo)` in the footer in English and German (T-1, S-2, T-9) |
| `globaltransit-logistics.com` | NETWORK, MAIL-ONLY | HTTP 404 at the host. Mail exchange records live, sender policy published, certificate renewed ten days before capture and running to 2026-11-12. **Treat as an active sending address** (R-3) |
| `safepupdelivery.com` (unhyphenated) | **NOT REGISTERED** | The second shipping front publishes a business email at this domain. RDAP 404, no nameserver, no mail exchange, no address record. **Mail to the published business address is undeliverable** (S-5) |
| `aozora-delivery.com` | CANDIDATE | Same `-delivery.com` naming family. Not independently verified (D12) |
| `onayami-delivery.com` | CANDIDATE | Same family. Not independently verified (D12) |
| `rush-delivery.com` | CANDIDATE | Same family. Not independently verified (D12) |
| `yalla-delivery.com` | CANDIDATE | Same family. Not independently verified (D12) |

**Two generic domains were removed from this family list.** `delivery.com` and `logistics.com` appeared in the raw extraction as substring artifacts. Both are or may be real unrelated businesses and neither is asserted as network infrastructure (D12).

A hosting-provider content delivery edge hostname for the second shipping front also appears in the raw extraction. It is provider infrastructure, not a separately registered asset.

## 5. Hosting and nameserver detail

| Domain | Apex address | Nameservers | Mail |
|---|---|---|---|
| `royalpawscompanions.com` | 77.37.34.75 | `pixel` and `byte` at `dns-parking.com` | Hostinger |
| `evergreencompaniondogs.com` | 77.37.34.75 | `nebula` and `aurora` at `dns-parking.com` | Hostinger |
| `globaltransit-logistics.com` | 77.37.34.75, plus an IPv6 record | `ns1` and `ns2` at `dns-parking.com` | Hostinger, sender policy published, DMARC set to monitor-only |
| `safepup-delivery.com` | 2.57.91.196, 84.32.84.119 | `hyperion` and `atlas` at `dns-parking.com` | Hostinger |
| `usapetsforhome.com` | Vercel | `ns1.vercel-dns.com` | Spacemail, with a published DKIM key |

### The shared-address caution, in full

**Do not cite the shared address 77.37.34.75 as proof of common control.** This claim was made, tested, and narrowed twice (R-4, S-6).

- The address carries 48 or more co-hosted domains, so co-residency there is close to meaningless on its own (R-4).
- The three domains use **three different nameserver pairs**. The provider assigns pairs per hosting plan, so three distinct pairs is consistent with three separate hosting purchases, not one account holding three domains (R-4).
- The address is a shared **file-transfer gateway**, not a web host. Of roughly 87 co-tenancy entries, the overwhelming majority are `ftp.` hostnames whose apex resolves elsewhere entirely (S-6).
- One storefront is on a completely different stack: different registrar, different host, different nameservers, different mail provider (R-4).

**The narrow observation that survives:** three domains have their apex address, not merely their file-transfer hostname, on that gateway, and they serve live content from it, while every other tenant uses it only for file transfer. That is tighter and more unusual than the raw list suggested, and it is how it should be stated (S-6).

**The A-to-A linkage rests on the persona reuse at the content layer, not on the address** (R-4). An analyst who tests the address claim and finds shared hosting will discount everything downstream of it.

## 6. Storefront candidates, pattern-matched and unverified

These match the naming and structural pattern but have **not** been individually verified by registry, hosting, or content review. Every one is `UNVERIFIED` and none should be characterised as network infrastructure without independent confirmation (D12).

| Domain | Note |
|---|---|
| `homeraiseddachshunds.com` | Original brand name family |
| `smhomeralseddachshunds.com` | Typosquat or optical-character-recognition variant of the original brand domain |
| `happydachshundfamily.com` | Name family |
| `happydachshundhome.com` | Name family |
| `pagesdachshunds.com` | Name family |
| `poeticfrenchbulldogs.com` | Pending review (A4-7) |
| `royalpawsmaltese.com` | Brand extension beyond the documented "Royal Paws" storefront |
| `eliteyorkiesandbiewers.com` | Pattern match |
| `superstarpuppiesraleigh.com` | Pattern match |
| `kimberliskuties.com` | Pattern match |
| `prettiestsppuppies.com` | Pattern match |
| `thebernedoodles.com` | Pattern match |
| `buildempire.land` | Adjacent cluster, role unclear |
| `empirelandsolutions.com` | Adjacent cluster, role unclear |

## 7. Card-harvest storefront family

A cluster of short throwaway `.click` domains operating as card-harvesting storefronts (D12).

`adfreetvmk.click`, `adfrestmk.click`, `banbestmk.click`, `chubfreecxzd.click`, `dkmlovemk.click`, `goodmecar.click`, `goodzhuostu.click`, `ikloveov.click`, `loveisleet.click`, `lufasaletrt.click`, `tsalessm.click`, `ufasaletrt.click`, `wclovertsh.click`, `wowlovervs.click`

One domain in this family is the subject of the single disclosed contamination event in this investigation. See [`methodology.md`](methodology.md) section on contamination controls.

## 8. Payment and hosted-commerce layer

| Asset | Note |
|---|---|
| `pekira.de` | European payment-adjacent domain with a registered entity behind it (A3h) |
| `nv6w2d-tj.myshopify.com` | Hosted-commerce shop, documented alongside redirect evidence (A3g) |
| `aliou-store-5.myshopify.com` | Hosted-commerce shop. The subdomain contains a given name matching an admin-layer handle observed elsewhere in the corpus, and the sequential `-5` suffix implies sibling stores exist. **This is a string observation about a domain, not an identification of a person.** See [`who-is-not-a-suspect.md`](who-is-not-a-suspect.md) |

One further hosted-commerce shop carrying an unverified personal-sounding name has been withheld from this page. It is `UNVERIFIED`, and publishing an unconfirmed shop bearing what may be a real person's name would be exactly the error this corpus is built to avoid.

## 9. What is deliberately not on this page

Three categories were removed, and saying so is part of the record.

**Image-theft victim domains.** Roughly thirty real breeder, rescue, and stock-photography domains appear in the raw extraction because their photographs or names were stolen. They are **victims, and seven of the eight primary entities have not yet been notified** (Y-5, D12). Publishing a victim's domain on a fraud-investigation page tells the internet before it tells them, and permanently attaches their business to the phrase "puppy scam" in search results. They are named only in the private notification tracker. See [`who-is-not-a-suspect.md`](who-is-not-a-suspect.md) section 3b.

**Co-tenant noise.** Roughly a dozen unrelated businesses share the file-transfer gateway described in section 5. They surfaced only through reverse-address lookup and are innocent bystanders unless independently linked. **None has been linked.** They are excluded from network claims and are not named here (D12, S-7).

**Tooling, platform, and investigator-owned domains.** Search engines, content delivery networks, generic mail providers, the open-source tools used during the investigation, and the investigator's own business domains all appear in a raw extraction of every domain string in the corpus. All are noise and all are excluded (D12).

## 10. Scale, stated honestly

The raw extraction produced 236 unique domain strings. After noise removal the in-corpus slice is roughly **90 candidate domains** (D12).

A larger investigator-tracked total exists across sessions. **The enumeration reconciling the two is in progress and is not complete.** The standing instruction for any filing or article is to cite the confirmed count that can actually be enumerated, and to label the larger figure as investigator-tracked with enumeration in progress (D12). This page follows that instruction, and no aggregate scale claim here should be quoted beyond it.

## 11. Reproducing this

Every row in section 2 and section 3 can be re-derived from public registry data in a few minutes.

```bash
# Registry record, creation and expiry dates, registrar
curl -s https://rdap.verisign.com/com/v1/domain/royalpawscompanions.com | python3 -m json.tool

# A deregistered domain returns HTTP 404 from RDAP
curl -s -o /dev/null -w '%{http_code}\n' \
  https://rdap.verisign.com/com/v1/domain/smhomeraiseddachshunds.com

# Live authoritative DNS: nameservers, address records, mail exchange
dig +short NS royalpawscompanions.com
dig +short A  royalpawscompanions.com
dig +short MX globaltransit-logistics.com
dig +short TXT globaltransit-logistics.com
```

**Read only.** Do not submit anything to any of these hosts. The contamination controls in [`methodology.md`](methodology.md) apply to readers of this corpus exactly as they applied to the investigation.

Registry state changes. Several rows above will drift, and domains going dead is itself a finding rather than a broken link. [`changelog.md`](changelog.md) records the drift.
