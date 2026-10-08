# Ad creative briefs

Six creatives. Every one reuses an existing rendered gig image and an end-card line that already survived the verification gate, so no new claim enters the world through an ad.

**Why reuse rather than design new.** The nine gig images at `research/gig-images/gig1-a.png` through `gig3-c.png` already carry the brand palette (ink `#06070C`, cyan `#62E9FF` for measurement, violet `#8C6BFF` for law, mint `#3DF5B6` for verified) and, critically, they already carry each figure's source and read-date on the same frame. That last property is not decoration. It is what makes a number on an ad defensible, and it is why a new creative made from scratch is a liability rather than a refresh.

---

## Rules that apply to all six

| Rule | Reason |
|---|---|
| **No phone number, no email, no external contact detail**, printed or spoken, in the ad or in the gig it lands on | Personal contact details in a gig are an explicit denial trigger. The demo line is delivered inside the order or shown in the gig video |
| **No em dashes**, in headline, body, caption, or text baked into an image | The ship gate. Run the dash scan against SVG labels and template strings too |
| **PII-masked dashboard views only** | The public dashboard already reads masked views. Screenshot the masked view by default |
| **No client, dealership or agency named**, ever | Anonymise to industry plus size plus region |
| **Every printed figure carries its measurement basis and the date** | A target is never quoted as a result |
| **Never present a demo metric as a production metric** | Answer rate, booking rate and calls-at-scale are not measured. Latency is |
| **Label AI-generated media where platform policy requires** | And never a misleading synthetic visual or a deepfake |
| **Compliance is engineering, not legal advice** | Never imply US bar admission. Never imply insurance licensure |
| No hype, no superlatives, no emoji, no exclamation marks | House voice. Confident engineer-lawyer |
| Landing URL is the gig URL | The only landing page whose conversion the ledger can measure, and the only one where an order is also a permanent ranking deposit |

`LANDING_URL_GIG1`, `LANDING_URL_GIG2` and `LANDING_URL_GIG3` are placeholders. Gig 1's slug is locked at `build-ai-voice-receptionist-for-car-dealerships-and-insurance-agencies`. Gig 2's and Gig 3's slugs lock on first save and are still `TODO` in `accounts.json`. **Do not launch a campaign against a placeholder URL.**

---

## Brief 1: "761 ms to first word"

| | |
|---|---|
| **Creative** | `research/gig-images/gig1-a.png`. End-card line already on the frame: **761 ms to first word**, sub-line "Measured on simulated calls, 26 August 2026." |
| **Headline** | Your phone agent answers in 761 ms |
| **Primary text** | Most vendor phone agents take 1.6 to 1.9 seconds to say their first word. That pause is where callers decide you are a machine. We measured a median 761 ms to first audio on simulated calls on 26 August 2026, against a prior vendor's production p50 of 1.64 to 1.9 seconds across 17 archived calls. Same stack, rebuilt. The recorded-line and AI disclosure is fixed text outside the model, so it fires first on every call and cannot drift. |
| **CTA** | Learn more |
| **Audience** | US car dealership decision makers: dealer principals, general managers, BDC managers, fixed operations directors. Franchise and independent rooftops |
| **Channel** | `meta-dealers-us`, and the headline carries over to `gads-search-intent` text ads |
| **Landing** | `LANDING_URL_GIG1` |
| **Note** | The strongest asset we hold, because it is the one number nobody else on either platform publishes with a method |

---

## Brief 2: "Consent checked before the dial"

| | |
|---|---|
| **Creative** | `research/gig-images/gig2-a.png`. End-card line: **Consent checked before the dial**, sub-line "DNC, quiet hours and allowlist gated in code." |
| **Headline** | Four gates run before the dial |
| **Primary text** | Everyone selling AI calling sells you the dialing. The expensive half happens before the dial, and it is the half that gets audited. Consent basis on file, Do-Not-Call clear, quiet hours checked in the callee's own time zone, allowlist pass. Four gates, enforced in code, with a refusal path that blocks rather than warns. Written from TCPA, 47 CFR 64.1200, CIPA and California AB 2905, read from the statutes. Engineering, not legal advice: your counsel signs off on the language, the system enforces it. |
| **CTA** | Learn more |
| **Audience** | US independent insurance agency owners and principals, agency operations managers |
| **Channel** | `meta-agencies-us`, headline carries to `gads-tcpa` |
| **Landing** | `LANDING_URL_GIG2` |
| **Note** | The widest demand-to-supply gap in the whole research pack. 2,232 competing Fiverr services on ai-cold-calling and not one top result mentions consent |

---

## Brief 3: "Built for dealerships and agencies"

| | |
|---|---|
| **Creative** | `research/gig-images/gig1-c.png`. End-card line: **Built for dealerships and agencies**, sub-line "BDC, service drive, quote intake, renewals." |
| **Headline** | An AI receptionist that knows what a BDC is |
| **Primary text** | A general-purpose voice bot has to be told what a service drive is, what a quote intake looks like, and why a renewal call is not a sales call. This one is built for those two businesses and nothing else. Sales, service and parts on the inbound side. Quote, renewal and first notice of loss on the agency side. Booking, warm transfer with context, and a structured write into the CRM you already run. One direction-aware agent on your existing number, not the two-agent split most vendors force on you. |
| **CTA** | Learn more |
| **Audience** | Split test: dealership job titles against insurance agency job titles, same creative, so the vertical response difference is readable |
| **Channel** | `meta-dealers-us` and `meta-agencies-us`, plus `gads-search-intent` |
| **Landing** | `LANDING_URL_GIG1` |
| **Note** | This is the vertical-first rule as an ad. The Fiverr `car-dealership` keyword carries 2,699 services and zero AI voice supply |

---

## Brief 4: "Written from the statutes"

| | |
|---|---|
| **Creative** | `research/gig-images/gig2-c.png`. End-card line: **Written from the statutes**, sub-line "TCPA, 47 CFR 64.1200, CIPA, AB 2905." |
| **Headline** | The person who wrote your calling gates read the statutes |
| **Primary text** | Most AI calling vendors put compliance in an FAQ. Some put it in the prompt, where the model can talk itself past it. I trained as a lawyer before I built this, and the gates are code: consent, Do-Not-Call, quiet hours in the callee's time zone, allowlist, plus disclosure as fixed first-utterance text that is identical on call one and call ten thousand. Every call carries an audit trail of consent state and disclosure delivery. Engineering, not legal advice. Your counsel signs off on the language. |
| **CTA** | Get a free audit |
| **Audience** | LinkedIn: US insurance agency principals and owners, dealership general managers and BDC directors. Job title and seniority targeting, US only. Frankie's profile and face |
| **Channel** | `li-insurance-us` |
| **Landing** | LinkedIn Lead Gen Form routed to the Compliance-Safe AI Audit. Fulfilment stays on the platform the conversation started on |
| **Note** | Frankie's producer licence is stated as his own credential with the boundary explicit. Oraya is not a licensed entity |

---

## Brief 5: "The calls nobody picks up"

| | |
|---|---|
| **Creative** | `research/gig-images/gig1-b.png`, or the missed-call reel `r1_missedcall_ig.mp4` where video is supported. End-card line on the still: **Compliance spoken first, every call** |
| **Headline** | The expensive calls are the daytime ones |
| **Primary text** | After-hours calls are the ones everybody worries about. The expensive ones ring six times at 2pm while your advisor is with a customer. Those callers do not leave a voicemail. They call the next dealer, and you never find out it happened. An agent that picks up on every one of them, books what it can, transfers what it cannot, and writes the call into your CRM, answers in a measured median 761 ms, measured on simulated calls on 26 August 2026. |
| **CTA** | Learn more |
| **Audience** | Retargeting: gig visitors and dashboard-demo viewers, plus a lookalike built from audit leads |
| **Channel** | `meta-dealers-us-retarget` |
| **Landing** | `LANDING_URL_GIG1` |
| **Note** | Do not launch until the source audience exceeds 300 people. Below that the spend buys frequency against a handful of people |

---

## Brief 6: "It tells you when it breaks"

| | |
|---|---|
| **Creative** | `research/gig-images/gig3-b.png`. End-card line: **It tells you when it breaks**, sub-line "Dead-letter path and alerting on every call." |
| **Headline** | A workflow that tells you when it breaks |
| **Primary text** | Most n8n builds work on the demo canvas and fail silently in week three. This one ships with retries, a dead-letter path, alerting on every failed call, and a runbook that says what to do when each one fires. Idempotent by default, so a replay never double-writes your CRM. Up to six integrations, Supabase or Postgres persistence, and a monitoring dashboard you can actually read. Built by someone whose day job is production voice infrastructure, where a silent failure is a dropped phone call. |
| **CTA** | Learn more |
| **Audience** | Operations and RevOps leads at small US B2B companies already running n8n, Make or Zapier. Interest and tool targeting |
| **Channel** | `meta-dealers-us` as a secondary ad set, or a `gads` ad group once the first two prove out |
| **Landing** | `LANDING_URL_GIG3` |
| **Note** | Lowest-priority of the six. Gig 3 is the order counter, not the revenue engine, and paid traffic to a $250 tier has thin ROI headroom. Run it only after briefs 1 and 2 have a measured cost per message |

---

## Testing discipline

One variable at a time, always. The measurement contract in `ads/ads-plan.md` section 6 gate G6 is not advice, it is a gate.

| Week | Test | Held constant |
|---|---|---|
| 1 | Brief 1 against Brief 3, dealership audience | Audience, budget, landing URL |
| 2 | Winner of week 1 against Brief 2, split by vertical audience | Creative pair, budget |
| 3 | Winning creative, budget doubled, nothing else changed | Creative, audience, landing URL |
| 4 | Brief 4 on LinkedIn, two-week review window because CTR is 0.44% to 0.65% and one week is not enough signal | Everything else frozen |

Every creative launch, pause and change gets a ledger event against its campaign id:

```bash
python3 hub.py log --platform meta --account TODO --entity ad \
  --ref meta-dealers-us --action creative_launched \
  --detail "brief 1, 761 ms headline, gig1-a.png, dealership job titles, 10 a day cap" \
  --actor chitraksh
```
