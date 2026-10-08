# Marketplace Expansion: Upwork, Multi-Account Structure, Paid Visibility and the Channel Hub
### Oraya / Hanflux AI, September 2026

**Scope.** This is the companion to `fiverr-market.md`. That document established the Fiverr surface: the vertical keywords are empty, the tool keywords are saturated at the floor, compliance is sold by nobody, and Fiverr ranks credential and price above review count. This document covers everything that sits outside Fiverr: the Upwork market and its mechanics, the exact multi-account rules that govern a two-founder company, paid visibility on both platforms plus off-platform ads, the other channels worth a slot, the monitoring instrumentation, and the 30-day operating model.

**Who we are, for the reader who arrives here first.** Chitraksh Mayank, graduate lawyer (B.B.A. LL.B. Hons., Business Law), based in India, builds and ships the product: Twilio ConversationRelay plus Deepgram Flux STT plus Claude Haiku 4.5 plus ElevenLabs Flash, on Supabase, with measured median time-to-first-audio of **761 ms to 900 ms** against a prior-vendor production baseline of **p50 approximately 1.64 to 1.9 seconds**, and with TCPA, CIPA, FCC AI-disclosure, DNC and quiet-hours logic enforced in code rather than in a prompt. Frankie Alicea, US-based licensed insurance producer, is the sales lead and the US-facing face. Every figure in this paragraph is from `oraya-facts.md` sections 1 and 4.

**Writing rule observed throughout:** no em dashes, per `oraya-growth-engine/WRITING-RULES.md`.

---

## 0. THE ONE-PARAGRAPH ANSWER

Upwork is a **bigger, better-paying, and structurally more hostile** market than Fiverr for us. Bigger: **127,607 deduplicated public job postings in June 2026**, one every 20 seconds ([Vibeworker Upwork job market report, June 2026](https://tryvibeworker.com/blog/upwork-job-market-report-june-2026)). Better-paying at the top: Upwork's own buyer guidance puts a production-grade voice deployment at **$2,400 to $24,000** ([Upwork: hire AI voice agent developers](https://www.upwork.com/hire/ai-voice-agent-developers/)) against Fiverr page-one entry prices of $10 to $90. Structurally hostile because the median posted fixed budget is **$100** and the median effective hourly rate is **approximately $8.75** ([Vibeworker](https://tryvibeworker.com/blog/upwork-job-market-report-june-2026)), because the mean proposal reply rate across 133,872 measured proposals is **7.45%** ([GigRadar AI proposals data](https://gigradar.io/blog/ai-proposals-upwork)), and because every proposal costs real money at **$0.15 per Connect** ([Upwork: Understanding and using Connects](https://support.upwork.com/hc/en-us/articles/211062898-Understanding-and-using-Connects)). The winning shape is therefore not "post gigs and wait" as on Fiverr, but **a small number of very high-signal proposals into under-fished niches, sent fast, priced high, backed by a Loom**. On multi-accounts: both platforms permit exactly one account per human, both permit a legitimate agency on top, and we have two humans, so the compliant structure is three entities and no grey area at all.

---

## 1. UPWORK MARKET, SEPTEMBER 2026

### 1.1 Platform size, direction and money

| Metric | Value | Source |
|---|---|---|
| Public job postings, June 2026 (deduplicated) | **127,607** | [Vibeworker](https://tryvibeworker.com/blog/upwork-job-market-report-june-2026) |
| Posting cadence | one every **20 seconds** | [Vibeworker](https://tryvibeworker.com/blog/upwork-job-market-report-june-2026) |
| Q1 2026 Gross Services Volume | **$987M**, flat year over year | [GigRadar Upwork market report 2026](https://gigradar.io/blog/upwork-market-report-2026) |
| Active clients | **784,000**, down 6% from 832,000 | [GigRadar](https://gigradar.io/blog/upwork-market-report-2026) |
| GSV per active client | **$5,138**, up 5% | [GigRadar](https://gigradar.io/blog/upwork-market-report-2026) |
| **AI category annualized GSV** | **$300M, up 50% year over year** | [GigRadar](https://gigradar.io/blog/upwork-market-report-2026) |
| Jobs completed on Upwork, 2025 | **1.9 million** | [Upwork: hire AI agent developers](https://www.upwork.com/hire/ai-agent-developers/) |
| First-time clients who complete a contract | **89%** | [Upwork](https://www.upwork.com/hire/ai-agent-developers/) |
| Average time from job post to first proposal | **three hours** | [Upwork: hire AI voice agent developers](https://www.upwork.com/hire/ai-voice-agent-developers/) |

The shape matches Fiverr's: fewer buyers, more money each, and AI as the only growing line. Fiverr's annual active buyers fell 21.9% while spend per buyer rose 15.6% and $1,000+ projects grew 13% ([Fiverr Q2 2026 results](https://www.fiverr.com/news/fiverr-q2-2026-earnings)). Upwork's client count fell 6% while GSV per client rose 5% and AI GSV rose 50%. **Both marketplaces are consolidating into higher-value work, and AI is where the growth sits on both.**

### 1.2 Upwork's own demand data

From [Upwork's In-Demand Skills 2026 press release](https://www.upwork.com/press/releases/upworks-in-demand-skills-2026-demand-for-top-ai-skills-more-than-doubles-as-ai-is-embedded-into-everyday-work), published 4 February 2026, with growth measured year over year:

| Skill | Growth | Category |
|---|---|---|
| AI Video Generation & Editing | **+329%** | Design & Creative |
| **AI Integration** | **+178%** | Coding & Web Development |
| AI Data Annotation & Labeling | +154% | Data Science & Analytics |
| Ecommerce Management | +130% | Customer Service & Admin |
| AI Image Generation & Editing | +95% | Design & Creative |
| **AI Chatbot Development** | **+71%** | Coding & Web Development |
| Medical Virtual Assistance | +44% | Customer Service & Admin |
| Generative AI Modeling | +21% | Data Science & Analytics |

Headline figures from the same release: **skills explicitly tied to applying AI within existing roles grew 109% year over year**; **77% of business leaders say AI is increasing their need for specialized, fractional talent rather than traditional full-time roles**; and nearly half of business leaders say they would pay a premium for creative and innovative independent talent.

Two readings matter for us. First, **"AI Integration" at +178% is the single most relevant named skill to what we actually sell**, and it is the fastest-growing coding skill on the platform. Second, freelancers doing AI work are reported to earn **34% more per hour than non-AI freelancers across all categories** ([RemoteAITools analysis of Upwork data](https://remoteaitools.com/upwork-ai-automation-jobs-2026/)).

### 1.3 Tool-mention density: the supply-side early warning

Vibeworker counts tool mentions per 100,000 postings, which is the closest available proxy for what buyers are actually asking for by name ([Vibeworker, June 2026](https://tryvibeworker.com/blog/upwork-job-market-report-june-2026)):

| Tool named in job post | Mentions per 100k postings | Month-over-month |
|---|---|---|
| Claude | **433.4** | −12.2% |
| **n8n** | **283.7** | −11.0% |
| "AI agent" | 269.6 | −6.1% |
| **OpenAI** | 88.6 | **+30.5%** |
| ChatGPT | 58.8 | −9.3% |
| Gemini | 34.5 | +1.5% |

Claude is the most-named model on Upwork job posts by a factor of nearly 5x over OpenAI, which is consistent with Fiverr's **+938% Claude Code search surge** ([Fiverr Business Trends Index June 2026](https://www.fiverr.com/resources/guides/reports/business-trends-index-june-2026)). n8n is the second-most-named tool on the entire platform. Neither Vapi nor Retell nor LiveKit nor ElevenLabs appears in the top tool list at all, which tells us the voice-agent vendor names are **below the measurement threshold on Upwork** while they carry 12,000 to 15,000 services each on Fiverr. That asymmetry is the whole Upwork thesis: **on Upwork, voice work is bought by outcome and by integration stack, not by vendor name.**

### 1.4 Live job-post volumes by niche

Read directly off `upwork.com/freelance-jobs/<slug>/` pages, which publish an exact "N open jobs" counter, on 11 September 2026.

| Niche (slug) | Open jobs | Source |
|---|---|---|
| [cold-calling](https://www.upwork.com/freelance-jobs/cold-calling/) | **4,135** | Upwork |
| [outbound-sales](https://www.upwork.com/freelance-jobs/outbound-sales/) | **3,804** | Upwork |
| [lead-generation](https://www.upwork.com/freelance-jobs/lead-generation/) | **3,116** | Upwork |
| [automation](https://www.upwork.com/freelance-jobs/automation/) | **2,212** | Upwork |
| [appointment-setting](https://www.upwork.com/freelance-jobs/appointment-setting/) | **2,024** | Upwork |
| [artificial-intelligence](https://www.upwork.com/freelance-jobs/artificial-intelligence/) | **1,892** | Upwork |
| [chatbot-development](https://www.upwork.com/freelance-jobs/chatbot-development/) | **1,159** | Upwork |
| [conversational-ai](https://www.upwork.com/freelance-jobs/conversational-ai/) | **1,119** | Upwork |
| [api-integration](https://www.upwork.com/freelance-jobs/api-integration/) | **790** | Upwork |
| [n8n](https://www.upwork.com/freelance-jobs/n8n/) | **626** | Upwork |
| [ai-compliance-skills](https://www.upwork.com/freelance-jobs/ai-compliance-skills/) | **373** | Upwork |

Note the shape. **Cold calling, outbound sales, lead generation and appointment setting together carry more than 13,000 open jobs**, roughly six times the AI-and-automation cluster. Almost all of that demand is currently being filled by human VAs at $6 to $20 per hour ([Upwork: hire cold callers](https://www.upwork.com/hire/cold-callers/) reports cold callers "typically charge $11 to $20 per hour", with featured profiles at $6 and $7). **That is the arbitrage on Upwork: 13,000 buyers who have already decided they need outbound calling and are currently buying it as headcount, not as software.**

### 1.5 What buyers actually pay: Upwork's published guidance by niche

Upwork publishes buyer-facing price expectations on each `/hire/` page. These are not freelancer asks; they are the numbers Upwork itself sets in the buyer's head before the buyer posts. Treat them as the ceiling we are allowed to quote without looking mad.

**AI voice agent developers** ([source](https://www.upwork.com/hire/ai-voice-agent-developers/)), hourly guidance **$30 to $150/hr**:

| Engagement | Range |
|---|---|
| Single-flow voice agent | **$600 to $6,000** |
| Multi-intent voice assistant | **$1,200 to $12,000** |
| Production-grade deployment | **$2,400 to $24,000** |
| Enterprise multi-agent system | **$4,800 to $48,000** |
| Ongoing maintenance and optimization | **$1,500 to $4,500** |

**AI agent developers** ([source](https://www.upwork.com/hire/ai-agent-developers/)), hourly guidance **$30 to $150/hr**, 4.8/5 across **12,953 client reviews**:

| Engagement | Range |
|---|---|
| Chatbot / virtual assistant | $500 to $2,000 |
| **Workflow automation agent** | **$2,000 to $5,000** |
| Custom LLM-powered agent | $5,000 to $15,000 |
| Multi-agent system | $10,000 to $30,000 |
| Ongoing maintenance | $1,000 to $5,000 |

**Conversational AI specialists** ([source](https://www.upwork.com/hire/conversational-ai-specialists/)), hourly **$5 to $150**, most clustering **$30 to $61**, 4.9/5 across **633 reviews**:

| Engagement | Range |
|---|---|
| Basic FAQ / support chatbot | $1,200 to $3,000 |
| Multi-intent NLU assistant | $3,000 to $7,500 |
| **Voice / IVR systems** | **$5,000 to $12,000** |
| Enterprise multichannel assistant | $12,000 to $30,000 |
| Ongoing optimization retainer | $1,500 to $5,000/month |

**n8n experts** ([source](https://www.upwork.com/hire/n8n-experts/)), hourly **$40 to $100**, 4.8/5 across **5,201 reviews**:

| Engagement | Range |
|---|---|
| Basic app-to-app workflows | $200 to $600 |
| **Custom integrations with error handling** | **$800 to $2,500** |
| Enterprise automation pipelines | $3,000+ |
| Ongoing support / optimization | $800 to $3,000/month |

**MCP server developers** ([source](https://www.upwork.com/hire/mcp-server-developers/)), hourly **$17 to $95** (entry $17 to $20, mid $35 to $50, senior $95+), 4.8/5 across only **310 reviews**.

**AI policy compliance professionals** ([source](https://www.upwork.com/hire/ai-policy-compliance-professionals/)), hourly **$29 to $75**:

| Engagement | Range |
|---|---|
| Policy and gap assessment | $600 to $1,500 |
| Bias and risk audit | $1,200 to $3,000 |
| **AI governance framework** | **$1,500 to $4,000** |
| Ongoing compliance advisory | $2,000 to $6,000 |

**Cold callers** ([source](https://www.upwork.com/hire/cold-callers/)), hourly **$11 to $20**, 4.6/5 across **18,780 reviews**:

| Engagement | Range |
|---|---|
| Lead list building | $200 to $500 |
| Short-term campaigns | $500 to $1,500 |
| Ongoing support | $1,000 to $3,000 |
| **Full-funnel appointment setting** | **$2,000 to $5,000** |
| Strategic programs | $3,000 to $8,000 |

### 1.6 The reality check: what jobs are actually posted at

Upwork's guidance is aspirational. The posting distribution is not. From [Vibeworker's 50,019 fixed-price postings with listed budgets, June 2026](https://tryvibeworker.com/blog/upwork-job-market-report-june-2026):

| Budget band | Count | Share |
|---|---|---|
| Under $50 | 15,738 | **31.5%** |
| $50 to $100 | 6,644 | 13.3% |
| $100 to $250 | 10,707 | 21.4% |
| $250 to $500 | 5,783 | 11.6% |
| $500 to $1,000 | 4,907 | 9.8% |
| **$1,000+** | **6,240** | **12.5%** |

Median posted budget **$100**. Median effective hourly rate **approximately $8.75**. A further **49,099 postings used hourly billing**. Experience level requested: Intermediate 67.4% (85,926 jobs), Expert 24.4% (31,069), Entry 8.3% (10,541). And **24.0% of postings come from clients with unverified payment**, with 4.8% carrying a red-flag score of 3 or below out of 10.

Live examples found on the public job pages, September 2026, which show the full spread inside our exact niche:

- "Create Simple Conversational Retell AI / Vapi Voice Agent with Basic API & n8n Setup", **$10.00 fixed price** ([Upwork job](https://www.upwork.com/freelance-jobs/apply/Create-Simple-Conversational-Retell-Vapi-Voice-Agent-with-Basic-API-n8n-Setup_~022072486623594733415/))
- "Outbound AI Voice Agent Developer (Vapi, Twilio, n8n) for Cold Calling Automation", **$150.00 fixed price** ([Upwork job](https://www.upwork.com/freelance-jobs/apply/Outbound-Voice-Agent-Developer-Vapi-Twilio-n8n-for-Cold-Calling-Automation_~022087531216573679596/))
- "Retell AI Voice Agent + n8n + GoHighLevel Automation for Booking & Lead Management", **$50** ([n8n jobs page](https://www.upwork.com/freelance-jobs/n8n/))
- "n8n+Claude Automation for Freight Quoting Workflow", **$1,000** ([api-integration jobs page](https://www.upwork.com/freelance-jobs/api-integration/))
- "AI Agent Engineer for Enterprise SaaS Integration & Support Workflows", **$2,000** ([api-integration](https://www.upwork.com/freelance-jobs/api-integration/))
- "AI-powered SMS assistant for watersports rental business", **$3,000** ([chatbot-development](https://www.upwork.com/freelance-jobs/chatbot-development/))
- "Mobile App Developer Needed to Build V1 No-Code MVP", **$25,000** ([conversational-ai](https://www.upwork.com/freelance-jobs/conversational-ai/))

**The $10 Retell job and the $2,000 enterprise agent job are the same category.** The entire skill on Upwork is filtering, and filtering costs Connects, which is why section 2 matters as much as this one.

### 1.7 Proposal volume and reply rates: the competitive density

The single best dataset available is GigRadar's analysis of **133,872 proposals sent between December 2025 and February 2026** ([GigRadar Upwork market report 2026](https://gigradar.io/blog/upwork-market-report-2026)).

**Platform mean reply rate: 7.45%.** By category:

| Category | Reply rate |
|---|---|
| Game Design & Development | 14.58% |
| **Lead Generation & Telemarketing** | **14.38%** |
| Sales & Marketing Copywriting | 14.24% |
| Marketing / PR / Brand Strategy | 13.64% |
| **Information Security & Compliance** | **11.21%** |
| Product Design / UX | 10.78% |
| **AI & Machine Learning** | **7.21%** |
| Web Development | 5.80% |
| Mobile Development | 5.60% |

Read that table next to section 1.4. **Lead Generation & Telemarketing has 3,116 to 4,135 open jobs AND the second-highest reply rate on the platform at 14.38%, nearly double AI & Machine Learning at 7.21%.** Information Security & Compliance at 11.21% is the third data point that says the same thing: the compliance-and-outbound framing wins on Upwork for exactly the reason it wins on Fiverr, which is that the people selling into it are not technical and the people selling AI are not compliance-literate.

By client type:

| Client lifetime spend | Reply rate |
|---|---|
| $1,000 to $5,000 | **8.15%** (highest) |
| $0, brand new | 6.89% |
| $500,000+ "whales" | 3.85% (lowest) |

By bid position relative to the posted budget:

| Bid as % of posted budget | Reply rate |
|---|---|
| Under 50% | 20.6% |
| **200% to 500% (premium bid)** | **16.4%** |
| 95% to 105% (matching the budget) | **8.8%, the worst position** |

That third row is counterintuitive and extremely actionable: **bidding exactly the posted budget performs worse than bidding two to five times it.** Matching the budget signals a commodity supplier. Bidding 3x with a reason attached signals a different category of vendor. This is the Upwork restatement of the Fiverr finding that a low anchor keeps you off page one.

By speed:

| Time from post to proposal | Reply rate |
|---|---|
| Under 5 minutes | **8.99%** |
| 5 to 10 minutes | 6.91% |
| 12 to 15 minutes | 8.07% |

And on proposal density: premium opportunities attract **40+ proposals within 2 hours of posting** ([UpHunt first-client guide](https://uphunt.io/blog/how-to-get-first-client-upwork-2026-complete-guide)), with practitioners reporting **20 to 50 proposals on essentially every beginner-to-intermediate post** ([Quora practitioner thread, 2026](https://www.quora.com/Upwork-in-2026-every-job-post-for-beginner-intermediate-has-20-to-50-proposals-and-connects-are-pricier-the-platform-is-primed-for-established-professionals-and-against-newbies-What-advice-can-you-give-a-web-dev)).

### 1.8 Supply: how many competitors, and how good

Upwork does not publish per-skill freelancer counts. The usable proxy is the total client-review count on each `/hire/` page, which scales with the number of completed engagements in that skill and therefore with entrenched supply.

| Niche | Client reviews (supply proxy) | Rating | Source |
|---|---|---|---|
| Cold callers | **18,780** | 4.6/5 | [Upwork](https://www.upwork.com/hire/cold-callers/) |
| AI agent developers | **12,953** | 4.8/5 | [Upwork](https://www.upwork.com/hire/ai-agent-developers/) |
| n8n experts | **5,201** | 4.8/5 | [Upwork](https://www.upwork.com/hire/n8n-experts/) |
| Conversational AI specialists | **633** | 4.9/5 | [Upwork](https://www.upwork.com/hire/conversational-ai-specialists/) |
| **MCP server developers** | **310** | 4.8/5 | [Upwork](https://www.upwork.com/hire/mcp-server-developers/) |

MCP at 310 reviews is the thinnest entrenched supply of any niche measured on either platform, and it sits adjacent to Claude at 433.4 mentions per 100k postings, the most-named tool on Upwork. On Fiverr, `mcp-server` carried 2,487 services at a uniform $100 anchor (`fiverr-market.md` section 1.2). **MCP is thin on both platforms simultaneously and adjacent to the largest demand signal on both.**

### 1.9 The eight best niches for us, ranked by demand against defensible supply

Scoring: demand from live job counts and Upwork's own growth data; supply from review-count proxies and observed rate floors; reply rate from the GigRadar category table; fit from `oraya-facts.md` sections 1, 2 and 4 (what we can actually prove).

| Rank | Niche | Demand signal | Supply | Category reply rate | Our proof | Price to bid |
|---|---|---|---|---|---|---|
| **1** | **TCPA-compliant outbound / AI SDR calling for regulated verticals** | 4,135 cold-calling + 3,804 outbound-sales + 2,024 appointment-setting open jobs | Human VAs at $6 to $20/hr, zero compliance framing | **14.38%** (Lead Gen & Telemarketing) | Consent, DNC, quiet-hours and AI-disclosure gating enforced in code; CIPA, TCPA, 47 CFR 64.1200, AB 2905, TSR verified against primary sources | **$3,500 to $8,000** fixed, or $95 to $150/hr |
| **2** | **AI voice receptionist for insurance agencies** | BFSI is 32.9% of the AI voice agent market ([CloudTalk](https://www.cloudtalk.io/blog/ai-voice-agent-statistics/)); voice/IVR guidance $5,000 to $12,000 | Conversational AI has only 633 reviews; no insurance-specific supply found | 7.21% base, lifted by vertical framing | Frankie is a licensed producer; insurance-side content track already built | **$2,500 to $6,000** |
| **3** | **AI voice agent / BDC automation for auto dealerships** | Production-grade voice deployment guidance $2,400 to $24,000 | Same thin conversational-AI supply | 7.21% base | Reference dealership build live, TTFT median 761 ms, deviation register vs prior vendor documented | **$2,500 to $6,000** |
| **4** | **Sub-second-latency voice infrastructure (measured TTFT as the product)** | "AI Integration" +178%, the fastest-growing coding skill | Nobody on either platform publishes a measured latency number with method | 7.21% | **Median 761 ms to 900 ms measured, against prior-vendor p50 of 1.64 to 1.9s**; per-stage latency budget documented | **$4,000 to $10,000** |
| **5** | **Production n8n pipelines with error handling, retries and monitoring** | 626 open n8n jobs; n8n is the 2nd most-named tool at 283.7 per 100k | 5,201 reviews, crowded but shallow; $200 to $600 basic anchors | 7.21% | Post-call webhook already shaped to a 41-node n8n pipeline | **$1,200 to $3,000** (Upwork's own "custom integrations with error handling" band is $800 to $2,500) |
| **6** | **MCP server development** | Claude at 433.4 mentions per 100k, the most-named tool on Upwork | **310 reviews, the thinnest supply measured anywhere** | 7.21% | Claude-native architecture throughout the stack | **$1,500 to $4,000** |
| **7** | **AI compliance audit and governance framework (non-voice)** | 373 open AI-compliance jobs; guidance $1,500 to $4,000 for a governance framework | $29 to $75/hr, generalist policy people with no build capability | **11.21%** (InfoSec & Compliance) | Lawyer plus engineer in one person is the exact gap; primary-source compliance work already done | **$1,500 to $4,000**, plus it feeds ranks 1 to 4 |
| 8 | **Claude / OpenAI custom agents in Python or Node** | Claude 433.4 and OpenAI 88.6 (+30.5% MoM) mentions per 100k | 12,953 reviews, genuinely crowded | 7.21% | Direction-aware single-brain agent replacing a two-agent vendor split | $2,000 to $5,000 (Upwork's "workflow automation agent" band) |

**Not recommended as an entry wedge:** generic AI chatbot (1,159 jobs but $500 to $2,000 guidance and commoditized), generic lead generation (3,116 jobs but the Fiverr prohibited-services problem on selling scraped contact data applies to the same framing here, per [Fiverr prohibited services](https://help.fiverr.com/hc/en-us/articles/49174165608593-Prohibited-services-on-Fiverr)), and Twilio-only telephony plumbing (no dedicated Upwork jobs slug, weak as a standalone).

**The single highest-leverage insight in this section:** rank 1 and rank 7 sit in the two highest-reply-rate categories on Upwork (14.38% and 11.21%) while every pure-AI framing sits at 7.21%. **Leading a proposal with compliance and outbound rather than with AI roughly doubles the odds of getting read.**

---

## 2. UPWORK MECHANICS FOR A NEW PROFILE

### 2.1 Connects: the cost of existing

| Item | Value | Source |
|---|---|---|
| Price per Connect | **$0.15** | [Upwork Connects help](https://support.upwork.com/hc/en-us/articles/211062898-Understanding-and-using-Connects) |
| Free monthly Connects, Basic plan | **10** | [Upwork help](https://support.upwork.com/hc/en-us/articles/211062898-Understanding-and-using-Connects), [GigRadar fees](https://gigradar.io/blog/upwork-fees) |
| One-time new-freelancer bonus | **50 Connects, only after purchasing Connects or subscribing to Freelancer Plus** | [Upwork help](https://support.upwork.com/hc/en-us/articles/211062898-Understanding-and-using-Connects) |
| Minimum purchase | 10-Connect packs | [GigRadar](https://gigradar.io/blog/upwork-fees) |
| Cost per proposal, basic/entry job | 4 to 6 Connects = **$0.60 to $0.90** | [OutBid Connects calculator](https://useoutbid.com/blog/upwork-connects-cost-per-proposal-2026) |
| Cost per proposal, standard job | 8 to 10 Connects = **$1.20 to $1.50** | [OutBid](https://useoutbid.com/blog/upwork-connects-cost-per-proposal-2026) |
| Cost per proposal, large budget | 12 to 14 Connects = $1.80 to $2.10 | [OutBid](https://useoutbid.com/blog/upwork-connects-cost-per-proposal-2026) |
| Cost per proposal, enterprise/featured | 14 to 16 Connects = $2.10 to $2.40 | [OutBid](https://useoutbid.com/blog/upwork-connects-cost-per-proposal-2026) |
| Typical burn per proposal, all-in | 6 to 16 Connects | [GigRadar fees](https://gigradar.io/blog/upwork-fees) |

Connects are refunded **only** if the client cancels the job before any contract is formed, or Upwork removes the post for a Terms of Service violation. They are **not** refunded for a rejected proposal, a client hiring someone else, an expired job, or a withdrawn proposal ([Upwork help](https://support.upwork.com/hc/en-us/articles/211062898-Understanding-and-using-Connects)).

**Cost per acquired client, by win rate** ([OutBid](https://useoutbid.com/blog/upwork-connects-cost-per-proposal-2026)), assuming 8 to 10 Connects per proposal:

| Win rate | Connects cost per client |
|---|---|
| 2% | $60.00 |
| 5% | $24.00 |
| 10% | $12.00 |
| 15% | $8.40 |
| 20% | $6.00 |

At a $3,500 first engagement, even a 2% win rate means **$60 of Connects against $3,500 of revenue**. Connects are not the constraint. Proposal-writing time is. Plan accordingly: filter hard, write few, write well.

### 2.2 Boosted proposals

Mechanics, quoted from [Upwork's own help article](https://support.upwork.com/hc/en-us/articles/4406395531795-How-to-boost-your-proposal):

- There are **four boosted slots** at the top of the client's proposal list, each carrying a "Boosted" icon.
- You "can bid any Connects amount". Upwork publishes no minimum or maximum.
- The auction settles on the bidder's own bid, not the runner-up's: in Upwork's worked example, "You bid 35 Connects... The other winning bidders bid 30, 25, and 20 Connects. You'll pay the exact amount of your bid of 35 Connects."
- You pay only if you are in the top four when the auction closes, **or** the client interacts with your proposal. Otherwise the boost Connects are refunded after the auction closes.
- **Only the extra boost Connects are refundable. The standard Connects used to submit the proposal are not.**
- The boost holds until the client interacts, opens it three times without action, sees it five times without interaction, or you are outbid.

Third-party data: the auction runs 7 days or until a hire; typical boosts of ~20 Connects across 25 boosted proposals per month equal **$75 in boost spend alone**; Upwork claims boosted proposals are **17% more likely to be seen** and can raise hire probability **by up to 24%** ([Zenlance on boosted proposals](https://zenlance.net/upwork-boosted-proposals/)). Recommended practice is to bid slightly above the visible high end of the range and keep boost spend under 2% of expected contract value ([Zenlance](https://zenlance.net/upwork-boosted-proposals/)), and to boost **20% to 30% of proposals strategically** rather than indiscriminately ([Jobbers Upwork algorithm guide](https://www.jobbers.io/the-complete-upwork-algorithm-guide-2026/)).

**Our rule:** boost only jobs priced $1,500+ where we have a named vertical proof, cap the boost at 30 Connects ($4.50), and never boost a job we would not personally want.

### 2.3 Badges: Rising Talent, Top Rated, Top Rated Plus, Expert-Vetted

**Rising Talent**, quoted from [Upwork's help article](https://support.upwork.com/hc/en-us/articles/211063228-How-to-become-a-Rising-Talent-on-Upwork). You qualify by being invited by Upwork **or** by meeting all of:
- "an average star rating of 4.8 or above and earned at least $250 USD in the past 12 months"
- "Maintain a 100% complete profile with accurate skills and genuine work"
- "Have submitted a proposal or worked within the past 90 days"
- "Have a Job Success Score (JSS) of 90% or higher, if you've earned one"
- No account holds, no public or private negative feedback
- Identification verified badge and a valid withdrawal method

**This is the critical asymmetry with Fiverr.** Fiverr's inbound "Briefs" channel is locked behind Success Score 7, which is the Level 2 threshold requiring 20 orders from 10 unique clients (`fiverr-market.md` section 4.2). **Upwork's Rising Talent badge needs $250 in earnings and one 4.8+ rating.** One $450 order clears it. Rising Talent is reachable on Upwork in week two; the equivalent Fiverr status takes months.

**Top Rated**, quoted from [Upwork](https://support.upwork.com/hc/en-us/articles/211068468-How-to-become-Top-Rated-on-Upwork):
- "A current Job Success Score of 90% or higher"
- "First project on Upwork was more than 90 days ago"
- "12-month earnings of at least $1,000"
- "A 100% complete profile"
- "Maintained Rising Talent status or a Job Success Score of at least 90% for at least 13 of the last 16 weeks"
- Up-to-date availability, account in good standing, activity in the past 90 days

**Top Rated Plus**: Top Rated plus "total earnings over $10,000 in the past 12 months" for freelancers, or **$20,000 in the past 12 months for agencies** ([Upwork talent badges](https://support.upwork.com/hc/en-us/articles/211063568-Understand-freelancer-talent-badges)).

**Expert-Vetted**: "the top 1%", requires passing "a screening process by Talent Managers", and is **"only visible to you if you are signed up for a Business Plus or Enterprise plan"** ([Upwork](https://support.upwork.com/hc/en-us/articles/211063568-Understand-freelancer-talent-badges)). Invitation only, same shape as Fiverr Pro.

The critical-path arithmetic: **Top Rated needs 90 days of account age and $1,000 of 12-month earnings.** At a $2,500 first engagement, the money bar clears on order one and **the binding constraint is the 90-day clock plus 13 of 16 weeks at JSS 90%+**. That means the Upwork account must be opened on day 1 even if we do not bid hard until week 3, because the 90-day clock starts at first project, and every week of delay is a week later to Top Rated.

### 2.4 Job Success Score

Per [UpHunt's 2026 JSS explainer](https://uphunt.io/blog/upwork-job-success-score-jss-2026-explained):

- Base form: (successful outcomes minus negative outcomes) divided by total outcomes.
- **JSS does not display until 10 billable hours or one completed fixed-price contract.**
- Recalculated daily in the background; **visible profile updates every 14 days**.
- Three simultaneous windows at 6, 12 and 24 months, and **the highest of the three is displayed**, which creates a forgiveness curve: a bad outcome drops out of the 6-month window by about month 7.
- **Private feedback (1 to 10) is weighted as heavily as the public star rating.** "A 5-star public rating with a 6 in private feedback can still drag your JSS down."
- Recurring clients paying every 90 days weigh **very high** and compound as additional successful outcomes.
- **Freelancer-initiated cancellations are a very strong negative.**
- Below JSS 75, "response rates collapse".

Upwork's search algorithm reportedly weights JSS at **25% to 30%**, relevance matching 20% to 25%, availability and response metrics 15% to 20%, earnings history 10% to 15%, profile completeness 10% to 15%, and reviews 10% to 15%; setting status to "Not Available" is reported to cost a **50% to 70% reduction in visibility** ([Jobbers Upwork algorithm guide](https://www.jobbers.io/the-complete-upwork-algorithm-guide-2026/)).

**Two operating rules follow.** First, **never cancel a contract ourselves**; negotiate a reduced-scope close instead. Second, **the recurring-client weight means a $500/month monitoring retainer attached to every build is worth more than its revenue**, because a client paying every 90 days compounds into JSS as repeated successful outcomes.

### 2.5 Specialized profiles

Upwork allows multiple profiles under one account: a general profile plus specialized profiles ([Upwork: how to add new profiles](https://support.upwork.com/hc/en-us/articles/115013660327-How-to-add-new-profiles-to-your-Upwork-account)). "Specialized profiles rank higher for niche searches," and the guidance is to choose "1-2 primary service offerings" and decline work outside expertise to "protect JSS" ([Jobbers](https://www.jobbers.io/the-complete-upwork-algorithm-guide-2026/)).

**Our configuration:** general profile headlined on compliance-aware voice infrastructure, plus two specialized profiles, one for **AI voice agents and telephony** and one for **workflow automation and AI integration (n8n, MCP, Claude agents)**. Each gets its own rate, its own portfolio subset, and its own headline. This is free and it is the cheapest ranking lever available on the platform.

### 2.6 Project Catalog

Project Catalog is Upwork's productized-offer surface, the closest analogue to a Fiverr gig: fixed-scope, fixed-price, buyer purchases without a proposal. "The freelancer service fee on projects and consultations works like other contracts" ([Upwork: getting started with Project Catalog](https://support.upwork.com/hc/en-us/articles/360058234233-How-to-get-started-with-Project-Catalog-as-a-freelancer)). Upwork does not publish the eligibility gate on that page, so **treat availability as something to check inside the dashboard at signup rather than as a guaranteed channel**. Confirmed live examples exist in our exact niche, for instance a published Project Catalog listing "You will get 24/7 AI Receptionist | AI Voice Agent | using ElevenLabs, Vapi or Retell" ([Upwork Project Catalog](https://www.upwork.com/services/product/development-it-24-7-ai-receptionist-ai-voice-agent-using-elevenlabs-vapi-or-retell-1995380400744282985)), which confirms the category is open to this kind of offer.

Treat Project Catalog as the **Connects-free inbound channel**: it costs no Connects to list, it converts browsing buyers, and it is the direct port of our Fiverr gig packaging.

### 2.7 Availability Badge

A Connects-priced badge that shows "Available now" on the profile and in search results, and lets clients filter for it when sending invitations. Upwork describes it as "a way for you to earn more invites with less effort" ([Upwork](https://support.upwork.com/hc/en-us/articles/40367622397075-How-does-the-Availability-Badge-work)). Pricing floats and **"there's no maximum price for the Availability Badge"**, but the freelancer sets a personal spending cap in Connects and the badge is removed automatically when that cap is reached ([Upwork](https://support.upwork.com/hc/en-us/articles/40367930714899-Is-there-a-maximum-price-for-the-badge)).

**Our rule:** switch it on with a hard cap of 100 Connects ($15) per month during the first 60 days, when invitations matter more than anything, and measure invitations received in Stats and trends before renewing.

### 2.8 Profile verification

Identification verification is a hard prerequisite for the Rising Talent badge ([Upwork](https://support.upwork.com/hc/en-us/articles/211063228-How-to-become-a-Rising-Talent-on-Upwork)) and Upwork states "We may restrict or permanently suspend your account if we cannot verify the information you provide" ([Upwork: Represent yourself authentically](https://support.upwork.com/hc/en-us/articles/18513114070419-Represent-yourself-authentically)). Do it on day one, on both accounts, before any bidding.

### 2.9 Agency accounts

The rules, from Upwork's own help centre:

- **"each freelancer can only create one agency on Upwork"** ([How to create an agency](https://support.upwork.com/hc/en-us/articles/211067598-How-to-create-an-agency)).
- To add team members you must subscribe to **Agency Plus** ([same source](https://support.upwork.com/hc/en-us/articles/211067598-How-to-create-an-agency)), priced at approximately **$19.99/month**, which "unlocks the ability to buy Connects; it does not hand you any" ([UpHunt Agency Plus guide](https://uphunt.io/blog/upwork-agency-plus-complete-guide-2026)).
- Joining an agency requires "an invitation from the agency's owner or agency administrator" ([Agencies FAQ](https://support.upwork.com/hc/en-us/articles/35389337775123-Agencies-Frequently-Asked-Questions)).
- **"all agency members can submit proposals"** and "Each proposal draws from the agency's collective balance of Connects", but **"Only business managers can accept an offer"** ([How agencies work for freelancers](https://support.upwork.com/hc/en-us/articles/211062608-How-agencies-work-for-freelancers)).
- Members keep their own login and privacy: "your account remains private and sign-in details must not be shared with the agency owner or any other party" ([same source](https://support.upwork.com/hc/en-us/articles/211062608-How-agencies-work-for-freelancers)).
- Members **"can still create a project as a freelancer if you are not exclusive to an agency"** ([Agencies FAQ](https://support.upwork.com/hc/en-us/articles/35389337775123-Agencies-Frequently-Asked-Questions)).
- **"All contract earnings are paid to the agency's financial account on Upwork"**, and "Payments from agencies to agency members are not protected or facilitated by Upwork" ([How agency finances work](https://support.upwork.com/hc/en-us/articles/360009524554-How-agency-finances-work)).
- On agency closure, "all completed contracts... will be counted towards their respective Job Success Score... in their individual freelancer accounts" ([Agencies FAQ](https://support.upwork.com/hc/en-us/articles/35389337775123-Agencies-Frequently-Asked-Questions)).
- Agency Plus also gives unlimited team members, a custom agency profile URL, competitor bid visibility, and Upwork Chat Pro; there is no cap on business manager roles ([UpHunt](https://uphunt.io/blog/upwork-agency-plus-complete-guide-2026)).

**This is the structural key for us and it is worth stating plainly.** A business manager "can submit proposals on behalf of anyone in the agency" ([UpHunt](https://uphunt.io/blog/upwork-agency-plus-complete-guide-2026)), which means **Frankie, as a business manager, can bid US-facing on work that Chitraksh will deliver, legitimately, inside the platform's own rules.** That is exactly the division of labour we want, and it requires no grey-area behaviour at all. Frankie is also the only one of the two who can accept offers, which puts the commercial close where the sales lead is.

### 2.10 Upwork Enterprise and Talent Scout

**Talent Scout** is a recruiter-mediated channel launched in 2021: Upwork recruiters curate shortlists for clients from the existing talent pool, and freelancers receive invitations to roles that are never publicly posted ([Upwork press release](https://www.upwork.com/press/releases/upwork-introduces-talent-scout)). There is no application form. Sourcing runs through Upwork's recruiters, the same shape as Fiverr Pro's talent sourcing team.

**Expert-Vetted** is the badge that makes us visible to Business Plus and Enterprise clients, and it is gated at the top 1% behind a Talent Manager screen ([Upwork](https://support.upwork.com/hc/en-us/articles/211063568-Understand-freelancer-talent-badges)).

**Treat both as phase-three outcomes, not phase-one channels.** The prerequisite is Top Rated Plus, which needs $20,000 of agency earnings in 12 months. That is six to eight engagements at our target price. It is reachable inside a year but it is not a launch plan.

### 2.11 Hourly versus fixed price, and payment protection

**Fixed-price protection** requires three things, quoted from [Upwork](https://support.upwork.com/hc/en-us/articles/211063748-How-Fixed-Price-Payment-Protection-works-for-freelancers-on-Upwork):
- "The milestone was fully funded before you began working"
- "You used the Submit Work for Payment button to deliver your work"
- "The submitted work matches the milestone description"

Upwork's own advice: "Break big projects into smaller milestones. It keeps your work on track, builds client trust, and helps ensure you're paid as you go." Disputes can be filed when a client does not release a milestone, releases only part, requests a refund, or ends the contract with funds still in escrow.

**Hourly protection** is a separate scheme keyed to time logged through the Upwork desktop app with work-diary screenshots.

**Our rule, stated without hedging:** **fixed-price with milestones, always, for build work.** Three reasons. First, our delivery is a productized one-session clone process (`oraya-facts.md` section 2d), so hours logged badly misrepresent the value. Second, JSS weights contract value, and a fixed $3,500 contract reads better than 40 logged hours at $87. Third, the work-diary requirement is incompatible with the way the build actually happens. Use hourly **only** for open-ended tuning retainers after launch, where the recurring-client JSS compounding is the real prize.

**Fees.** The freelancer service fee is variable, **0% to 15% per contract**, and is locked at the moment the proposal is sent; the blended average for agencies runs **11% to 13.5%**, and the all-in effective take rate including Connects burn, proposal labour and withdrawal fees runs **22% to 34%** for typical agencies and **14% to 18%** for well-filtered ones ([GigRadar Upwork fees 2026](https://gigradar.io/blog/upwork-fees)). Clients additionally pay a contract initiation fee of up to $4.95 ([same source](https://gigradar.io/blog/upwork-fees)). Compare Fiverr's flat **20% on all earnings** ([Jobbers fee encyclopedia](https://www.jobbers.io/the-freelance-platform-fee-encyclopedia-every-fee-on-every-platform-documented/)). **Upwork is cheaper than Fiverr on fees if and only if we filter hard.** Spray-and-pray bidding is what pushes the effective rate to 34%.

### 2.12 Proposal best practices, with measured effects

This is the highest-value subsection in the document because it is the only place where the effect sizes are measured rather than asserted. All figures from [GigRadar's analysis of 133,872 proposals](https://gigradar.io/blog/ai-proposals-upwork), baseline reply rate 7.45%.

**AI cliché density is a kill switch:**

| Clichés in the cover letter | Reply rate |
|---|---|
| Zero | **7.55%** |
| One | 6.84% |
| Three | 4.17% |
| **Four or more** | **0.00%** |

**Worst opening lines, measured as percentage-point drag against the 7.45% baseline:**

| Opening | Drag |
|---|---|
| "Hi! Thanks for posting" | **−5.50pp** |
| "Many freelancers..." | −4.03pp |
| "Good day" | −3.68pp |
| "I have experience with" | −3.67pp |
| "I'll help" | −3.17pp |

**Elements that lift reply rate:**

| Element | Lift |
|---|---|
| **Offer a Loom walkthrough** | **+3.70pp** |
| Reference recently completed work | +2.52pp |
| Open with a specific question | +2.34pp |
| Include the word "guarantee" | included in the winning combination |
| Include "any questions" as a low-friction close | included in the winning combination |

**Proposals combining those signals replied at 13.77%, nearly double the platform mean.**

Two more measured findings. Hand-written templates replied at **8.13%** against GPT-4o auto-bidders at **7.13%** and newer LLM stacks at **6.91%**, so the AI-written proposal is measurably worse than a human template. And defensive disclaimers backfire: proposals containing "non-ChatGPT generated proposal" replied at only **5.9%**.

On length and structure, the practitioner consensus is **150 to 250 words**, opening with a question about their project or a specific reference from the job description rather than "I am interested" or "Dear hiring manager", and a **60 to 90 second Loom** addressing the client by name for high-touch roles ([UpHunt first-client guide](https://uphunt.io/blog/how-to-get-first-client-upwork-2026-complete-guide)).

**The Oraya proposal template, derived from the data above.** Two lines before the fold, no greeting, no gratitude:

> Line 1: a specific question about their setup that only someone who has built this would ask. Example for a dealership BDC post: "Are your after-hours calls currently rolling to voicemail, or to an answering service that charges per call?"
>
> Line 2: the measured number and the named vertical. Example: "I build phone agents at a measured median 761 ms time-to-first-audio, currently running for a dealership BDC, with the recorded-line and AI disclosure locked as the first utterance in code rather than in the prompt."

Then: one paragraph on their specific job, one line referencing the most recently delivered comparable build, an offer of a **90-second Loom showing a live call with the latency readout visible**, a scope guarantee, and "happy to answer any questions". Under 250 words. Zero clichés. No em dashes.

**The Loom is not optional.** It is the single largest measured lift available (+3.70pp, roughly a 50% relative increase on the 7.45% baseline), and it is also the only way to demonstrate a voice product in a text medium. We already have the raw material: dashboard screenshots with the latency waterfall, and a live demo line.

### 2.13 Time to first hire: benchmarks

| Profile quality | Time to first client | Source |
|---|---|---|
| Strong portfolio, clear niche | **1 to 3 weeks** | [GigUpHQ](https://giguphq.com/blog/how-long-does-it-take-to-get-your-first-upwork-client) |
| Decent skills, average profile | 3 to 8 weeks | [GigUpHQ](https://giguphq.com/blog/how-long-does-it-take-to-get-your-first-upwork-client) |
| Generic profile, broad niche | 2 to 4+ months | [GigUpHQ](https://giguphq.com/blog/how-long-does-it-take-to-get-your-first-upwork-client) |
| Focused strategy, consistent bidding | **2 to 6 weeks** | [UpHunt](https://uphunt.io/blog/how-to-get-first-client-upwork-2026-complete-guide) |
| Proposals needed before first client | **20 to 80 serious proposals** | [GigUpHQ](https://giguphq.com/blog/how-long-does-it-take-to-get-your-first-upwork-client) |

Recommended volume: "3 to 5 strong-fit jobs per day is better than 20 random ones" ([GigUpHQ](https://giguphq.com/blog/how-long-does-it-take-to-get-your-first-upwork-client)); ramp from 5 to 10 proposals in week 2 to 10 to 15 in week 3 ([UpHunt](https://uphunt.io/blog/how-to-get-first-client-upwork-2026-complete-guide)).

**Our planning number: 30 to 50 high-signal proposals to first hire, spread over 3 to 5 weeks, at roughly 10 Connects each, so $45 to $75 of Connects.** We sit in the "strong portfolio, clear niche" bucket if and only if the portfolio is populated on day one, which makes the day-one portfolio build the highest-leverage 4 hours in the entire 30-day plan.

### 2.14 Freelancer Plus: worth it or not

$19.99/month, including **100 Connects per month** (a $15 value on its own), competitor bid visibility, Uma the AI assistant, and a 0% service fee on clients you bring to Upwork yourself ([Upwork Freelancer Plus](https://www.upwork.com/work/freelancerplus), [GigRadar fees](https://gigradar.io/blog/upwork-fees)). Upwork states that "Freelancer Plus subscribers on average have a 50% higher chance of being hired" and that "40% of subscribers are Top Rated or Top Rated Plus" ([Upwork](https://www.upwork.com/work/freelancerplus)).

Read that second statistic carefully: **it is a selection effect, not a causal claim.** Top Rated freelancers subscribe; subscribing does not make you Top Rated. The honest case for Plus is arithmetic: 100 Connects is worth $15, the marginal cost of the subscription is therefore about $5/month, and **competitor bid visibility is genuinely useful** given the finding that bidding 95% to 105% of budget is the worst-performing position. Subscribe on day one on the bidding account.

**The 0% service fee on self-brought clients is the sleeper feature.** Any client we generate off-platform (LinkedIn, ads, referral) and route through Upwork for contracting and escrow costs 0% instead of 10% to 15%. That turns Upwork into free payment infrastructure for our own pipeline.

---

## 3. MULTI-ACCOUNT RULES, EXACTLY

### 3.1 Fiverr: the clause, verbatim

From [Fiverr's Community Standards](https://help.fiverr.com/hc/en-us/articles/32242973123985-Our-Community-Standards):

> **"In order to buy and/or sell services on Fiverr you may have only one account."**

The same page lists the prohibited purposes of multiple accounts: to "Gain a competitive advantage", to "Harass or mislead other users through messaging and/or ordering systems", to "Engage in any fraudulent activity", to "Abuse the Fiverr Referral program", and to "Bypass a restriction, or permanent suspension of a previous account".

Consequence, quoted:

> **"Any violation of this policy can lead to permanent suspension of the account(s) involved in this activity."**

Note the plural in parentheses. **The suspension reaches every account in the cluster, not just the offending one.**

The page's only stated exception is holding a seller account plus an additional seat within a **Team Account**. It also warns users against sharing credentials such as email, payment information or phone number that could allow others to create accounts on their behalf.

Fiverr's [Account restrictions page](https://help.fiverr.com/hc/en-us/articles/34551010553489-Account-restrictions) confirms that multiple accounts sits under the "Integrity & Authenticity" restriction family alongside fake identities and off-platform transactions, and that for severe violations "This decision was taken after careful consideration and cannot be reversed."

**On per-household and per-business:** Fiverr's own text is silent on households. It is written per person and enforced per account cluster. Third-party practitioner analysis describes the detection surface as four-part: shared IP ("If two accounts are regularly accessed from the same IP address, home network, office network, mobile hotspot, the pattern is flagged"), shared payment methods ("same PayPal account, same bank account, same credit card"), behavioural signals (writing style, response-time patterns, the same portfolio images on two accounts), and network relationships ([Fiverr Tutorials on multiple accounts](https://fiverrtutorials.com/fiverr-secrets-multiple-fiverr-accounts/)). The same analysis states that accounts belonging to "a registered company" and "an employee of that company" can coexist if they maintain separate payment methods, devices and IP addresses. **That is a third-party reading, not Fiverr policy, and it should not be relied on as a safe harbour.** The binding text is the one-account clause above.

### 3.2 Fiverr: the legitimate structures

**Fiverr Agencies.** Per [Fiverr's agency help article](https://help.fiverr.com/hc/en-us/articles/29454085707409-Fiverr-agencies), an agency requires "a team of at least 3 in-house professionals", an active presence in an eligible category, and demonstrated capacity for large-scale projects. Agencies are currently restricted to five categories: Digital Marketing, **Programming & Tech**, Graphics & Design, Video and Animation, and Business. Entry is invitation-based: Fiverr "sends invitations to users meeting current standards, who then complete an application form", with a waiting list for those not yet eligible. Critically for continuity: **"Your orders, Gigs, chats, and reviews carry over when you switch to an agency profile."** The onboarding requirements page adds: **"Up to 9 team members are allowed. Required to add at least 3 team members"**, at least one and ideally three industries, and services from at least 2 and at most 10 categories ([Fiverr agencies onboarding requirements](https://help.fiverr.com/hc/en-us/articles/21836241851409-Fiverr-agencies-onboarding-requirements)).

**Two founders is one short of the Fiverr agency minimum of three.** That is a hard blocker today, not a soft one. It is also easily solved later by a third contributor.

**Fiverr Pro.** Acceptance rates are reported "below 3% of applicants" with a review taking "two to four weeks", and the vetting weights verifiable professional credentials earned outside Fiverr over Fiverr-internal review counts ([Fiverr Tutorials on Fiverr Pro](https://fiverrtutorials.com/fiverr-pro-seller)). That weighting favours us unusually strongly: a law degree plus a licensed insurance producer plus a measured latency benchmark is exactly the kind of off-platform credential Pro screens for, and it is the reason Pro is worth applying to even with zero Fiverr order history.

### 3.3 Upwork: the clauses, verbatim

From [Why you can't have two Upwork accounts](https://support.upwork.com/hc/en-us/articles/39505058710163-Why-you-can-t-have-two-Upwork-accounts):

> **"Upwork allows only one account per person to ensure fairness, trust, and security."**

> "you can only have one Upwork account for life. However, under that main account you can have one freelancer profile, one agency account, and multiple client accounts."

From the [Multiple accounts FAQ](https://support.upwork.com/hc/en-us/articles/36738402656531-Multiple-accounts-Frequently-Asked-Questions):

> **"No, having multiple accounts is not allowed and it is considered a violation of our Terms of Service."**

> "you can have a Client, Freelancer, and Agency profile, under the same account."

Reopening a closed account with the same email "is also considered a violation of the Terms of Service".

From [Represent yourself authentically](https://support.upwork.com/hc/en-us/articles/18513114070419-Represent-yourself-authentically):

> "When you join Upwork we ask that you only create one main account."

> **"You cannot log into someone else's account or let anyone log into your account and work or communicate on your behalf."**

> "The name on your account should be what you use to identify yourself in everyday life."

> "The address you provide should be your business address."

> "We may restrict or permanently suspend your account if we cannot verify the information you provide."

### 3.4 Upwork: can Frankie hold his own account and be in an agency

Yes, explicitly. Three provisions combine:

1. Agency members "retain individual account privacy" and "your account remains private and sign-in details must not be shared with the agency owner or any other party" ([How agencies work for freelancers](https://support.upwork.com/hc/en-us/articles/211062608-How-agencies-work-for-freelancers)). Membership does not merge accounts.
2. Members "can still create a project as a freelancer if you are not exclusive to an agency" ([Agencies FAQ](https://support.upwork.com/hc/en-us/articles/35389337775123-Agencies-Frequently-Asked-Questions)).
3. On agency closure, completed contracts "will be counted towards their respective Job Success Score... in their individual freelancer accounts" ([Agencies FAQ](https://support.upwork.com/hc/en-us/articles/35389337775123-Agencies-Frequently-Asked-Questions)), which only makes sense if individual accounts persist alongside agency membership.

The agency itself is created by a freelancer account and **"each freelancer can only create one agency on Upwork"** ([How to create an agency](https://support.upwork.com/hc/en-us/articles/211067598-How-to-create-an-agency)), with Agency Plus required to add members.

### 3.5 The compliant structure for Oraya, stated as a build order

| # | Entity | Owner | Platform | Purpose | Status |
|---|---|---|---|---|---|
| 1 | **Chitraksh personal freelancer account (India)** | Chitraksh | Upwork | Builder identity. Specialized profiles for voice/telephony and for automation/AI integration. Holds the JSS that badges depend on. | Open day 1 |
| 2 | **Oraya Labs agency** | Created by Chitraksh's account (one agency per freelancer) | Upwork, Agency Plus ~$19.99/mo | Contracting entity. Frankie added as a **business manager** so he can submit proposals on behalf of the agency and is the only party who can accept offers. | Open day 1, add Frankie day 2 |
| 3 | **Frankie personal freelancer account (US)** | Frankie | Upwork | His own identity, his own JSS, and the US-located account. Member of the agency as business manager. | Open day 1 |
| 4 | **Chitraksh Fiverr seller account** | Chitraksh | Fiverr | The three gigs from `fiverr-market.md` section 6.2. One account, one person, no ambiguity. | Already the plan |
| 5 | **Fiverr agency** | n/a | Fiverr | **Blocked.** Requires a minimum of 3 in-house team members. Revisit when a third person joins. | Deferred |

**What is explicitly NOT allowed and must never be attempted:**

- A second Fiverr account for "the company" alongside Chitraksh's personal one. The clause is "you may have only one account" and the consequence is permanent suspension of **"the account(s) involved"** ([Fiverr Community Standards](https://help.fiverr.com/hc/en-us/articles/32242973123985-Our-Community-Standards)).
- Frankie operating Chitraksh's Upwork account or vice versa. "You cannot log into someone else's account or let anyone log into your account and work or communicate on your behalf" ([Upwork](https://support.upwork.com/hc/en-us/articles/18513114070419-Represent-yourself-authentically)).
- Shared payment methods, shared withdrawal accounts, or shared devices between the two Upwork accounts. Linked accounts are "usually flagged via browser fingerprint or shared IP" and payment-method connections are monitored ([UpHunt suspension guide](https://uphunt.io/blog/upwork-account-suspended-recovery-appeal-guide-2026)).
- A US-fronted Fiverr or Upwork account operated from India to appear US-based. Upwork requires the account name to be the one used "in everyday life" and the address to be "your business address", with permanent suspension for unverifiable information ([Upwork](https://support.upwork.com/hc/en-us/articles/18513114070419-Represent-yourself-authentically)).

### 3.6 Does a US-based account help with US buyers

**On Upwork, materially and provably yes, for one specific reason.** Clients can restrict a job post by freelancer location, and the restriction is hard, not cosmetic:

> **"If you choose U.S. only, then only freelancers in the U.S. will be able to see your post and submit a proposal."** ([Upwork: choose a freelancer location when posting a job](https://support.upwork.com/hc/en-us/articles/115005777188-Choose-a-freelancer-location-when-posting-a-job))

For every other country preference the restriction is soft: "freelancers outside those locations can still submit proposals" and simply see the stated preference ([same source](https://support.upwork.com/hc/en-us/articles/115005777188-Choose-a-freelancer-location-when-posting-a-job)). Clients can also filter searches to U.S. freelancers only ([Upwork](https://support.upwork.com/hc/en-us/articles/17938843522963--Search-for-U-S-freelancers-only)).

**Frankie's US account is therefore not a nice-to-have. It is the only key to an entire class of job posts that Chitraksh's account cannot see at all.** In our niches specifically, that class is large: insurance and dealership BDC work is disproportionately posted by US clients with compliance reasons to prefer US-based contractors, and the TCPA framing makes US-location salience higher still.

Secondary benefits, harder to quantify but real: same-timezone response speed, given that reply rate falls from 8.99% under 5 minutes to 6.91% at 5 to 10 minutes ([GigRadar](https://gigradar.io/blog/upwork-market-report-2026)); a licensed-producer credential that is only meaningful in the US regulatory context; and phone-call availability in US business hours for discovery calls.

**On Fiverr the effect is weaker.** Fiverr search shows seller location but does not offer a hard US-only gate equivalent to Upwork's, and we can only hold one Fiverr account per person regardless. The Fiverr play remains Chitraksh's single account with US-market positioning in the copy.

### 3.7 Consequences of violation

**Fiverr:** "Any violation of this policy can lead to permanent suspension of the account(s) involved in this activity" ([Community Standards](https://help.fiverr.com/hc/en-us/articles/32242973123985-Our-Community-Standards)). For severe violations the decision "cannot be reversed" ([Account restrictions](https://help.fiverr.com/hc/en-us/articles/34551010553489-Account-restrictions)).

**Upwork:** suspensions escalate through three states, restricted, then suspended and appealable, then permanently closed; "a second account is" the fastest route to permanent ([UpHunt](https://uphunt.io/blog/upwork-account-suspended-recovery-appeal-guide-2026)). Detection uses device fingerprinting, browser fingerprinting and shared IP, and monitors payment-method links ([same source](https://uphunt.io/blog/upwork-account-suspended-recovery-appeal-guide-2026)). Funds are held during suspension and "typically released after the appeal is decided in your favor". Appeals are reviewed within 2 business days, 3 to 5 for complex cases, and should be a single focused submission under 400 words with new evidence.

**The asymmetry that should settle every judgement call:** the upside of a second account is one extra listing surface. The downside is the permanent, unappealable loss of a JSS and review history that takes six months to rebuild, on both accounts, with funds frozen during the process. There is no version of the arithmetic where it is worth it. **Two humans, two accounts, one agency, zero grey area.**

---

## 4. ADS AND PAID VISIBILITY

### 4.1 Fiverr Promoted Gigs

**Model.** A cost-per-click auction. Fiverr states: "Our auction system will calculate the minimum amount per click you need to pay to win over other ads." You "Control your daily budget" and "Your ads will be promoted until your budget runs out for the day." Payment is retrospective: "At the end of every month, we'll withdraw payment for your ad activity directly from your Fiverr earnings, no upfront payments needed" ([Fiverr Promoted Gigs](https://www.fiverr.com/pages/promoted-gigs)). Fiverr's own page carries seller testimonials claiming "return on investment of x11" and "return on investment went up to x47", which are testimonials rather than guarantees.

**Eligibility.** Fiverr does not publish the gate on its own page. Third-party reporting puts it at "Level 1 sellers and above with a gig that has at least 20 completed orders (in some categories) or meets Fiverr's minimum quality threshold for promotion", with new gigs ineligible until they have conversion data ([Fiverr Tutorials Promoted Gigs guide](https://fiverrtutorials.com/fiverr-ranking-guide/fiverr-promoted-gigs-guide)). A separate source states Level 2 sellers gain "full Promoted Gigs access" ([Jobbers Fiverr gig optimization guide](https://www.jobbers.io/the-complete-fiverr-gig-optimization-guide-2026/)).

**The operational consequence is decisive: Promoted Gigs is unavailable to us in the first 30 days.** Any budget plan that assumes it is wrong. Budget for it in month 2 or 3.

**Costs when it does open.** Typical CPCs run **$0.10 to $2.00** ([Jobbers](https://www.jobbers.io/the-complete-fiverr-gig-optimization-guide-2026/)). Recommended test: "Set a daily budget of $3 to $5 to start" for two to three weeks ([Fiverr Tutorials](https://fiverrtutorials.com/fiverr-ranking-guide/fiverr-promoted-gigs-guide)). The ROI rule: positive if cost per order stays "below 20% of your net earnings per order", and the maths works best for higher-priced gigs with 8%+ organic conversion, failing entirely for gigs under $30 ([same source](https://fiverrtutorials.com/fiverr-ranking-guide/fiverr-promoted-gigs-guide)). At a $450 Starter package netting $360 after Fiverr's 20%, the ceiling is $72 per order, which at $0.50 CPC and 5% conversion means $10 per order. **Promoted Gigs will be extremely profitable for us once eligible, precisely because our anchor is high.** This is another argument against ever launching a cheap gig.

### 4.2 Fiverr Seller Plus Kickstart

**$15/month**, "exclusively for New freelancers who haven't yet received a Fiverr level", refundable if cancelled "within 48 hours of your last monthly payment" ([Fiverr: Seller Plus Kickstart](https://help.fiverr.com/hc/en-us/articles/27291415082257-Seller-Plus-Kickstart-Start-your-freelance-journey-strong)). Features, quoted:

- "Access your performance dashboard and in-depth data on your business, including **Keyword research and pricing insights**"
- "Receive actionable, AI-powered suggestions to improve your Gigs"
- "Gain insights into client behavior to optimize your strategy"
- Promotions and coupons for client conversion
- "Live walkthrough session with a Fiverr onboarding specialist"
- **"Verify your identity easily to build client trust"**
- "Access faster response times from our Customer Support"

**Seller Plus buys no ranking.** Free and paid sellers are treated equally by the search algorithm ([GigRankPro](https://gigrankpro.com/is-fiverr-seller-plus-worth-it/)). Buy it for exactly one reason: the keyword data settles the **tool-keyword versus vertical-keyword question empirically within weeks**, which is the single largest open strategic question from `fiverr-market.md` section 6.1. ID verification is a second, smaller reason.

### 4.3 Upwork Boosted Proposals and Availability Boost

Covered in full at sections 2.2 and 2.7. Summarised as a spend line: at $0.15 per Connect, a disciplined boost policy of 25% of proposals at 20 to 30 Connects each is **$0.75 to $1.35 per boosted proposal**, and the Availability Badge caps at whatever Connects ceiling we set. **Total paid visibility on Upwork is measured in tens of dollars per month, not hundreds.** This is the cheapest paid channel available to us anywhere, and it should be maxed before a single dollar goes to Meta or Google.

### 4.4 Off-platform traffic to gig and profile URLs

**Is it allowed on Fiverr? Yes, explicitly and enthusiastically.** From [Promoting your Gigs outside of Fiverr](https://help.fiverr.com/hc/en-us/articles/360010490438-Promoting-your-Gigs-outside-of-Fiverr):

> **"Sharing a link to your Gig or profile is encouraged."**

Permitted: dedicated social business accounts, personal websites and blogs, forums and communities, **paid advertising on Facebook, Instagram and Google**, guest posts and podcast appearances. Prohibited: sharing personal contact information in external promotion, moving communication off-platform (Fiverr's TOS requires "all communication to happen on the platform"), fake reviews or fabricated testimonials, AI-generated misleading visuals or deepfakes, and impersonation.

**Is it rewarded?** Yes, structurally. "When someone from LinkedIn, Reddit, or your personal network clicks your Fiverr gig link and places an order, that interaction looks identical to Fiverr's algorithm to an order that came through organic search" ([Fiverr Tutorials on promoting gigs](https://fiverrtutorials.com/promote-fiverr-gigs-tips)). Conversion is the dominant ranking signal on Fiverr and click-through plus conversion rate are "one of the strongest positive signals in the Fiverr algorithm" ([Zenlance Fiverr algorithm guide](https://zenlance.net/fiverr-algorithm/)). So an externally-driven order is a permanent ranking deposit, not a one-off sale.

**The honeymoon window.** New gigs receive elevated visibility for **48 hours to several weeks** as a data-collection phase ([Zenlance](https://zenlance.net/fiverr-algorithm/)). The counterweight: "Fiverr's algorithm is not your sales team during the first 60 to 90 days" ([Fiverr Tutorials](https://fiverrtutorials.com/promote-fiverr-gigs-tips)). Both statements are true and they define the launch strategy exactly: **the algorithm gives you a short window of free impressions, and whether you convert them determines your ranking for months. External traffic during that window is the single highest-leverage launch action available.**

**Paid-traffic benchmarks for the three channels we would use:**

| Channel | Metric | Value | Source |
|---|---|---|---|
| Google Search, Business Services | Avg CPC | **$5.87** | [WordStream 2026 Google Ads benchmarks](https://www.wordstream.com/blog/2026-google-ads-benchmarks) |
| Google Search, Business Services | CTR / CVR / CPL | 6.10% / 4.85% / **$93.69** | [WordStream](https://www.wordstream.com/blog/2026-google-ads-benchmarks) |
| Google Search, Automotive (For Sale) | Avg CPC | **$2.27** | [WordStream](https://www.wordstream.com/blog/2026-google-ads-benchmarks) |
| Google Search, Automotive (For Sale) | CTR / CVR / CPL | 8.28% / 6.01% / **$44.26** | [WordStream](https://www.wordstream.com/blog/2026-google-ads-benchmarks) |
| Google Search, B2B SaaS non-brand | Median CPC | $8.50 to $14.00 | [Marqeable B2B SaaS benchmarks](https://www.marqeable.com/blog/google-ads-benchmarks-b2b-saas/) |
| Google Search, B2B SaaS | CPL | $180 to $350 typical, $80 to $180 top quartile | [Marqeable](https://www.marqeable.com/blog/google-ads-benchmarks-b2b-saas/) |
| Meta, B2B | Avg CPC | **$2.52** | [Adamigo Meta CPL benchmarks 2026](https://www.adamigo.ai/blog/meta-ads-cost-per-lead-benchmarks-industry-2026) |
| Meta, B2B SaaS | Avg CPL | **$63.40** (qualified $150 to $250) | [Adamigo](https://www.adamigo.ai/blog/meta-ads-cost-per-lead-benchmarks-industry-2026) |
| Meta, Professional Services | Avg CPL | $72.40 | [Adamigo](https://www.adamigo.ai/blog/meta-ads-cost-per-lead-benchmarks-industry-2026) |
| Meta, Financial Services | Avg CPL | $58.70 | [Adamigo](https://www.adamigo.ai/blog/meta-ads-cost-per-lead-benchmarks-industry-2026) |
| LinkedIn, Sponsored Content | CPC | **$5 to $8** | [Meet-Lea LinkedIn benchmarks 2026](https://meet-lea.com/en/blog/linkedin-advertising-costs-roi-benchmarks) |
| LinkedIn | Median CPM / Avg CTR | $31 / 0.44% to 0.65% | [Meet-Lea](https://meet-lea.com/en/blog/linkedin-advertising-costs-roi-benchmarks) |
| LinkedIn, Lead Gen Forms | CPL | **$75 to $150** at 6% to 10% form conversion | [Meet-Lea](https://meet-lea.com/en/blog/linkedin-advertising-costs-roi-benchmarks) |

**The comparison that decides the budget.** Meta B2B at **$2.52 CPC** is roughly half Google Business Services at **$5.87** and a third of LinkedIn at **$5 to $8**. Automotive search at **$2.27 CPC and $44.26 CPL** is the cheapest qualified traffic in the entire table and maps exactly onto our strongest vertical. And the exact-match commercial query "ai receptionist for car dealership" is a low-volume, high-intent, low-competition long-tail phrase: expect CPC nearer the automotive $2.27 than the B2B SaaS $8.50 to $14.00, because almost nobody is bidding on a four-word intent phrase in a category where, per `fiverr-market.md` section 1.2, the `car-dealership` Fiverr keyword carries **2,699 services and zero AI voice gigs**.

**One hard constraint on ad creative.** Never print a phone number, email or external contact detail in an ad that lands on a Fiverr gig, and never print one in the gig itself, because personal contact details in gigs are an explicit denial trigger ([Fiverr Policy Violations Explained](https://help.fiverr.com/hc/en-us/articles/48022851354385-Policy-Violations-Explained)). Ads may drive to the gig URL; the demo line is delivered inside the order or shown in the gig video.

### 4.5 First-30-days budget plans

All three plans assume: Fiverr gigs published day 1, Upwork accounts live day 1, Promoted Gigs unavailable (ineligible), and the goal is **first order plus first review on each platform**, not revenue maximisation.

#### Plan A: $300 total

| Line | Spend | Rationale |
|---|---|---|
| Fiverr Seller Plus Kickstart, 1 month | **$15** | Keyword data settles the tool-vs-vertical question. Refundable in 48 hours. |
| Upwork Freelancer Plus, 1 month | **$20** | 100 Connects (worth $15) plus competitor bid visibility. Net marginal cost ~$5. |
| Upwork Agency Plus, 1 month | **$20** | Required to add Frankie as business manager. Non-negotiable structural cost. |
| Extra Upwork Connects (400) | **$60** | ~40 additional proposals at 10 Connects each. |
| Upwork boosts (25% of proposals at 25 Connects) | **$35** | ~14 boosted proposals on $1,500+ jobs only. |
| Availability Badge cap | **$15** | 100 Connects ceiling for the month. |
| **Google Search, exact-match long tail** | **$135** | ~4 weeks at ~$4.80/day. At an automotive-adjacent $2.27 CPC that is ~59 clicks. Keywords: "ai receptionist for car dealership", "ai phone agent insurance agency", "tcpa compliant ai calling". |
| **Total** | **$300** | |

**Expected outcome:** 50 to 70 Upwork proposals sent, 14 boosted, roughly 4 to 5 replies at the 7.45% baseline and 8 to 10 at the 13.77% rate the Loom template achieves; ~59 paid clicks to the Fiverr gigs during the honeymoon window. **Target: 1 order.**

#### Plan B: $1,000 total

Everything in Plan A, plus:

| Line | Spend | Rationale |
|---|---|---|
| Everything in Plan A | $300 | |
| Extra Upwork Connects (600 more) | **$90** | Total ~100 proposals across the month, split across both accounts. |
| More boosts (30 more at 25 Connects) | **$113** | Boost every job above $2,500. |
| **Google Search, scaled** | **$300** | ~$10/day. Two ad groups: dealership BDC, insurance agency intake. Separate TCPA ad group at a lower bid. |
| **Meta lead ads, US, dealership and agency job titles** | **$200** | At $2.52 B2B CPC and a $63.40 B2B SaaS CPL benchmark, expect ~3 leads. Offer: the free "Compliance-Safe AI Audit" already documented in `oraya-facts.md` section 6. |
| Loom Business / screen-recording and editing | ~$0 to $25 | Loom free tier covers 90-second clips; budget a small buffer. |
| **Total** | **~$1,000** | |

**Expected outcome:** ~100 proposals, ~44 boosted, 8 to 14 replies, ~130 paid Google clicks, ~3 Meta audit leads. **Target: 2 to 3 orders, first review on both platforms.**

#### Plan C: $3,000 total

Everything in Plan B, plus:

| Line | Spend | Rationale |
|---|---|---|
| Everything in Plan B | $1,000 | |
| **Google Search, full** | **$900** | ~$30/day across 3 ad groups (dealership, insurance, TCPA). At $2.27 to $5.87 CPC that is 150 to 400 clicks. At WordStream's 4.85% to 6.01% CVR that is 7 to 24 conversions. |
| **Meta lead ads, full** | **$600** | At $63.40 B2B SaaS CPL, ~9 leads. Retarget Fiverr gig visitors and dashboard-demo viewers. |
| **LinkedIn lead gen forms, US, insurance and dealership decision-makers** | **$400** | At $75 to $150 CPL, 3 to 5 leads, but the highest-quality of the three channels: LinkedIn's reported average conversion rate is 6.1% versus 3.75% for Google Search ([Meet-Lea](https://meet-lea.com/en/blog/linkedin-advertising-costs-roi-benchmarks)). Frankie's account, Frankie's face, insurance targeting. |
| Extra Connects and boosts | **$100** | Headroom for a high-value week. |
| **Total** | **$3,000** | |

**Expected outcome:** ~120 proposals, 10 to 17 replies, 15 to 38 paid-traffic conversions across three channels. **Target: 4 to 6 orders and at least one engagement above $2,500.**

**The rule that governs all three plans.** Spend the platform-native budget first (Connects, boosts, Kickstart, Availability), because it is measured in tens of dollars and converts against buyers who are already in-market. Only then buy external traffic, and point it at the Fiverr gig during the honeymoon window rather than at a landing page, because a Fiverr order bought with ad money is also a permanent ranking deposit while a landing-page lead is not.

---

## 5. OTHER CHANNELS: WHICH EARN A SLOT

| Channel | Fit for AI-agent work | Cost to us | Approval gate | Verdict |
|---|---|---|---|---|
| **LinkedIn Services page** | High. Free inbound lead form, prospects self-qualify on budget and timeline before we reply. | **$0** ([ConnectSafely guide](https://connectsafely.ai/articles/linkedin-providing-services-section-guide-2026)) | None. Regional availability only; live in US, UK, Canada, India and more. | **YES, week 1.** Zero cost, zero gate, and we already run a LinkedIn content engine. Expect 0 to 2 inquiries/month on a thin profile, 2 to 8 once established, 10 to 25 in high-demand categories ([same source](https://connectsafely.ai/articles/linkedin-providing-services-section-guide-2026)). Toggle "Provide free consultation" on and route it to the existing Compliance-Safe AI Audit offer. |
| **Contra** | Good. Profile-led discovery, no bidding, explicitly positioned for "AI automation, workflow automation, n8n, OpenAI integration" ([Digino Contra review](https://digino.org/tools/contra/)). | **0% commission** ([Jobbers fee encyclopedia](https://www.jobbers.io/the-freelance-platform-fee-encyclopedia-every-fee-on-every-platform-documented/)) | None | **YES, week 2.** Zero fee, zero gate, and profiles that submit proposals within their first seven days get search prioritisation ([Digino](https://digino.org/tools/contra/)), so the signup window matters. Lower volume than Upwork but no downside. |
| **Toptal** | Moderate. Rates $60 to $200+/hr for developers, 0% freelancer fee ([Memvers Toptal guide](https://memvers.com/for-freelancers/platforms/toptal)). But the listed categories are software development, design, finance and project management, with AI/automation not named. | **0%** | **~3% acceptance.** Five stages: application (1 to 3 day review), 15 to 30 min language and personality interview, 90-minute technical screen, 1 to 2 week live project test, matching. Screening takes 2 to 5 weeks; first engagement 2 to 4 weeks after acceptance ([Memvers](https://memvers.com/for-freelancers/platforms/toptal)) | **LATER, month 3.** The 0% fee and $60 to $200/hr band are the best economics on this list, but 2 to 5 weeks of unpaid screening plus a 1 to 2 week project test is a serious time cost during a launch. Apply once Upwork is producing. |
| **A.Team** | **Very high.** Explicitly recruits "AI/ML engineers and architects" and "fractional CTOs", with "AI roles... dedicated emphasis with enterprise-focused missions" ([A.Team join page](https://www.a.team/join)). Missions run 12 to 18 months at 10 to 20 hrs/week or full time. | **0% from builders. "You set your rate, and we don't skim it."** ([A.Team](https://www.a.team/join)) | **Under 2% acceptance.** Portfolio submission, 30 to 45 minute human interview over two to three projects, then mission matching ([A.Team](https://www.a.team/join)) | **LATER, month 2.** Highest-quality fit on this entire list and zero fee, but the 12 to 18 month mission shape is a different business from productized builds. Apply once we have two named case studies. Worth the application time even at a 2% rate because the interview is one call, not a 1 to 2 week project test. |
| **Braintrust** | High. AI/ML engineering $80 to $200/hr; common projects include "LLM integration and fine-tuning"; targets "Senior software engineers (5+ years experience)" ([AI Gig Jobs Braintrust guide](https://www.aigigjobs.com/blog/braintrust-complete-guide)) | **0% from talent; the client pays the platform fee** ([same source](https://www.aigigjobs.com/blog/braintrust-complete-guide)) | Profile creation, skills verification via technical assessments or work samples, **1 to 5 business days**. "Incomplete profiles rarely get approved." | **YES, week 3.** Fastest approval of any vetted network (days, not weeks), 0% fee, and $80 to $200/hr for AI/ML. Cheapest high-quality option available. |
| **Clutch** | Moderate. Buyer-side agency directory, strong for enterprise discovery, weak for individual contractors. | Free Basic profile. **Clutch Verified $499/year.** Sponsorships priced by custom quote with a **12-month minimum commitment, no early cancellation** ([Clutch pricing 2026](https://www.hireinsouth.com/post/clutch-pricing)) | Free profile has no gate; reviews must be collected from real clients. | **LATER (free listing now, paid never yet).** Claim the free profile in month 1 for the backlink and directory presence. Do not touch Verified or sponsorship until we have 5+ collectible client reviews, and note that Clutch "does not operate on a pay-per-lead model" ([same source](https://www.hireinsouth.com/post/clutch-pricing)), so a 12-month commitment is a pure bet on visibility. |
| **GoodFirms** | Moderate, same shape as Clutch, lower authority. | Sponsorship **from $300/mo**; position #1 in Software Development US is **$1,200/mo**, #2 $799, #3 $549, #5 $429, #10 $349, #15 $300. PRO bundle separately **$49/mo billed annually** ([GoodFirms sponsorship pricing](https://www.goodfirms.co/sponsors/pricing)) | Free listing available | **NO for paid, free listing only.** $300/month for a #15 slot is a worse dollar than $300 of Google Search at a $2.27 automotive CPC. Claim the free profile, spend nothing. |
| **Freelancer.com** | Low. Bid-based race to the bottom; 10% commission with a $5 minimum ([Jobbers fee encyclopedia](https://www.jobbers.io/the-freelance-platform-fee-encyclopedia-every-fee-on-every-platform-documented/)) | Memberships: Basic $4.99/50 bids, Plus $9.99/100, Professional $49/300, Premier $99/1,500 ([Freelancer.com pricing 2026](https://www.hireinsouth.com/post/freelancer-pricing)) | None | **NO.** Everything Upwork does badly, done worse. The bid-volume model (1,500 bids/month on Premier) is structurally the opposite of our high-signal, low-volume strategy. |
| **PeoplePerHour** | Low to moderate. UK-weighted. Tiered commission: **20% on the first ~£250, 7.5% from ~£250 to £5,000, 3.5% above £5,000** ([Jobbers](https://www.jobbers.io/the-freelance-platform-fee-encyclopedia-every-fee-on-every-platform-documented/)), which is genuinely attractive at our price points. | Proposal credit system | Moderated application: profile photo, job title, accurate location, top skills, about-you. "Location mismatch" risks rejection. No published review timeline ([PeoplePerHour freelancer application process](https://support.peopleperhour.com/hc/en-us/articles/4408655983633-Freelancer-Application-Process)) | **LATER, month 3.** The 3.5% fee above £5,000 is the best marginal rate of any open marketplace, but the UK buyer base does not match our US insurance and dealership thesis. Revisit if we add UK verticals. |
| **Arc.dev** | Moderate. Freelance rates "$15 per hour and can exceed $110"; also runs full-time placement at 20% of first-year salary ([Arc.dev pricing](https://www.hireinsouth.com/post/arc-dev-pricing)) | Not published for freelancers | AI-powered applicant screening plus technical and communication assessments; acceptance rate not published | **NO for now.** The $15/hr floor tells you the buyer mix skews to cheap offshore placement, which is the opposite of our positioning. |
| **Catalant** | Moderate to high for the compliance and governance line specifically. Capability areas include "digital & AI"; consultants are paid by Catalant rather than by clients ([Catalant partner page](https://catalant.com/for-independent-consultants/how-to-partner/)) | Fee structure not disclosed | Application and verification in **2 to 5 business days**, then profile, project search, pitch, interview, proposal | **LATER, month 3.** Fast approval and enterprise-consulting buyers who would pay for an AI governance framework at the $1,500 to $4,000 Upwork band or well above. But "experts typically get better terms working with Catalant than when working directly with clients" is an undisclosed-fee claim we cannot evaluate. Apply after the compliance offer has a case study. |
| **Bark** | **Poor.** Pay-per-lead at ~£1.20 per credit, 5 to 8 credits (~£7 to £12) for small jobs up to 15 to 20+ (~£22 to £40+) for larger ones; **"Between three and five tradespeople typically contact the same customer"**; realistic cost per job won reported at £48 and often £80 to £150; credits purchased after 1 November 2025 **expire three months after purchase** ([NobleLeads Bark credit costs](https://nobleleads.uk/blog/how-much-do-bark-credits-cost)) | £7 to £40 per shared lead | None | **NO.** Bark is a home-services lead broker. The lead is sold to 3 to 5 competitors simultaneously, the expiry clock forces recurring purchase, and the buyer intent does not exist for a $3,500 compliance-gated voice deployment. |

**Summary of the hub.** Open now, free: **LinkedIn Services page, Contra, Clutch free profile, GoodFirms free profile**. Open week 3, free and fast: **Braintrust**. Apply month 2 to 3: **A.Team, Toptal, Catalant, PeoplePerHour**. Never: **Bark, Freelancer.com, Arc.dev, and any paid directory sponsorship**.

---

## 6. MONITORING: WHAT TO LOG, WHERE IT LIVES, AND WHAT PREDICTS A FIRST ORDER

### 6.1 Fiverr: daily and weekly

Every metric below is in the Fiverr **Analytics dashboard** unless noted ([Fiverr Tutorials seller analytics guide](https://fiverrtutorials.com/fiverr-ranking-guide/fiverr-seller-analytics)).

| Metric | Cadence | Where in the UI | Benchmark |
|---|---|---|---|
| **Impressions** | Daily | Analytics dashboard | A competitive-category gig can generate ~5,000/month ([Fiverr Tutorials](https://fiverrtutorials.com/fiverr-ranking-guide/fiverr-seller-analytics)) |
| **Clicks** | Daily | Analytics dashboard | derived |
| **Click-through rate** (clicks ÷ impressions) | Daily | Computed | 2% to 5% typical for established gigs ([Fiverr Tutorials](https://fiverrtutorials.com/fiverr-ranking-guide/fiverr-seller-analytics)); 8% to 15% is strong ([Jobbers](https://www.jobbers.io/the-complete-fiverr-gig-optimization-guide-2026/)) |
| **Orders** | Daily | Analytics dashboard | |
| **Conversion rate** (orders ÷ clicks) | Weekly | Computed | 3% to 8% is strong ([Jobbers](https://www.jobbers.io/the-complete-fiverr-gig-optimization-guide-2026/)); **under 2% on an established gig means rewrite the description** ([Fiverr Tutorials](https://fiverrtutorials.com/fiverr-ranking-guide/fiverr-seller-analytics)) |
| **Response rate** | Daily | Analytics dashboard **and public profile** | "The percentage of first messages you replied to within 24 hours over the last 90 days"; below 90% needs urgent attention ([Fiverr Tutorials](https://fiverrtutorials.com/fiverr-ranking-guide/fiverr-seller-analytics)). Level 1 requires 80%, Level 2 requires 90% (`fiverr-market.md` section 4.1) |
| **Response time** | Daily | **Public seller profile** | Under 1 hour outranks 6+ hours, all else equal ([Zenlance Fiverr algorithm](https://zenlance.net/fiverr-algorithm/)) |
| **Success Score (1 to 10)** | Weekly | Analytics dashboard and Seller Level dashboard | Six components: **client satisfaction, communication quality, order quality, revision handling, dispute resolution, delivery experience** ([Fiverr Tutorials](https://fiverrtutorials.com/fiverr-ranking-guide/fiverr-seller-analytics)). 5.0+ for Level 1, 7.0+ for Level 2 and for Briefs eligibility, 9.0+ for Top Rated (`fiverr-market.md` section 4.1) |
| **Seller level progress counters** (orders, unique clients, lifetime earnings, rating, days active) | Weekly | Seller Level dashboard | Level 1: 60 days, 5 orders, 3 clients, $400, 4.4+, 80% response, SS 5.0+. Level 2: 120 days, 20 orders, 10 clients, $2,000, 4.6+, 90%, SS 7.0+ (`fiverr-market.md` section 4.1) |
| **Keyword terms buyers used to reach the gig** | Weekly | Seller Plus Kickstart keyword insights | The tool-vs-vertical decision data |

### 6.2 Upwork: daily and weekly

Everything below is under **profile icon > "Stats and trends"** ([Upwork: how to use your stats and trends](https://support.upwork.com/hc/en-us/articles/211062968-My-stats)).

| Metric | Cadence | What it is, per Upwork | Benchmark |
|---|---|---|---|
| **Profile views** | Weekly | "How many people checked out your profile" | |
| **Invitations** | Weekly | "How many invites you've received" | The primary Availability Badge ROI measure |
| **Impressions and clicks (when boosted)** | Weekly | "How often your boosted profile showed up and how many people clicked" | |
| **Proposals sent** | **Daily** | count submitted | 3 to 5/day target ([GigUpHQ](https://giguphq.com/blog/how-long-does-it-take-to-get-your-first-upwork-client)) |
| **Proposals viewed** | **Daily** | "How many clients opened them" | |
| **Interviews** | **Daily** | "How many led to client responses" | **Reply rate baseline 7.45%; our Loom template target 13.77%** ([GigRadar](https://gigradar.io/blog/ai-proposals-upwork)) |
| **Hires** | Weekly | "How many led to a contract" | 5% to 10% of proposals is a healthy win rate ([OutBid](https://useoutbid.com/blog/upwork-connects-cost-per-proposal-2026)) |
| Boosted vs organic split | Weekly | Stats show which | Boost only where boosted interviews exceed organic |
| **Connects balance and spend** | **Daily** | Stats and trends | Cost per client at 5% win = $24; at 10% = $12 ([OutBid](https://useoutbid.com/blog/upwork-connects-cost-per-proposal-2026)) |
| **Job Success Score** | Every 14 days | "your current JSS, based on client satisfaction and contract outcomes" | Displays only after 10 billable hours or one completed fixed-price contract; recalculated daily, **visible every 14 days**; below 75 "response rates collapse" ([UpHunt JSS guide](https://uphunt.io/blog/upwork-job-success-score-jss-2026-explained)) |
| **Earnings, trailing 12 months** | Weekly | Stats and trends | $250 gates Rising Talent; $1,000 gates Top Rated; $10,000 (freelancer) or $20,000 (agency) gates Top Rated Plus |
| **Badge status and next badge** | Weekly | Stats and trends | Upwork names the next badge and the gap |
| **Client relationship / repeat activity** | Monthly | Stats and trends | Recurring clients paying every 90 days weight **very high** in JSS ([UpHunt](https://uphunt.io/blog/upwork-job-success-score-jss-2026-explained)) |
| Time-to-proposal on each job | Per proposal | Manual log | Under 5 min replies at 8.99%, 5 to 10 min at 6.91% ([GigRadar](https://gigradar.io/blog/upwork-market-report-2026)) |
| Bid as % of posted budget | Per proposal | Manual log | 200% to 500% replies at 16.4%; **95% to 105% is the worst position at 8.8%** ([GigRadar](https://gigradar.io/blog/upwork-market-report-2026)) |
| Cliché count in the cover letter | Per proposal | Manual check before send | **Zero. Four or more replies at 0.00%** ([GigRadar](https://gigradar.io/blog/ai-proposals-upwork)) |

### 6.3 Paid-channel metrics

| Metric | Cadence | Where | Benchmark |
|---|---|---|---|
| Google Ads impressions, clicks, CTR, CPC, conversions, CPL | Daily | Google Ads dashboard | Business Services CPC $5.87, CTR 6.10%, CVR 4.85%, CPL $93.69; Automotive CPC $2.27, CTR 8.28%, CVR 6.01%, CPL $44.26 ([WordStream](https://www.wordstream.com/blog/2026-google-ads-benchmarks)) |
| Meta CPC, CPM, CPL, lead quality | Daily | Meta Ads Manager | B2B CPC $2.52; B2B SaaS CPL $63.40 ([Adamigo](https://www.adamigo.ai/blog/meta-ads-cost-per-lead-benchmarks-industry-2026)) |
| LinkedIn CPC, CPM, CTR, form CPL | Weekly | LinkedIn Campaign Manager | CPC $5 to $8, CPM median $31, CTR 0.44% to 0.65%, form CPL $75 to $150 ([Meet-Lea](https://meet-lea.com/en/blog/linkedin-advertising-costs-roi-benchmarks)) |
| **Fiverr gig clicks attributable to ads** | Weekly | Fiverr impressions/clicks jump correlated against ad-platform click counts | Fiverr does not expose referrer. Correlate the daily click delta. |

### 6.4 The leading indicators that predict a first order in 14 days

Ranked by how early they move and how reliably they precede money.

1. **Upwork proposal view rate (proposals viewed ÷ proposals sent).** The earliest signal in the entire system, moving within 24 hours of a send. If proposals are being sent but not opened, the problem is the first two lines and the profile headline, not the offer. This is fixable same-day.
2. **Upwork interview rate (interviews ÷ proposals sent).** The measured target is 7.45% baseline, 13.77% with the full template ([GigRadar](https://gigradar.io/blog/ai-proposals-upwork)). **Below 5% after 20 proposals means stop bidding and rewrite the template.** Above 13% means increase volume immediately.
3. **Fiverr click-through rate.** Moves within 48 hours of publishing because of the honeymoon impression boost ([Zenlance](https://zenlance.net/fiverr-algorithm/)). If impressions are arriving and CTR sits below 2%, the thumbnail and title are wrong. If impressions are not arriving at all, the category and tags are wrong.
4. **Fiverr and Upwork message response time.** The only leading indicator that is 100% within our control and is an explicit ranking input on both platforms ([Zenlance](https://zenlance.net/fiverr-algorithm/), [Jobbers Upwork algorithm](https://www.jobbers.io/the-complete-upwork-algorithm-guide-2026/)). Sub-one-hour, always.
5. **Upwork invitations received.** Invitations are the purest signal that the profile itself, independent of any proposal, is converting. Invited jobs convert far better than bid jobs because the shortlist is shorter. If the Availability Badge spend produces zero invitations in 14 days, turn it off.
6. **Fiverr gig conversion rate (orders ÷ clicks).** The lagging half of the funnel and the dominant Fiverr ranking signal ([Zenlance](https://zenlance.net/fiverr-algorithm/)). Under 2% with healthy click volume means the packages, price ladder or gig description are failing, not the discovery.
7. **Number of $1,500+ jobs identified per day.** A pipeline-input metric, not a platform metric. If we cannot find 3 to 5 jobs per day worth a real proposal, the niche filters are wrong and no amount of proposal quality will compensate.

**The 14-day decision rule.** At day 14: if interview rate is above 7% and no hire has landed, keep going without changing anything, because 20 to 80 proposals is the documented range to first client ([GigUpHQ](https://giguphq.com/blog/how-long-does-it-take-to-get-your-first-upwork-client)). If interview rate is below 5%, stop bidding entirely for one day, rewrite the two opening lines and record a new Loom, then resume. If proposals are not even being opened, the problem is upstream of the proposal and sits in the profile headline, the specialized-profile choice, or the badge state.

---

## 7. RECOMMENDED OPERATING MODEL

### 7.1 What each founder owns

**Chitraksh builds and delivers.** He owns: the Upwork builder account and both specialized profiles; the Oraya Labs agency entity (because only a freelancer account can create an agency, and one per freelancer, per [Upwork](https://support.upwork.com/hc/en-us/articles/211067598-How-to-create-an-agency)); the Fiverr seller account and all three gigs; every technical proposal answer; every delivery; the case-study capture; and the JSS, which is the asset everything else compounds on.

**Frankie sells and fronts the US.** He owns: his own US Upwork freelancer account; the business-manager seat in the agency, which means **he submits proposals on behalf of the agency and is the only party who can accept offers** ([UpHunt Agency Plus](https://uphunt.io/blog/upwork-agency-plus-complete-guide-2026), [Upwork](https://support.upwork.com/hc/en-us/articles/211062608-How-agencies-work-for-freelancers)); every US-only job post, which Chitraksh's account literally cannot see ([Upwork](https://support.upwork.com/hc/en-us/articles/115005777188-Choose-a-freelancer-location-when-posting-a-job)); all discovery and closing calls; the LinkedIn Services page and LinkedIn ads under his own name; and the insurance-vertical positioning, where he is the licensed producer and Oraya is explicitly not a licensed entity (`oraya-facts.md` section 2f).

**The hard boundary, restated because it is the only thing that can destroy the business:** neither person ever logs into the other's account. "You cannot log into someone else's account or let anyone log into your account and work or communicate on your behalf" ([Upwork](https://support.upwork.com/hc/en-us/articles/18513114070419-Represent-yourself-authentically)). Separate devices, separate payment methods, separate withdrawal accounts. The agency is the legitimate shared surface; the accounts are not.

### 7.2 The 30-day account-opening order

**Days 1 to 2: the foundations. Everything free or structural.**

1. Chitraksh opens the Upwork freelancer account and completes ID verification, because verification gates Rising Talent ([Upwork](https://support.upwork.com/hc/en-us/articles/211063228-How-to-become-a-Rising-Talent-on-Upwork)) and unverifiable information risks permanent suspension ([Upwork](https://support.upwork.com/hc/en-us/articles/18513114070419-Represent-yourself-authentically)).
2. Frankie opens his US Upwork account and completes ID verification, on his own device, his own payment method.
3. Chitraksh creates the Oraya Labs agency, subscribes to Agency Plus, and invites Frankie as a business manager.
4. Both profiles to 100% completeness, which is a Rising Talent prerequisite and 10% to 15% of the search algorithm ([Jobbers](https://www.jobbers.io/the-complete-upwork-algorithm-guide-2026/)).
5. Chitraksh creates two specialized profiles: voice agents and telephony, and workflow automation and AI integration.
6. **Portfolio population, the highest-leverage four hours of the month.** From `oraya-facts.md` section 3: dashboard screenshots showing the call-detail drawer with latency waterfall and the compliance panel, the reels already exported (`r1_compliance_ig.mp4`, `r1_missedcall_ig.mp4`, `oraya_reel_voiceagent_ig_li.mp4`), and the data graphics. Anonymised per the project's own rule; no real dealership or agency names.
7. Record the **90-second Loom**: a live call to the demo line with the latency readout visible on screen. This single asset carries the largest measured proposal lift available, at +3.70pp ([GigRadar](https://gigradar.io/blog/ai-proposals-upwork)).
8. Fiverr: publish all three gigs from `fiverr-market.md` section 6.2, subscribe to Seller Plus Kickstart at $15/month.
9. LinkedIn Services page live on Frankie's profile, free consultation toggle on, routed to the Compliance-Safe AI Audit.

**Days 3 to 7: first bids and the honeymoon push.**

10. Subscribe to Freelancer Plus for the 100 Connects and competitor bid visibility. Turn the Availability Badge on with a 100-Connect cap.
11. Frankie starts bidding: 3 to 5 proposals/day, every one under 250 words, zero clichés, opening with a specific question, offering the Loom, bidding 200% to 500% of the posted budget where the budget is low and the scope is real.
12. Point the paid traffic at the Fiverr gigs during the honeymoon window, not at a landing page. Google Search ad groups on "ai receptionist for car dealership", "ai phone agent insurance agency", "tcpa compliant ai calling".
13. Claim free Clutch and GoodFirms profiles.

**Days 8 to 14: instrument and correct.**

14. Apply the 14-day decision rule from section 6.4. This is the only scheduled stop-and-rewrite point in the month.
15. Open Contra (remember: proposals within the first seven days of the profile get search prioritisation, per [Digino](https://digino.org/tools/contra/)).

**Days 15 to 21: widen.**

16. Apply to Braintrust. Verification is 1 to 5 business days and the profile must be complete on submission ([AI Gig Jobs](https://www.aigigjobs.com/blog/braintrust-complete-guide)).
17. Scale the winning ad group, kill the losing one.
18. If a first order has landed: the case-study protocol in 7.4 runs immediately, not later.

**Days 22 to 30: consolidate and set up month 2.**

19. Refresh Fiverr gigs with anything learned from Kickstart keyword data.
20. Apply to A.Team (one 30 to 45 minute interview, no project test) and to Fiverr Pro (2 to 4 week review, so start the clock now).
21. Review the Rising Talent gate: $250 earned plus a 4.8+ rating clears it. If one order has landed at our prices, we are already there.

### 7.3 The daily 30-minute routine

Run it at the same time every day, ideally overlapping US morning so that sub-5-minute proposal speed is achievable on fresh US posts.

| Minutes | Action |
|---|---|
| **0 to 5** | **Clear the inbox on both platforms.** Response time is an explicit ranking input on Fiverr ([Zenlance](https://zenlance.net/fiverr-algorithm/)) and 15% to 20% of the Upwork algorithm ([Jobbers](https://www.jobbers.io/the-complete-upwork-algorithm-guide-2026/)). Nothing else in this routine matters more. |
| **5 to 10** | **Log yesterday's numbers** into one sheet: Fiverr impressions, clicks, CTR, orders, response rate; Upwork proposals sent, viewed, interviews, Connects spent, invitations. Five minutes, no analysis. |
| **10 to 22** | **Scan and bid.** Filter Upwork to the eight niches in section 1.9, posted in the last hour, client payment verified (24% are not, per [Vibeworker](https://tryvibeworker.com/blog/upwork-job-market-report-june-2026)), budget $1,000+. Pick 2 to 3. Write each proposal in about 4 minutes from the template in section 2.12: specific question, measured number, named vertical, Loom offer, scope guarantee, under 250 words. Boost only if the job is $1,500+ and we have named-vertical proof. |
| **22 to 27** | **One portfolio or proof increment.** A screenshot annotated, a Loom re-recorded for a specific vertical, a gig FAQ improved, one LinkedIn post published. Compounding, not urgent. |
| **27 to 30** | **Check the three red flags.** Response rate below 90%? Interview rate below 5% over the last 20 proposals? Fiverr CTR below 2% with healthy impressions? Any yes triggers a rewrite block tomorrow instead of a bidding block. |

Weekly additions, 30 minutes on the same day each week: pull JSS (updates every 14 days, per [UpHunt](https://uphunt.io/blog/upwork-job-success-score-jss-2026-explained)), read the Fiverr Success Score components, read Kickstart keyword data, review ad CPC and CPL against the section 4.4 benchmarks, and check the badge-gap line in Stats and trends.

### 7.4 Case-study capture protocol, after every delivery

Every engagement must produce a reusable asset, because the two largest measured proposal lifts are "reference recently completed work" at +2.52pp and the Loom at +3.70pp ([GigRadar](https://gigradar.io/blog/ai-proposals-upwork)), and both require fresh, specific, defensible material. The protocol also has to survive the project's own rules: "Never: fabricated metrics, fake social proof, or invented client stories" and "Anonymize client data" (`oraya-facts.md` section 5).

**Step 1, before the build starts.** Put a single clause in the scope message: permission to describe the work anonymously, by industry and outcome, with no company name, no logo and no recording. Ask at kickoff, never at the end. A client who says yes at the start says yes at the end; a client asked at the end says "let me check with legal".

**Step 2, during the build, capture as you go.** Screenshot the latency waterfall on a real call on their number. Screenshot the compliance panel showing the locked disclosure as the first utterance. Screenshot the before state (voicemail greeting, missed-call log, manual intake sheet) on day one, because it cannot be recreated later. Record the per-call cost telemetry.

**Step 3, at delivery, ask the client for exactly four things.** Ask in one message, make three of them one-click:
1. A **public review** on the platform, with a suggested sentence they can edit. Note that Fiverr also collects invisible private feedback that feeds ranking separately from the public review ([Zenlance](https://zenlance.net/fiverr-algorithm/)), and Upwork weights private feedback 1 to 10 as heavily as the public stars ([UpHunt](https://uphunt.io/blog/upwork-job-success-score-jss-2026-explained)), so the ask should be for honest feedback rather than for stars.
2. **One number they care about**, in their words: calls answered after hours, bookings taken, minutes of staff time returned. One number, not a survey.
3. **Permission to quote one sentence** of what they said, attributed to a role and industry only, such as "Service manager, 3-rooftop dealership group, Midwest US".
4. **A 30-day check-in slot**, which doubles as the retainer conversation and as JSS insurance, because recurring clients paying every 90 days weight very high in JSS ([UpHunt](https://uphunt.io/blog/upwork-job-success-score-jss-2026-explained)).

**Step 4, anonymisation rules, applied before anything leaves the building.**
- Replace the business name with industry plus size plus region: "independent P&C agency, 12 producers, US Southeast".
- Blur or replace phone numbers, caller names, addresses and policy or VIN numbers in every screenshot. The product already reads only PII-masked Postgres views on the public dashboard (`oraya-facts.md` section 1), so screenshot the masked view by default.
- Never publish call audio. Live recordings are gated behind auth in Supabase and Twilio for a reason (`oraya-facts.md` section 3).
- State measured numbers with the date and the method, per the project's own visual standard: "median 761 ms time-to-first-audio, measured over simulated calls on the deployed demo, 26 August 2026".
- Never present a demo or simulated-call metric as a production-scale metric. `oraya-facts.md` section 1 is explicit that answer rate, booking rate and calls-at-scale are **not** measured production numbers and must not be claimed.
- Add "not legal advice" framing to anything in the compliance lane, per `oraya-growth-engine/guardrails.md`.

**Step 5, within 48 hours, produce three artefacts from every delivery.**
1. A **one-paragraph case card**: vertical, problem, what we built, the one number, the anonymised quote. This is what gets pasted into proposals as "recently completed work".
2. A **new 60 to 90 second Loom** for that vertical, showing the build and the latency readout. Vertical-specific Looms outperform generic ones because the proposal lift comes from specificity.
3. A **portfolio item** on both Upwork specialized profiles and the Fiverr gig gallery, plus one LinkedIn post that satisfies the house rule: "contains a real number, real artifact, or first-person story, or it dies" (`oraya-facts.md` section 5).

**Step 6, feed it back into pricing.** After every third delivery, raise the entry price by 10% to 15%. The evidence on both platforms is unambiguous that price and credential outrank review count in this category: a Top Rated Fiverr seller holds slot one on a 44,698-service keyword at **$1,800 with 2 reviews** (`fiverr-market.md` section 5.8), and on Upwork bidding 200% to 500% of the posted budget replies at 16.4% against 8.8% for matching it ([GigRadar](https://gigradar.io/blog/upwork-market-report-2026)). **The low anchor is the trap. Raising price is a growth action, not a risk.**

---

## SOURCES

**Upwork platform, market and demand**
- [Upwork In-Demand Skills 2026 press release](https://www.upwork.com/press/releases/upworks-in-demand-skills-2026-demand-for-top-ai-skills-more-than-doubles-as-ai-is-embedded-into-everyday-work) · [Barchart coverage](https://www.barchart.com/story/news/21201/upworks-in-demand-skills-2026-demand-for-top-ai-skills-more-than-doubles-as-ai-is-embedded-into-everyday-work)
- [Vibeworker: the Upwork job market in June 2026, 127,607 postings analyzed](https://tryvibeworker.com/blog/upwork-job-market-report-june-2026)
- [GigRadar Upwork market report 2026](https://gigradar.io/blog/upwork-market-report-2026) · [GigRadar AI proposals reply-rate data](https://gigradar.io/blog/ai-proposals-upwork) · [GigRadar Upwork fees 2026](https://gigradar.io/blog/upwork-fees)
- [RemoteAITools: Upwork AI automation jobs 2026](https://remoteaitools.com/upwork-ai-automation-jobs-2026/)
- Live job counts: [cold-calling](https://www.upwork.com/freelance-jobs/cold-calling/) · [outbound-sales](https://www.upwork.com/freelance-jobs/outbound-sales/) · [lead-generation](https://www.upwork.com/freelance-jobs/lead-generation/) · [automation](https://www.upwork.com/freelance-jobs/automation/) · [appointment-setting](https://www.upwork.com/freelance-jobs/appointment-setting/) · [artificial-intelligence](https://www.upwork.com/freelance-jobs/artificial-intelligence/) · [chatbot-development](https://www.upwork.com/freelance-jobs/chatbot-development/) · [conversational-ai](https://www.upwork.com/freelance-jobs/conversational-ai/) · [api-integration](https://www.upwork.com/freelance-jobs/api-integration/) · [n8n](https://www.upwork.com/freelance-jobs/n8n/) · [ai-compliance-skills](https://www.upwork.com/freelance-jobs/ai-compliance-skills/)
- Upwork price guidance: [AI voice agent developers](https://www.upwork.com/hire/ai-voice-agent-developers/) · [AI agent developers](https://www.upwork.com/hire/ai-agent-developers/) · [conversational AI specialists](https://www.upwork.com/hire/conversational-ai-specialists/) · [n8n experts](https://www.upwork.com/hire/n8n-experts/) · [MCP server developers](https://www.upwork.com/hire/mcp-server-developers/) · [AI policy compliance professionals](https://www.upwork.com/hire/ai-policy-compliance-professionals/) · [cold callers](https://www.upwork.com/hire/cold-callers/)
- Live job examples: [$10 Retell/Vapi voice agent](https://www.upwork.com/freelance-jobs/apply/Create-Simple-Conversational-Retell-Vapi-Voice-Agent-with-Basic-API-n8n-Setup_~022072486623594733415/) · [$150 outbound Vapi/Twilio/n8n agent](https://www.upwork.com/freelance-jobs/apply/Outbound-Voice-Agent-Developer-Vapi-Twilio-n8n-for-Cold-Calling-Automation_~022087531216573679596/) · [Project Catalog AI receptionist listing](https://www.upwork.com/services/product/development-it-24-7-ai-receptionist-ai-voice-agent-using-elevenlabs-vapi-or-retell-1995380400744282985)

**Upwork mechanics**
- [Understanding and using Connects](https://support.upwork.com/hc/en-us/articles/211062898-Understanding-and-using-Connects) · [OutBid Connects cost per proposal 2026](https://useoutbid.com/blog/upwork-connects-cost-per-proposal-2026)
- [How to boost your proposal](https://support.upwork.com/hc/en-us/articles/4406395531795-How-to-boost-your-proposal) · [Zenlance on boosted proposals](https://zenlance.net/upwork-boosted-proposals/)
- [How to become a Rising Talent](https://support.upwork.com/hc/en-us/articles/211063228-How-to-become-a-Rising-Talent-on-Upwork) · [How to become Top Rated](https://support.upwork.com/hc/en-us/articles/211068468-How-to-become-Top-Rated-on-Upwork) · [Understand freelancer talent badges](https://support.upwork.com/hc/en-us/articles/211063568-Understand-freelancer-talent-badges)
- [UpHunt: Upwork JSS explained 2026](https://uphunt.io/blog/upwork-job-success-score-jss-2026-explained) · [Jobbers: complete Upwork algorithm guide 2026](https://www.jobbers.io/the-complete-upwork-algorithm-guide-2026/)
- [Availability Badge: how it works](https://support.upwork.com/hc/en-us/articles/40367622397075-How-does-the-Availability-Badge-work) · [Is there a maximum price for the badge](https://support.upwork.com/hc/en-us/articles/40367930714899-Is-there-a-maximum-price-for-the-badge)
- [How to add new profiles to your Upwork account](https://support.upwork.com/hc/en-us/articles/115013660327-How-to-add-new-profiles-to-your-Upwork-account) · [Project Catalog for freelancers](https://support.upwork.com/hc/en-us/articles/360058234233-How-to-get-started-with-Project-Catalog-as-a-freelancer)
- [Fixed-Price Payment Protection](https://support.upwork.com/hc/en-us/articles/211063748-How-Fixed-Price-Payment-Protection-works-for-freelancers-on-Upwork) · [How Upwork protects your payments](https://support.upwork.com/hc/en-us/articles/211062568-How-Upwork-protects-your-payments)
- [Freelancer Plus](https://www.upwork.com/work/freelancerplus)
- [Upwork Talent Scout press release](https://www.upwork.com/press/releases/upwork-introduces-talent-scout) · [Upwork Enterprise](https://support.upwork.com/hc/en-us/articles/226526507-Upwork-Enterprise)
- Time-to-first-hire: [GigUpHQ](https://giguphq.com/blog/how-long-does-it-take-to-get-your-first-upwork-client) · [UpHunt first-client guide 2026](https://uphunt.io/blog/how-to-get-first-client-upwork-2026-complete-guide) · [Quora practitioner thread on 20 to 50 proposals per post](https://www.quora.com/Upwork-in-2026-every-job-post-for-beginner-intermediate-has-20-to-50-proposals-and-connects-are-pricier-the-platform-is-primed-for-established-professionals-and-against-newbies-What-advice-can-you-give-a-web-dev)
- [Upwork stats and trends](https://support.upwork.com/hc/en-us/articles/211062968-My-stats)

**Multi-account rules and account structure**
- Fiverr: [Our Community Standards, the one-account clause](https://help.fiverr.com/hc/en-us/articles/32242973123985-Our-Community-Standards) · [Account restrictions](https://help.fiverr.com/hc/en-us/articles/34551010553489-Account-restrictions) · [Fiverr agencies](https://help.fiverr.com/hc/en-us/articles/29454085707409-Fiverr-agencies) · [Fiverr agencies onboarding requirements](https://help.fiverr.com/hc/en-us/articles/21836241851409-Fiverr-agencies-onboarding-requirements) · [Fiverr Tutorials on multiple accounts and detection](https://fiverrtutorials.com/fiverr-secrets-multiple-fiverr-accounts/) · [Fiverr Tutorials on Fiverr Pro](https://fiverrtutorials.com/fiverr-pro-seller) · [Prohibited services](https://help.fiverr.com/hc/en-us/articles/49174165608593-Prohibited-services-on-Fiverr) · [Policy Violations Explained](https://help.fiverr.com/hc/en-us/articles/48022851354385-Policy-Violations-Explained)
- Upwork: [Why you can't have two Upwork accounts](https://support.upwork.com/hc/en-us/articles/39505058710163-Why-you-can-t-have-two-Upwork-accounts) · [Multiple accounts FAQ](https://support.upwork.com/hc/en-us/articles/36738402656531-Multiple-accounts-Frequently-Asked-Questions) · [Represent yourself authentically](https://support.upwork.com/hc/en-us/articles/18513114070419-Represent-yourself-authentically) · [How agencies work for freelancers](https://support.upwork.com/hc/en-us/articles/211062608-How-agencies-work-for-freelancers) · [How to create an agency](https://support.upwork.com/hc/en-us/articles/211067598-How-to-create-an-agency) · [Agencies FAQ](https://support.upwork.com/hc/en-us/articles/35389337775123-Agencies-Frequently-Asked-Questions) · [How agency finances work](https://support.upwork.com/hc/en-us/articles/360009524554-How-agency-finances-work) · [About the Agency Plus plan](https://support.upwork.com/hc/en-us/articles/211062958-About-the-Agency-Plus-plan-on-Upwork) · [UpHunt Agency Plus guide 2026](https://uphunt.io/blog/upwork-agency-plus-complete-guide-2026) · [UpHunt suspension and appeal guide 2026](https://uphunt.io/blog/upwork-account-suspended-recovery-appeal-guide-2026)
- Location: [Choose a freelancer location when posting a job](https://support.upwork.com/hc/en-us/articles/115005777188-Choose-a-freelancer-location-when-posting-a-job) · [Search for U.S. freelancers only](https://support.upwork.com/hc/en-us/articles/17938843522963--Search-for-U-S-freelancers-only) · [Verify location for U.S.-only jobs](https://support.upwork.com/hc/en-us/articles/115005613127-Verify-location-for-U-S-only-jobs)

**Ads and paid visibility**
- [Fiverr Promoted Gigs](https://www.fiverr.com/pages/promoted-gigs) · [Fiverr Tutorials Promoted Gigs guide](https://fiverrtutorials.com/fiverr-ranking-guide/fiverr-promoted-gigs-guide) · [Jobbers Fiverr gig optimization guide 2026](https://www.jobbers.io/the-complete-fiverr-gig-optimization-guide-2026/)
- [Seller Plus Kickstart](https://help.fiverr.com/hc/en-us/articles/27291415082257-Seller-Plus-Kickstart-Start-your-freelance-journey-strong) · [Seller Plus Standard and Premium](https://help.fiverr.com/hc/en-us/articles/360017140717-Seller-Plus-Standard-and-Premium-Advanced-tools-for-business-growth) · [GigRankPro on Seller Plus](https://gigrankpro.com/is-fiverr-seller-plus-worth-it/)
- [Promoting your Gigs outside of Fiverr](https://help.fiverr.com/hc/en-us/articles/360010490438-Promoting-your-Gigs-outside-of-Fiverr) · [Fiverr Tutorials on external traffic](https://fiverrtutorials.com/promote-fiverr-gigs-tips) · [Zenlance Fiverr algorithm 2026](https://zenlance.net/fiverr-algorithm/)
- [WordStream 2026 Google Ads benchmarks](https://www.wordstream.com/blog/2026-google-ads-benchmarks) · [Marqeable B2B SaaS Google Ads benchmarks 2026](https://www.marqeable.com/blog/google-ads-benchmarks-b2b-saas/) · [Adamigo Meta CPL benchmarks by industry 2026](https://www.adamigo.ai/blog/meta-ads-cost-per-lead-benchmarks-industry-2026) · [Meet-Lea LinkedIn advertising benchmarks 2026](https://meet-lea.com/en/blog/linkedin-advertising-costs-roi-benchmarks)

**Other channels**
- [LinkedIn Services page guide 2026](https://connectsafely.ai/articles/linkedin-providing-services-section-guide-2026)
- [Digino Contra review for AI automation builders](https://digino.org/tools/contra/) · [Jobbers freelance platform fee encyclopedia](https://www.jobbers.io/the-freelance-platform-fee-encyclopedia-every-fee-on-every-platform-documented/)
- [Memvers Toptal application guide 2026](https://memvers.com/for-freelancers/platforms/toptal) · [A.Team join page](https://www.a.team/join) · [AI Gig Jobs Braintrust guide](https://www.aigigjobs.com/blog/braintrust-complete-guide) · [Arc.dev pricing 2026](https://www.hireinsouth.com/post/arc-dev-pricing) · [Catalant: how to partner](https://catalant.com/for-independent-consultants/how-to-partner/)
- [Clutch pricing 2026](https://www.hireinsouth.com/post/clutch-pricing) · [GoodFirms sponsorship pricing](https://www.goodfirms.co/sponsors/pricing) · [NobleLeads Bark credit costs 2026](https://nobleleads.uk/blog/how-much-do-bark-credits-cost) · [Freelancer.com pricing 2026](https://www.hireinsouth.com/post/freelancer-pricing) · [PeoplePerHour freelancer application process](https://support.peopleperhour.com/hc/en-us/articles/4408655983633-Freelancer-Application-Process)

**Cross-referenced from the companion documents**
- [Fiverr Q2 2026 results](https://www.fiverr.com/news/fiverr-q2-2026-earnings) · [Fiverr Business Trends Index June 2026](https://www.fiverr.com/resources/guides/reports/business-trends-index-june-2026) · [CloudTalk AI voice agent statistics](https://www.cloudtalk.io/blog/ai-voice-agent-statistics/)
- `/home/claude/research/fiverr-market.md` sections 1, 3, 4, 5, 6
- `/home/claude/research/oraya-facts.md` sections 1, 2, 3, 4, 5, 6

**Research limitations, stated plainly.**
1. Upwork does not publish per-skill freelancer counts, so supply in section 1.8 is proxied by total client-review counts on `/hire/` pages. That proxy scales with completed engagements, not with live competitor count, and it undercounts freelancers who have listed a skill but never sold it.
2. Upwork's public `/freelance-jobs/<slug>/` pages publish an open-job count but not a proposal-count distribution or a hire rate. Proposal density figures in section 1.7 come from practitioner reporting and the GigRadar proposal dataset, not from Upwork.
3. Neither Vapi, Retell, LiveKit nor ElevenLabs appears as a named tool in the Vibeworker mention index, so section 1.3's claim that they are below the measurement threshold on Upwork is an inference from absence, not a measured zero.
4. Fiverr does not publish Promoted Gigs eligibility on its own page. Section 4.1's Level 1 plus 20 completed orders figure is third-party and the two third-party sources disagree (Level 1 vs Level 2 for full access). Verify inside the seller dashboard.
5. Upwork does not publish Project Catalog eligibility criteria on the freelancer getting-started page. Section 2.6 is therefore hedged.
6. Catalant and Arc.dev do not publish freelancer-side fee structures. Both are marked "later" partly for that reason.
7. All ad benchmarks are cross-industry medians. No benchmark exists for the exact query "ai receptionist for car dealership", and the CPC estimate in section 4.4 is reasoned from the automotive category figure rather than measured.
