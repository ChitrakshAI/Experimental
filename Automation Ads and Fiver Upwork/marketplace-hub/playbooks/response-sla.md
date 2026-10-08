# Playbook: response SLA

## The rule

**Every buyer message gets a real reply inside 60 minutes, between 08:00 and 23:00 IST. Inside 8 hours overnight.**

Not an acknowledgement. A reply that moves the conversation.

## Why it is the cheapest lever on the list

Response time is a direct ranking input. Sellers who consistently respond within one to two hours rank above sellers who do not, all else equal, and a sub-one-hour response time consistently places a seller better than a six-hour one. It costs nothing, it needs no approval, and it works from hour one, which is more than can be said for anything else available to a new account.

Two things follow:

- **Install the mobile app and turn notifications on.** This is the entire implementation.
- **Never let the auto-response placeholder answer for you.** The platform counts it. Buyers do not.

There is a second reason, quieter and more expensive to get wrong. Private feedback is collected invisibly after every order and feeds ranking separately from the public review. A five-star public review can sit next to negative private feedback. Communication quality, not just delivery quality, moves ranking.

---

## The shape of a first reply

Four lines, in this order, every time:

1. **Answer the question they actually asked.** Directly, in the first line. Do not open with a greeting and bury the answer in paragraph three.
2. **One qualifying question.** One. It has to be a question that only someone who has built this would ask.
3. **The honest boundary.** Say what you will not do, or what you do not yet know, before they find it.
4. **A next step with a duration.** Named and specific.

What never appears in a first reply: a price drop, an off-platform contact detail, a promise about timing you have not checked, a superlative, an emoji, an em dash.

---

## Canned first replies

Load these into Quick Responses. Edit the specifics before sending: a canned reply that reads canned is worse than a slow one.

### Universal opener, when the message is just "hi" or "are you available"

```text
Yes, available. Two questions so I can answer properly rather than guess.

Roughly how many calls a week, and what should the agent be able to finish on its own without a human?

I will tell you which package fits. I will also tell you if none of them do.
```

---

## Gig 1: AI voice receptionist for car dealerships and insurance agencies

### Asks about price

```text
The three tiers cover most of what comes through, and the difference between them is scope, not quality.

Starter Line at $450 is one agent, one direction, a single call flow, live on your number in 5 days. Front Desk at $1,200 adds multiple intents, calendar booking and a CRM write. Production at $2,800 is the full build with the compliance surface, post-call extraction and 21 days to get it right.

Tell me what the agent should be able to finish on its own and I will tell you which one you actually need, including if that is the cheapest one.

I do not discount the published prices. If the scope is close but not exact, I will add an extra rather than move the number.
```

### Asks about latency or how fast it sounds

```text
Median 761 ms to first audio, measured on simulated calls on 26 August 2026. The vendor stack that build replaced measured 1.64 to 1.9 s across 17 archived production calls.

Two things matter as much as the median. It stops the instant a caller interrupts, and the disclosure at the start is fixed text concatenated outside the model, so it never drifts and never adds a delay that varies.

Those figures are from my own test calls, and I will say so on every number I give you. If you want a number measured on your traffic, that comes from the tuning period after go-live, not from me before it.
```

### Asks about compliance

```text
The short version: the agent says it is an AI and that the line is recorded, as the first thing on every call, in fixed text the model never generates and cannot skip or reword.

Underneath that, consent state, quiet hours and Do-Not-Call are code gates, not instructions in a prompt. That distinction is the whole point: a prompt is a request, a gate is a refusal.

I trained as a lawyer before I built this and I read the statutes myself: TCPA, 47 CFR 64.1200, the FCC's 2024 position that an AI voice is an artificial voice, CIPA 632 and 632.7, and California AB 2905.

This is engineering, not legal advice, and I am not your attorney. Have your own counsel review the consent language before you go live. I will give you the exact text to send them.
```

### Asks about a different vertical

```text
Honest answer: the engine is vertical-agnostic, the expertise is not.

What transfers to any vertical is the telephony, the sub-second response path, the interruption handling, the disclosure and consent architecture, and the post-call extraction into your systems. That is most of the build.

What does not transfer for free is the domain: the intents, the objections, the vocabulary and what counts as a good outcome on a call. For dealerships and insurance agencies I already have that. For yours I would be learning it from you, which is workable and which I would rather say now than discover in week two.

Tell me the vertical and the call types. If I think someone else is a better fit, I will say so.
```

---

## Gig 2: AI cold calling agents, TCPA consent, DNC and quiet hours gating

### Asks about price

```text
Audit at $350 is a written review of your current calling setup against TCPA and the state rules, plus the consent and disclosure script text, in 3 days. It is standalone and useful even if you never build anything with me.

Gated Dialer at $1,200 is the working outbound agent with consent basis, Do-Not-Call, quiet hours and allowlist gating in code, in 12 days. Full Pipeline at $2,800 adds the second flow, the audit trail and the CRM integration.

Most people should start with the Audit. It usually changes what the build should be.
```

### Asks about latency

```text
Median 868 ms to first audio on the outbound orchestrator, measured on simulated calls on 26 August 2026.

On outbound the number that decides the outcome is not the median anyway. It is what happens in the first two seconds after the connect: the disclosure has to land, cleanly and identically, every time, before anything else. That text is concatenated outside the model, so it is the same on call one and call ten thousand.
```

### Asks about compliance

```text
This is the part of the gig that is actually the gig.

Four gates run before the dialer is allowed to place a call: consent basis on file, Do-Not-Call clear, local time inside quiet hours in the callee's own time zone, and allowlist pass. Fail any one and the call does not get placed. They are code, not a line in a prompt the model can talk itself past.

Written from TCPA, 47 CFR 64.1200, the FCC's 2024 artificial-voice ruling, CIPA 632 and 632.7, California AB 2905, and the 5-year retention requirement at 16 CFR 310.5.

Two boundaries, stated up front. I do not sell or source lead data: you bring the list and the consent records. And this is engineering, not legal advice. Your counsel reviews the consent language, and I will hand you the exact text for that review.

What is your consent basis on the list today?
```

### Asks about a different vertical

```text
The gating is vertical-neutral, which is unusual and is why this gig exists. Consent basis, Do-Not-Call, quiet hours and allowlist are the same four checks whether you are calling dealership service customers or clinic patients.

What changes by vertical is which rules stack on top. Some verticals carry a whole second regime, and if yours is one of them I will tell you that before you order rather than after.

Tell me the vertical, the states you call into, and where the consent comes from. If there is a regime I would be learning rather than one I already know, you will hear it from me first.
```

---

## Gig 3: n8n AI agent workflows, production error handling and monitoring

### Asks about price

```text
Workflow at $250 is one production workflow with retries, a dead-letter path and alerting, in 4 days. Agent System at $750 is a multi-step agent with tools and state, in 8 days. Pipeline at $2,000 is the full build across your integrations with cost telemetry and a runbook, in 15 days.

Send me your integrations list first. I will confirm feasibility before you order, and if one of your integrations has no usable API I would rather tell you that now than after you have paid.
```

### Asks about latency or reliability

```text
Latency is rarely the problem in workflow automation. Silent failure is.

Most automations do not break loudly. They break in week three and nobody finds out until a customer does. So every external call gets retry with backoff, everything that still fails lands in a dead-letter path instead of vanishing, and an alert fires the moment it does. Writes are idempotent, so a replayed webhook never double-writes your CRM.

I hold ordinary workflows to the standard I use on live phone infrastructure, where a failed webhook is a customer still on the line.
```

### Asks about compliance

```text
Two parts to this.

If the workflow touches calling, messaging or recording, the same rules as my voice work apply: consent basis, quiet hours, Do-Not-Call, disclosure. I build those as gates in the flow, not as instructions in a prompt.

If it is data movement, the questions are different and I will raise them rather than wait: what personal data moves, where it lands, who can read it, and how long it is kept. I build with row-level security and masked read views by default.

Engineering, not legal advice. Your counsel signs off on the policy. I make the system do what the policy says.
```

### Asks about a different vertical

```text
Workflow automation is the most portable of the three things I do. The patterns transfer completely: retries, dead-letter handling, idempotency, alerting, cost telemetry, a runbook your team can follow at 2am.

What I need from you is the integrations list and one sentence on what a failure costs when it happens. That second answer decides how much of the build is machinery and how much is monitoring.
```

---

## Messages that need a different reply entirely

| Message | Response |
|---|---|
| Asks for a lower price | Concede scope, never price. Offer an extra at no charge. The order value on record stays where it is |
| Asks to move to email, WhatsApp or a call off-platform | Decline and keep it on the platform. Taking business off-platform is a named account warning. Say the escrow and the contract are the reason, because they are |
| Asks whether AI is used in the build process | Answer plainly and immediately. No hedging |
| Asks to clone a specific named person's voice | Only with that person's recorded consent, reviewed before go-live. Otherwise licensed stock voices |
| Asks you to buy or scrape a lead list | Decline. Prohibited, and not the business |
| Describes a scope none of the packages fit | Custom offer. Never a fourth published package |
| Looks like it would end in a cancellation | Qualify harder, or decline the order. A cancellation costs more ranking than the order was worth |

---

## Logging

Log a message only when something happened that changes state: a qualified lead, a custom offer sent, a decline, an off-platform request refused. Do not log every hello, and do not paste buyer personal data into the ledger.

```bash
python3 hub.py log --platform fiverr --account hanfluxai --entity message \
  --ref buyer-2026-10-04-a --action qualified \
  --detail "dealership BDC, about 400 calls a week, asked about compliance, sent the gig2 audit tier" \
  --metric response_minutes=18 --actor chitraksh
```

And once, when the templates are loaded:

```bash
python3 hub.py log --platform fiverr --account hanfluxai --entity message \
  --ref quick-responses --action quick_responses_saved \
  --detail "first-reply templates loaded into Fiverr Quick Responses" --actor chitraksh
```
