# Oraya Fact Sheet (for Fiverr seller profile)
Compiled 2026-09-10 from two mounted folders on the user's Mac:
`Oraya Voice Product` (the voice-agent engineering repo) and `oraya-growth-engine` (the CMO/content repo).
No em dashes used anywhere below, per the project's own writing rule.

---

## 1. PRODUCT: the Oraya voice agent

**What it is.** A phone-answering AI voice agent product, built as a "product engine" so it can be cloned for any client business in one session. Reference client is a Mercedes-Benz dealership (fictionalized in this note per anonymization rules below); a second demo runs for a fictional multi-brand dealership; a third is Oraya's own sales concierge.

**Call flow (current, production-target architecture).**
Twilio ConversationRelay (Deepgram Flux STT, eager end-of-turn detection) streams audio to a Supabase Edge Function socket (`cr-ws`) that runs the conversation brain on Claude Haiku 4.5 (streaming, cached system-prompt prefix, max_tokens capped per turn, Sonnet escalation on precision states like identity/email capture), then ElevenLabs TTS (Flash v2.5) speaks back with native barge-in (caller can interrupt mid-sentence). Turns are logged to Supabase in near real time and shown on a live dashboard.

**Target production architecture (documented, not yet fully shipped).** Twilio/Telnyx SIP trunk to a self-hosted LiveKit Agents (Python) media plane, Deepgram Flux STT + eager end-of-turn, one direction-aware Claude Haiku 4.5 brain (with Sonnet escalation) replacing the two separate agents the prior vendor (Retell) required, Cartesia Sonic-3 TTS with ElevenLabs Flash as hot-failover, Supabase Postgres data plane with row-level security and per-tenant multi-tenancy, plus an eval plane and a human-gated self-improvement plane.

**Capabilities:**
- Inbound calls: answers, greets with a locked compliance disclosure (recorded-line + AI-voice notice, always the first utterance, never model-generated), routes caller between "Sales" and "Service" style branches, answers questions from a persona-specific knowledge base, discusses inventory/pricing with a "no live-inventory claims, prices subject to change" guardrail.
- Appointment booking flow: designed to offer exactly 3 time-slot options (morning/afternoon/evening), read numbers digit-by-digit, never state the current date aloud; in demo mode the agent is instructed to say it cannot truly book (honesty rule).
- Outbound calling: architecture supports it (a "direction" runtime variable, not a separate agent) but outbound dialing is gated behind an allowlist, consent-basis check, quiet-hours check (8am-9pm callee-local), and Do-Not-Call check, all enforced in code, not in the prompt. No live outbound campaigns are running; the dialer is structurally blocked from calling non-allowlisted numbers pre-ship-gate.
- Follow-ups / mid-call SMS: a "midcallSms" capability sends an SMS confirmation mid-call via Twilio A2P messaging (built; live send was blocked at last check for lack of a non-protected sender).
- Call transfer to a human: cold transfer with bridge cue, "never claim to be human" as a locked compliance rule.
- Barge-in / interruption handling, voicemail detection, DTMF (keypad) capture, silence-timeout handling, per-turn latency logging.
- Multi-persona routing: one phone number can host an orchestrator ("Ada") that pitches the product to callers and then hands off, mid-call, to a live demo persona ("Jessica" for the dealership demo, "Robin" for the fictional multi-brand demo), each with a distinct ElevenLabs voice.
- Post-call data pipeline: a 15-field structured extraction from each call (caller intent, contact info, appointment details, consent flags, etc.), with a webhook payload shaped to be compatible with an existing n8n automation pipeline built for a prior vendor.
- Dashboard: per-call view (audio player, full transcript, timestamps, latency waterfall, cost), live call board, KPI tiles, a compliance/legal panel, PII-masked views (the public dashboard reads only masked Postgres views, never raw tables).

**Integrations / stack named in the repo:**
- Telephony: Twilio (ConversationRelay; SIP-agnostic design, Telnyx considered).
- STT: Deepgram Flux (primary), AssemblyAI (hot-standby).
- LLM "brain": Claude Haiku 4.5 (default) with Claude Sonnet escalation on precision states. Anthropic has no speech-to-speech product; this was evaluated and rejected as the default path (see below).
- TTS: ElevenLabs (Flash v2.5, currently live) and Cartesia Sonic-3 (named as the target/evaluated TTS, "Brooke" voice) in an A/B bake-off against ElevenLabs.
- Media/orchestration (target): LiveKit Agents (self-hosted, Python), LiveKit Cloud free tier used in dev.
- Data plane: Supabase Postgres (with row-level security, per-tenant), Supabase Edge Functions (Deno) for the call-brain socket.
- Automation: n8n (the post-call webhook is deliberately shaped to match what an existing n8n pipeline already consumes).
- Dashboard hosting: Vercel.
- No LiveKit/Cartesia production cutover confirmed live at time of this scan; ElevenLabs + Claude Haiku on Supabase Edge + Twilio ConversationRelay is what is actually live.

**S2S (speech-to-speech) evaluation.** Explicitly evaluated and explicitly NOT the default shipping architecture. Findings documented: Fish Audio sells no true S2S product; OpenAI Realtime and Amazon Nova Sonic are real S2S options but were not adopted because full S2S forfeits byte-exact compliance disclosures, transcript fidelity, and tool-call accuracy (measured at 66.5% in their research), and removes the text-patchable "surgical prompt edit" self-improvement workflow that is treated as the product's real moat. The brain layer is built as a swappable interface (cascade / half-cascade / full S2S) so a different choice can be revisited.

### Measured metrics (only ones with numbers in the repo; everything below is either measured on their own test calls or a stated target, and is labeled which)

- **Time-to-first-token/audio (TTFT), MEASURED on the deployed demo:**
  - Reference dealership demo (Jessica persona), deployed 2026-08-26: **median 761 ms**, min 748 ms, max 1082 ms, over simulated calls.
  - Same demo, an earlier measurement on 2026-08-21: min 0.73s, **median 0.89s**.
  - Orchestrator/concierge persona ("Ada"/"Eric" voice): **median 868 ms** over 8 simulated conversations (2026-08-26), was 904 ms at an earlier check.
  - Fictional multi-brand demo ("Robin"/"Bella" voice), first deploy 2026-08-26: **median 900 ms**.
- **Baseline being beaten (their own prior vendor, Retell, measured on their real production calls, 17 archived calls):** inbound p50 approx 1.9s, outbound p50 approx 1.64s, p90 range 1.9s-2.5s. This is the number Oraya's own agent is benchmarked against.
- **Production latency target (not yet measured at scale, a design budget):** less than or equal to 800ms p50, less than or equal to 1,200ms p95, alert threshold above 1,500ms. Per-stage sub-budgets are documented (telephony hop 40-80ms, STT+turn-detection 150-260ms, LLM first token 200-350ms, first-sentence-to-TTS-audio 90-150ms, playout buffer 40-60ms).
- **Cost target (a research-derived band, not yet a measured production number):** $0.047-$0.081 per minute of call, versus the prior vendor's own per-call cost figure (available in their archive for side-by-side comparison but not restated here as a hard number).
- **Cost of running one branded demo line, stated in their own sales script and repeated to prospects:** "about a dollar a month plus pennies per call" (explicitly the ONLY dollar figure the in-call agent is allowed to say; the repo has a hard rule against the agent doing any arithmetic on this number after it was once caught inventing "fifty to a hundred bucks a month" by multiplying permitted figures).
- **Actual line-item cost of a demo number:** phone number purchase approx $1.15/month, plus Twilio usage approx $0.014/minute of calls.
- **Deepgram Flux STT cost:** $0.0065/min pay-as-you-go (English), $0.0057/min on their Growth tier, $0.0078/min multilingual. $200 free signup credit.
- **ElevenLabs TTS cost:** roughly $0.0375/min effective at their Creator plan ($22/mo covers about 586 minutes).
- **Cartesia (evaluated TTS alternative) cost:** approx $0.0375/min per their own pricing note; Fish Audio TTS priced separately at $15 per 1M UTF-8 bytes (approx $0.02/min).
- **Monthly fixed-cost picture for running the build (their own budget line, not a client price):** approx $60-130/month during build, plus approx $0.05-0.08/min of call usage.
- **Answer rate, booking rate, calls handled at scale:** NOT FOUND as measured production numbers anywhere in the repo. The product has run supervised test/demo calls (single digits to low tens of simulated conversations) and is explicitly NOT yet carrying real customer call volume; do not claim production-scale metrics.

### Known limitations, stated honestly in their own docs (useful for accurate seller-profile claims)

- Call length currently capped by the Supabase Edge Function wall-clock limit: 150 seconds on the free tier, 400 seconds on the paid tier, until the brain socket moves to an uncapped host.
- The current live demo mode (as opposed to the target LiveKit architecture) has no true full-duplex barge-in on one of its legs and runs at roughly 1.9-2.4 seconds per turn rather than sub-second, by their own admission ("Do not benchmark the two against each other").
- Outbound dialing is not live to real customers; it is demo/inbound-only until a compliance ship-gate is explicitly approved.

---

## 2. CASE STUDIES / USE CASES

Everything below is anonymized per the project's own rule (no real dealership or agency names are to be used in outward marketing; the source repo does name a specific real dealership internally, which is not reproduced here). All figures are from the mounted repos; anything referenced but physically located outside the two mounted folders is marked "OUTSIDE MOUNTED FOLDERS, not verified in this pass."

### a. Reference client: a dealership voice-agent build (dealership vertical), status: LIVE DEMO
- Built as a full clone/replacement pipeline for a Retell-based voice agent the client was previously running. Oraya's version replaces the vendor's forced two-agent split (inbound/outbound) with one direction-aware agent, and targets more than 2x latency improvement over the prior vendor's measured production numbers.
- Persona: a saleswoman-style AI voice with a defined sales methodology (assertive-certainty plus a structured discovery-question style), tuned to speak in short 1-3 sentence turns and ask one question per turn.
- Deployed on a dedicated demo phone number; TTFT measured at median 761-890ms (see Section 1).
- Deviation register vs. the prior vendor documented explicitly (things Oraya fixed on purpose): actually stops recording when a caller withholds consent (the prior vendor kept recording anyway), fixed a male fallback voice to a female one for persona continuity, resolved a self-contradictory transfer-to-human policy, upgraded the AI-disclosure wording to be explicit rather than "virtual assistant."
- Status: live demo/reference build, not yet cut over to the client's real production phone line; a formal parity checklist and compliance sign-off gate everything before that cutover.

### b. Fictional multi-brand dealership demo, status: LIVE (demo/prospect-facing)
- Built specifically as a "safe to show any prospect" demo: wholly invented dealership identity, but as of 2026-09-10 advises on REAL cars (BMW, Mercedes-Benz, Toyota models) with verified specs and prices from primary sources, after founder feedback that invented car models felt gimmicky on real sales calls.
- Persona is an "unbiased best-deal advisor" across three real car brands, engineered specifically NOT to push one brand, and instructed never to invent colors, rates, lease numbers, stock, or DERIVED dollar figures (a specific bug was found and fixed where the agent invented "you'd pocket thirteen grand" from real inputs; the fix bans any arithmetic on sanctioned figures).
- Live via the same "one number, many personas" router used for the dealership reference demo.

### c. Oraya's own sales-concierge voice agent ("company answers its own demo line"), status: BUILT, NOT YET DEPLOYED to the live number at last check (build proven end-to-end, dashboard-verified, gated on founder go-ahead)
- Designed to answer the shared demo phone number first, pitch the product to a prospective buyer in conversation, then route the caller live, mid-call, to either the dealership demo persona or the fictional multi-brand persona depending on what the caller wants to hear.
- Also demonstrated a mid-call SMS send capability (send a text to the caller while still on the phone with them) as a sales-flow example.

### d. Voice-agent "engine" / productized cloning process, status: LIVE INTERNAL PROCESS
- A documented, repeatable playbook exists to spin up a brand-new client demo (new persona, new voice, new phone number, new dashboard) inside a single working session: intake, gated number purchase (~$1.15/mo), data-plane provisioning, brain-socket deploy, telephony config, and a verification pass (simulated conversation, latency check, live TwiML check) before handing the number to the client.
- This is the core of what would be sold/delivered to a Fiverr buyer: "we can stand up a working, branded phone-answering AI voice agent for your business, provably working, inside one build session."

### e. Insurance lead-generation voice agent ("Maya"), referenced but OUTSIDE MOUNTED FOLDERS (lives in a separate, off-limits project directory not included in this scan)
- Referenced in the growth-engine repo as existing portfolio proof: an outbound + inbound voice-agent flow (21-node conversational flow graph) with over 100 iterations of tuning, and a widely cited internal finding that **54% of 100 real AI sales calls died in the first 15 seconds** ("the autopsy" post). Also referenced: a companion n8n post-call automation with 41 nodes.
- Not verified against source files in this pass; treat as claimed portfolio material until the source project is scanned directly.

### f. Insurance-side client relationship: Frankie Alicea (licensed insurance producer)
- Frankie Alicea is named throughout the growth-engine repo as the licensed producer fronting insurance-side customer communications; the repo is explicit and repeated that Oraya itself is NOT a licensed insurance entity and must never imply otherwise in any content.
- A dedicated LinkedIn content track ("Desk franchise") was authored in Frankie's voice, covering insurance-industry data (see Section 3 static posts below: top P&C insurer league tables, independent-agent channel share, insurance AI adoption gap, insurance hiring/talent-gap data). As of the last content-ledger audit, these posts had NOT been confirmed as actually published on Frankie's personal LinkedIn; they were instead scheduled on the Oraya company page, an open discrepancy flagged for the founder to resolve.

### g. LinkedIn/content case studies (the growth engine's own output, usable as "we also do content/automation for lead gen" proof)
- A themed data-post series (10 static LinkedIn graphics, "Desk"/insurance + dealership market data) built across two content batches, each post citing a primary-source statistic (examples: "Top 7 US dealership groups, $166B combined," "42% of dealer service calls unanswered," "Top 10 US P&C insurers league table," "independent agents place 62% of US P&C premium," "12 voice-AI funding rounds, $2.42B, Jan-Jul 2026").
- A reel/short-video production pipeline: 7 completed batches of short-form vertical video content (see Section 3), each batch iterating on visual technique, narration, and a "conversion arc" (hook, evidence, product turn, call-to-action with a DM keyword), with an explicit self-improving "do not repeat" register of used visual engines, color palettes, and statistics across batches.
- A static editorial-graphics pipeline ("visual-rig") for LinkedIn data posts, with reusable WebGL engines and verification gates (arithmetic-checking script, render-checking script) before anything ships.

---

## 3. PROOF ASSETS (file paths, description, size)

All paths below are relative to the two mounted folders on the user's Mac:
`Oraya Voice Product` = the voice-agent repo
`oraya-growth-engine` = the content/growth repo

### Demo videos (MP4, short-form vertical/social content, in `oraya-growth-engine`)
| Path | Description | Size |
|---|---|---|
| `reels-batch-01/final/hanflux_reel_helix_ig.mp4` | Hanflux AI brand reel, helix visual motif, Instagram cut | 37M |
| `reels-batch-01/final/hanflux_reel_helix_v2_4x5_meta.mp4` | Same, 4x5 Meta-format cut | 16M |
| `reels-batch-01/final/oraya_reel_consultancy_li.mp4` | Oraya consultancy-positioning reel, LinkedIn cut | 4.8M |
| `reels-batch-01/final/oraya_reel_frontier_x.mp4` | "Frontier engines" / generative-AI-value reel, X cut | 7.8M |
| `reels-batch-01/final/oraya_reel_manifesto_ig.mp4` | Oraya brand manifesto reel | 7.4M |
| `reels-batch-01/final/oraya_reel_voiceagent_ig_li.mp4` | Voice-agent explainer reel | 5.0M |
| `reels-batch-02/final/oraya_r1_missedcall_ig.mp4` | Missed-call cost problem reel | 9.3M |
| `reels-batch-02/final/oraya_r1_missedcall_4x5.mp4` | Same, 4x5 cut | 4.5M |
| `reels-batch-02/final/r1_compliance_ig.mp4` | TCPA compliance-risk reel | 6.0M |
| `reels-batch-02/final/r1_compliance_4x5.mp4` | Same, 4x5 cut | 2.8M |
| `reels-batch-02/final/r2_coldfollowup_ig.mp4` | Cold-follow-up decay reel | 4.1M |
| `reels-batch-02/final/r2_coldfollowup_4x5.mp4` | Same, 4x5 cut | 1.8M |
| `reels-batch-02/final/r3_doubleentry_ig.mp4` | Double-data-entry problem reel | 4.0M |
| `reels-batch-02/final/r3_doubleentry_4x5.mp4` | Same, 4x5 cut | 1.5M |
| `reels-batch-02R/final/r1_compliance_ig.mp4` | Rebuilt/upgraded compliance reel | 22M |
| `reels-batch-02R/final/r1_missedcall_ig.mp4` | Rebuilt missed-call reel ("YOUR FRONT DESK NEVER SLEEPS," Eric narration + live front-desk panel visual) | 6.6M |
| `reels-batch-02R/final/r2_coldfollowup_ig.mp4` | Rebuilt cold-follow-up reel | 18M |
| `reels-batch-02R/final/r3_doubleentry_ig.mp4` | Rebuilt double-entry reel | 19M |
| `reels-batch-04-data/final/r1_timegap_ig.mp4` | "Time gap" data-driven reel, abstract data-viz engine | 53M |
| `reels-batch-05-real/final/r7_ghosttest_ig.mp4` | "Ghost test" reel, real-photo WebGL engine | 20M |

Note: batches 05 (6 more reels) and 06 (all 7 reels) were fully scripted and built as HTML source but were NOT found exported to MP4 in the mounted folder (source files exist under each batch's `src/` folder; per the content ledger these are "built but never placed" as final video). If MP4 exports are needed for portfolio use, they would need to be rendered from `reels-batch-05-real/src/` and `reels-batch-06/src/` first.

### PDFs
| Path | Description | Size |
|---|---|---|
| `linkedin-field-notes/carousels/post2-hallucination-sanctions.pdf` | 6-page LinkedIn carousel PDF, "Legal Hallucination Index" (AI hallucination court-sanction data), confirmed posted live, 301 impressions | 4.9M |

No proposal PDFs, one-pagers, or sales-deck PDFs were found in either mounted folder.

### Static graphics / screenshots
| Path | Description | Size |
|---|---|---|
| `linkedin-field-notes/singles/post3-delhi-hc-training-research.png` | Legal data single-image post | 1.7M |
| `linkedin-field-notes/singles/post1-two-leaderboards.png` | AI benchmark leaderboards single-image post | 1.6M |
| `linkedin-field-notes/singles/post5-metr-measurement.png` | METR AI-benchmark data post, confirmed posted live, 168 impressions | 1.6M |
| `linkedin-frankie-batch-01/final/p1_dealer_top7.png` | "Top 7 US dealership groups, $166B combined" | 468K |
| `linkedin-frankie-batch-01/final/p2_dealer_phones.png` | "42% of dealer service calls unanswered" | 428K |
| `linkedin-frankie-batch-01/final/p3_agency_league.png` | "Top 10 US P&C insurers league table" | 428K |
| `linkedin-frankie-batch-01/final/p4_agency_ai.png` | "Insurance AI leaders vs laggards, 6.1x" | 468K |
| `linkedin-frankie-batch-01/final/p5_voiceai_map.png` | Voice AI market map, 15 companies across 4 layers | 432K |
| `linkedin-frankie-batch-02/final/p6_fixedops.png` | Dealership fixed-ops revenue/margin data | 1.9M |
| `linkedin-frankie-batch-02/final/p7_paymentwall.png` | "$777 record average new-vehicle payment" | 2.6M |
| `linkedin-frankie-batch-02/final/p8_channel.png` | "Independent agents place 62% of US P&C premium" | 1.6M |
| `linkedin-frankie-batch-02/final/p9_talentcliff.png` | Insurance talent-gap data | 1.4M |
| `linkedin-frankie-batch-02/final/p10_signal.png` | "12 voice-AI funding rounds, $2.42B, Jan-Jul 2026" | 2.2M |

Dashboard product screenshots (`Oraya Voice Product/dashboard/tests/shots/`): desktop view, mobile/phone view, call-detail drawer with a real logged call, legal/compliance panel (light and dark theme), admin filter view, a recording-playback demo-gate flow (locked / wrong-passcode / unlocked / playing states). 11 PNGs, 124K-376K each. Useful as product-UI portfolio evidence, though they show internal/admin views rather than a client-facing surface.

### Sample voice / call audio
`Oraya Voice Product/clients/_auditions/` and `Oraya Voice Product/voice-auditions/`: a set of voice-casting audition clips (WAV/MP3, 80-92K each), recordings of the same scripted line in different ElevenLabs voice candidates (used to pick the personas' voices), not full sample sales calls. No full recorded customer-facing sample call was found accessible in the mounted folders (live call recordings are stored in Supabase/Twilio and gated behind a password/auth layer described in the code, not present as local files).

### Landing pages / dashboards (live URLs referenced in the repo, not local files)
- Dashboard, deployed on Vercel: `https://oraya-voice-dashboard.vercel.app` (production) and a preview URL under the same Vercel project, per `state.json`. Not confirmed reachable/current from this pass; treat as "as of last recorded deploy."
- No separate marketing landing page (e.g. orayalabs.ai) was found as a local file in either mounted folder; the domain `orayalabs.ai` is referenced repeatedly as the destination URL in reel/graphic end-cards.

---

## 4. BRAND

**Company / brand names:** Oraya (parent brand), Oraya Labs (venture/product-studio surface, domain **orayalabs.ai**), Hanflux AI (the client-delivery/services business).

**Founder:** Chitraksh Mayank. Described in the growth-engine repo as a graduate lawyer (B.B.A. LL.B., Hons., Business Law, NMIMS Bengaluru), based Ranchi/Bengaluru, India, positioned explicitly as "a lawyer who ships production AI systems." LinkedIn: linkedin.com/in/chitraksh-mayank-7705a9205. No other team-member names/titles were found in the mounted folders except Frankie Alicea, described specifically as "the licensed [insurance] producer" who fronts insurance-side customer communications (not an Oraya employee/title per se).

**Positioning statement (locked, repeated verbatim across the content repo):** "a lawyer who ships production AI systems, with cinematic product films as proof" / own the "compliance-first AI" education lane. Proposed LinkedIn headline language: "Lawyer who builds AI systems. Voice agents and automation for insurance and auto retail. Founder, Oraya Labs."

**Tagline / CTA lines used on video end-cards (multiple, rotated per reel, brand `orayalabs.ai` always the closing card):**
"SPEED IS THE WHOLE GAME" · "DEMAND NEVER SLEEPS" · "SEAL THE LEAK" · "BE FIRST. EVERY TIME." · "CLOSE THE GAP" · "PERSISTENCE, AUTOMATED" · "RETENTION ON RADAR" · "YOUR FRONT DESK NEVER SLEEPS" · "KEEP THE HUMANS FOR THE HUMAN PART" · "GIVE YOUR CLOSERS THEIR WEEK BACK" · "FIRST ACCURATE ANSWER WINS."

**Compliance moat / positioning language:** the repo repeatedly frames legal/compliance knowledge as the core competitive moat, e.g. "LAW x AI (the moat): compliance-first education... You are the only voice in this lane with both credentials. This pillar builds authority that generic AI automation bros cannot copy." The technical build treats the same idea as an engineering property: "the text-patchable self-improvement moat" (ability to surgically edit and re-test text prompts, as opposed to opaque end-to-end speech-to-speech models).

**Compliance laws actually cited and verified against primary sources in the repo (useful for accurate claims):**
- CIPA, California Penal Code Section 632 and Section 632.7 (all-party call-recording consent).
- TCPA (federal Telephone Consumer Protection Act) and the FCC's 2024 ruling that AI-generated voices count as "artificial voice" under TCPA.
- 47 CFR Section 64.1200 (quiet hours, Do-Not-Call, consent revocation rules).
- California AB 2905 / Public Utilities Code Section 2874 (California's AI-voice-disclosure law for automated calls), identified as the actually-binding California AI-disclosure authority (a separate, older California "bot disclosure" statute, Business & Professions Code Section 17940, was checked and found NOT to apply to phone calls, only to websites/apps).
- Truth in Caller ID Act / STIR-SHAKEN caller-ID attestation rules.
- FTC Telemarketing Sales Rule (16 CFR 310.5), 5-year record-retention requirement.
- **CPRA was NOT found cited anywhere in either mounted folder.** The one place CCPA/CPRA is mentioned is a single line in an internal client-dashboard template noting that "who counts as 'the business' for CCPA/CPRA" on a client's call data is an open question to resolve per client, not a verified compliance claim. Do not claim CPRA compliance analysis has been done; only CIPA, TCPA, and the AI-disclosure statute above have primary-source verification in this repo.

**Visual brand system (locked, "Field Notes" content system, from `oraya-growth-engine/VISUAL-STANDARD.md`):**
- Color palette (hex, locked tokens): ink `#06070C`, surface `#0B0E17`, raise `#111622`, cyan `#62E9FF` (data/measurement), violet `#8C6BFF` (law/regulation), mint `#3DF5B6` (verified/correct), amber `#FFC15C` (caution/disputed), magenta `#FF5CA8` (failure/alarm/sanction), text `#F2F6FC`, muted `#93A0B5`, dim `#5C6880`.
- Typography: display and body font is **Hanken Grotesk** (weights 400/600/800); all figures, kickers, citations, and labels use **Geist Mono** (400/500/700); statute/judicial quotations use **Newsreader** with italics. Explicitly chosen to feel "Mercedes-adjacent: elegant, humanist, simple, highly readable," after an earlier, generic-feeling font set (Unbounded/Space Grotesk/JetBrains Mono/Instrument Serif) was rejected by the founder.
- Design rule: every graphic must include a real WebGL (Three.js) rendered layer, never a flat gradient or stock texture; every number printed must show its source and the date it was read, on the same image; a fixed "spine" (kicker, hairlines, corner ticks, signature block, citation block) never changes across assets.

**Logo files found:** no first-party Oraya/Hanflux logo files were found in the mounted folders. The `assets/logos/` folders present (`linkedin-frankie-batch-01/`, `linkedin-frankie-batch-02/`, `visual-rig/`) contain third-party competitor/reference logos only (insurance carriers like GEICO, Progressive, Allstate, State Farm, USAA, Liberty Mutual, Farmers, Travelers, Chubb, Zurich; dealership groups like AutoNation, Group 1, Lithia, Sonic, Asbury, Penske, Hendrick; and AI-voice competitors like ElevenLabs, Deepgram, Cartesia, Bland.ai, Vapi, Sierra, Retell, Synthflow, Numa, Poly.ai, Crescendo, Parloa, Telli, Rime, Phonely, Decagon, Gradium), used for comparison graphics, not Oraya's own mark.

---

## 5. WRITING RULES (quoted, must apply to any public copy)

From `oraya-growth-engine/WRITING-RULES.md`, founder-locked 2026-07-29, described as overriding style preferences in every other file:

> "RULE 1 (ABSOLUTE): NO EM DASHES. EVER. The character (em dash, U+2014) is banned from every output in this project. No exceptions."

Applies to: "LinkedIn captions and posts, text baked into graphics, reels and slides, headlines, sub-decks, footnotes, citation lines, docs, READMEs, prompts, memory files, DMs, emails, ad copy, anything a human will read."

Stated reason (quoted): "Heavy em-dash use is the single most recognisable tell of AI-generated writing. Every one of them costs credibility on a personal brand built on being an engineer who checks things."

Fix order of preference (paraphrased from the file): (1) split into two sentences with a full stop, (2) use a colon when the second half defines the first, (3) use a comma for a light aside, (4) use paired commas for a mid-sentence interruption (never paired em dashes), (5) use a middot "·" for metadata/labels/citation lines, (6) restructure the sentence entirely if none of the above work.

Also banned as substitutes: a double hyphen "--", a hyphen used with spaces as a clause break, and an en dash used as a clause break. The ONE allowed dash is an en dash for numeric ranges only (example given: "95% CI 5-40", "$500-$1,500").

Ship gate (quoted requirement): before shipping anything, grep the deliverable for the em-dash character and confirm the count is zero, across source files and any text baked into images (SVG labels, JS template strings included).

From `oraya-growth-engine/guardrails.md` (also binding on any public content):
- "AI-slop test on every LinkedIn draft: contains a real number, real artifact, or first-person story, or it dies."
- "Label AI-generated media where platform policy requires."
- "'Not legal advice' framing on LAW x AI educational content."
- "Anonymize client data; Frankie Alicea is the licensed producer, Oraya never implies licensure."
- "Never: fabricated metrics, fake social proof, or invented client stories."

---

## 6. PRICING / OFFER STRUCTURE

No formal public price list, rate card, or "$300 Plan" was found by name anywhere in either mounted folder (the exact phrase "$300 Plan" does not appear in the repo; do not reference it as confirmed).

What IS documented as pricing/offer structure:

- **Demo/build cost economics (internal, not a client-facing price):** a single branded demo phone line costs approximately $1.15/month (Twilio number) plus roughly $0.014/minute of call usage; the sanctioned spoken line to prospects is "about a dollar a month plus pennies per call." Total stated cost per demo: "~$1.15/mo plus pennies of usage."
- **Internal build-phase budget ceilings (not client pricing):** approx $60-130/month fixed cost during the engineering build phase, plus approx $0.05-0.08/minute of call usage once live; a per-session token/time ceiling of "$25 tokens / 4 hours" is used internally for AI-assisted build sessions.
- **The sales funnel / offer structure (from the growth-engine playbook), which IS the closest thing to a productized offer:**
  1. Free lead-magnet offer: a **"Compliance-Safe AI Audit"**, described as a Loom-style teardown of a prospective client's phone/intake/follow-up flow plus a personalized 90-second demo clip, offered at no cost to generate a booked sales call.
  2. That audit call is explicitly framed as the justification for a paid retainer with Hanflux AI (the delivery arm). A stated market benchmark for "adjacent AI-audit niches" retainers is **$2,500-$25,000 per month**, cited as external market context, not as Oraya's own confirmed price.
  3. No confirmed per-minute, per-rooftop (per-dealership-location), or flat setup-fee pricing for the voice-agent product itself was found documented anywhere in either mounted folder.

Recommendation for the Fiverr profile: since no confirmed client-facing price list exists in the source material, price the Fiverr gig independently (e.g., a flat "build you a working branded demo voice agent" gig price) rather than quoting any number above as a fixed product price, and do not state "$300" or any other unverified figure as an official Oraya plan.

---

## Sources / method note

All information above was extracted directly from files under `$HOME/mnt/Oraya Voice Product/` and `$HOME/mnt/oraya-growth-engine/` on the user's Mac via a remote shell, reading `.md`, `.json` and file-listing output only (no PDFs contained extractable data beyond the one already-flat file paths listed; the growth-engine PDF found was a rendered LinkedIn carousel export, not a text-based proposal document). Anything stated as "referenced but OUTSIDE MOUNTED FOLDERS" (the insurance lead-gen agent "Maya," the cinematic product film HTML, the Oraya Autoloop, the Daily Brief, a separate insurance-ads project) lives in sibling project directories explicitly marked off-limits or not-mounted in the source CLAUDE.md files, and was not verified against source files in this pass; treat those specific claims as reported-but-unverified.
