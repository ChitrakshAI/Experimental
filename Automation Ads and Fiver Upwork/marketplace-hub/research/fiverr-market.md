# Fiverr Market Analysis: AI Voice Agents, Agentic Automation and Compliance-Aware Outbound
### Marketplace research, September 2026

**Scope:** AI voice agents (Retell, Vapi, ElevenLabs Conversational AI, LiveKit, Twilio), agentic workflows and automation (n8n, Make, Zapier, custom Python/Node agents, Claude/OpenAI agents, MCP servers), AI lead-gen and outbound pipelines (Apollo, Playwright scrapers, Supabase), AI chatbots, AI-powered CRM integrations, and compliance-aware AI calling (TCPA).

**Method note:** Fiverr blocks automated access to `/search/gigs` under robots.txt. Two paths remain open and were used throughout: the taxonomy pages under `/categories/...` and the keyword landing pages under `/gigs/<keyword>`, which publish an exact "X services available" counter. Every count below was read directly off a live Fiverr page on 10 September 2026 and the URL is given. Where a `/gigs/<keyword>` page does not exist, Fiverr redirects to search, which is itself a supply signal: the keyword sits below the threshold at which Fiverr builds a landing page.

---

## 0. MACRO CONTEXT: WHY THE TIMING IS UNUSUAL

Fiverr is shrinking in volume and growing in value per transaction, and it is saying so out loud. Q2 2026 revenue was **$97.8 million, down 10.0% year over year** from $108.6 million. Marketplace revenue fell harder, **$63.1 million, down 15.5%**. Annual active buyers fell **21.9% to 2.7 million**, from 3.4 million. But annual spend per buyer rose **15.6% to $368**, take rate rose to **28.0%** from 27.6%, and, critically, **"Clients completing $1,000+ projects grew 13% y/y on a trailing twelve month basis."** Full-year 2026 guidance is $356 to $372 million, a decline of 17% to 14%. Source: [Fiverr Q2 2026 results](https://www.fiverr.com/news/fiverr-q2-2026-earnings).

Read that as a strategic brief rather than a warning. AI is eating the $5 to $50 transactional layer of the marketplace, buyer counts are collapsing at the bottom, and the surviving buyers are spending more each on harder work. A seller entering in late 2026 with genuinely complex, production-grade delivery is entering the only segment that is growing. A seller entering to compete on price is entering the segment that is being automated away.

Fiverr's own commentary on its Q1 2026 call put **AI development up 118% year over year** ([Memvers analysis of Fiverr and Upwork agent demand](https://memvers.com/blog/upwork-fiverr-ai-agents-marketplace-shift-2026)).

The underlying category is real, not a marketplace artifact. Grand View Research sizes AI voice agents at **$2.54 billion in 2025 growing to $35.24 billion by 2033, a 39.0% CAGR**, with financial services and insurance the largest vertical at **32.9% market share** and healthcare the fastest growing at **42.0% CAGR**. McKinsey's State of AI 2025 has **62% of enterprises actively testing AI agents**. Sources: [CloudTalk AI voice agent statistics](https://www.cloudtalk.io/blog/ai-voice-agent-statistics/), [Grand View Research AI voice agents market report](https://www.grandviewresearch.com/industry-analysis/ai-voice-agents-market-report).

---

## 1. CATEGORY MAP

### 1.1 The taxonomy that actually exists today

Fiverr reorganized its AI taxonomy during 2025 and 2026. The important structural fact for a new seller is that **there is no single "AI Agents" category**. The work we do is split across at least four different trees, and choosing the wrong one costs visibility.

**Tree A: Programming & Tech > AI Development (URL slug `ai-coding`)**

Live at [fiverr.com/categories/programming-tech/ai-coding](https://www.fiverr.com/categories/programming-tech/ai-coding). The page reports **28,000+ results**. Its five children, named verbatim on the parent [Programming & Tech](https://www.fiverr.com/categories/programming-tech) page:

- AI Websites & Software (`/ai-coding/ai-software-website`)
- AI Mobile Apps (`/ai-coding/ai-applications`)
- AI Integrations
- **AI Agents**
- AI Technology Consulting

**Tree B: Programming & Tech > Software Development > Automations & Workflows**

This is the highest-value discovery of the sweep. The leaf lives at [fiverr.com/categories/programming-tech/ai-coding/ai-agents-development](https://fiverr.com/categories/programming-tech/ai-coding/ai-agents-development) but presents as **"Automations & Agents"** with the tagline "Streamline your business through automations & workflows!" and a breadcrumb reading **Programming & Tech > Software Development > Automations & Workflows**. It reports **18,000+ results**. Its filter chips are "Workflow Automation Consultants", "Zapier Automations", and "N8n Automation".

The slug says `ai-agents-development`, the breadcrumb says Automations & Workflows, and the H1 says Automations & Agents. Fiverr has merged agent-building and workflow automation into one commercial surface. That merge is why n8n gigs and Vapi voice-agent gigs sit side by side in the same result set, and it is why a positioning that spans both is coherent rather than scattered.

The gigs ranking on page one of this leaf on 10 September 2026:

| Seller | Exact gig title | Badge | Rating | From |
|---|---|---|---|---|
| Jerry Steve | "I will build custom ai automation and voice agents with retell ai and vapi" | none | 5.0 (18) | $15 |
| Mariam A | "I will build make com automation, n8n automation workflow, fix make com, base44, ghl" | Level 1 | 5.0 (10) | $10 |
| Daniel | "I will be your n8n expert" | Level 1 | 5.0 (12) | $10 |
| Jordan | "I will fix, setup make com automation, zapier automation, airtable database" | none | 5.0 (12) | $10 |
| Ayodeji O. | "I will gohighlevel api integration CRM automation client dashboard portal ghl expert" | Level 2 | 4.9 (49) | $45 |
| Micky J | "I will build make com automation ai voice agent ai receptionist with retell, vapi, n8n" | Level 1 | 5.0 (20) | $25 |
| Hamza Irshad | "I will build ai automation workflows using make, zapier and ai" | Level 2 | 4.9 (742) | $40 |
| Ali Raza | "I will do n8n ai automation, n8n ai agent and n8n scalable workflows" | Level 1 | 5.0 (29) | $50 |

Note what page one looks like: seven of eight sellers are Level 1 or unbadged, entry prices cluster at $10 to $50, and only one seller has meaningful review depth. **This is a weakly defended front page.** For comparison, the Software Development parent category runs **86,000+ results at 4.9/5 across approximately 710K reviews with typical project cost stated as $130 to $1,500**, which is a far more mature and defended surface.

**Tree C: Programming & Tech > Chatbot Development**

[fiverr.com/categories/programming-tech/chatbot-development](https://www.fiverr.com/categories/programming-tech/chatbot-development), **13,000+ results**, average **4.9/5 across approximately 67K reviews**. Two children: "AI Chatbot" and "Rules Based Chatbot". Fiverr's own FAQ on that page states a basic chatbot typically runs **$150 to $800**. Page one includes Mubashir Saleem (Top Rated, 721 reviews, from $45) selling Twilio SMS and voice calls, which is the closest direct competitor to a telephony-first positioning.

**Tree D: the AI Services vertical**

[fiverr.com/categories/ai-services](https://www.fiverr.com/categories/ai-services) is a marketing overlay rather than a true taxonomy, advertising "10K+ AI experts" and "20+ types of services related to AI". It surfaces AI Agents, AI Chatbots, AI Applications, AI Integrations, AI Fine-Tuning, Data Model Training, AI Technology Consulting (new), and Generative Engine Optimization (new). Its audio branch, **Voice Synthesis & AI > Text to Speech / Custom AI Voices / Speech Recognition**, sits under Music & Audio and is the wrong home for conversational telephony. Filing a Vapi or Retell gig there would bury it among voiceover sellers.

**Tree E: Vibe Coding**

A genuinely new Programming & Tech subcategory with children "Development & MVP", "Troubleshooting & Improvements", "Deployments & DevOps", "Consultation & Training". Relevant only as evidence that Fiverr creates categories fast when search volume justifies it.

### 1.2 Supply signal: exact "services available" counts

Every figure read live from the named URL, 10 September 2026, sorted descending.

| # | Keyword (`/gigs/` slug) | Services available | Top-result price band | Quality read |
|---|---|---|---|---|
| 1 | [ai-integration](https://www.fiverr.com/gigs/ai-integration) | **113,213** | $20 to $100 | Saturated, meaningless breadth |
| 2 | [ai-automation](https://www.fiverr.com/gigs/ai-automation) | **88,405** | $20 to $100 | Saturated |
| 3 | [crm-integration](https://www.fiverr.com/gigs/crm-integration) | **78,710** | $80 to $995 | Saturated but high ceiling |
| 4 | [conversational-ai](https://www.fiverr.com/gigs/conversational-ai) | **51,852** | $5 to $300 | Polluted (image-conversion gigs rank) |
| 5 | [voice-ai](https://www.fiverr.com/gigs/voice-ai) | **46,911** | $20 to $75 | Polluted (voice cloning dominates) |
| 6 | [ai-chatbot](https://www.fiverr.com/gigs/ai-chatbot) | **45,643** | $5 to $150 | Saturated, commoditized |
| 7 | [ai-agent](https://www.fiverr.com/gigs/ai-agent) | **44,698** | $1,800 top result | Saturated, but top slot is Top Rated at $1,800 |
| 8 | [ai-lead-generation](https://www.fiverr.com/gigs/ai-lead-generation) | **42,030** | $5 to $40 | Saturated, race to bottom |
| 9 | [n8n-automation](https://www.fiverr.com/gigs/n8n-automation) | **37,861** | $40+ | Crowded, quality rising |
| 10 | [zapier-automation](https://www.fiverr.com/gigs/zapier-automation) | **36,939** | $10 | Saturated, template titles |
| 11 | [gohighlevel](https://www.fiverr.com/gigs/gohighlevel) | **32,734** | $20 to $45 | Crowded agency-adjacent |
| 12 | [ai-consulting](https://www.fiverr.com/gigs/ai-consulting) | **31,899** | $15 to $30 | Crowded, thin credibility |
| 13 | [claude-code](https://www.fiverr.com/gigs/claude-code) | **26,481** | $5 to $500 | Crowded but very new, wide price variance |
| 14 | [supabase](https://www.fiverr.com/gigs/supabase) | **21,732** | $20 to $150 | Crowded backend generalists |
| 15 | [ai-agent-development](https://www.fiverr.com/gigs/ai-agent-development) | **19,687** | $35 to $50 | Crowded |
| 16 | [vapi](https://www.fiverr.com/gigs/vapi) | **14,986** | $5 to $25 | Crowded, extremely low anchors |
| 17 | [ai-voice-agent](https://www.fiverr.com/gigs/ai-voice-agent) | **12,823** | $30 to $100 | Crowded, mixed quality |
| 18 | [retell-ai](https://www.fiverr.com/gigs/retell-ai) | **12,134** | $200 top result | Crowded, healthier anchors |
| 19 | [make-com-automation](https://www.fiverr.com/gigs/make-com-automation) | **11,858** | $20 to $50 | Crowded, keyword-stuffed titles |
| 20 | [ai-calling-agent](https://www.fiverr.com/gigs/ai-calling-agent) | **10,762** | $40 to $90 | Crowded |
| 21 | [twilio](https://www.fiverr.com/gigs/twilio) | **10,155** | $300 top result | Moderate, Top Rated holds slot 1 |
| 22 | [ai-receptionist](https://www.fiverr.com/gigs/ai-receptionist) | **3,974** | $80 to $225 | **Moderate supply, strong prices** |
| 23 | [elevenlabs](https://www.fiverr.com/gigs/elevenlabs) | **3,817** | $10 | Voiceover only, agents absent |
| 24 | [insurance-agency](https://www.fiverr.com/gigs/insurance-agency) | **3,445** | $10 to $120 | **No AI voice gigs present** |
| 25 | [n8n-ai-receptionist](https://www.fiverr.com/gigs/n8n-ai-receptionist) | **2,762** | $30 to $90 | Thin |
| 26 | [car-dealership](https://www.fiverr.com/gigs/car-dealership) | **2,699** | $55 to $80 | **No AI voice gigs present** |
| 27 | [mcp-server](https://www.fiverr.com/gigs/mcp-server) | **2,487** | $100 | **Thin, uniform $100 anchor** |
| 28 | [ai-phone-agent](https://www.fiverr.com/gigs/ai-phone-agent) | **2,421** | $15 to $300 | Thin |
| 29 | [ai-cold-calling](https://www.fiverr.com/gigs/ai-cold-calling) | **2,232** | $50 to $120 | **Thin, no compliance framing anywhere** |
| 30 | [dental-office](https://www.fiverr.com/gigs/dental-office) | **807** | $20 | Logo design only, zero AI |
| 31 | [apollo-io](https://www.fiverr.com/gigs/apollo-io) | **795** | $15 to $20 | **Very thin, low anchors** |
| 32 | [livekit](https://www.fiverr.com/gigs/livekit) | **195** | $15 | **Near-empty, one Vetted Pro** |
| 33 | [ai-sdr-agent](https://www.fiverr.com/gigs/ai-sdr-agent) | **163** | $35 to $250 | **Near-empty, strong prices** |

**Keywords with no landing page at all** (Fiverr redirects to robots-blocked search, indicating supply below its landing-page threshold): `tcpa-compliance`, `elevenlabs-conversational-ai`, `ai-appointment-setter`, `ai-voice-agent-for-real-estate`, `ai-workflow-automation`.

Two of these matter enormously. **There is no TCPA landing page on Fiverr.** And **there is no ElevenLabs Conversational AI landing page**, even though `elevenlabs` has 3,817 services, because essentially all of them are voiceover gigs rather than agent builds.

### 1.3 Pro and Top Rated presence

Pro and Top Rated sellers are present but sparse in the automation and voice surfaces. On the Automations & Agents leaf, zero of the eight page-one gigs carried a Pro or Top Rated badge. On `livekit`, one of two visible results was a "Vetted Pro". On `ai-agent`, the number-one result was Top Rated Karthik Pillai at **$1,800 with only 2 reviews**, which tells you Fiverr will rank a credentialed seller at a high price point with almost no order history. On `twilio`, Top Rated Mubashir Saleem holds slot one at **$300 with 7 reviews**. On `crm-integration`, Top Rated Ajay Kumar holds slot two at **$995 with a 4.1 rating across 9 reviews**.

The pattern is consistent and it is the single most actionable finding in this section: **in these niches Fiverr is ranking badge and price over review volume.** A credible high-priced gig can hold a top slot on very few reviews.

---

## 2. DEMAND SIGNALS

### 2.1 Fiverr's own search data (the strongest single source)

Fiverr's [June 2026 Business Trends Index](https://www.fiverr.com/resources/guides/reports/business-trends-index-june-2026) compares searches in **November 2025 to April 2026 against May to October 2025**. The AI and automation lines, quoted exactly:

| Search term | Growth |
|---|---|
| Claude Code | **+938%** |
| Excel data cleaning | +210% |
| PDF to Excel conversion | +153% |
| **n8n AI automation** | **+125%** |
| Base44 | +95% |
| AI mobile app development | +92% |
| Vibe coding | +61% |
| **AI voice agents** | **+49%** |
| AI automation (Writing category) | +49% |
| AI website development | +39% |
| **Programming & Tech, whole category** | **+94%** |

Fiverr headlined the report on the Claude Code number: [Businesses Race to Hire Claude Code Specialists As Demand Surges 938%](https://www.fiverr.com/news/business-trends-index-ai-2026), corroborated by [StockTitan](https://www.stocktitan.net/news/FVRR/businesses-race-to-hire-claude-code-specialists-as-demand-surges-6x7lep85s2n8.html).

Three readings matter here.

First, **+49% for AI voice agents is the weakest headline number in the AI cluster but the most bankable one.** It is a second-derivative signal: the term is past its explosive phase and into steady compounding. Compare it with Fiverr's May 2025 report of an **18,347% search surge for AI agents over the six months from September 2024 to March 2025** ([Memvers](https://memvers.com/blog/upwork-fiverr-ai-agents-marketplace-shift-2026)). A category that ran 18,347% and is still adding 49% half-yearly two years later is a category that converted from hype into budget.

Second, **n8n at +125% is growing 2.6x faster than voice agents** and is the only named workflow tool in the index. Make and Zapier do not appear. That is a demand asymmetry against a supply position where n8n (37,861 services) is already less crowded than Zapier (36,939) at far higher growth.

Third, **Claude Code at +938% is the largest under-served demand signal on the platform**, and it maps directly onto custom Python/Node agent work rather than no-code tooling.

### 2.2 Platform-level evidence that buyers are moving upmarket

From [Fiverr Q2 2026 results](https://www.fiverr.com/news/fiverr-q2-2026-earnings): clients completing **$1,000+ projects grew 13% year over year** while total buyers fell 21.9% and spend per buyer rose 15.6% to $368. Fiverr's leadership attributed the shift to "accelerated evolution" from AI adoption and described repositioning toward higher-value work as AI absorbs transactional tasks. Corroborated by [Staffing Industry Analysts](https://www.staffingindustry.com/news/global-daily-news/fiverr-q2-revenue-slips-10-amid-ai-led-market-shift) and [TipRanks](https://www.tipranks.com/news/company-announcements/fiverr-cuts-2026-outlook-as-ai-pushes-marketplace-upmarket).

The demand for cheap gigs is genuinely evaporating. The demand for $1,000+ engagements is the only growing buyer cohort on the platform.

### 2.3 Upwork cross-check

Upwork's own hiring guide for [AI voice agent developers](https://www.upwork.com/hire/ai-voice-agent-developers/) publishes the price expectations it sets for buyers, which is the cleanest available proxy for what this work is actually worth off Fiverr:

| Engagement type | Upwork's stated range |
|---|---|
| Single-flow voice agent | **$600 to $6,000** |
| Multi-intent voice assistant | **$1,200 to $12,000** |
| Production-grade deployment | **$2,400 to $24,000** |
| Enterprise multi-agent system | **$4,800 to $48,000** |
| Ongoing maintenance | **$1,500 to $4,500** |

Hourly guidance is **$30 to $150/hour** for AI developers, though the specific freelancers surfaced on that page were listing $5 to $10/hour, which is the same bimodal split visible on Fiverr.

Upwork also reports **skills explicitly referencing AI up 109% year over year** in 2025 ([Memvers](https://memvers.com/blog/upwork-fiverr-ai-agents-marketplace-shift-2026)), and [Upwork's In-Demand Skills report](https://www.barchart.com/story/news/21201/upworks-in-demand-skills-2026-demand-for-top-ai-skills-more-than-doubles-as-ai-is-embedded-into-everyday-work) headlines demand for top AI skills more than doubling.

**The gap between Upwork's $600 to $24,000 guidance and Fiverr's $10 to $90 page-one entry prices is the arbitrage.** The same work, the same tools, the same buyer, priced one to two orders of magnitude apart. Fiverr buyers are not inherently cheaper; Fiverr's voice-agent supply has simply anchored itself at the floor and nobody credible is contesting the ceiling.

### 2.4 Vertical demand evidence

BFSI holds **32.9% of the AI voice agent market**, the largest single vertical, and healthcare is growing fastest at **42.0% CAGR** ([CloudTalk](https://www.cloudtalk.io/blog/ai-voice-agent-statistics/)). Contact-center deployment was still early as of 2024, with only 1 in 6 having deployed generative AI and 42% more planning deployment ([Deloitte Digital 2024 Contact Center Survey](https://www.deloittedigital.com/us/en/insights/perspective/2024-contact-center-survey.html)).

Insurance is the largest vertical in the market and has **3,445 services on Fiverr with zero AI voice gigs visible on page one** ([insurance-agency](https://www.fiverr.com/gigs/insurance-agency)). Automotive dealerships show **2,699 services and no AI voice gigs** ([car-dealership](https://www.fiverr.com/gigs/car-dealership)). Dental shows **807 services, all logo design** ([dental-office](https://www.fiverr.com/gigs/dental-office)).

### 2.5 TCPA as an off-platform demand signal with no on-platform supply

A search for TCPA-compliant AI calling returns a dense, recent, commercially motivated content layer built entirely by vendors: [Revmo AI's 2026 TCPA rules and checklist](https://revmo.ai/blog/tcpa-compliance-guide-ai), [Leads Now AI's plain-English guide](https://leadsnow.ai/tcpa-compliance-for-ai-voice-and-sms-agents-2026/), [Plura's TCPA consent requirements 2026](https://www.plura.ai/articles/tcpa-consent-requirements-2026), [Klariqo's operator's guide](https://klariqo.com/blog/tcpa-compliance-ai-voice-agents/), [OptInFix on AI calling laws](https://optinfix.com/blog/ai-calling-laws-tcpa-consent-requirements-2026), and a dedicated [SaaS law firm practice page on AI voice agent compliance covering TCPA, FCC and state AI law](https://www.njbusiness-attorney.com/ai-voice-agent-compliance-tcpa-fcc-state-laws/).

That much vendor content exists only where buyers are anxious and searching. **Fiverr has no TCPA landing page and no compliance-framed voice gig anywhere in the top results of `ai-cold-calling` (2,232 services).** Every single one of the top cold-calling gigs sells the calling and says nothing about consent, quiet hours, DNC, recorded-line disclosure or AI disclosure. This is the widest demand-to-supply gap found in the entire sweep.

---

## 3. DEMAND-vs-SUPPLY MATRIX

Demand is scored from the Fiverr Business Trends Index growth rate, the vertical market share data, and the off-platform content density. Supply is the live "services available" count plus a qualitative read of page-one strength. Opportunity is demand divided by defensible supply.

| Rank | Niche | Demand | Supply (live count) | Page-one strength | Verdict | Realistic price ladder |
|---|---|---|---|---|---|---|
| **1** | **Compliance-aware AI outbound calling (TCPA, DNC, quiet hours, recorded-line and AI disclosure)** | High and rising; no on-platform competitor addresses it | **2,232** on `ai-cold-calling`; **zero** compliance-framed | Very weak, $50 to $120, no differentiation | **WIN FAST.** Uncontested. | $450 / $1,200 / $2,800 |
| **2** | **AI voice agent for auto dealerships (BDC, service, sales follow-up)** | High; dealership BDC spend is real budget | **2,699** on `car-dealership`, **zero** AI voice | No competitor at all in-vertical | **WIN FAST.** Vertical language beats tool language. | $500 / $1,500 / $3,500 |
| **3** | **AI voice agent for insurance agencies (quote intake, renewals, FNOL triage)** | Highest vertical share at 32.9% of market | **3,445** on `insurance-agency`, **zero** AI voice | No competitor at all in-vertical | **WIN FAST.** Largest vertical, empty shelf. | $500 / $1,500 / $3,500 |
| **4** | **AI SDR / appointment-setting agent** | High; `ai-appointment-setter` has no landing page | **163** on `ai-sdr-agent` | Near-empty; $35 to $250 already | **WIN FAST.** Lowest supply of any live keyword. | $350 / $900 / $2,200 |
| **5** | **Sub-second-latency voice agents (measured TTFT as the product claim)** | High; latency is the top buyer objection | Not a keyword; **12,823** on `ai-voice-agent` broadly | Only one seller (Exousia) makes a latency claim | **WIN FAST.** A measured number is a moat. | $600 / $1,500 / $3,500 |
| 6 | Apollo-driven outbound pipeline build | Moderate to high; Apollo is standard tooling | **795** on `apollo-io` | Weak, $15 to $20 anchors | Strong. Thin supply, terrible anchors, easy to reprice. | $300 / $800 / $2,000 |
| 7 | LiveKit real-time voice infrastructure | Moderate; the serious-buyer signal | **195** on `livekit` | Near-empty, one Vetted Pro | Strong. Lowest supply on the platform. Low volume, high intent. | $750 / $2,000 / $5,000 |
| 8 | MCP server development | High and very new; adjacent to Claude Code +938% | **2,487** on `mcp-server` | Thin, uniform $100 anchor | Strong. New category, undifferentiated supply. | $350 / $900 / $2,500 |
| 9 | Custom Claude / OpenAI agents in Python or Node | **+938%** for Claude Code | **26,481** on `claude-code` | Crowded but chaotic, $5 to $500 | Good. High growth outruns supply; price variance means room at the top. | $400 / $1,200 / $3,000 |
| 10 | AI receptionist (inbound answering) | High; the clearest SMB buying trigger | **3,974** on `ai-receptionist` | Moderate; **best price anchors on the platform**, $80 to $225 | Good. Supply exists but has already trained buyers to pay. | $400 / $1,000 / $2,500 |
| 11 | n8n production pipelines with error handling and monitoring | **+125%**, second-fastest AI term | **37,861** on `n8n-automation` | Crowded but shallow; page one is Level 1 at $10 to $50 | Good. Volume is high, depth is not. Differentiate on production-grade. | $250 / $750 / $2,000 |
| 12 | Telephony integration (Twilio, SIP, number provisioning, call routing) | Moderate; the plumbing nobody wants to touch | **10,155** on `twilio` | Moderate; Top Rated at $300 | Fair. Defensible as an add-on, weak as a standalone hero gig. | $300 / $750 / $1,800 |
| 13 | AI-powered CRM integration (GoHighLevel, HubSpot, Salesforce) | High but generic | **78,710** on `crm-integration`, **32,734** on `gohighlevel` | Saturated, though ceiling is $995 | Fair. Use as a package inclusion, not a hero gig. | $250 / $700 / $1,800 |
| 14 | Playwright / Python scraping for lead data | Moderate | **7,100+** on data scraping | Strong and entrenched: Level 2 sellers with 548, 691 and 1,000+ reviews at $5 to $30 | **Avoid as a hero gig.** Genuinely defended, priced at the floor. | n/a |
| 15 | Generic AI chatbot | Declining relative to voice | **45,643** on `ai-chatbot` | Saturated and commoditized from $5 | **Avoid.** Fiverr's own FAQ caps a basic chatbot at $150 to $800. | n/a |

### 3.1 The five to win fastest, and why

**Rank 1, 2 and 3 all rest on the same insight.** The tool keywords (`vapi` 14,986, `retell-ai` 12,134, `ai-voice-agent` 12,823) are crowded and anchored at $5 to $100. The vertical keywords (`car-dealership` 2,699, `insurance-agency` 3,445) are one-fifth the size and contain **no AI voice supply at all**. Competing on "I will build a Vapi agent" puts you against 14,986 sellers starting at $5. Competing on "AI voice receptionist for car dealerships" puts you against effectively nobody, in front of buyers who already have a BDC budget line.

Production experience with auto dealerships and insurance is not a nice-to-have here. It is the entire moat, because the two verticals with genuine in-house experience are precisely the two verticals with zero in-vertical supply.

**Rank 4** is arithmetic. 163 services is the lowest live count in the sweep, and existing sellers already list $250 (Manzar A, "I will build an ai sdr agent for lead qualification and booking"). A niche where the thinnest supply already carries the third-highest anchor is a niche where the market has decided the price and forgotten to fill the shelf.

**Rank 5** is about credibility, not category. Exousia is the only seller found on the entire platform making a latency claim ("just under 1 second for English voice assistants"), and Exousia is Top Rated at 5.0 across 60 reviews charging **$500 for the basic package** while unbadged sellers charge $15 for the same tool stack. The correlation is not accidental. A **measured median TTFT of 0.89 seconds** stated as a number, with the measurement method described, is a claim no competitor in the sweep can match and one that Fiverr's own ranking behavior rewards.

### 3.2 What buyers actually pay, by evidence tier

Synthesizing the observed anchors and Upwork's published guidance:

- **$150 to $300:** the credible Fiverr entry point for a single-flow inbound agent. Below this you are competing with $5 gigs and signalling that you are one of them. Evidence: Retell top result at $200 ([retell-ai](https://www.fiverr.com/gigs/retell-ai)), AI receptionist top results at $225 and $300 ([ai-receptionist](https://www.fiverr.com/gigs/ai-receptionist), [ai-phone-agent](https://www.fiverr.com/gigs/ai-phone-agent)), Twilio top result at $300, AI SDR at $250.
- **$500 to $1,500:** the working mid-tier. Evidence: Exousia's basic at **$500** with 60 reviews behind it, Fiverr's own chatbot FAQ topping out at **$800**, Fiverr's Software Development category stating typical project cost **$130 to $1,500**, Ibrahim S describing his project range as **$50 to $2,500**, and Ethan Moon's reviews describing **$100 to $800** engagements.
- **$1,500 to $3,500:** achievable on Fiverr with badge or credential. Evidence: Karthik Pillai, Top Rated, **$1,800 with 2 reviews**, ranking first on `ai-agent`; Ajay Kumar, Top Rated, **$995** on `crm-integration`. Fiverr's Q2 disclosure that **$1,000+ projects grew 13% y/y** confirms this cohort is expanding while the rest contracts.
- **$3,500 and above:** exists, but on Fiverr this is Pro catalog and custom-offer territory rather than published packages. Upwork's stated **$2,400 to $24,000 for production-grade deployment** is the true market rate for the work described.

---

## 4. WHAT WINS ON FIVERR IN 2026: ALGORITHM AND CONVERSION

### 4.1 The level system and its real thresholds

Requirements per [Fiverr Tutorials' 2026 seller levels guide](https://fiverrtutorials.com/fiverr-seller-levels):

| Level | Days active | Orders / unique clients | Lifetime earnings | Rating | Response rate | Success Score | Gig slots |
|---|---|---|---|---|---|---|---|
| New Seller | 0 | 0 | $0 | n/a | n/a | n/a | 7 |
| Level 1 | 60 | 5 / 3 | $400 | 4.4+ | 80% | **5.0+** | 10 |
| Level 2 | 120 | 20 / 10 | $2,000 | 4.6+ | 90% | **7.0+** | 20 |
| Top Rated | 180 consecutive at L2 | 40 / 20 | $10,000 | 4.7+ | 90% | **9.0+** | 30 |

Level 1 and Level 2 evaluate **daily**, with advancement inside 24 hours of meeting all criteria at once. Top Rated is a **manual editorial review**. All levels carry a **30-day grace period** before demotion, except that an active Terms of Service warning puts Top Rated status at immediate risk. Level 2 unlocks custom offers up to **$10,000**, which is the practical ceiling on packaging large engagements.

Note the arithmetic that follows from our recommended pricing: at a $500 to $1,500 average order value, **Level 1's $400 lifetime-earnings bar clears on the first order** and Level 2's $2,000 bar clears on roughly the third or fourth. The binding constraints are the order counts (5 and 20) and unique-client counts (3 and 10), not the money. This argues for a deliberate mixed ladder: a low-friction entry tier that accumulates order count alongside the high-value tiers that accumulate revenue.

### 4.2 The "apply to buyer needs" motion, and its hard gate

Buyer Requests is gone. It was replaced by **Briefs**. Per Fiverr's official [Personalized offers (Briefs) for freelancers](https://help.fiverr.com/hc/en-us/articles/4415608857745-Personalized-offers-Briefs-for-freelancers):

- Clients submit project briefs, AI-assisted for clarity, from [Post a project brief](https://help.fiverr.com/hc/en-us/articles/4415601609361-Post-a-project-brief-get-tailored-offers-for-your-project).
- "An intelligent algorithm" matches briefs to freelancers by analyzing "your skills and experience" and pricing level.
- Briefs arrive on the Briefs page, by email, and via in-app notification. A freelancer can create an offer, decline, or ask a question.
- **"Each brief is available for a freelancer to answer within 72 hours."**
- Custom offers can be single payment, subscription, milestones, or hourly.
- **Eligibility: "a success score of 7 or higher."**

That last line is the most important operational fact in this report. **A brand-new seller cannot receive Briefs.** Success Score 7 is also the Level 2 threshold. The inbound-application motion is locked until roughly 20 completed orders from 10 unique clients.

The practical consequence: **for the first 10 to 20 orders there is no "apply" motion on Fiverr.** There is only search ranking, gig conversion, and off-platform traffic driven to your gig URL. Plan accordingly rather than waiting for briefs that will not arrive.

The other inbound routes:

- **Fiverr Pro** ([pro.fiverr.com](https://pro.fiverr.com/)) is not an open application in practice. Fiverr states "Our industry experts evaluate every Fiverr Pro freelancer before they are accepted and continue to hold them to the highest standards during their activity on Pro," and freelancers are described as receiving invitations from a **talent sourcing team**. Fiverr Tutorials puts the acceptance rate at **approximately 1% of applicants** and notes Pro status is independent of the standard level system, so it can be held at any level. Pro buyers get hourly and project engagements, dedicated hiring experts, a money-back guarantee, team tools with shared budgets, and compliance add-ons including background checks and NDAs.
- **Project Partner** is Fiverr's managed-project offering: dedicated project managers who "plan, coordinate, and execute your projects with a team of freelance talent." It is a buyer-side product; the seller-side benefit is being sourced into those teams, which again runs through the sourcing team rather than an application form.

### 4.3 Seller Plus

Official pricing from [Fiverr's Seller Plus help article](https://help.fiverr.com/hc/en-us/articles/360017140717-Seller-Plus-Standard-and-Premium-Advanced-tools-for-business-growth):

| Tier | Price | Eligibility |
|---|---|---|
| **Kickstart** | **$15/month** | New freelancers with no level yet ([help article](https://help.fiverr.com/hc/en-us/articles/27291415082257-Seller-Plus-Kickstart-Start-your-freelance-journey-strong)) |
| **Standard** | **$25/month** (or $128 semi-annual, $225 annual) | Level 1 and above |
| **Premium** | **$49/month** (or $250 semi-annual, $441 annual) | Level 2 and above |

Both paid tiers include advanced analytics and client insights, highlighted reviews, live walkthrough sessions, priority support, promotions and coupons, **$5/month Fiverr Ads credit**, follow-up messaging, keyword research and pricing insights. Premium adds a dedicated Customer Success Manager, early payout, request-to-order, Top Rated review priority, up to 20 coupons and 20 promotional orders monthly. Kickstart notably includes **ID verification** as a listed benefit alongside AI-generated gig feedback and a guided onboarding session, and is refundable within 48 hours of charge.

**Critical caveat: Seller Plus does not buy ranking.** [GigRankPro](https://gigrankpro.com/is-fiverr-seller-plus-worth-it/) states plainly that "Joining the paid subscription does not give you an automatic organic boost in search results" and that free and paid sellers are treated equally by the search algorithm. That source also lists $19 and $29 monthly pricing, which conflicts with the official help page; treat the Fiverr help centre figures as authoritative and the third-party figures as stale.

The genuinely valuable feature for a new seller is the keyword analytics, which show **the exact search terms buyers used to find and click your gigs**. Given the tool-versus-vertical positioning question raised in Section 3, that data resolves the question empirically within weeks. Kickstart at $15/month is worth it for that alone during the launch phase.

### 4.4 Ranking mechanics and gig construction

Synthesized from [Zenlance's 2026 Fiverr algorithm guide](https://zenlance.net/fiverr-algorithm/) and [LetsUncover's page-one guide](https://letsuncover.pk/how-to-rank-fiverr-gig-on-page-1-in-2026/):

**Title formula.** Primary Keyword + Niche Qualifier + Compelling Outcome, **under 80 characters**, with the primary keyword **in the first five words**. Note that the gig URL locks permanently at first save, so the recommended sequence is to publish with an exact-match keyword title to secure the URL slug, then edit to a reader-friendly title afterwards.

**Tags.** Fill **all five** slots with specific long-tail phrases sourced from Fiverr's own search autocomplete rather than invented terms. Tags are a secondary relevance signal that extends reach beyond the title's keyword range, so do not duplicate words already in the title.

**Conversion is the dominant signal.** Click-through rate and conversion rate are described as "one of the strongest positive signals in the Fiverr algorithm." Positions rotate dynamically: "your position can shift significantly within a single day based on real-time performance signals."

**Private feedback.** Collected invisibly from buyers after every order and fed directly into ranking, separate from the public review. A public five-star review can sit alongside negative private feedback. This is why communication quality, not just delivery quality, moves ranking.

**Response time.** "Sellers who consistently respond within one to two hours outrank sellers with slower response patterns, all else being equal," and "a response time under one hour consistently places you in a stronger ranking position than a response time of six hours or more."

**Video and images.** Gigs with video show higher conversion; optimal length **45 to 75 seconds**; thumbnail canvas is **550 x 370 pixels** and should use clean contrast, bold text overlay, and visible sample work. For a voice-agent gig the video is not optional: it is the only way to demonstrate the product, and a recorded live call with a visible latency readout is a demonstration no competitor in this sweep offers.

**Honeymoon period.** New gigs receive elevated visibility for **48 hours to several weeks** as a data-collection phase. Driving external traffic during that window to generate early orders is the single highest-leverage launch action.

**Refresh cadence.** Small updates every **45 to 60 days** signal freshness. Use Vacation Mode rather than going quiet, since genuine inactivity suppresses promotion while Vacation Mode does not.

**Timeline expectation.** "Typically takes 2 to 8 weeks to rank Fiverr gig on page 1 for a fully optimized gig in a moderately competitive niche."

### 4.5 Verification and what gets AI gigs denied

**Gig denial reasons**, quoted from [Policy Violations Explained](https://help.fiverr.com/hc/en-us/articles/48022851354385-Policy-Violations-Explained):

- "Your Gig description, title, or packages were found to be unclear or misleading."
- "we do not allow the inclusion of external payment methods and personal contact details in Gigs, such as email addresses, phone numbers, or alternative payment systems."
- Selling "a product instead of a service, as it is not customized for each client."
- "Your Gig description, or parts of it, might be copied from another Fiverr freelancer."

Account warnings additionally cover "taking business off-platform", "misrepresenting your Gig service" including "misleading clients regarding the price or scope of your service", and "repeatedly offering prohibited services."

Two of these are live risks for exactly the kind of gig we would publish. **Listing a demo phone number in the gig description is a denial trigger** under the personal-contact-details rule, so a live demo line must be delivered inside the order or via the gig video, never as a number printed in the description. And **selling a pre-built agent template rather than a per-client build risks the "product instead of a service" denial**, which argues for describing the offer as a per-client configured build rather than a productized clone.

**Prohibited services** most relevant to us, quoted from [Prohibited services on Fiverr](https://help.fiverr.com/hc/en-us/articles/49174165608593-Prohibited-services-on-Fiverr):

- "Sharing personal data of individuals, such as email addresses, phone numbers, or similar contact details"
- "Scraping social media platforms to obtain information about others"
- "Using personal data to support identity misuse, impersonation, phishing, scams, spam, or other deceptive outreach"
- "Using AI to impersonate real individuals or falsely represent identity, affiliation, or endorsement"

**Two hard consequences follow.** First, **selling scraped lead lists is prohibited**, and social-media scraping is named explicitly. A lead-gen offer must be framed as building the client's own pipeline infrastructure operating on the client's own data and licensed sources, not as delivering contact data. Second, **voice cloning of a real person is prohibited without authorization**. Fiverr's [AI guidelines](https://help.fiverr.com/hc/en-us/articles/34998793899665-Using-AI-on-Fiverr-Guidelines-for-freelancers-and-clients) forbid "unauthorized use of voice or likeness" and "deceptive synthetic and manipulated media (Deepfakes)". Any gig offering to clone a named human's voice for a client's agent needs that human's documented consent, and Fiverr's stated consequences for trust breaches run to "permanent suspension".

**On AI disclosure**, Fiverr's position is narrower than commonly assumed. Freelancers must "honor a client's explicit request for non-AI work" and disclose their intended workflow when a client states that preference before or at order start. Work must be "high-quality, original, and meaningfully refined and customized to the client's specific requirements", and "generic, unmodified, or reused AI output" is prohibited. There is **no requirement to proactively disclose AI use in a gig listing**; the analysis at [Memvers on AI disclosure rules](https://memvers.com/blog/ai-disclosure-rules-freelance-platforms-2026) confirms disclosure is conditional rather than upfront, and notes Fiverr's own line that "Freelancers do not necessarily disclose all the tools they use in their Gigs". Enforcement turns on quality and honesty, not on tooling.

**Verification.** ID verification appears as a listed benefit of the $15/month Kickstart tier, which indicates it is available on request and is a credibility marker rather than a universal gate at signup. Fiverr's dedicated verification help article was not reachable at the time of research (404), so this point is stated from the Kickstart article and should be re-verified at signup.

---

## 5. COMPETITOR TEARDOWN

Eight gigs across the target niches, titles quoted exactly as published.

### 5.1 "I will make an ai voice agent using vapi, retell, synthflow"
[fiverr.com/joashnaicker/make-an-ai-voice-caller-using-air-bland-vapi](https://www.fiverr.com/joashnaicker/make-an-ai-voice-caller-using-air-bland-vapi)

Seller Exousia (joashnaicker). **Top Rated. 5.0 stars across 60 reviews. Basic $500, 6-day delivery, 1 revision**, including "Data Syncing, Conditional Logic, AI model integration". Standard adds simple external-platform integrations; Premium adds complex integrations such as "booking multiple appointment types to multiple calendars".

The description claims "cutting-edge AI voice agents that integrate seamlessly with your existing systems" and, uniquely in this entire sweep, a performance number: **"just under 1 second for English voice assistants."** Multilingual work is cited with named examples (Romanian, French). The capability list is the category standard: calendar booking, CRM integration (GoHighLevel, ActiveCampaign), automated email and SMS, FAQ knowledge base, lead capture, human transfer. Stack claimed: Retell AI, Vapi AI, LangChain, Make.com, Zapier, OpenAI, Google Gemini. The FAQ notably addresses **cold-calling legality**, which is the only compliance touch found on any gig in the sweep, and it is a single FAQ line rather than a positioning.

**This is the benchmark to beat.** It is the highest-credibility voice gig found: Top Rated badge, 60 reviews, $500 entry, and the only latency claim on the platform. It is beatable on exactly two axes: the latency number is vague ("just under 1 second") where ours is measured (median 0.89s), and compliance is an afterthought where ours would be the product.

### 5.2 "I will make an ai voice agent ai receptionist using vapi or retell"
[fiverr.com/ethxn787/make-an-ai-voice-agent-using-vapi-or-synthflow](https://www.fiverr.com/ethxn787/make-an-ai-voice-agent-using-vapi-or-synthflow)

Ethan Moon. **Level 2. 5.0 across 23 reviews. Basic $90, 3-day delivery, 3 revisions.** Promises include "Automatically sending emails and SMS to your leads and customers", calendar booking, GoHighLevel CRM integration, FAQ knowledge bases, lead extraction and storage, multilingual support, live transfer.

The genuinely instructive element is the portfolio structure: completed projects are listed **by vertical** as medical clinic receptionists, real estate lead qualification, restaurant reservation systems, cold-calling automation, and customer support. Reviews indicate real engagements ran **$100 to $800** despite the $90 published entry. The published price is a door, not a rate.

### 5.3 "I will build ai voice agent, retell ai receptionist, vapi ai calling agent n8n ai agent"
[fiverr.com/saleem951/develop-custom-ai-agents-using-openai-agentkit-and-n8n-ai-agent-automation](https://www.fiverr.com/saleem951/develop-custom-ai-agents-using-openai-agentkit-and-n8n-ai-agent-automation)

saleem951 (ecom automation). **Level 2. 5.0 across 14 reviews. Basic $80, 5-day delivery**, scoped as "1 Inbound or outbound AI voice agent to handle incoming or outgoing call with data capture + storage".

A textbook keyword-stuffed title: four separate high-volume search terms crammed into one string. It works for search and reads badly to a buyer. The FAQ covers platform selection guidance, customization, CRM integration, language support, conversation quality, post-delivery updates and support availability, which is the standard seven-question set across this niche.

### 5.4 "I will build ai voice agent, ai calling agent, ai receptionist for cold calling"
[fiverr.com/nexcore23/build-ai-voice-agent-cold-calling-bot-vapi-retell-n8n-ai-automation-for-business](https://www.fiverr.com/nexcore23/build-ai-voice-agent-cold-calling-bot-vapi-retell-n8n-ai-automation-for-business)

Nexcore23. **Level 1. 5.0 across 10 reviews. Basic $50, 2-day delivery**, including AI LLM integration, RAG, conversation flow, 1 CRM integration, authentication, multi-language support, **and source code**.

The hook is the best copywriting found in the sweep: **"Every unanswered call is a lead your competitor picks up."** Targets real estate, SaaS, agencies, medical, dental and home services. Source-code delivery at $50 is a notable giveaway that suppresses the price ceiling for everyone in the niche.

### 5.5 "I will build n8n lead capture, CRM and ai follow up automation"
[fiverr.com/imalick/build-ai-automation-and-custom-workflows-with-n8n-and-llms](https://www.fiverr.com/imalick/build-ai-automation-and-custom-workflows-with-n8n-and-llms)

Ibrahim S (imalick). **Level 2 and Fiverr Pro vetted. 4.9 across 4 reviews. Basic $90, 2-day delivery, 1 revision**, scoped precisely as "1 API integrated, 1 Trigger/Action, 2 platforms automated, data syncing, conditional logic, AI model integration".

This is the most professionally constructed gig in the sweep and the closest model for how to sell seniority. Credentials are stated explicitly: **"30+ years in IT, cloud, automation, CRM, and systems integration"** plus AWS Certified Solutions Architect and Pro vetting. Stack: n8n with HubSpot, Salesforce, Bitrix24, GoHighLevel, plus OpenAI, Claude and Gemini. He requires a pre-order message to confirm feasibility, API access, scope, timeline and package fit, which is a qualification gate that protects delivery quality and, by extension, the private-feedback score. Reviews describe projects from **$50 to $2,500**, and praise documentation practices.

Four reviews and Level 2 with a Pro badge, ranking on a 37,861-service keyword. Credentials substitute for volume.

### 5.6 "I will build ai automation workflows using make, zapier and ai"
Hamza Irshad. **Level 2. 4.9 across 742 reviews. From $40.** Ranked seventh on the [Automations & Agents leaf](https://fiverr.com/categories/programming-tech/ai-coding/ai-agents-development).

The review-volume leader in the automation niche and the clearest illustration of the trap: 742 reviews at a $40 entry price is an enormous amount of accumulated delivery for a modest revenue base. Volume built on a low anchor is very hard to reprice later. Do not replicate this ladder.

### 5.7 "I will setup twilio sms broadcast service"
Mubashir Saleem. **Top Rated. 5.0 across 7 reviews. From $300.** Ranked first on [twilio](https://www.fiverr.com/gigs/twilio). The same seller appears on the [Chatbot Development](https://www.fiverr.com/categories/programming-tech/chatbot-development) leaf with a separate Twilio SMS and voice gig at from $45 across 721 reviews.

The instructive contrast is internal to one seller: **721 reviews at $45 on the chatbot gig, 7 reviews at $300 on the Twilio gig, and the $300 gig holds the number-one slot on a 10,155-service keyword.** Seven reviews. This is the strongest single piece of evidence that on these keywords Fiverr ranks badge plus specificity above review volume.

### 5.8 "I will build an ai agent" and "I will build an ai sdr agent for lead qualification and booking"

Karthik Pillai. **Top Rated. 4.8 across 2 reviews. From $1,800.** Ranked **first** on [ai-agent](https://www.fiverr.com/gigs/ai-agent), a 44,698-service keyword. Offers video consultations.

Manzar A. **From $250.** Ranked first on [ai-sdr-agent](https://www.fiverr.com/gigs/ai-sdr-agent), 163 services.

Two reviews, $1,800, first place on the largest AI keyword on the platform. Read alongside 5.7, the conclusion is unambiguous: **in the AI agent and voice surfaces, price and credential outrank review count.** The conventional Fiverr wisdom of starting at $5 to farm reviews is not merely suboptimal in this category, it is actively counterproductive, because a low anchor is the signal that keeps you off the front page.

### 5.9 Cross-cutting patterns

**Every gig in the sweep promises the same seven capabilities:** calendar booking, CRM integration (GoHighLevel almost universally), email and SMS automation, FAQ knowledge base, lead capture, multilingual support, live human transfer. There is no feature differentiation available in this market.

**Almost nobody makes a measurable claim.** One latency claim across the entire sweep, and it is imprecise.

**Almost nobody sells compliance.** One FAQ line about cold-calling legality across the entire sweep.

**Almost nobody sells a vertical.** Verticals appear as portfolio lists after the sale, never as the gig's positioning.

Those three absences are the whole opportunity.

---

## 6. RECOMMENDED POSITIONING

### 6.1 The profile angle

Position as **a production voice-infrastructure engineer who ships compliance-aware phone agents for regulated, high-ticket verticals, not as a Vapi or Retell configurator.** The entire competitive set sells tool names at $10 to $90 and promises an identical seven-item feature list; the market has no way to tell any of them apart, which is why prices have collapsed to the floor even as Fiverr's own data shows AI voice agent searches up 49% and $1,000+ projects up 13%. Three assets we hold and nobody in the sweep holds are: a **measured median TTFT of 0.89 seconds against a 1.6 to 1.9 second industry baseline**, stated as a number with the measurement method described; **compliance built into the call flow in code** rather than mentioned in an FAQ, covering recorded-line and AI disclosure as fixed first-utterance text, plus DNC, quiet hours and consent gating; and **genuine production deployments in auto dealerships and insurance**, which are respectively a 2,699-service and 3,445-service Fiverr surface containing zero AI voice supply, while insurance is simultaneously the largest vertical in the AI voice market at 32.9% share. The profile headline should lead with the vertical and the number, never the vendor: buyers searching "vapi" are shopping on price against 14,986 sellers, buyers searching "AI receptionist for insurance agency" are shopping on outcome against nobody. Price from $450 upward from day one, because the evidence is overwhelming that Fiverr ranks credential and price above review count in this category, and a low opening anchor is a trap that Hamza Irshad's 742 reviews at $40 illustrate perfectly.

### 6.2 The three gigs to launch first

**GIG 1: The wedge. Highest opportunity, zero direct competition.**

- **Title:** `AI Voice Receptionist For Car Dealerships And Insurance Agencies` (62 characters, primary keyword in first four words, under the 80-character limit)
- **Category:** Programming & Tech > Software Development > **Automations & Workflows** (the `ai-coding/ai-agents-development` leaf), service type **AI Agents**
- **Tags (5):** `ai voice agent`, `ai receptionist`, `vapi ai`, `retell ai`, `ai phone agent`
- **Packages:**
  - **Starter $450**, 5 days, 2 revisions: one inbound agent, single call flow, your existing number ported or a new one provisioned, recorded-line and AI disclosure compliance block, calendar booking, one CRM write, call transcripts to your CRM.
  - **Professional $1,200**, 10 days, 3 revisions: everything in Starter, plus after-hours and overflow routing, multi-intent flows (sales, service, parts, or quote, renewal, claim), warm human transfer with context, SMS follow-up, measured latency report on your live number.
  - **Production $2,800**, 21 days, unlimited revisions within scope: everything above, plus outbound campaign capability with consent and DNC gating, full call analytics dashboard, per-call cost telemetry, 30 days of post-launch tuning.
- **Why:** 2,699 and 3,445 services in these verticals with zero AI voice supply, against 12,823 on the tool keyword. The tags still catch the tool traffic while the title owns the vertical.

**GIG 2: The differentiator. Sells the thing nobody else sells.**

- **Title:** `TCPA Compliant AI Cold Calling Agent With Consent And DNC Gating` (63 characters)
- **Category:** Programming & Tech > Software Development > **Automations & Workflows**, service type **AI Agents**
- **Tags (5):** `ai cold calling`, `ai sdr agent`, `ai calling agent`, `outbound ai agent`, `ai appointment setter`
- **Packages:**
  - **Audit $350**, 3 days: review of your existing calling setup against TCPA, FCC AI-disclosure and state rules, written remediation plan, consent-language and disclosure scripts.
  - **Compliant Outbound $1,200**, 12 days: outbound agent with consent verification, DNC scrubbing, quiet-hours enforcement and disclosure blocks enforced in code rather than in the prompt, CRM write-back, call recording and retention policy.
  - **Full Pipeline $2,800**, 21 days: everything above, plus lead-source integration into your own CRM, qualification scoring, appointment booking, campaign analytics, 30 days of tuning.
- **Why:** `ai-cold-calling` has 2,232 services and not one of the top results mentions consent, DNC, quiet hours or disclosure, while an entire vendor content industry exists off-platform because buyers are anxious about exactly this. `ai-sdr-agent` at 163 services is the thinnest live keyword found and already anchors at $250. Fiverr has no TCPA landing page, so this gig would be first into the category if one is ever created. Note the compliance framing: sell risk reduction on the client's own outreach, never lead data, which would collide with the prohibited-services rule on sharing personal data.

**GIG 3: The volume engine. Rides the fastest-growing search term.**

- **Title:** `Build Production n8n AI Agent Workflows With Error Handling` (58 characters)
- **Category:** Programming & Tech > Software Development > **Automations & Workflows**, service type **N8n Automation**
- **Tags (5):** `n8n automation`, `n8n ai agent`, `ai automation`, `mcp server`, `api integration`
- **Packages:**
  - **Workflow $250**, 4 days, 2 revisions: one production n8n workflow, up to 3 integrations, error handling, retry logic, failure alerting, documentation.
  - **Agent System $750**, 8 days, 3 revisions: multi-step AI agent with tool calling, custom MCP server if needed, up to 6 integrations, Supabase or Postgres persistence, monitoring dashboard.
  - **Pipeline $2,000**, 15 days: full lead or ops pipeline, Apollo or equivalent source integration, enrichment, scoring, CRM sync, cost telemetry per run, 30 days of support.
- **Why:** n8n AI automation grew **+125%**, the second-fastest AI term Fiverr published, and Fiverr named n8n while naming neither Make nor Zapier. The `mcp-server` tag reaches a 2,487-service keyword with a uniform $100 anchor and no differentiation, and it is adjacent to the **+938%** Claude Code surge. This gig also carries the lowest entry price of the three, which is deliberate: it accumulates the order count and unique-client count that gate Level 1 (5 orders, 3 clients) and Level 2 (20 orders, 10 clients), while Gigs 1 and 2 carry the revenue.

### 6.3 The apply motion, stated plainly

**For the first 10 to 20 orders there is effectively no inbound application channel on Fiverr, and any plan that assumes otherwise will stall.** Briefs, the replacement for Buyer Requests, require a **Success Score of 7 or higher**, which is the same threshold as Level 2, itself gated at 20 completed orders from 10 unique clients. Fiverr Pro is invitation-driven through a talent sourcing team with an acceptance rate around 1%, not an open application. Project Partner is a buyer-side managed-team product that sources through the same route.

What actually works in phase one, in priority order:

1. **Search ranking and gig conversion.** This is the only channel available. It means the title formula, all five tags drawn from Fiverr's own autocomplete, a 45 to 75 second gig video showing a real call with a visible latency readout, and a 550 x 370 thumbnail.
2. **External traffic during the honeymoon window.** New gigs get elevated visibility for 48 hours to several weeks, and orders landed in that window compound into permanent ranking. This is the highest-leverage single action at launch and it is entirely within our control.
3. **Sub-one-hour response time**, which is an explicit ranking input and costs nothing.
4. **Seller Plus Kickstart at $15/month** for the keyword analytics that reveal the exact buyer search terms hitting our gigs. That data settles the tool-keyword versus vertical-keyword question empirically inside a few weeks and is worth far more than its cost. Do not expect a ranking boost from it; Seller Plus confers none.
5. **Level 2 as the explicit phase-one objective**, because it unlocks Briefs, custom offers up to $10,000, 20 gig slots and Seller Plus Premium. At a $450 to $1,200 average order value the $2,000 earnings bar clears on the third or fourth order, so the binding constraints are the 20 orders and 10 unique clients. Gig 3's $250 tier exists to clear those counters.

Two compliance guardrails to build in from the first draft, both of which are denial or suspension risks rather than style preferences. Never print a demo phone number in a gig description, because personal contact details in gigs are an explicit denial trigger; deliver the demo line inside the order or show it in the gig video. And never describe the offer as a pre-built template being resold, because "selling a product instead of a service, as it is not customized for each client" is a named denial reason; describe every package as a per-client configured build.

---

## SOURCES

**Fiverr taxonomy and live supply counts** (all read 10 September 2026)
- [Programming & Tech](https://www.fiverr.com/categories/programming-tech)
- [AI Development / ai-coding](https://www.fiverr.com/categories/programming-tech/ai-coding)
- [Automations & Agents leaf](https://fiverr.com/categories/programming-tech/ai-coding/ai-agents-development)
- [Chatbot Development](https://www.fiverr.com/categories/programming-tech/chatbot-development)
- [AI Services vertical](https://www.fiverr.com/categories/ai-services)
- Keyword landing pages: [ai-integration](https://www.fiverr.com/gigs/ai-integration) · [ai-automation](https://www.fiverr.com/gigs/ai-automation) · [crm-integration](https://www.fiverr.com/gigs/crm-integration) · [conversational-ai](https://www.fiverr.com/gigs/conversational-ai) · [voice-ai](https://www.fiverr.com/gigs/voice-ai) · [ai-chatbot](https://www.fiverr.com/gigs/ai-chatbot) · [ai-agent](https://www.fiverr.com/gigs/ai-agent) · [ai-lead-generation](https://www.fiverr.com/gigs/ai-lead-generation) · [n8n-automation](https://www.fiverr.com/gigs/n8n-automation) · [zapier-automation](https://www.fiverr.com/gigs/zapier-automation) · [gohighlevel](https://www.fiverr.com/gigs/gohighlevel) · [ai-consulting](https://www.fiverr.com/gigs/ai-consulting) · [claude-code](https://www.fiverr.com/gigs/claude-code) · [supabase](https://www.fiverr.com/gigs/supabase) · [ai-agent-development](https://www.fiverr.com/gigs/ai-agent-development) · [vapi](https://www.fiverr.com/gigs/vapi) · [ai-voice-agent](https://www.fiverr.com/gigs/ai-voice-agent) · [retell-ai](https://www.fiverr.com/gigs/retell-ai) · [make-com-automation](https://www.fiverr.com/gigs/make-com-automation) · [ai-calling-agent](https://www.fiverr.com/gigs/ai-calling-agent) · [twilio](https://www.fiverr.com/gigs/twilio) · [ai-receptionist](https://www.fiverr.com/gigs/ai-receptionist) · [elevenlabs](https://www.fiverr.com/gigs/elevenlabs) · [insurance-agency](https://www.fiverr.com/gigs/insurance-agency) · [n8n-ai-receptionist](https://www.fiverr.com/gigs/n8n-ai-receptionist) · [car-dealership](https://www.fiverr.com/gigs/car-dealership) · [mcp-server](https://www.fiverr.com/gigs/mcp-server) · [ai-phone-agent](https://www.fiverr.com/gigs/ai-phone-agent) · [ai-cold-calling](https://www.fiverr.com/gigs/ai-cold-calling) · [dental-office](https://www.fiverr.com/gigs/dental-office) · [apollo-io](https://www.fiverr.com/gigs/apollo-io) · [livekit](https://www.fiverr.com/gigs/livekit) · [ai-sdr-agent](https://www.fiverr.com/gigs/ai-sdr-agent) · [web-scraping](https://www.fiverr.com/gigs/web-scraping)

**Demand data**
- [Fiverr Business Trends Index, June 2026](https://www.fiverr.com/resources/guides/reports/business-trends-index-june-2026)
- [Fiverr: Claude Code demand surges 938%](https://www.fiverr.com/news/business-trends-index-ai-2026) · [StockTitan coverage](https://www.stocktitan.net/news/FVRR/businesses-race-to-hire-claude-code-specialists-as-demand-surges-6x7lep85s2n8.html)
- [Fiverr Q2 2026 results](https://www.fiverr.com/news/fiverr-q2-2026-earnings) · [Staffing Industry Analysts](https://www.staffingindustry.com/news/global-daily-news/fiverr-q2-revenue-slips-10-amid-ai-led-market-shift) · [TipRanks](https://www.tipranks.com/news/company-announcements/fiverr-cuts-2026-outlook-as-ai-pushes-marketplace-upmarket)
- [Upwork: hire AI voice agent developers](https://www.upwork.com/hire/ai-voice-agent-developers/) · [Upwork In-Demand Skills 2026](https://www.barchart.com/story/news/21201/upworks-in-demand-skills-2026-demand-for-top-ai-skills-more-than-doubles-as-ai-is-embedded-into-everyday-work)
- [Memvers: AI agents as a hiring category, Upwork and Fiverr data 2026](https://memvers.com/blog/upwork-fiverr-ai-agents-marketplace-shift-2026)
- [CloudTalk AI voice agent statistics](https://www.cloudtalk.io/blog/ai-voice-agent-statistics/) · [Grand View Research AI voice agents market](https://www.grandviewresearch.com/industry-analysis/ai-voice-agents-market-report) · [McKinsey State of AI 2025](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai) · [Deloitte Digital 2024 Contact Center Survey](https://www.deloittedigital.com/us/en/insights/perspective/2024-contact-center-survey.html)

**TCPA and compliance**
- [Revmo AI TCPA compliance for AI calls 2026](https://revmo.ai/blog/tcpa-compliance-guide-ai) · [Leads Now AI](https://leadsnow.ai/tcpa-compliance-for-ai-voice-and-sms-agents-2026/) · [Plura TCPA consent requirements 2026](https://www.plura.ai/articles/tcpa-consent-requirements-2026) · [Klariqo operator's guide](https://klariqo.com/blog/tcpa-compliance-ai-voice-agents/) · [OptInFix AI calling laws](https://optinfix.com/blog/ai-calling-laws-tcpa-consent-requirements-2026) · [Bosin LLC on TCPA, FCC and state AI law](https://www.njbusiness-attorney.com/ai-voice-agent-compliance-tcpa-fcc-state-laws/)

**Seller mechanics and policy**
- [Personalized offers (Briefs) for freelancers](https://help.fiverr.com/hc/en-us/articles/4415608857745-Personalized-offers-Briefs-for-freelancers) · [Post a project brief](https://help.fiverr.com/hc/en-us/articles/4415601609361-Post-a-project-brief-get-tailored-offers-for-your-project)
- [Seller Plus Standard and Premium](https://help.fiverr.com/hc/en-us/articles/360017140717-Seller-Plus-Standard-and-Premium-Advanced-tools-for-business-growth) · [Seller Plus Kickstart](https://help.fiverr.com/hc/en-us/articles/27291415082257-Seller-Plus-Kickstart-Start-your-freelance-journey-strong) · [GigRankPro on Seller Plus](https://gigrankpro.com/is-fiverr-seller-plus-worth-it/)
- [Fiverr Pro](https://pro.fiverr.com/) · [Fiverr Tutorials seller levels 2026](https://fiverrtutorials.com/fiverr-seller-levels)
- [Prohibited services on Fiverr](https://help.fiverr.com/hc/en-us/articles/49174165608593-Prohibited-services-on-Fiverr) · [Policy Violations Explained](https://help.fiverr.com/hc/en-us/articles/48022851354385-Policy-Violations-Explained) · [Using AI on Fiverr](https://help.fiverr.com/hc/en-us/articles/34998793899665-Using-AI-on-Fiverr-Guidelines-for-freelancers-and-clients) · [Memvers on AI disclosure rules 2026](https://memvers.com/blog/ai-disclosure-rules-freelance-platforms-2026)
- [Zenlance Fiverr algorithm 2026](https://zenlance.net/fiverr-algorithm/) · [LetsUncover rank on page 1 in 2026](https://letsuncover.pk/how-to-rank-fiverr-gig-on-page-1-in-2026/)

**Competitor gigs**
- [Exousia](https://www.fiverr.com/joashnaicker/make-an-ai-voice-caller-using-air-bland-vapi) · [Ethan Moon](https://www.fiverr.com/ethxn787/make-an-ai-voice-agent-using-vapi-or-synthflow) · [saleem951](https://www.fiverr.com/saleem951/develop-custom-ai-agents-using-openai-agentkit-and-n8n-ai-agent-automation) · [Nexcore23](https://www.fiverr.com/nexcore23/build-ai-voice-agent-cold-calling-bot-vapi-retell-n8n-ai-automation-for-business) · [Ibrahim S](https://www.fiverr.com/imalick/build-ai-automation-and-custom-workflows-with-n8n-and-llms)

**Research limitation:** Fiverr's `/search/gigs` endpoint is disallowed by robots.txt, so per-keyword seller-badge distributions could not be counted exhaustively. Badge observations are drawn from the page-one results visible on category leaves and `/gigs/` landing pages. Seller-level thresholds in section 4.1 come from a third-party guide because Fiverr's own level-system help article returned 404 at the time of research, and should be re-verified in the seller dashboard at signup. Seller Plus pricing is cited from Fiverr's official help centre where a third-party source disagreed.
