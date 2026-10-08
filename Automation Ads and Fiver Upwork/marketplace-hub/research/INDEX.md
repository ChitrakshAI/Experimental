# Research index

Four files. Every strategic claim in `STRATEGY.md`, every mechanic in the playbooks, and every benchmark in `ads/ads-plan.md` traces back to one of them. They are cited by section, as `marketplace-expansion.md §2.12`, rather than by URL, because the URLs are inside the files and repeating them in every document would make all of them unreadable.

These are **copies**, taken 11 September 2026 from `/home/claude/research/`. They are frozen at that date. A number read off a platform after that date beats a number in here, and when the two disagree the ledger gets the new reading with its date and the file gets a note, never a silent edit.

---

## `marketplace-expansion.md` (120 KB)

The Upwork, multi-account, ads, channels, monitoring and operating-model report. Eight sections. Section 1 maps the Upwork market: 127,607 deduplicated public job postings in June 2026, one every 20 seconds, AI category GSV up 50% year over year, and the counts that matter to us, with 13,000+ open jobs across cold calling, outbound sales, lead generation and appointment setting, currently filled by human VAs at $6 to $20 an hour. It also carries the reality check: median posted budget $100, median effective hourly rate about $8.75, 24.0% of postings with unverified payment. Section 2 is the mechanics, and it is the densest part of the whole pack: Connects at $0.15 each, the boost auction settling on your own bid, Rising Talent at $250 earned against Fiverr's Success Score 7 for Briefs, the JSS windows and the private-feedback weighting, specialized profiles, Project Catalog, and the proposal data measured across 133,872 proposals where zero clichés reply at 7.55% and four or more reply at 0.00%. Section 3 quotes the one-account clauses on both platforms verbatim with their consequences, and derives the three-entity structure we actually use. Section 4 is the paid surface: Promoted Gigs eligibility and CPC, Seller Plus Kickstart, boosts, the Availability Badge, Fiverr's explicit permission for external paid traffic, the honeymoon window, the Meta, Google and LinkedIn benchmark table, and three budget plans at $300, $1,000 and $3,000. Section 5 grades twelve other channels yes, later or no. Section 6 is the monitoring specification this hub's daily check is built from, including where each number lives in each UI and the seven leading indicators ranked by how early they move. Section 7 is the 30-day operating model and the case-study protocol. It closes with seven stated research limitations, which is the part to read before treating any single number as settled.

**Feeds:** `STRATEGY.md` in its entirety, `playbooks/upwork-proposal.md`, `playbooks/upwork-account-setup.md`, `ads/ads-plan.md`, `ads/campaigns.json`, `monitoring/daily-check.md`, `accounts.json` tos_notes.

---

## `fiverr-market.md` (66 KB)

The Fiverr market analysis that came first and set the positioning. It maps the category taxonomy that actually exists, counts exact "services available" figures per keyword, and finds the shape the whole strategy rests on: the tool keywords are saturated at the floor, with 12,823 to 14,986 services anchored at $10 to $90, while the vertical keywords are empty, with `car-dealership` carrying 2,699 services and `insurance` 3,445, neither containing any AI voice supply at all. Section 4 is the algorithm and the level system with its real thresholds, including the Level 2 gate at 20 orders from 10 unique clients that locks the Briefs inbound channel, and section 4.5 lists what actually gets AI gigs denied. Section 5 is a competitor teardown of eight top-ranking gigs, and it produces the single most important pricing finding in the pack: a Top Rated seller holds slot one on a 44,698-service keyword at $1,800 with two reviews, while a seller with 742 reviews at $40 cannot reprice out of it. **Price and credential outrank review count, and a low anchor is permanent.** Section 6 is the recommended positioning and the three gigs to launch, with titles, categories, tags, packages and the reasoning behind each.

**Feeds:** the Fiverr half of `STRATEGY.md` sections (a) and (b), the gig definitions in `accounts.json`, `playbooks/fiverr-gig-build.md`, the level thresholds in `monitoring/daily-check.md`.

---

## `fiverr-profile-package.md` (65 KB)

The paste-ready copy, field by field, written against verified field limits. Section 0 lists those limits, which is why the copy fits on the first attempt. Section 1 is the account: username options, display name, tagline, profile description, languages, skills, education, certifications, photo direction and a 45 to 60 second intro video script. Sections 2, 3 and 4 are the three gigs in full, each with title and exact character count, category path, service-type metadata, five search tags, three packages, the gig description, seven FAQs, buyer requirements, gig extras, a 55 to 60 second video script, and three gig image headlines with sub-lines. Section 5 is six portfolio projects with their status labels and their source files, plus an explicit list of what is deliberately excluded because it is unverified. Section 6 is the 14-day launch sequence to five orders, including the four traffic sources we control and the first-order pricing tactics that do not anchor low. Section 7 is a risk checklist.

**This is the file a fresh session opens to resume the browser work.** Gig 2's description, FAQs and requirements are in section 3. Gig 3, which has not been started, is in section 4 in full.

**Feeds:** every gig field, the portfolio build in `playbooks/upwork-account-setup.md` step 7, the end-card lines reused in `ads/creative-briefs.md`, the resume points in `NEXT-SESSION.md`.

---

## `oraya-facts.md` (33 KB)

The ground truth. Everything factual about the product, extracted directly from the two mounted source folders, with each claim labelled measured, target, or unverified. Section 1 is the product and the measured metrics: **median 761 ms time-to-first-audio on the reference dealership demo over simulated calls on 26 August 2026**, against a prior vendor's production baseline of **p50 approximately 1.64 s outbound and 1.9 s inbound across 17 archived calls**, plus the per-stage latency budget, the cost bands, and a short, blunt list of known limitations. Its most valuable paragraph is the one that says **answer rate, booking rate and calls handled at scale are not measured anywhere in the repo and must not be claimed**, which is the line that keeps every other number in this hub defensible. Section 2 is the case studies with honest status labels. Section 3 is the proof assets with file paths and sizes. Section 4 is the brand. Section 5 is the writing rules, quoted, which are inherited by every file in this folder. Section 6 is the pricing and offer structure, including the Compliance-Safe AI Audit lead magnet and the explicit finding that no confirmed client-facing price list exists, which is why the Fiverr and Upwork ladders were priced independently rather than copied from a rate card that does not exist.

**Feeds:** every number quoted anywhere in this hub, the writing rules in `README.md`, the anonymisation rules in `playbooks/case-study-capture.md` and `STRATEGY.md` section (h).

---

## `gig-images/`

Eleven rendered PNGs: three per gig at 1280 x 769, plus a cover and a contact sheet. Brand palette, and every figure printed on a frame carries its source and read-date on the same frame. They are the Fiverr gig images, the Upwork portfolio visuals and the paid-ad creatives, all three, which is why `ads/creative-briefs.md` reuses them rather than commissioning anything new: a new creative made from scratch would be a new claim with no verification behind it.
