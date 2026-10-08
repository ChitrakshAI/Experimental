# STRATEGY

The master plan for Oraya / Hanflux AI on the freelance marketplaces. Written 11 September 2026.

Everything below is derived from four research files that now live in `research/`. Sections are cited as `marketplace-expansion.md §1.9` rather than by URL: the URLs are in the research files, one click away, and repeating them here would make this document unreadable. Key numbers are repeated, because a plan that hides its numbers cannot be argued with.

**Founder directives, received 11 September 2026, quoted so they cannot be softened later:**

> "Fiverr and Upwork we need to be top of the game to get clients at all levels"

> "GLOBAL positioning, no limits, maximum results, ads across native boosts of Upwork, Fiverr, Meta etc, perform on the budget and get clients"

> "whatever makes most sense to get the clients in the first place"

And the standing rule that governs the whole hub: everything gets logged.

Those directives are taken literally in section (b), which sets global positioning with no geographic limit, and in section (f), which includes a no-limits tier. They are also taken seriously in section (f)'s measurement contract, because "perform on the budget" is a performance instruction, not a spending instruction, and the fastest way to fail it is to scale a channel before it has a measured conversion rate.

---

## (a) Thesis, in 10 lines

1. **Who buys.** US car dealerships (BDC, service drive, after-hours overflow) and US independent insurance agencies (quote intake, renewals, first notice of loss), plus the 13,000+ Upwork buyers who have already decided they need outbound calling and are currently buying it as human headcount at $6 to $20 per hour (`marketplace-expansion.md §1.4`).
2. **Why us, asset one: measured latency.** Median **761 ms** time-to-first-audio on the reference dealership build, measured over simulated calls on 26 August 2026, against a prior-vendor production baseline of **p50 approximately 1.64 s outbound and 1.9 s inbound** across 17 archived calls (`oraya-facts.md §1`). Nobody on either platform publishes a measured latency number with its method (`marketplace-expansion.md §1.9`, rank 4).
3. **Why us, asset two: compliance in code.** Recorded-line and AI disclosure as fixed first-utterance text outside the model, plus four pre-dial gates: consent basis, Do-Not-Call, quiet hours in the callee's own time zone, allowlist. Written against TCPA, 47 CFR 64.1200, CIPA and AB 2905, read from the statutes. On Fiverr, `ai-cold-calling` carries 2,232 services and not one top result mentions consent, DNC, quiet hours or disclosure (`fiverr-market.md §6.2`).
4. **Why us, asset three: real vertical experience.** A live dealership reference build, and Frankie Alicea as a US-licensed insurance producer. Fiverr's `car-dealership` keyword carries 2,699 services with zero AI voice supply; `insurance` carries 3,445 with the same gap, while insurance is 32.9% of the AI voice agent market (`fiverr-market.md §6.1`).
5. **The structural read.** Both marketplaces are consolidating into higher-value work and AI is the only growing line on either: Fiverr buyers down 21.9% with spend per buyer up 15.6%, Upwork clients down 6% with GSV per client up 5% and AI GSV up 50% year over year (`marketplace-expansion.md §1.1`).
6. **The objective for the next 30 days is five orders, not revenue.** Five orders from three or more unique clients is the Fiverr Level 1 bar and the thing that converts a dead profile into a ranked one. On Upwork, one $450 contract at a 4.8 rating clears Rising Talent.
7. **The Fiverr ladder.** New Seller now. **Level 1** at 60 days active, 5 orders, 3 unique clients, $400 lifetime, 4.4+ rating, 80% response rate, Success Score 5.0+. **Level 2** at 120 days, 20 orders, 10 unique clients, $2,000 lifetime, 4.6+, 90%, Success Score 7.0+, which is what unlocks Briefs, custom offers to $10,000 and 20 gig slots (`fiverr-market.md §4.1`).
8. **The Upwork ladder, which is dramatically faster.** **Rising Talent** needs a 4.8+ average, **$250 earned in 12 months**, a 100% complete profile, ID verification, and a proposal or contract in the last 90 days. **Top Rated** needs JSS 90%+, first project more than **90 days ago**, $1,000 of 12-month earnings, and 13 of the last 16 weeks at Rising Talent or JSS 90%+. **Top Rated Plus** needs $10,000 as a freelancer or **$20,000 as an agency** (`marketplace-expansion.md §2.3`).
9. **The asymmetry that decides sequencing.** Fiverr's inbound Briefs channel is locked behind Success Score 7, which means 20 orders from 10 clients, which is months away. Upwork's Rising Talent clears on one order. **The Upwork account must be opened on day 1** even if we do not bid hard until week 3, because the 90-day Top Rated clock starts at the first project and every day of delay is a day later to the badge.
10. **The trap to avoid, stated once.** A low anchor is permanent. A Top Rated Fiverr seller holds slot one on a 44,698-service keyword at $1,800 with 2 reviews, while a seller with 742 reviews at $40 cannot reprice out of it (`fiverr-market.md §5.8`). On Upwork, bidding 200% to 500% of the posted budget replies at 16.4% while matching the budget replies at 8.8%, the worst position on the board (`marketplace-expansion.md §1.7`). Price is the positioning.

---

## (b) Global positioning

### The positioning statement

> **We build compliance-aware phone agents for regulated, high-ticket verticals, at a measured median 761 ms to first audio, with consent, Do-Not-Call, quiet hours and AI disclosure enforced in code rather than in a prompt. A lawyer writes the gates. An engineer ships the system. We are not a Vapi or Retell configurator.**

One statement, used everywhere, with the vertical swapped and nothing else. Global in reach: we sell to any buyer in any country who has a phone problem in a regulated vertical. The compliance lane happens to be written against US statutes, which is where the demand and the anxiety both are, and that is a targeting decision rather than a geographic limit.

### Per-platform titles

| Surface | Title | Why |
|---|---|---|
| Fiverr Gig 1 | `AI Voice Receptionist For Car Dealerships And Insurance Agencies` | Vertical in the title, tool names in the tags. The tags still catch tool traffic while the title owns a keyword surface with zero AI voice supply |
| Fiverr Gig 2 | `TCPA Compliant AI Cold Calling Agent With Consent And DNC Gating` | Sells the one thing 2,232 competing services do not mention |
| Fiverr Gig 3 | `Build Production n8n AI Agent Workflows With Error Handling` | Rides the +125% n8n term. Lowest anchor of the three, deliberately, because it is the order counter |
| Fiverr profile tagline | Compliance-aware voice infrastructure for dealerships and insurance agencies. Measured latency, gates in code | Credential plus number, never a vendor name |
| Upwork general profile | Compliance-Aware AI Voice Infrastructure, TCPA and CIPA Gates Enforced in Code | Leads with compliance, which sits in an 11.21% reply-rate category rather than the 7.21% AI category |
| Upwork specialized profile 1 | AI Voice Agents and Telephony, Sub-Second Latency, Measured | Specialized profiles rank higher for niche searches and cost nothing (`marketplace-expansion.md §2.5`) |
| Upwork specialized profile 2 | Workflow Automation and AI Integration, n8n, MCP, Claude Agents | Reaches the +178% "AI Integration" skill, the fastest-growing coding skill on Upwork |
| Upwork agency profile | Oraya Labs (orayalabs.ai): AI agents, voice systems and automation that ship to production, compliance in code. Full studio scope (voice, agentic systems, n8n and custom automation, integrations, document processing, local LLMs); dealerships and insurance are case studies inside it, not the identity | The contracting entity. Frankie fronts it |
| LinkedIn Services page | AI Voice Agents, Compliance Automation, Workflow Automation | Free, no gate, Frankie's profile, free-consultation toggle routed to the Compliance-Safe AI Audit |

### Price ladders

**Fiverr, published packages, locked.** These are the positioning, not a negotiating position.

| Gig | Basic | Standard | Premium |
|---|---|---|---|
| Gig 1, voice receptionist | Starter **$450**, 5 days | Front Desk **$1,200**, 10 days | Production **$2,800**, 21 days |
| Gig 2, compliance-gated outbound | Audit **$350**, 3 days | Gated Dialer **$1,200**, 12 days | Full Pipeline **$2,800**, 21 days |
| Gig 3, n8n workflows | Workflow **$250**, 4 days | Agent System **$750**, 8 days | Pipeline **$2,000**, 15 days |

The published span is **$250 to $2,800**. Anything above the top tier goes out as a custom offer, capped at $10,000 once Level 2 lands, never as a fourth published package. The $250 tier is the one low anchor we allow ourselves and it exists for exactly one reason: order count and unique-client count gate the levels, revenue does not.

**Upwork, proposal pricing.** Upwork publishes buyer-facing guidance, which is the number in the buyer's head before they post (`marketplace-expansion.md §1.5`):

| Engagement, per Upwork's own page | Upwork's published range |
|---|---|
| Single-flow voice agent | $600 to $6,000 |
| Multi-intent voice assistant | $1,200 to $12,000 |
| **Production-grade deployment** | **$2,400 to $24,000** |
| Enterprise multi-agent system | $4,800 to $48,000 |
| Voice / IVR systems, conversational AI page | $5,000 to $12,000 |
| Workflow automation agent | $2,000 to $5,000 |
| n8n custom integrations with error handling | $800 to $2,500 |
| AI governance framework | $1,500 to $4,000 |
| Full-funnel appointment setting | $2,000 to $5,000 |

And the posted reality, from 50,019 fixed-price postings with listed budgets: **median posted budget $100**, median effective hourly rate about **$8.75**, with 31.5% of postings under $50 and only 12.5% at $1,000 or more (`marketplace-expansion.md §1.6`). A $10 Retell job and a $2,000 enterprise agent job sit in the same category. The entire skill on Upwork is filtering.

So we bid against Upwork's guidance, not against the post:

| Our lane | Bid band | Anchored on |
|---|---|---|
| TCPA-compliant outbound / AI SDR for regulated verticals | **$3,500 to $8,000** fixed, or $95 to $150/hr | Full-funnel appointment setting $2,000 to $5,000, plus a compliance premium nobody else can charge |
| Voice receptionist, insurance agency | **$2,500 to $6,000** | Voice / IVR $5,000 to $12,000 |
| Voice agent / BDC automation, dealership | **$2,500 to $6,000** | Production-grade deployment $2,400 to $24,000 |
| Sub-second latency voice infrastructure | **$4,000 to $10,000** | Production-grade deployment, with the measured number as the differentiator |
| Production n8n pipelines | **$1,200 to $3,000** | Custom integrations with error handling $800 to $2,500 |
| MCP server development | **$1,500 to $4,000** | MCP developers, thinnest supply measured anywhere at 310 reviews |
| AI compliance audit and governance | **$1,500 to $4,000** | AI governance framework $1,500 to $4,000 |

**The floor we will not go under: $1,200 on any Upwork build contract, and $350 on any Fiverr package.** The only exceptions are the published Fiverr $250 Workflow tier, which is the level counter, and a genuine paid audit at $350 that leads a larger scope. Below those numbers the engagement costs more in proposal time, delivery time and JSS risk than it returns, and it permanently anchors us in the wrong bracket. A job posted at $150 is not a discount opportunity, it is a different market. Walk.

**Pricing behaviour, three rules.** Never discount a published package price: concede scope instead, by adding an extra at no charge, so the order value on record stays intact. On Upwork, bid 200% to 500% of a low posted budget with the reason attached, because that band replies at 16.4% and matching the budget replies at 8.8%. After every third delivery, raise the entry price by 10% to 15% (`marketplace-expansion.md §7.4`, step 6).

### The vertical-first rule

**Lead with the vertical and the number. Never lead with the vendor name.** Buyers searching "vapi" are shopping on price against 14,986 sellers. Buyers searching "AI receptionist for insurance agency" are shopping on outcome against nobody. On Upwork the same rule has a measured payoff: Lead Generation and Telemarketing replies at **14.38%** and Information Security and Compliance at **11.21%**, while AI and Machine Learning replies at **7.21%** (`marketplace-expansion.md §1.7`). Leading a proposal with compliance and outbound rather than with AI roughly doubles the odds of being read.

Tool names live in tags, in skill lists and in the body of a proposal. They never lead.

---

## (c) The compliant account structure

Two humans. Two accounts. One agency. Zero grey area.

### The clauses, quoted

**Fiverr**, from its Community Standards:

> **"In order to buy and/or sell services on Fiverr you may have only one account."**

Consequence, quoted from the same page:

> **"Any violation of this policy can lead to permanent suspension of the account(s) involved in this activity."**

Note the plural in the parentheses: the suspension reaches every account in the cluster, not only the offending one. For severe violations, Fiverr's Account restrictions page states the decision "cannot be reversed" (`marketplace-expansion.md §3.1`, §3.7).

**Upwork**, from "Why you can't have two Upwork accounts":

> **"Upwork allows only one account per person to ensure fairness, trust, and security."**

> "you can only have one Upwork account for life. However, under that main account you can have one freelancer profile, one agency account, and multiple client accounts."

From Represent yourself authentically:

> **"You cannot log into someone else's account or let anyone log into your account and work or communicate on your behalf."**

> "The name on your account should be what you use to identify yourself in everyday life."

> "We may restrict or permanently suspend your account if we cannot verify the information you provide."

(`marketplace-expansion.md §3.3`.)

### The structure that is legitimate

| # | Entity | Owner | Platform | Purpose | When |
|---|---|---|---|---|---|
| 1 | Chitraksh personal freelancer account, India | Chitraksh | Upwork | Builder identity. Two specialized profiles. Holds the JSS everything compounds on | Day 1 |
| 2 | **Oraya Labs agency** | Created from Chitraksh's account. One agency per freelancer | Upwork, Agency Plus about $19.99/month | Contracting entity. Frankie added as a **business manager**, so he can submit proposals on behalf of the agency and is the only party who can accept offers | Created day 1, Frankie added day 2 |
| 3 | Frankie personal freelancer account, US | Frankie | Upwork | His own identity, his own JSS, and the **US-located** account | Day 1 |
| 4 | Chitraksh Fiverr seller account `@hanfluxai` | Chitraksh | Fiverr | Three gigs, one account, one person | Live |
| 5 | Fiverr agency | n/a | Fiverr | **Blocked.** Requires a minimum of 3 in-house team members, and up to 9 are allowed. Two founders is one short | Deferred until a third person joins |

Three provisions make the agency structure work, all quoted in `marketplace-expansion.md §2.9` and §3.4: "all agency members can submit proposals" while "Only business managers can accept an offer"; members "retain individual account privacy" and their sign-in details "must not be shared with the agency owner or any other party"; and members "can still create a project as a freelancer if you are not exclusive to an agency". On agency closure, completed contracts count toward each member's own JSS, which only makes sense because individual accounts persist alongside membership.

**Why Frankie's US account is load-bearing and not a nicety.** Upwork lets a client restrict a job post by freelancer location, and for the US the restriction is hard:

> **"If you choose U.S. only, then only freelancers in the U.S. will be able to see your post and submit a proposal."**

Every other country preference is soft. So Frankie's account is the only key to an entire class of job posts that Chitraksh's account cannot see at all, and in our niches that class is large, because dealership BDC and insurance work is disproportionately posted by US clients with compliance reasons to prefer US contractors (`marketplace-expansion.md §3.6`).

### Never do

1. **Never open a second Fiverr account** for "the company", for a brand, or for any reason. One account per person, permanent suspension of the account(s) involved.
2. **Never log into the other person's account**, on any platform, for any reason, not even to fix a typo. This is the single rule that can destroy the business.
3. **Never share payment methods, withdrawal accounts, devices, browsers or IP** between the two Upwork accounts. Linked accounts are flagged by device and browser fingerprint and by payment-method links.
4. **Never front a US identity on an account operated from India.** The account name must be the one used in everyday life and the address must be the business address.
5. **Never reopen a closed Upwork account with the same email.** Upwork names that as a Terms of Service violation in its own FAQ.
6. **Never open a Fiverr agency before a third in-house member exists.** The minimum is 3.
7. **Never route a marketplace conversation off-platform** for payment or for contact details. Fiverr requires all communication on the platform, and personal contact details in a gig are an explicit denial trigger.
8. **Never cancel an Upwork contract ourselves.** Freelancer-initiated cancellations are a very strong JSS negative. Negotiate a reduced-scope close instead.
9. **Never buy a review, coach a review, or place an order for a deliverable we do not genuinely deliver.** Order manipulation is a termination risk, not a warning.
10. **Never claim production-scale metrics.** Answer rate, booking rate and calls-at-scale are not measured. Latency is. Say only what is measured, with the method and the date.

**The asymmetry that settles every judgement call.** The upside of a second account is one extra listing surface. The downside is permanent, unappealable loss of a JSS and a review history that take six months to rebuild, across every linked account, with funds frozen during the appeal.

---

## (d) The 30-day build order, with an owner on every step

Owners: **C** is Chitraksh, who builds and delivers. **F** is Frankie, who sells, fronts the US and holds the US Upwork account that unlocks US-only job posts.

### Days 1 to 2: foundations, everything free or structural

| # | Step | Owner |
|---|---|---|
| 1 | Clear the Fiverr publishing gates in one sitting: ID verification, W-8BEN, India GST form, payout method. Nothing publishes until these clear | C |
| 2 | Open the Upwork freelancer account, India. Complete ID verification the same day, because verification gates Rising Talent | C |
| 3 | Open the US Upwork freelancer account, own device, own payment method, own ID verification | F |
| 4 | Create the Oraya Labs agency from Chitraksh's account, subscribe to Agency Plus, invite Frankie as **business manager** | C, then F accepts |
| 5 | Both profiles to 100% completeness. It is a Rising Talent prerequisite and 10% to 15% of the Upwork search algorithm | C and F |
| 6 | Create two specialized profiles: voice agents and telephony, workflow automation and AI integration | C |
| 7 | **Populate the portfolio. The highest-leverage four hours of the month.** Six entries from `fiverr-profile-package.md §5`, PII-masked views only, no client named | C |
| 8 | Record the **90-second Loom**: a live call on the demo line with the latency readout visible. Largest single measured proposal lift available at +3.70pp | C |
| 9 | Publish Fiverr Gig 1 in the morning, Gig 2 four hours later, Gig 3 the next morning. Verify each slug in the URL bar and record it | C |
| 10 | Subscribe to Seller Plus Kickstart at $15/month, for the keyword data only | C |
| 11 | LinkedIn Services page live, free-consultation toggle on, routed to the Compliance-Safe AI Audit | F |
| 12 | Mirror the three Fiverr gigs as Upwork Project Catalog listings, if the dashboard offers the surface. Connects-free inbound | C |

### Days 3 to 7: first bids and the honeymoon push

| # | Step | Owner |
|---|---|---|
| 13 | Subscribe to Freelancer Plus on the bidding account: 100 Connects a month and competitor bid visibility | F |
| 14 | Turn the Availability Badge on with a hard cap of 100 Connects, about $15, for the month | F |
| 15 | Start bidding, 3 to 5 proposals a day, under 250 words, zero clichés, opening with a specific question, Loom offered every time | F writes and sends, C supplies the technical answer |
| 16 | Point paid traffic at the **Fiverr gig URLs**, not at a landing page, during the honeymoon window | C |
| 17 | Direct outreach to warm dealership and insurance contacts, asking for the $350 audit or the $250 workflow tier, genuinely delivered | F |
| 18 | Claim the free Clutch and GoodFirms profiles | F |
| 19 | Load the first-reply templates into Fiverr Quick Responses. Install the mobile app, notifications on | C |

### Days 8 to 14: instrument and correct

| # | Step | Owner |
|---|---|---|
| 20 | Apply the 14-day decision rule in section (i). The only scheduled stop-and-rewrite point in the month | C and F |
| 21 | Open Contra. Proposals inside the profile's first seven days get search prioritisation, so the signup window matters | F |
| 22 | Read the Kickstart keyword data on day 10 and settle the tool-keyword versus vertical-keyword question with evidence | C |

### Days 15 to 21: widen

| # | Step | Owner |
|---|---|---|
| 23 | Apply to Braintrust. Verification takes 1 to 5 business days and the profile must be complete on submission | C |
| 24 | Scale the winning ad group, kill the losing one. One change per week per surface, so the effect is attributable | C |
| 25 | If a first order has landed, run the case-study protocol in section (h) immediately, not later | C |

### Days 22 to 30: consolidate and set up month 2

| # | Step | Owner |
|---|---|---|
| 26 | Refresh the Fiverr gigs with what the Kickstart keyword data actually said | C |
| 27 | Apply to A.Team, one interview and no project test, and to Fiverr Pro, whose review takes 2 to 4 weeks, so the clock starts now | C applies to A.Team, C applies to Pro |
| 28 | Review the Rising Talent gate: $250 earned plus a 4.8+ rating clears it. One order at our prices is already past it | F |
| 29 | Month 2 budget decision, gated on the measurement contract in section (f) | C and F |

---

## (e) Channel matrix

| Channel | Verdict | Cost | Gate | Reason |
|---|---|---|---|---|
| **Fiverr** | **YES, live now** | 20% flat on earnings | ID, W-8BEN, GST | Three gigs on keyword surfaces with zero AI voice supply. The honeymoon window is the highest-leverage launch action available |
| **Upwork** | **YES, day 1** | 0% to 15%, blended 11% to 13.5% for agencies | ID verification | 127,607 postings in June 2026, one every 20 seconds. Rising Talent clears on one order. The 90-day Top Rated clock starts at first project |
| **LinkedIn Services page** | **YES, week 1** | **$0** | None | Free inbound lead form, prospects self-qualify before we reply. Expect 0 to 2 inquiries a month on a thin profile, 2 to 8 once established. We already run a LinkedIn content engine |
| **Contra** | **YES, week 2** | **0% commission** | None | Zero fee, zero gate, and profiles submitting proposals inside their first seven days get search prioritisation |
| **Braintrust** | **YES, week 3** | **0% from talent**, client pays | Profile plus skills verification, **1 to 5 business days** | Fastest approval of any vetted network, and $80 to $200/hr for AI/ML. Cheapest high-quality option on the list |
| **Clutch, free profile** | **YES, free tier only** | $0 free, $499/year Verified | None on the free tier | Claim it for the directory presence and the backlink. Verified and sponsorship are a 12-month commitment with no early cancellation and no pay-per-lead, so not until 5+ collectible client reviews exist |
| **GoodFirms, free profile** | **YES, free tier only** | $0 free; sponsorship from $300/month | None | Claim the free listing. $300/month for a #15 slot is a worse dollar than $300 of Google Search at a $2.27 automotive CPC |
| **Upwork Project Catalog** | **YES, day 1 if available** | Same service fee as contracts | Eligibility not published, check the dashboard | The Connects-free inbound surface and the direct port of our Fiverr packaging. Confirmed live listings exist in our exact niche |
| **A.Team** | **LATER, month 2** | **0% from builders** | Under 2% acceptance, portfolio plus one 30 to 45 minute interview | Best fit on the list and zero fee, but 12 to 18 month missions are a different business shape. Apply once two named case studies exist. Cheap to try: one call, no project test |
| **Toptal** | **LATER, month 3** | 0% | About 3% acceptance, 2 to 5 weeks of screening plus a 1 to 2 week project test | Best economics on the list, worst time cost during a launch. Apply once Upwork is producing |
| **Catalant** | **LATER, month 3** | Not disclosed | Application and verification in 2 to 5 business days | Enterprise consulting buyers who would pay for an AI governance framework, but the fee structure is undisclosed and we cannot evaluate it. Apply after the compliance offer has a case study |
| **PeoplePerHour** | **LATER, month 3** | 20% to about £250, 7.5% to £5,000, **3.5% above £5,000** | Moderated application; location mismatch risks rejection | The best marginal fee rate of any open marketplace at our price points, but a UK-weighted buyer base that does not match a US insurance and dealership thesis. Revisit if we add UK verticals |
| **Fiverr agency** | **BLOCKED, not a no** | n/a | **Minimum 3 in-house members** | Two founders is one short. Orders, gigs, chats and reviews carry over on switching, so nothing is lost by waiting |
| **Fiverr Pro** | **APPLY, month 1, expect nothing** | n/a | Reported under 3% acceptance, 2 to 4 week review | The vetting weights verifiable off-platform credentials above Fiverr review counts, which is the one screen our law degree, producer licence and measured benchmark actually suit. Start the clock, plan without it |
| **Upwork Talent Scout and Expert-Vetted** | **PHASE 3** | n/a | Invitation and Talent Manager screen, top 1% | Prerequisite is Top Rated Plus at $20,000 of agency earnings in 12 months. Six to eight engagements at target price. Reachable inside a year, not a launch plan |
| **Freelancer.com** | **NO** | 10%, $5 minimum, plus bid memberships | None | Everything Upwork does badly, done worse. A 1,500-bids-a-month model is structurally the opposite of high-signal, low-volume |
| **Arc.dev** | **NO** | Not published | AI screening plus assessments | A $15/hr freelance floor tells you the buyer mix, and it is the opposite of our positioning |
| **Bark** | **NO** | £7 to £40 per **shared** lead, credits expire in 3 months | None | The lead is sold to 3 to 5 competitors at once, the expiry clock forces repurchase, and home-services buyer intent does not exist for a $3,500 compliance-gated deployment |
| **Any paid directory sponsorship** | **NO** | $300 to $1,200/month | None | Pure visibility bets with 12-month commitments and no pay-per-lead. The same dollar buys measured, killable traffic elsewhere |

Summary. Open now and free: LinkedIn Services, Contra, Clutch free, GoodFirms free. Week 3 and fast: Braintrust. Month 2 to 3: A.Team, Toptal, Catalant, PeoplePerHour. Never: Bark, Freelancer.com, Arc.dev, paid directory sponsorship.

---

## (f) Paid visibility plan

**The ordering rule that governs every tier.** Spend the platform-native budget first: Connects, boosts, Kickstart, the Availability Badge. It is measured in tens of dollars and it converts against buyers who are already in-market. Only then buy external traffic, and point it at the **Fiverr gig URL** during the honeymoon window rather than at a landing page, because an order bought with ad money is also a permanent ranking deposit while a landing-page lead is not.

**One mechanic that must be planned around, not wished away: Fiverr Promoted Gigs is unavailable to us in the first 30 days.** Fiverr does not publish the gate; third-party reporting puts it at Level 1 or Level 2 plus a completed-order threshold, with new gigs ineligible until they have conversion data, and the two sources disagree on which level. Any budget plan that assumes Promoted Gigs is wrong. Budget for it in month 2 or 3, and verify the real rule inside the seller dashboard (`marketplace-expansion.md §4.1`).

When it does open it should be very profitable precisely because our anchor is high: typical CPCs run $0.10 to $2.00, the ROI rule is cost per order below 20% of net earnings per order, and at a $450 package netting $360 the ceiling is $72 per order while $0.50 CPC at 5% conversion costs $10.

### Tier 1: $300 in the first 30 days

| Line | Spend | Rationale |
|---|---|---|
| Fiverr Seller Plus Kickstart, 1 month | **$15** | Keyword data settles the tool-versus-vertical question. Refundable within 48 hours of the last monthly payment. Buys no ranking, and nobody should expect any |
| Upwork Freelancer Plus, 1 month | **$20** | 100 Connects, worth $15, plus competitor bid visibility. Net marginal cost about $5 |
| Upwork Agency Plus, 1 month | **$20** | Required to add Frankie as business manager. A structural cost, not a growth cost |
| Extra Upwork Connects, 400 | **$60** | About 40 additional proposals at 10 Connects each |
| Upwork boosts, 25% of proposals at 25 Connects | **$35** | About 14 boosted proposals, on $1,500+ jobs only |
| Availability Badge cap | **$15** | A 100-Connect ceiling for the month |
| Google Search, exact-match long tail | **$135** | About 4 weeks at $4.80 a day. At an automotive-adjacent $2.27 CPC that is roughly 59 clicks. Keywords: "ai receptionist for car dealership", "ai phone agent insurance agency", "tcpa compliant ai calling" |
| **Total** | **$300** | |

Expected: 50 to 70 proposals, 14 boosted, 4 to 5 replies at the 7.45% baseline or 8 to 10 at the 13.77% the full template achieves, plus about 59 paid clicks into the gigs during the honeymoon window. **Target: 1 order.**

### Tier 2: $1,000 in the first 30 days

Everything in Tier 1, plus:

| Line | Spend | Rationale |
|---|---|---|
| Extra Connects, 600 more | **$90** | About 100 proposals across the month, split across both accounts |
| More boosts, 30 more at 25 Connects | **$113** | Boost every job above $2,500 |
| Google Search, scaled | **$300** | About $10 a day. Two ad groups: dealership BDC, insurance agency intake. A separate TCPA ad group at a lower bid |
| Meta lead ads, US, dealership and agency job titles | **$200** | At a $2.52 B2B CPC and a $63.40 B2B SaaS CPL, expect about 3 leads. Offer: the free Compliance-Safe AI Audit |
| Loom or screen recording buffer | **$0 to $25** | The free tier covers 90-second clips |
| **Total** | **about $1,000** | |

Expected: about 100 proposals, 44 boosted, 8 to 14 replies, about 130 paid Google clicks, about 3 Meta audit leads. **Target: 2 to 3 orders and a first review on both platforms.**

### Tier 3: $3,000 in the first 30 days

Everything in Tier 2, plus:

| Line | Spend | Rationale |
|---|---|---|
| Google Search, full | **$900** | About $30 a day across 3 ad groups. At $2.27 to $5.87 CPC that is 150 to 400 clicks, and at 4.85% to 6.01% CVR that is 7 to 24 conversions |
| Meta lead ads, full | **$600** | About 9 leads at $63.40 CPL. Retarget gig visitors and dashboard-demo viewers |
| LinkedIn lead gen forms, US insurance and dealership decision-makers | **$400** | 3 to 5 leads at $75 to $150 CPL, and the highest-quality of the three channels: a reported 6.1% average conversion rate against 3.75% for Google Search. Frankie's account, Frankie's face |
| Extra Connects and boosts | **$100** | Headroom for a high-value week |
| **Total** | **$3,000** | |

Expected: about 120 proposals, 10 to 17 replies, 15 to 38 paid conversions across three channels. **Target: 4 to 6 orders and at least one engagement above $2,500.**

### Tier 4: the no-limits tier, $10,000

The founder directive is "no limits, maximum results". Here is what $10,000 in a month actually buys, and the honest read on each line. This tier is **not authorised until the measurement contract below has passed**, because $10,000 spent against an unmeasured funnel buys noise at seven times the price of $1,500 spent against a measured one.

| Line | Spend | What it adds | Honest read |
|---|---|---|---|
| Google Search, all three ad groups plus a competitor-term group | **$2,500** | 400 to 1,100 clicks a month, full coverage of the long-tail intent set | The best-understood line here. Automotive at $2.27 CPC and $44.26 CPL is the cheapest qualified traffic in the whole benchmark table |
| Meta, prospecting plus retargeting plus a lookalike from audit leads | **$2,000** | About 30 leads at the $63.40 B2B SaaS CPL | Needs a retargeting pixel and a lead volume that does not exist yet. This line is worth nothing in month 1 and a lot in month 3 |
| LinkedIn lead gen forms and thought-leader ads on Frankie's profile | **$2,000** | 13 to 26 leads at $75 to $150 CPL | Highest-intent audience we can buy. Also the slowest to optimise, because CTR sits at 0.44% to 0.65% and a week produces little signal |
| Fiverr Promoted Gigs, once eligible | **$600** | About $20 a day across two gigs at $0.10 to $2.00 CPC | **Only if eligible.** At a $360 net order the ROI headroom is $72 per order, which is generous. This is the highest-expected-return line on the page and it cannot be bought yet |
| Upwork Connects, boosts and Availability at full tilt | **$400** | About 200 proposals a month, boosting every job above $1,500 | The cap here is human. 200 proposals a month at 4 minutes each is 13 hours. Past that, quality collapses and quality is the whole strategy |
| A second Loom and demo-video production pass per vertical | **$800** | Vertical-specific Looms, which outperform generic ones | The +3.70pp Loom lift is per-proposal and specificity is where it comes from. Cheap leverage |
| Contract proposal-writing support, US-hours, supervised | **$1,000** | Raises sustainable proposal volume without Frankie writing all of them | Risky. An outsourced proposal is measurably worse: AI-written proposals reply at 6.91% to 7.13% against 8.13% for hand-written templates. Only worth it as research-and-draft with a human rewrite |
| Paid data and job-alert tooling | **$300** | Faster time-to-proposal, and under 5 minutes replies at 8.99% against 6.91% at 5 to 10 minutes | Small, measurable, and directly attacks the one input with a published effect size |
| Reserve, unallocated | **$400** | Headroom to double the winning line mid-month | An unallocated reserve is what makes a scale decision possible on day 12 instead of day 31 |
| **Total** | **$10,000** | | |

**What we would not buy at any budget:** paid directory sponsorship on Clutch or GoodFirms, Bark credits, Freelancer.com bid memberships, or any placement sold on a 12-month commitment with no pay-per-lead. Those are not expensive, they are unmeasurable, and unmeasurable is the actual disqualifier.

### The measurement contract that gates every increment

**No channel gets more money until it has a measured baseline conversion rate on the previous budget.** Stated as hard gates, in order:

| Gate | Requirement before the next tier unlocks |
|---|---|
| **G1. Baseline exists** | The channel has run at its current budget for at least 7 consecutive days with spend and clicks logged daily through `hub.py ads log` against a registered campaign id |
| **G2. The funnel is measured end to end** | For that channel we can state clicks, then messages or leads, then orders, with real numbers. A channel that produces clicks and no downstream count is unmeasured, whatever the click volume |
| **G3. Cost per message is known** | Cost per message, or cost per interview on Upwork, has a number, not an estimate. Until then there is no denominator and no decision |
| **G4. It beats the alternative** | Its cost per message is at or below the cheapest currently-running channel, or it is the only channel reaching that audience and we say so in writing |
| **G5. The kill rule is written first** | The campaign record in `ads/campaigns.json` carries a kill rule with a number in it, entered before the spend, not rationalised after |
| **G6. One variable at a time** | No two gigs promoted in the same week during launch, and no simultaneous budget change plus creative change on the same campaign. Two variables moving at once produces a result nobody can attribute |

**Increment sizes.** Scale a proven line by at most **2x per week**. A channel that doubles weekly from $135 reaches $2,160 in five weeks, which is faster than we can generate the case studies to support the volume anyway. Kill a channel outright rather than halving it: a half-funded ad group produces half-signal at full attention cost.

---

## (g) The daily 30 minutes and the weekly review

Run the daily block at the same time every day, ideally overlapping the US morning, so that sub-5-minute proposal speed on fresh US posts is actually achievable.

| Minutes | Action | Why |
|---|---|---|
| **0 to 5** | **Clear the inbox on both platforms.** Every buyer message answered inside 60 minutes between 08:00 and 23:00 IST | Response time is an explicit Fiverr ranking input and 15% to 20% of the Upwork algorithm. Nothing else in this routine matters more, and it is the only lever that works from hour one |
| **5 to 10** | **Log yesterday's numbers.** Fiverr impressions, clicks, CTR, orders, response rate. Upwork proposals sent, viewed, interviews, Connects spent, invitations. Five minutes, no analysis | The analysis happens weekly. Mixing collection and interpretation is how a noisy day becomes a strategy change |
| **10 to 22** | **Scan and bid.** Filter Upwork to the eight ranked niches, posted in the last hour, client payment verified, budget $1,000+. Pick 2 to 3. Four minutes per proposal from the template. Boost only $1,500+ jobs where we have named-vertical proof | 24.0% of postings come from clients with unverified payment. Filtering is the skill |
| **22 to 27** | **One proof increment.** A screenshot annotated, a vertical-specific Loom recorded, a gig FAQ improved, one LinkedIn post published | Compounding, not urgent. The two largest measured proposal lifts both need fresh specific material |
| **27 to 30** | **Check the three red flags, then log what you did.** Response rate below 90%? Interview rate below 5% over the last 20 proposals? Fiverr CTR below 2% with healthy impressions? | Any yes turns tomorrow's bidding block into a rewrite block |

Commands for minutes 5 to 10 and 27 to 30 are in `monitoring/daily-check.md`. Nothing in this routine is done from memory.

**The weekly review, 30 to 40 minutes, same day each week.** Same slot, replacing minutes 22 to 30, and it is where decisions are made. The daily loop collects, the weekly loop decides, and keeping them apart is what stops one bad day from rewriting the plan.

1. `python3 hub.py metrics report` and read the week-over-week deltas and every flag.
2. Pull the Upwork JSS. It recalculates daily but only displays every 14 days, so half of these reads will be unchanged by design.
3. Read the six Fiverr Success Score components: client satisfaction, communication quality, order quality, revision handling, dispute resolution, delivery experience.
4. Read the Seller Plus Kickstart keyword data and note which search terms actually landed.
5. Review ad CPC and CPL against the benchmarks in `ads/ads-plan.md`, and apply the measurement contract gates before any budget change.
6. Read the badge-gap line in Upwork Stats and trends, which names the next badge and the distance to it.
7. Decide **one** change per surface, write it in the ledger with the reason, and change nothing else.
8. `python3 hub.py export` and commit the report.

---

## (h) The case-study capture protocol

Every engagement must produce a reusable asset, because the two largest measured proposal lifts are a Loom walkthrough at **+3.70pp** and referencing recently completed work at **+2.52pp**, and both need fresh, specific, defensible material. The protocol also has to survive our own rules: no fabricated metrics, no fake social proof, no invented client stories, and client data anonymised.

**Step 1, before the build starts.** One clause in the scope message: permission to describe the work anonymously, by industry and outcome, with no company name, no logo, no recording. Ask at kickoff, never at the end. A client who says yes at the start says yes at the end. A client asked at the end says "let me check with legal".

**Step 2, during the build, capture as you go.** Screenshot the latency waterfall on a real call on their number. Screenshot the compliance panel showing the locked disclosure as the first utterance. Screenshot the **before** state on day one, the voicemail greeting, the missed-call log, the manual intake sheet, because it cannot be recreated later. Record the per-call cost telemetry.

**Step 3, at delivery, ask for exactly four things, in one message, three of them one click.**

1. A **public review**, with a suggested sentence they are free to edit. Ask for honest feedback, never for stars: Fiverr collects invisible private feedback that feeds ranking separately, and Upwork weights private feedback 1 to 10 as heavily as the public rating.
2. **One number they care about**, in their words: calls answered after hours, bookings taken, minutes of staff time returned. One number, not a survey.
3. **Permission to quote one sentence**, attributed to a role and industry only, such as "Service manager, 3-rooftop dealership group, Midwest US".
4. **A 30-day check-in slot**, which doubles as the retainer conversation and as JSS insurance, because recurring clients paying every 90 days weigh very high in JSS.

**Step 4, anonymisation, applied before anything leaves the building.**

- Replace the business name with industry plus size plus region: "independent P&C agency, 12 producers, US Southeast".
- Blur or replace phone numbers, caller names, addresses, policy numbers and VINs in every screenshot. Screenshot the PII-masked dashboard view by default, because the public dashboard already reads masked views only.
- Never publish call audio.
- State every measured number with its method and date: "median 761 ms time-to-first-audio, measured over simulated calls on the deployed demo, 26 August 2026".
- **Never present a demo or simulated-call metric as a production-scale metric.** Answer rate, booking rate and calls-at-scale are not measured and must not be claimed.
- Compliance framing carries the "engineering, not legal advice" line. Never imply US bar admission. Never imply insurance licensure.

**Step 5, within 48 hours, produce three artefacts from every delivery.**

1. A **one-paragraph case card**: vertical, problem, what we built, the one number, the anonymised quote. This is what gets pasted into proposals as recently completed work.
2. A **new 60 to 90 second Loom** for that vertical. Vertical-specific Looms outperform generic ones because specificity is where the lift comes from.
3. A **portfolio item** on both Upwork specialized profiles and in the Fiverr gig gallery, plus one LinkedIn post carrying a real number, a real artifact or a first-person story.

**Step 6, feed it back into pricing.** After every third delivery, raise the entry price by 10% to 15%. Price and credential outrank review count in this category on both platforms. Raising price is a growth action, not a risk.

The operational version of this protocol, with the exact messages, is `playbooks/case-study-capture.md`. Every step gets logged.

---

## (i) Leading indicators and the kill/scale rules

Ranked by how early they move and how reliably they precede money (`marketplace-expansion.md §6.4`).

| # | Indicator | Where | Healthy | Action threshold |
|---|---|---|---|---|
| 1 | **Upwork proposal view rate**, viewed ÷ sent | Stats and trends | Moves within 24 hours of a send | If proposals are sent and not opened, the problem is the first two lines and the profile headline, not the offer. Fixable same-day |
| 2 | **Upwork interview rate**, interviews ÷ sent | Stats and trends | 7.45% baseline, **13.77%** with the full template | **Below 5% after 20 proposals: stop bidding and rewrite.** Above 13%: raise volume immediately |
| 3 | **Fiverr click-through rate** | Gig analytics | 2% to 5% typical, 8% to 15% strong | Moves within 48 hours of publishing. Below 2% with impressions arriving: the thumbnail and title are wrong. No impressions at all: the category and tags are wrong |
| 4 | **Message response time**, both platforms | Fiverr public profile, Upwork responsiveness | Under 1 hour | The only indicator that is 100% within our control and an explicit ranking input on both platforms. Over 1 hour is a same-day fix, not a weekly discussion |
| 5 | **Upwork invitations received** | Stats and trends | Any | The purest signal that the profile itself converts, independent of any proposal. Zero invitations in 14 days of Availability Badge spend: turn the badge off |
| 6 | **Fiverr conversion rate**, orders ÷ clicks | Computed | 3% to 8% strong | Under 2% with healthy click volume means the packages, the ladder or the description are failing, not the discovery |
| 7 | **$1,500+ jobs identified per day** | Manual count | 3 to 5 | A pipeline input, not a platform metric. Below 3 a day means the niche filters are wrong, and no amount of proposal quality compensates |

### The 14-day decision rule

At day 14, exactly one of three things happens.

- **Interview rate above 7% and no hire yet: change nothing and keep going.** 20 to 80 serious proposals is the documented range to a first client. Changing the template at proposal 25 destroys the only sample we have.
- **Interview rate below 5%: stop bidding for one full day.** Rewrite the two opening lines, record a new Loom, then resume. Do not do both a rewrite and a volume increase.
- **Proposals not being opened at all: the problem is upstream of the proposal.** It sits in the profile headline, the specialized-profile choice or the badge state. Fix there, not in the cover letter.

### Kill rules

| Kill | Trigger |
|---|---|
| A paid campaign | 7 days of spend producing clicks and zero messages, or cost per message above 10% of the Basic package price on the target gig, or any spend with zero clicks (pause first, diagnose second) |
| The Availability Badge | Zero invitations across 14 days of badge spend |
| Boosting | Boosted interviews not exceeding organic interviews over 20 boosted proposals |
| A proposal template | Interview rate below 5% over 20 proposals |
| A gig | 30 days live with 500+ impressions and a CTR below 1%, after one image change and one title change have each had their own week |
| A niche filter | Fewer than 3 qualifying $1,500+ jobs a day for a full week |
| An outsourced proposal writer | Any measured drop below the hand-written baseline |

### Scale rules

| Scale | Trigger |
|---|---|
| Proposal volume | Interview rate above 13% over 20+ proposals. Raise volume before touching anything else, because the template is working |
| A paid channel | All six measurement gates in section (f) passed, then at most 2x per week |
| Price | Every third delivery, up 10% to 15% |
| A winning ad group | Its cost per message at or below every other running channel, then 2x, with nothing else changed that week |
| Promoted Gigs | The moment eligibility is confirmed in the dashboard, at $3 to $5 a day for two to three weeks, on one gig only |
| A new channel from the section (e) matrix | Only when the current channels are at their human capacity ceiling, not when they are merely uncomfortable |

**The one rule underneath all of them: no scaling without a measured baseline conversion.** "Perform on the budget" means the budget has to be attributable to an outcome. A channel that cannot be measured cannot be scaled, and it cannot be defended either.
