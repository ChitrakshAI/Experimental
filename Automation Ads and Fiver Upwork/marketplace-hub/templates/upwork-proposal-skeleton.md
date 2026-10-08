# Template: Upwork proposal skeleton

**Status: live.** Every structural rule below is a measured finding from `research/marketplace-expansion.md` section 2.12, across 133,872 proposals. Baseline reply rate 7.45%. The full template combination replied at **13.77%**.

Operating rules and the mechanics are in `playbooks/upwork-proposal.md`.

---

## The frame

The client sees the first two lines of a collapsed list and nothing else until they click. Everything below them only matters if those two lines win.

| Section | Length | Job | Measured basis |
|---|---|---|---|
| Line 1 | 1 line | A specific question about their setup that only someone who has built this would ask | Opening with a specific question: **+2.34pp** |
| Line 2 | 1 line | The measured number and the named vertical | Reference to real completed work: **+2.52pp** |
| Body | 1 paragraph | Their specific job, not our capability list | |
| Recent work | 1 line | The most recently delivered comparable build | **+2.52pp** |
| Loom offer | 1 line | A 90-second walkthrough showing a live call with the latency readout | **+3.70pp**, the largest single lift available |
| Scope guarantee | 1 to 2 lines | What is in, what is out, and the word "guarantee" | Part of the 13.77% combination |
| Close | 1 line | "happy to answer any questions" | Part of the 13.77% combination |

**Hard gates, checked on every single send:**

- **Under 250 words.** 150 to 250 is the band.
- **Zero AI clichés.** Not "few". Four or more replies at **0.00%**.
- **No greeting, no gratitude, no "Hi! Thanks for posting"** at -5.50pp, no "Good day" at -3.68pp, no "I have experience with" at -3.67pp, no "I'll help" at -3.17pp, no "Many freelancers" at -4.03pp.
- **No defensive disclaimer.** "non-ChatGPT generated proposal" replies at 5.9%.
- **Hand-written.** Hand-written templates reply at 8.13%, AI auto-bidders at 6.91% to 7.13%.
- **No em dashes.**

---

## The skeleton

```text
[LINE 1: a specific question about their setup that only someone who has built this
would ask. Not "what is your timeline?". Something that reveals you already know
where this breaks.]

[LINE 2: the measured number, its method and date, plus the named vertical. One
number. Not three.]

[BODY, one paragraph: their specific job. What you read in their post, restated
more precisely than they stated it, and what you would do about it.]

[RECENT WORK, one line: the most recently delivered comparable build, anonymised
to industry plus size plus region.]

[LOOM: "I can send a 90-second walkthrough showing a live call with the latency
readout on screen, if that is useful."]

[SCOPE GUARANTEE: what is delivered, what is explicitly not, and the guarantee in
one sentence.]

[CLOSE: "Happy to answer any questions."]
```

---

## Worked example: dealership BDC voice agent, posted at $800, bid at $3,500

```text
Are your after-hours calls currently rolling to voicemail, or to an answering service that charges per call?

I build phone agents at a measured median 761 ms time-to-first-audio, measured over simulated calls on 26 August 2026 against a prior vendor's 1.64 to 1.9 s production p50, currently running for a dealership BDC, with the recorded-line and AI disclosure locked as the first utterance in code rather than in the prompt.

Your post describes the after-hours gap, but the expensive calls are usually the daytime ones that ring six times while an advisor is with a customer. Those callers do not leave a voicemail, they call the next dealer. I would put one direction-aware agent on your existing number covering both, rather than the two-agent inbound and outbound split most vendors force, with booking, warm transfer with context, and a structured write into the CRM you already run.

Most recent comparable build: a franchise rooftop in the US Midwest, vendor agent replaced, latency cut by roughly half.

I can send a 90-second walkthrough showing a live call with the latency readout on screen, if that is useful.

At $3,500 you get the agent, the compliance block, booking, transfer and CRM write, plus 30 days of tuning. I guarantee the disclosure fires as the first utterance on every call, because it is concatenated text outside the model. Not included: I do not rebuild your CRM, I write into what you have.

Happy to answer any questions.
```

Word count: 232. Clichés: 0. Bid: 437% of posted budget, which is inside the 200% to 500% band that replies at 16.4%.

---

## Worked example: compliance-led outbound, posted at $1,500, bid at $5,000

```text
What is the consent basis on your current list, and does it survive a revocation mid-campaign?

I build the gating layer that runs before the dial: consent basis on file, Do-Not-Call clear, quiet hours checked in the callee's own time zone, allowlist pass. All four are code, not a line in a prompt the model can talk itself past. I trained as a lawyer before I built this and I read the statutes myself.

Everyone else quoting on this post will quote you on the dialing. The expensive half happens before the dial, and it is the half that gets audited. Disclosure is fixed text concatenated outside the model, identical on call one and call ten thousand, with a per-call audit trail of consent state and disclosure delivery held to your retention requirement.

Most recent comparable build: an independent agency, US Southeast, outbound campaign gated and audited end to end.

I can send a 90-second walkthrough showing the compliance panel and a live gated call, if that is useful.

At $5,000 you get the gating layer with a refusal path that blocks rather than warns, the disclosure block, the audit trail, and your campaign flow on top. I guarantee no call is placed without all four gates passing. Not included: I do not sell or source lead data. You bring the list and the consent records.

Engineering, not legal advice: your counsel signs off on the language, I make the system enforce it.

Happy to answer any questions.
```

Word count: 247. Clichés: 0. Bid: 333% of posted budget.

---

## Pre-send checklist, run every time

- [ ] Under 250 words
- [ ] Zero AI clichés, counted not assumed
- [ ] No greeting, no gratitude, no banned opener
- [ ] Line 1 is a question only a builder would ask
- [ ] Exactly one measured number, with method and date
- [ ] The vertical is named
- [ ] Recent comparable work referenced, anonymised
- [ ] Loom offered
- [ ] One explicit exclusion and one guarantee sentence
- [ ] "any questions" close
- [ ] No em dashes
- [ ] No dialed phone number, no email, no off-platform contact route
- [ ] Bid is 200% to 500% of the posted budget, or above our $1,200 floor if the budget is unposted
- [ ] Client payment is verified. 24.0% of postings are not
- [ ] Fixed price with milestones, unless this is a tuning retainer
- [ ] Sent within 5 minutes of the post where possible. Under 5 minutes replies at 8.99%

---

## Logging

```bash
python3 hub.py log --platform upwork --account TODO-frankie --entity proposal \
  --ref job-abc123 --action sent \
  --detail "dealership BDC voice agent, fixed price, hook on daytime abandon rather than after-hours" \
  --metric connects=12 --metric bid_usd=3500 --metric posted_budget_usd=800 \
  --metric bid_pct_of_budget=437 --metric cliches=0 --metric words=232 \
  --metric minutes_since_post=4 --metric boosted=0 --actor frankie
```

Every proposal, every time. The interview rate is the second-most-predictive leading indicator in the whole system and it is unknowable without this line.
