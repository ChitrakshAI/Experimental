# Playbook: Upwork account and agency setup

The exact click path for three accounts, one agency, two specialized profiles, three Project Catalog listings, and the first week of bidding. Every rule quoted here is verified in `research/marketplace-expansion.md` sections 2 and 3, which carry the URLs.

**Read this before touching anything.** The structure is three entities and there is no grey area in it, but the order matters and two of the steps are irreversible in practice.

**The hard boundary, stated first because it is the only thing that can destroy the business:** neither founder ever logs into the other's account. Upwork: "You cannot log into someone else's account or let anyone log into your account and work or communicate on your behalf." Separate devices, separate browsers, separate payment methods, separate withdrawal accounts. The agency is the legitimate shared surface. The accounts are not.

---

## 0. What gets built, in order

| # | Entity | Owner | Day |
|---|---|---|---|
| 1 | Chitraksh personal freelancer account, India | Chitraksh | 1 |
| 2 | Frankie personal freelancer account, US | Frankie | 1 |
| 3 | Oraya Labs agency, created from account 1 | Chitraksh | 1 |
| 4 | Frankie added to the agency as business manager | Chitraksh invites, Frankie accepts | 2 |
| 5 | Two specialized profiles on account 1 | Chitraksh | 1 to 2 |
| 6 | Three Project Catalog listings mirroring the Fiverr gigs | Chitraksh | 2 |

**Why day 1 and not week 3.** Top Rated requires that the first project was more than **90 days ago**. The clock starts at the first project, so every day the account does not exist is a day later to the badge. Open it, verify it, complete it, even if serious bidding starts in week 2.

---

## 1. Chitraksh's freelancer account, India

1. Sign up at upwork.com as a freelancer, using the name used in everyday life and the real business address. Upwork: "The name on your account should be what you use to identify yourself in everyday life", "The address you provide should be your business address", and "We may restrict or permanently suspend your account if we cannot verify the information you provide."
2. **Complete identity verification the same day.** It is a hard prerequisite for Rising Talent and it gates nothing else usefully if left until later.
3. Submit the tax form. W-8BEN as a non-US person.
4. Add a withdrawal method. **This must be a method Frankie's account never touches.** A valid withdrawal method is also a Rising Talent requirement.
5. Complete the profile to **100%**. It is a Rising Talent prerequisite and 10% to 15% of the search algorithm. Photo, title, overview, skills, employment history, education, portfolio, languages, hourly rate.
6. Set the general profile headline: **Compliance-Aware AI Voice Infrastructure, TCPA and CIPA Gates Enforced in Code.** Compliance leads, because Information Security and Compliance replies at 11.21% against 7.21% for AI and Machine Learning.
7. **Populate the portfolio. This is the highest-leverage four hours of the month.** Six entries, the same set as the Fiverr portfolio in `research/fiverr-profile-package.md` section 5: the sub-second dealership build, the compliance panel, the two-persona handoff, the post-call extraction, and the two content pieces. PII-masked dashboard views only. No dealership, agency or client named. Every number carries its method and its date.
8. Record the **90-second Loom**: a live call on the demo line with the latency readout visible. Largest single measured proposal lift available at +3.70pp. Mask the dialed number in every frame.
9. Set status to Available. "Not Available" reportedly costs a 50% to 70% visibility reduction.
10. Log it.

```bash
python3 hub.py log --platform upwork --account TODO-chitraksh --entity account \
  --ref account --action created \
  --detail "Upwork freelancer account opened, India. Replace the handle in accounts.json with the real one." \
  --actor chitraksh
```

Then update `accounts.json`: replace `TODO-chitraksh` with the real handle, set `status` to `active`, set `created`, and move each `verification_state` entry as it clears.

---

## 2. Frankie's freelancer account, US

Same steps 1 to 6 and 9 to 10 as above, on **his own device, his own browser, his own payment method, his own withdrawal account**. Shared payment methods and shared devices are how linked accounts are detected.

Two differences:

- **US location verification.** This is the whole point of the account. Upwork: "If you choose U.S. only, then only freelancers in the U.S. will be able to see your post and submit a proposal." For every other country preference the restriction is soft. Frankie's account is the only key to that class of jobs.
- **Tax form is a W-9**, as a US person.

Headline: **AI Voice and Compliance Systems for Insurance Agencies and Dealerships, US-based.**

One standing copy rule on this account: Oraya never implies insurance licensure. Frankie's producer licence is his own credential and it is stated as his, with the boundary explicit.

---

## 3. The Oraya Labs agency

Created from Chitraksh's freelancer account, because only a freelancer account can create one and **"each freelancer can only create one agency on Upwork"**. Getting this wrong is not undoable in a tidy way, so read the whole section before clicking.

1. From Chitraksh's account, create the agency. Name: **Oraya Labs** (domain orayalabs.ai).
2. Subscribe to **Agency Plus**, about **$19.99/month**. This is required before any team member can be added. It "unlocks the ability to buy Connects; it does not hand you any". It also gives unlimited members, a custom agency profile URL, competitor bid visibility and Upwork Chat Pro, with no cap on business manager roles.
3. Complete the agency profile: overview, services, portfolio (the same anonymised set), and the agency rate. **Scope is the whole studio, not one vertical** (founder directive 2026-09-14): AI voice agents and telephony, agentic systems with real-world access, n8n and custom automation, CRM and back-office integrations, document review and risk flagging, local and private LLMs, compliance enforced in code. Dealerships and insurance appear as case studies and catalog listings, never as the top-level identity. Positioning block: `accounts.json` agency record `positioning`.
4. **Invite Frankie as a business manager.** Joining requires an invitation from the owner or an agency administrator. This is the structural key: "all agency members can submit proposals" and "Each proposal draws from the agency's collective balance of Connects", but **"Only business managers can accept an offer"**. Frankie can therefore bid US-facing on work Chitraksh delivers, legitimately, inside Upwork's own rules, and the commercial close sits with the sales lead.
5. Frankie accepts from his own account. His account stays private: "your account remains private and sign-in details must not be shared with the agency owner or any other party."
6. Note the money flow before the first contract: **"All contract earnings are paid to the agency's financial account on Upwork"**, and "Payments from agencies to agency members are not protected or facilitated by Upwork." The founder split therefore needs its own written agreement outside Upwork. Write it before the first contract closes, not after.
7. Note the exit case, so nobody panics later: on agency closure, completed contracts count toward each member's own Job Success Score in their individual freelancer account.

```bash
python3 hub.py log --platform upwork --account TODO-orayalabs-agency --entity account \
  --ref agency --action created \
  --detail "Oraya Labs agency created from Chitraksh's freelancer account. Agency Plus subscribed at about 19.99 a month." \
  --metric monthly_usd=19.99 --actor chitraksh

python3 hub.py log --platform upwork --account TODO-orayalabs-agency --entity account \
  --ref agency-member-frankie --action added \
  --detail "Frankie added as business manager. He can submit proposals on behalf of the agency and is the only role that can accept an offer." \
  --actor chitraksh
```

---

## 4. Specialized profiles

Upwork allows a general profile plus specialized profiles under one account. "Specialized profiles rank higher for niche searches." Each gets its own rate, its own portfolio subset and its own headline. **This is free and it is the cheapest ranking lever on the platform.**

| Profile | Headline | Rate | Portfolio subset |
|---|---|---|---|
| General | Compliance-Aware AI Voice Infrastructure, TCPA and CIPA Gates Enforced in Code | $95/hr | All six entries |
| Specialized 1 | AI Voice Agents and Telephony, Sub-Second Latency, Measured | $120/hr | The dealership build, the two-persona handoff, the compliance panel |
| Specialized 2 | Workflow Automation and AI Integration, n8n, MCP, Claude Agents | $95/hr | Post-call extraction, the n8n pipeline, the MCP work |

Two, not five. The guidance is to choose one or two primary service offerings and decline work outside them to protect JSS. Specialized 2 is aimed squarely at "AI Integration", up **178%** year over year and the fastest-growing coding skill on the platform.

---

## 5. Project Catalog listings

Project Catalog is Upwork's productized-offer surface: fixed scope, fixed price, bought without a proposal. It costs **no Connects to list**, which makes it the only Connects-free inbound channel on the platform, and it is the direct port of the Fiverr packaging.

**Check availability in the dashboard at signup.** Upwork does not publish the eligibility gate on its freelancer getting-started page, so treat the surface as something to confirm rather than assume. Confirmed live listings exist in our exact niche, so the category itself is open to this kind of offer.

Mirror the three Fiverr gigs, priced **at or above** the Fiverr ladder, because Upwork's own buyer guidance is one to two orders of magnitude higher:

| Catalog listing | Mirrors | Tiers | Note |
|---|---|---|---|
| AI Voice Receptionist for Car Dealerships and Insurance Agencies | gig1 | $450 / $1,200 / $2,800 | Same ladder as Fiverr. Raise after the first delivery |
| TCPA-Compliant AI Cold Calling Agent with Consent and DNC Gating | gig2 | $350 / $1,200 / $2,800 | The audit tier is the wedge. Maps to the 14.38% reply-rate category |
| Production n8n AI Agent Workflows with Error Handling | gig3 | $250 / $750 / $2,000 | Upwork's own band for custom integrations with error handling is $800 to $2,500, so the middle tier is already conservative |

Copy comes from `research/fiverr-profile-package.md` sections 2, 3 and 4, rewritten for Upwork's field structure rather than pasted, because the field limits differ. Same hard rules as everywhere: no dialed phone number, no email, no off-platform contact route, no em dashes, every number with its method and date.

The service fee on Project Catalog projects and consultations "works like other contracts", so the economics match a normal contract.

---

## 6. Paid visibility switches, week 1

| Switch | Cost | Rule |
|---|---|---|
| **Freelancer Plus**, on the bidding account | $19.99/month | 100 Connects (worth $15), competitor bid visibility, and a 0% service fee on clients we bring to Upwork ourselves. Net marginal cost about $5. Subscribe day 1. Note that "40% of subscribers are Top Rated" is a selection effect, not a causal claim |
| **New-freelancer bonus** | free | 50 Connects, but **only after** purchasing Connects or subscribing to Plus. Subscribing first is what unlocks it |
| **Availability Badge** | Connects, floating price, no maximum | Switch on with a **hard cap of 100 Connects (about $15) per month** for the first 60 days. The badge is removed automatically when the cap is reached. Measure invitations received in Stats and trends before renewing. **Zero invitations in 14 days: turn it off** |
| **Boosted proposals** | any Connects amount, we cap at 30 | $1,500+ jobs only, named vertical proof only, at most 25% of proposals. The auction settles on your own bid, not the runner-up's |

The whole Upwork paid surface costs tens of dollars a month, not hundreds. Max it before a single dollar goes to Meta or Google.

---

## 7. First-week proposal cadence and Connects budget

| Day | Proposals | Connects | Who | Note |
|---|---|---|---|---|
| 1 | 0 | 0 | both | Accounts, verification, profiles, portfolio, Loom. No bidding. Portfolio first is what puts us in the "strong portfolio, clear niche" bucket that benchmarks at 1 to 3 weeks to first client |
| 2 | 0 | 0 | both | Agency, Agency Plus, Frankie added, specialized profiles, Catalog listings |
| 3 | 3 | about 30 | Frankie sends, Chitraksh supplies the technical answer | First bids. No boosts yet: there is no baseline to compare a boost against |
| 4 | 4 | about 40 | Frankie | Include one US-only job, which only his account can see |
| 5 | 4 | about 40 + 25 boost | Frankie | First boost, on one $1,500+ job with named vertical proof |
| 6 | 4 | about 40 | Frankie | |
| 7 | 3 | about 30 + 25 boost | Frankie | Week 1 review: proposals sent, viewed, interviews, and the view rate |
| **Week 1 total** | **18** | **about 230 Connects, roughly $35** | | |

Then ramp: **5 to 10 proposals a day in week 2, 10 to 15 in week 3.** The planning number to first hire is **30 to 50 high-signal proposals over 3 to 5 weeks**, at roughly 10 Connects each, so **$45 to $75 of Connects total**.

**Filter before writing.** Every proposal goes to a job that passes all of these:

- Posted in the last hour where possible. Under 5 minutes from post replies at 8.99%.
- **Client payment verified.** 24.0% of postings are not.
- Budget $1,000+, or unposted with real scope.
- Inside the eight ranked niches in `research/marketplace-expansion.md` section 1.9.
- Client lifetime spend ideally $1,000 to $5,000, the band that replies at 8.15%.
- Not a whale. $500,000+ clients reply at 3.85%.

**If we cannot find 3 to 5 qualifying jobs a day, the filters are wrong and no amount of proposal quality compensates.** That is itself a leading indicator, and it is number 7 on the list in `STRATEGY.md` section (i).

Log every proposal. The interview rate is unknowable otherwise, and it is the second-most-predictive number in the whole system.

---

## 8. Day-1 checklist

- [ ] Chitraksh account created, real name, real address
- [ ] Chitraksh ID verification submitted
- [ ] Chitraksh W-8BEN submitted
- [ ] Chitraksh withdrawal method added, separate from Frankie's
- [ ] Chitraksh profile at 100%
- [ ] Frankie account created, own device, own payment method
- [ ] Frankie ID verification submitted
- [ ] Frankie US location verification submitted
- [ ] Frankie W-9 submitted
- [ ] Frankie profile at 100%
- [ ] Oraya Labs agency created from Chitraksh's account
- [ ] Agency Plus subscribed
- [ ] Frankie invited as business manager and accepted
- [ ] Founder revenue-split agreement written, outside Upwork
- [ ] Two specialized profiles created
- [ ] Portfolio populated on all profiles, PII masked, no client named
- [ ] 90-second Loom recorded, number masked in every frame
- [ ] Project Catalog availability checked and the answer logged
- [ ] Freelancer Plus subscribed on the bidding account
- [ ] Availability Badge on with a 100-Connect cap
- [ ] Both accounts set to Available
- [ ] `accounts.json` updated with the real handles and creation dates
- [ ] Every one of the above logged to the ledger
