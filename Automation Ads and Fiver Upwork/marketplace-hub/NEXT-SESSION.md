# NEXT SESSION

Resume brief for a fresh Claude session with no memory of this one. Written by `python3 hub.py handoff` on 2026-09-14T20:25:44Z. Everything below is derived from the ledger, `accounts.json` and `STRATEGY.md`, so it is current as of that run and not a moment later.

**Read these first, in this order:** `STRATEGY.md`, then `README.md`, then this file. The research behind every number is in `research/`, indexed in `research/INDEX.md`.

**Writing rules that apply to everything you produce, including ledger detail text:** no em dashes, no U+2014, ever. An en dash only inside a numeric range. No invented numbers. Every figure carries its measurement basis and the date it was read. No fabricated metrics, no fake social proof, no invented client stories. Anonymise client data. Compliance framing is engineering, not legal advice.

## 1. Who and what

Oraya / Hanflux AI. Two founders. **Chitraksh Mayank**, graduate lawyer based in India, builds and delivers. **Frankie Alicea**, US-based licensed insurance producer, sells, fronts the US, and holds the US Upwork account that is the only key to US-only job posts.

Three assets nobody else in the competitive set holds: a measured median **761 ms** time-to-first-audio on simulated calls, 26 August 2026, against a prior-vendor production p50 of **1.64 to 1.9 s**; **compliance enforced in code** rather than in a prompt; and **real dealership and insurance experience**.

The 30-day objective is **five orders**, not revenue.

## 2. Account state

- **fiverr / hanfluxai** [active] owner Chitraksh Mayank. Primary seller account. Sells per-client voice agent builds, compliance-gated outbound, and production n8n workflows to US car dealerships and insurance agencies.
- **upwork / TODO-chitraksh** [planned] owner Chitraksh Mayank. Builder identity and the JSS that every badge compounds on. Upwork's own buyer guidance puts a single-flow voice agent at $600 to $6,000 and a production-grade deployment at $2,400 to $24,000, one to two orders of magnitude above the Fiverr page-one floor. Creates and owns the Oraya Labs agency.
- **upwork / TODO-orayalabs-agency** [planned] owner Created from Chitraksh Mayank's freelancer account. The contracting entity and the broad studio surface. Oraya Labs (orayalabs.ai) covers the full range: AI voice agents and telephony, agentic systems and multi-agent workflows with real-world access, n8n and custom automation, CRM and back-office integration, document review and risk flagging, local and private LLM deployments, compliance enforced in code. The dealership and insurance voice work (Oraya) is one product line inside it, not the whole scope. Frankie joins as a business manager, which lets him submit proposals on behalf of the agency and makes him the only party who can accept an offer.
- **upwork / TODO-frankie** [planned] owner Frankie Alicea. Frankie's own identity and his own JSS, and the US-located account. This is the only account that can see US-only job posts, which is an entire class of work Chitraksh's account cannot see at all. Also carries the LinkedIn Services page and the insurance-vertical positioning, where Frankie is the licensed producer.
- **fiverr / TODO-agency** [planned] owner Oraya Labs. A Fiverr agency profile, if and when a third in-house member joins. Not a second account: a Fiverr agency is a switch of the existing seller profile, and orders, gigs, chats and reviews carry over.

Full verification state, listing states and the never-do list are in `accounts.json`. The registry is the source of truth for what exists; the ledger is the source of truth for what happened.

## 3. What is built

```
CLAUDE.md
CLOUD-AGENT.md
DIRECTIVES.md
NEXT-SESSION.md
README.md
RUNBOOK-FRANKIE-UPWORK.md
STRATEGY.md
accounts.json
ads/ads-plan.md
ads/campaigns.json
ads/creative-briefs.md
assets/ASSET-INDEX.md
assets/portfolio-final/portfolio-1-n8n-outbound-pipeline.png
assets/portfolio-final/portfolio-2-voice-control-center.png
assets/portfolio-final/portfolio-3-compliance-audit-ab2905.png
assets/portfolio-final/portfolio-4-governance-enforced-in-code.png
assets/source-screenshots/shot-1.png
assets/source-screenshots/shot-2.png
assets/source-screenshots/shot-3.png
assets/source-screenshots/shot-4.png
assets/source-screenshots/shot-5.png
checkpoints/frankie-upwork.json
gallery.html
hub.py
ledger/events.jsonl
ledger/metrics.jsonl
monitoring/daily-check.md
monitoring/scheduled-task-prompt.md
notebooklm-prompts.md
playbooks/case-study-capture.md
playbooks/fiverr-gig-build.md
playbooks/frankie-upwork-setup.md
playbooks/response-sla.md
playbooks/upwork-account-setup.md
playbooks/upwork-proposal.md
playbooks/weekly-review.md
reports/2026-09-11.md
reports/2026-09-12.md
reports/2026-09-13.md
research/INDEX.md
research/fiverr-market.md
research/fiverr-profile-package.md
research/marketplace-expansion.md
research/oraya-facts.md
templates/custom-offer.md
templates/delivery-message.md
templates/first-reply-gig1.md
templates/first-reply-gig2.md
templates/first-reply-gig3.md
templates/review-request.md
templates/upwork-proposal-skeleton.md
research/gig-images/   (11 rendered PNGs, not listed individually)
```

Launch checklist: **8 of 23 complete.** Run `python3 hub.py checklist` for the live version.

## 4. Exactly where the browser work stopped

**Chrome is disconnected.** The last session ended mid-build in the Fiverr gig editor. Reconnect Chrome to an already authenticated Fiverr session before touching any of this. Never attempt to log in and never accept credentials.

| Surface | State | Resume point |
|---|---|---|
| Fiverr seller profile | Live | Display name Chitraksh M. Education entry still incomplete, pending a confirmed graduation year |
| **Fiverr Gig 1**, voice receptionist | Draft complete | Slug locked as `build-ai-voice-receptionist-for-car-dealerships-and-insurance-agencies`. Three images and the video are still pending. Cannot publish until the verification gates clear |
| **Fiverr Gig 2**, compliance-gated outbound | **Paused at the Description step** | Overview and pricing are saved. Still to enter: the **description**, **7 FAQs**, **4 buyer requirements**, then upload images **gig2-a**, **gig2-b**, **gig2-c**. All copy is paste-ready in `research/fiverr-profile-package.md` section 3. Images are at `research/gig-images/gig2-a.png`, `gig2-b.png`, `gig2-c.png`. **Read the URL bar after the first save and write the real slug into `accounts.json`: it locks permanently** |
| **Fiverr Gig 3**, n8n workflows | **Not started** | Full paste-ready copy is in `research/fiverr-profile-package.md` section 4. Service type is **N8n Automation**, not AI Agents, which is what puts it in the workflow filter chip |
| **Upwork, all three entities** | **Not opened** | Chitraksh freelancer, Oraya Labs agency, Frankie US freelancer. Step-by-step click path is in `playbooks/upwork-account-setup.md`. Open on day 1: the 90-day Top Rated clock starts at first project |
| Ads | No spend, zero dollars | Campaigns registered and planned in `ads/campaigns.json`. Fiverr Promoted Gigs is not eligible in month 1 |

## 5. Gates only the user can clear

Do not attempt any of these. Flag them and stop. Each one needs the account holder in person.

| Gate | Why it is user-only | Blocks |
|---|---|---|
| **ID verification** | Identity document and a liveness check | Fiverr publishing, and Upwork Rising Talent |
| **W-8BEN** | A tax declaration signed by the taxpayer | Fiverr payouts |
| **India GST declaration form** | A tax declaration signed by the taxpayer | Fiverr publishing |
| **Education graduation year** | A fact only Chitraksh knows | Profile completeness, which is a Rising Talent prerequisite on Upwork |
| **Seller Plus Kickstart decision** | A 15 dollar a month spending decision | Nothing hard. It buys keyword data and no ranking. Refundable within 48 hours |
| Payout method | Bank credentials | Fiverr payouts, and a valid withdrawal method is a Rising Talent requirement |

## 6. Open blockers and overdue tasks

- **BLOCKER** `education-graduation-year` (2026-09-11): Education entry incomplete. Graduation year for the B.B.A. LL.B. (Hons.) is not confirmed, so the entry has not been saved.
- **BLOCKER** `id-verification` (2026-09-11): ID verification not passed. Publishing is gated on it.
- **BLOCKER** `w8ben` (2026-09-11): W-8BEN not submitted. Required as a non-US person before earnings can be paid out. Publishing is gated on it.
- **BLOCKER** `india-gst` (2026-09-11): India GST declaration form not submitted. Publishing is gated on it.
- **BLOCKER** `payout-setup` (2026-09-11): Payout method state not confirmed. Open until it has been read off the Fiverr dashboard and logged, rather than assumed either way.
- **BLOCKER** `seller-plus-kickstart` (2026-09-11): Seller Plus Kickstart at 15 USD a month was declined at signup. The decision is open, not settled. The one feature worth buying is the keyword analytics that show which search terms buyers actually used. It buys no ranking.
- **BLOCKER** `profile-dates` (2026-09-13): Work experience and education entries cannot be completed without two facts only Chitraksh has: the Oraya start date (Fiverr asks for an exact day, not a month) and the NMIMS LLB graduation year. Both entries left empty rather than guessed
- **BLOCKER** `profile-photo` (2026-09-13): Profile picture is still the ORAYA brand mark. The plan section 1.9 calls for a founder headshot instead, and no photo file exists anywhere in the connected folder, so it cannot be changed without Chitraksh supplying one
- **BLOCKER** `fiverr-bot-challenge` (2026-09-13): Fiverr served a press and hold human verification challenge on the profile edit page during skill editing. Automated editing of the profile is blocked until Chitraksh completes that challenge himself. Bot checks are never to be completed on his behalf

- **OVERDUE** `gig1-images` due 2026-09-12: Gig 1: upload three images at 1280 x 769 from research/gig-images/gig1-a.png, gig1-b.png, gig1-c.png.
- **OVERDUE** `gig2-description` due 2026-09-12: Gig 2: paste the description, 1200 character cap, and verify the counter before saving.
- **OVERDUE** `gig2-faq` due 2026-09-12: Gig 2: enter the FAQ set, first FAQ is the engineering not legal advice line.
- **OVERDUE** `gig2-images` due 2026-09-12: Gig 2: upload three images at 1280 x 769. Files already rendered at research/gig-images/gig2-a.png, gig2-b.png, gig2-c.png.
- **OVERDUE** `gig2-requirements` due 2026-09-12: Gig 2: enter buyer requirements, including the consent basis question that filters the orders that would cancel.
- **OVERDUE** `verification-pack` due 2026-09-12: Submit ID verification, W-8BEN and the India GST form together in one sitting. Nothing publishes until these clear, so every hour spent on gig copy before this is an hour spent on a listing that cannot go live.
- **OVERDUE** `education-year` due 2026-09-13: Confirm the graduation year and complete the education entry on the profile.
- **OVERDUE** `quick-responses` due 2026-09-13: Load the first-reply templates from templates/ into Fiverr Quick Responses. Response time under one hour is a direct ranking input and it costs nothing.
- **OVERDUE** `seller-plus-decision` due 2026-09-13: Decide Seller Plus Kickstart, yes or no, and write the reason in the ledger either way. Kickstart is refundable within 48 hours of charge, so the downside of trying it is bounded.
- **OVERDUE** `upwork-open-builder` due 2026-09-13: Open the Upwork freelancer account, India, and complete ID verification the same day. The 90 day Top Rated clock starts at first project, so every day of delay is a day later to the badge. Click path in playbooks/upwork-account-setup.md section 1.
- **OVERDUE** `upwork-open-us` due 2026-09-13: Frankie opens the US Upwork account on his own device and payment method, with US location verification. It is the only account that can see US only job posts. Section 2 of the setup playbook.

Pending checklist items: education_entry, seller_plus_decision, id_verification, w8ben, india_gst, payout_setup, gig1_video, gig1_published, gig2_published, gig3_published, sla_templates, mobile_app, first_metrics, first_order, five_orders

## 7. The first 10 steps, in order

```bash
cd marketplace-hub

# 1. Read the state. Nothing is done from memory.
python3 hub.py status

# 2. Read the one next action per account.
python3 hub.py next

# 3. Read what is still pending on the launch checklist.
python3 hub.py checklist

# 4. Read the plan. STRATEGY.md sections (d) build order and (i) leading indicators.
#    Then playbooks/fiverr-gig-build.md for the Fiverr interface quirks.

# 5. Ask the user to clear the user-only gates in section 5 above. Do not attempt them.
#    Log each one as it clears:
python3 hub.py log --platform fiverr --account hanfluxai --entity blocker \
  --ref id-verification --action closed --detail "ID verification passed" --actor chitraksh

# 6. Resume Fiverr Gig 2 at the Description step. Copy is in
#    research/fiverr-profile-package.md section 3. Paste the description, then the 7 FAQs,
#    then the 4 buyer requirements. Check the character counter before every save.
python3 hub.py log --platform fiverr --account hanfluxai --entity gig \
  --ref gig2 --action description_saved --detail "pasted the description, checked the counter" --actor chitraksh

# 7. Read the gig URL from the browser bar after the first save and write the real slug
#    into accounts.json. It locks permanently and is currently TODO.
python3 hub.py log --platform fiverr --account hanfluxai --entity gig \
  --ref gig2 --action slug_recorded --detail "real slug written into accounts.json" --actor chitraksh

# 8. Upload gig2-a, gig2-b and gig2-c from research/gig-images/ at 1280 x 769.
python3 hub.py log --platform fiverr --account hanfluxai --entity gig \
  --ref gig2 --action images_uploaded --detail "three images uploaded" --actor chitraksh

# 9. Build Gig 3 from research/fiverr-profile-package.md section 4.
#    Service type is N8n Automation, NOT AI Agents.

# 10. Log the day and refresh the report.
python3 hub.py metrics add --platform fiverr --account hanfluxai --gig gig1 \
  --impressions 0 --clicks 0 --orders 0 --messages 0 --source fiverr-gig-analytics
python3 hub.py export
python3 hub.py handoff
```

**When Upwork is next on the list** rather than Fiverr, the click path is `playbooks/upwork-account-setup.md` and the first-week bidding cadence is its section 7. Open all three Upwork entities on the same day: the 90-day Top Rated clock starts at first project, and Rising Talent clears on a single 250 dollar order.

## 8. Current next action per account

```
NEXT ACTION PER ACCOUNT   read 2026-09-14T20:25:44Z
one action each, ranked: overdue task, then open blocker, then next due task, then the STRATEGY build order

  account                       state    from          due         next action
  ----------------------------  -------  ------------  ----------  ------------------------------------------------------------------------------------------------
  fiverr/hanfluxai              active   OVERDUE TASK  2026-09-12  gig1-images: Gig 1: upload three images at 1280 x 769 from research/gig-images/gig1-a.png, gig1-
  upwork/TODO-chitraksh         planned  OVERDUE TASK  2026-09-13  upwork-open-builder: Open the Upwork freelancer account, India, and complete ID verification the
  upwork/TODO-orayalabs-agency  planned  TASK          2026-09-16  upwork-create-agency: Create the Oraya Labs agency from Chitraksh's freelancer account, subscrib
  upwork/TODO-frankie           planned  OVERDUE TASK  2026-09-13  upwork-open-us: Frankie opens the US Upwork account on his own device and payment method, with U
  fiverr/TODO-agency            planned  BUILD ORDER   -           BLOCKED until a third in-house member exists. Fiverr agencies require a minimum of 3 team member

  Owners: Chitraksh builds and delivers. Frankie sells, fronts the US, and holds the US Upwork
  account that is the only key to US-only job posts. See STRATEGY.md section (d).
```

## 9. Full status at handoff time

```
MARKETPLACE HUB STATUS   read 2026-09-14T20:25:44Z
ledger: 73 events, 0 metric snapshots

FIVERR / hanfluxai   [active]
=============================
  owner: Chitraksh Mayank   jurisdiction: India (Ranchi / Bengaluru)   created: 2026-09-11
  purpose: Primary seller account. Sells per-client voice agent builds, compliance-gated outbound, and production n8n workflows to US car dealerships and insurance agencies.

  Verification
    gate                   state
    ---------------------  --------------------------------------------------------------------------------------------------------------------------------------
    education_entry        pending, graduation year to confirm
    id_verification        pending
    india_gst_form         pending
    payout_method          pending
    seller_plus_kickstart  declined at signup, decision open. $15/month, refundable within 48 hours of the last monthly payment, buys keyword data and no ranking
    w8ben                  pending

  Listings
    ref   listing                                       state  ladder         last action      on
    ----  --------------------------------------------  -----  -------------  ---------------  ----------
    gig1  AI voice receptionist, dealers and agencies   draft  450/1200/2800  images_uploaded  2026-09-12
    gig2  AI cold calling, TCPA and DNC gated           draft  350/1200/2800  draft_complete   2026-09-12
    gig3  n8n AI workflows, error handling and monitor  draft  250/750/2000   pricing_saved    2026-09-12

  Open blockers (9)
    blocker                    detail                                                            opened
    -------------------------  ----------------------------------------------------------------  ----------
    education-graduation-year  Education entry incomplete. Graduation year for the B.B.A. LL.B.  2026-09-11
    id-verification            ID verification not passed. Publishing is gated on it.            2026-09-11
    w8ben                      W-8BEN not submitted. Required as a non-US person before earning  2026-09-11
    india-gst                  India GST declaration form not submitted. Publishing is gated on  2026-09-11
    payout-setup               Payout method state not confirmed. Open until it has been read o  2026-09-11
    seller-plus-kickstart      Seller Plus Kickstart at 15 USD a month was declined at signup.   2026-09-11
    profile-dates              Work experience and education entries cannot be completed withou  2026-09-13
    profile-photo              Profile picture is still the ORAYA brand mark. The plan section   2026-09-13
    fiverr-bot-challenge       Fiverr served a press and hold human verification challenge on t  2026-09-13

  Next actions (12 open)
    task                     detail                                                    due         flag
    -----------------------  --------------------------------------------------------  ----------  ---------
    gig1-images              Gig 1: upload three images at 1280 x 769 from research/g  2026-09-12  OVERDUE
    gig2-description         Gig 2: paste the description, 1200 character cap, and ve  2026-09-12  OVERDUE
    gig2-faq                 Gig 2: enter the FAQ set, first FAQ is the engineering n  2026-09-12  OVERDUE
    gig2-images              Gig 2: upload three images at 1280 x 769. Files already   2026-09-12  OVERDUE
    gig2-requirements        Gig 2: enter buyer requirements, including the consent b  2026-09-12  OVERDUE
    verification-pack        Submit ID verification, W-8BEN and the India GST form to  2026-09-12  OVERDUE
    education-year           Confirm the graduation year and complete the education e  2026-09-13  OVERDUE
    quick-responses          Load the first-reply templates from templates/ into Five  2026-09-13  OVERDUE
    seller-plus-decision     Decide Seller Plus Kickstart, yes or no, and write the r  2026-09-13  OVERDUE
    gig3-build               Gig 3: create the n8n gig. Service type is N8n Automatio  2026-09-14  DUE TODAY
    gig-videos               Record all three gig videos in one sitting, 55 to 60 sec  2026-09-15
    founder-split-agreement  Write the founder revenue split agreement before the fir  2026-09-20

UPWORK / TODO-chitraksh   [planned]
===================================
  owner: Chitraksh Mayank   jurisdiction: India (Ranchi / Bengaluru)   created: None
  purpose: Builder identity and the JSS that every badge compounds on. Upwork's own buyer guidance puts a single-flow voice agent at $600 to $6,000 and a production-grade deployment at $2,400 to $24,000, one to two orders of magnitude above the Fiverr page-one floor. Creates and owns the Oraya Labs agency.

  Verification
    gate                   state
    ---------------------  -------------------------------------------------------------------------------
    freelancer_plus        not started, $19.99/month including 100 Connects and competitor bid visibility
    identity_verification  not started, do it day 1, it gates Rising Talent
    profile_completeness   0%, 100% is a Rising Talent prerequisite and 10% to 15% of the search algorithm
    tax_form               not started, W-8BEN as a non-US person
    withdrawal_method      not started, must be separate from Frankie's

  Listings
    ref              listing                                       state        ladder       last action  on
    ---------------  --------------------------------------------  -----------  -----------  -----------  --
    general          Compliance-Aware AI Voice Infrastructure, TC  not-started  general      -            -
    spec-voice       AI Voice Agents and Telephony, Sub-Second La  not-started  specialized  -            -
    spec-automation  Workflow Automation and AI Integration, n8n,  not-started  specialized  -            -

  Open blockers (0)
    (none)

  Next actions (1 open)
    task                 detail                                                    due         flag
    -------------------  --------------------------------------------------------  ----------  -------
    upwork-open-builder  Open the Upwork freelancer account, India, and complete   2026-09-13  OVERDUE

UPWORK / TODO-orayalabs-agency   [planned]
==========================================
  owner: Created from Chitraksh Mayank's freelancer account   jurisdiction: India, with a US-based business manager   created: None
  purpose: The contracting entity and the broad studio surface. Oraya Labs (orayalabs.ai) covers the full range: AI voice agents and telephony, agentic systems and multi-agent workflows with real-world access, n8n and custom automation, CRM and back-office integration, document review and risk flagging, local and private LLM deployments, compliance enforced in code. The dealership and insurance voice work (Oraya) is one product line inside it, not the whole scope. Frankie joins as a business manager, which lets him submit proposals on behalf of the agency and makes him the only party who can accept an offer.

  Verification
    gate                         state
    ---------------------------  -----------------------------------------------------------------------------------------------------
    agency_plus_subscription     not started, about $19.99/month, required before Frankie can be added
    agency_profile_completeness  0%
    financial_account            not started, agency earnings land here and the founder split needs a written agreement outside Upwork

  Listings
    (none)

  Open blockers (0)
    (none)

  Next actions (1 open)
    task                  detail                                                    due         flag
    --------------------  --------------------------------------------------------  ----------  ----
    upwork-create-agency  Create the Oraya Labs agency from Chitraksh's freelancer  2026-09-16

UPWORK / TODO-frankie   [planned]
=================================
  owner: Frankie Alicea   jurisdiction: United States   created: None
  purpose: Frankie's own identity and his own JSS, and the US-located account. This is the only account that can see US-only job posts, which is an entire class of work Chitraksh's account cannot see at all. Also carries the LinkedIn Services page and the insurance-vertical positioning, where Frankie is the licensed producer.

  Verification
    gate                      state
    ------------------------  ------------------------------------------------------------------------------
    availability_badge        not started, hard cap 100 Connects (about $15) per month for the first 60 days
    freelancer_plus           not started, $19.99/month, this is the primary bidding account
    identity_verification     not started, day 1
    profile_completeness      0%
    tax_form                  not started, W-9 as a US person
    us_location_verification  not started, required to see and bid on US-only job posts
    withdrawal_method         not started, must be separate from Chitraksh's

  Listings
    ref      listing                                       state        ladder   last action  on
    -------  --------------------------------------------  -----------  -------  -----------  --
    general  AI Voice and Compliance Systems for Insuranc  not-started  general  -            -

  Open blockers (0)
    (none)

  Next actions (1 open)
    task            detail                                                    due         flag
    --------------  --------------------------------------------------------  ----------  -------
    upwork-open-us  Frankie opens the US Upwork account on his own device an  2026-09-13  OVERDUE

FIVERR / TODO-agency   [planned]
================================
  owner: Oraya Labs   jurisdiction: India   created: None
  purpose: A Fiverr agency profile, if and when a third in-house member joins. Not a second account: a Fiverr agency is a switch of the existing seller profile, and orders, gigs, chats and reviews carry over.

  Listings
    (none)

  Open blockers (0)
    (none)

  Next actions (0 open)
    (none)

LAUNCH CHECKLIST
================
  8 of 23 complete. Run `python3 hub.py checklist` for the item list.
```

## 10. Before anything ships

Run the dash scan from `README.md` and confirm `total banned dash characters: 0`. Run it against text baked into images too, including SVG labels and JavaScript template strings. Then log what you did. If it is not in the ledger, it did not happen.
