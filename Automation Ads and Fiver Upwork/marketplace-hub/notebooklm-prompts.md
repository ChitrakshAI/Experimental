# NotebookLM prompts for the Marketplace Hub

Paste block A first (as a chat message, and trimmed into every Customize box). Then use the per-output prompts. The sources in the notebook are flat markdown files with no folder names, so block A is the map the model does not have.

Files NotebookLM probably could not ingest: `hub.py`, `accounts.json`, `campaigns.json`, `events.jsonl`, `metrics.jsonl`. README.md and STRATEGY.md describe them; the prompts tell the model to rely on those descriptions.

---

## A. Master context brief (paste into chat first, then reuse)

```
CONTEXT BRIEF. Read this before answering anything.

You are looking at 28 files from one project folder called "marketplace-hub". The folder names were lost on upload, so here is the map.

WHO: Oraya, also called Hanflux AI. Two founders. Chitraksh Mayank, a lawyer-engineer in India, builds AI phone agents (software that answers or makes phone calls with a synthetic voice) and business automations. Frankie Alicea, a licensed insurance agent in the USA, sells. They want paying clients from freelance marketplaces (Fiverr and Upwork) fast, to earn money and collect case studies.

WHAT THE PROJECT IS: an operating system for winning clients on those marketplaces. It is a folder of documents plus a small command-line program (hub.py, not uploaded) that keeps an append-only log of every action and every metric.

READING ORDER AND WHAT EACH FILE IS:
Root level:
- CLAUDE.md: rules for the AI assistant that operates the hub.
- README.md: what the hub is, folder map, daily routine, how to run commands.
- STRATEGY.md: the master plan. Read this first for the big picture.
- NEXT-SESSION.md: exactly where work stopped and the next steps.
- 2026-09-11.md: an auto-generated status report (from the reports folder).
Research folder (the evidence everything else is built on):
- fiverr-market.md: Fiverr demand and supply analysis, competitor teardown, positioning.
- marketplace-expansion.md: Upwork analysis, the one-account-per-person rules, ads, other channels, monitoring, operating model.
- oraya-facts.md: verified facts about the product, measured numbers, brand rules.
- fiverr-profile-package.md: the finished copy for the Fiverr profile and three gigs.
- INDEX.md: one paragraph per research file.
- gig3-c.png and other PNGs: ad and gig images.
Playbooks folder (step by step procedures):
- fiverr-gig-build.md, upwork-account-setup.md, upwork-proposal.md, response-sla.md, case-study-capture.md, weekly-review.md.
Templates folder (message copy to reuse):
- first-reply-gig1.md, first-reply-gig2.md, first-reply-gig3.md, custom-offer.md, delivery-message.md, review-request.md, upwork-proposal-skeleton.md.
Ads folder: ads-plan.md, creative-briefs.md (campaigns.json not uploaded).
Monitoring folder: daily-check.md, scheduled-task-prompt.md.

KEY TERMS: "gig" = a service listing on Fiverr. "proposal" = a bid on an Upwork job. "TTFT" = time to first audio, how fast the AI answers (761 milliseconds measured). "TCPA, CIPA, DNC" = US phone-call laws and the Do-Not-Call list; the product enforces them in code. "Level 1, Level 2, Rising Talent, Top Rated" = seller ranks on Fiverr and Upwork. "Briefs" = Fiverr's inbound job requests, locked until Level 2. "ledger" = the append-only log.

CURRENT STATE (11 Sept 2026): Fiverr account @hanfluxai has a live seller profile; Gig 1 is a complete draft, Gig 2 is half built, Gig 3 not started; nothing is published yet because ID verification and tax forms are pending. Upwork accounts are not opened yet.

RULES FOR YOUR OUTPUT: assume the listener knows nothing about freelancing, AI voice agents, or this company. Define every term the first time. Use only numbers that appear in the sources and say which file they come from. Do not invent clients, results or reviews. Do not use em dashes.
```

---

## B. Audio Overview (podcast)

Customize box (NotebookLM keeps this short, so this is the condensed brief):

```
Audience: a complete beginner who knows nothing about freelancing, Fiverr, Upwork, AI phone agents, or this company. Define every term the first time it appears.

Structure, in order: (1) Who Oraya / Hanflux AI is and what a compliance-gated AI phone agent does, from oraya-facts.md. (2) The problem: they need paying clients fast from Fiverr and Upwork, from STRATEGY.md. (3) What the research found: on Fiverr the tool keywords are crowded and cheap while the dealership and insurance keywords have zero AI voice supply; on Upwork jobs are bigger but every proposal costs money and reply rates are low, from fiverr-market.md and marketplace-expansion.md. (4) The three advantages: measured 761 ms answer time, compliance enforced in code, real dealership and insurance experience. (5) The rules: one account per person per platform, Frankie's US account unlocks US-only jobs, never anchor prices low. (6) How the hub works day to day: the ledger, the daily 30-minute routine, the three gigs, the budget tiers for ads. (7) Where things stand today and the next steps, from NEXT-SESSION.md.

Tone: two hosts, one explains and one asks the beginner's questions. Concrete numbers with the file they come from. No hype, no invented results. Length: long, deep dive.
```

Chat prompt to run first if the Customize box truncates:

```
Using the CONTEXT BRIEF above, write a 12-minute two-host podcast script that explains this project to someone who knows nothing. Follow the seven-part structure in the brief, define every term, cite the file for every number, and end with the three things the founders must do before anything goes live.
```

---

## C. Video Overview

```
Make an explainer video for a complete beginner. Title: "How Oraya wins its first clients on Fiverr and Upwork."

Scenes, in order:
1. What the company sells: an AI that answers a car dealership's or insurance agency's phone in 761 milliseconds and follows US calling laws in code (oraya-facts.md). Define "AI voice agent", "latency", "TCPA".
2. Why marketplaces: Fiverr for inbound search, Upwork for bidding on posted jobs (STRATEGY.md section a).
3. The Fiverr finding: crowded tool keywords versus empty vertical keywords, with the service counts from fiverr-market.md section 3.
4. The Upwork finding: bigger budgets, paid proposals, low reply rates, and the Rising Talent shortcut (marketplace-expansion.md sections 1, 2).
5. The account structure: two humans, two accounts, one agency, and why a second Fiverr account is never allowed (marketplace-expansion.md section 3).
6. The three gigs and their prices (fiverr-profile-package.md).
7. The hub: the ledger, the daily routine, the kill and scale rules for ads (README.md, ads-plan.md, monitoring/daily-check.md).
8. Status today and next steps (NEXT-SESSION.md).

Style: minimalist, dark, one idea per scene, every number on screen with its source file. No em dashes. No invented results.
```

---

## D. Report (PDF)

Report type: custom. Prompt:

```
Write a briefing document titled "Marketplace Hub: Read This First" for a new team member who has never seen the project and knows nothing about freelancing or AI voice agents.

Sections:
1. Plain-language summary (10 lines): what Oraya sells, who buys it, what the hub is for.
2. Glossary: every term a beginner needs (gig, proposal, Connects, TTFT, TCPA, CIPA, DNC, Level 1 and 2, Rising Talent, Top Rated, JSS, Briefs, ledger, honeymoon window, Seller Plus, Promoted Gigs, boosted proposal).
3. The folder, file by file: what each of the 28 files is for and when to open it, grouped as root, research, playbooks, templates, ads, monitoring.
4. The strategy in one page, from STRATEGY.md sections a to i.
5. The evidence: the ten most important numbers from the research files, each with the file and section it comes from.
6. The rules that must never be broken (accounts, pricing floor, measured numbers only, logging).
7. Current state on 11 September 2026 and the next ten actions, from NEXT-SESSION.md, with who owns each.
8. Open decisions waiting on the founders.

Constraints: cite the source file for every fact, do not invent anything not in the sources, no em dashes, headings and short paragraphs, tables where they help.
```

---

## E. Slide Deck

```
Create a 15-slide deck titled "Marketplace Hub: the plan to win the first five clients" for an audience that knows nothing about the project.
Slide order: 1 title; 2 who Oraya is and what an AI phone agent does; 3 the goal, five orders in 30 days; 4 the three advantages with the measured numbers; 5 Fiverr findings; 6 Upwork findings; 7 the account structure and the one-account rule; 8 the three Fiverr gigs and prices; 9 the Upwork approach and price floor; 10 channel matrix, yes, later, never; 11 ads budget tiers and the measurement gates; 12 the daily 30-minute routine; 13 the seven leading indicators; 14 status today; 15 the next ten actions and owners.
One idea per slide, a source file named at the bottom of every slide, define terms on first use, no em dashes, no invented numbers.
```

---

## F. Mind Map

```
Build a mind map with the root "Marketplace Hub". First-level branches: Company and product; Fiverr; Upwork; Account rules; Ads and budget; Daily operations; Research files; Current status. Under each, add the key facts and the file they come from. Keep labels short enough for a beginner to follow.
```

---

## G. Infographic

```
One-page infographic for a beginner: "How Oraya gets clients on Fiverr and Upwork." Show the funnel from marketplace search or job post, to gig or proposal, to first order, to case study. Include the three advantages with numbers (761 ms, compliance in code, dealership and insurance experience), the three gig prices, the one-account rule, and the five-orders-in-30-days goal. Dark minimalist style. Every number labelled with its source file. No em dashes.
```

---

## H. Flashcards and Quiz

```
Create flashcards that teach a beginner the vocabulary and the rules of this project: marketplace terms, the platform ranks and their thresholds, the account rules, the pricing floors, the measured product numbers, and the daily routine. Each card states the source file. Then a 20-question quiz on the same material.
```

---

## I. Data Table

```
Extract a table of every quantitative claim in the sources: value, what it measures, platform, source file and section, date if given. Add a second table of the three Fiverr gigs: title, package names, prices, delivery days, revisions, tags. Add a third table of the account build order with owner, platform, status and blocker.
```

---

## J. Useful chat questions once the brief is loaded

```
Explain to me like I am new: what is the difference between how we get clients on Fiverr and on Upwork, and why does the plan open Upwork on day 1?
```
```
List everything only the founders can do (verification, forms, accounts), by person, with the file that says so.
```
```
Walk me through one full day of running the hub using README.md and monitoring/daily-check.md, including the exact commands.
```
```
What are the seven leading indicators and what decision does each one trigger?
```
```
Which channels are marked never, and why?
```
```
Which numbers in the sources are measured, which are targets, and which are external benchmarks?
```
