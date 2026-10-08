# First replies: Gig 1, AI voice receptionist for car dealerships and insurance agencies

Paste-ready. Edit the specifics before sending: a canned reply that reads canned is worse than a slow one.

Voice: confident engineer-lawyer. No hype, no superlatives, no emoji, no exclamation marks, no em dashes. Every number carries its measurement basis and the date it was read.

Shape of every reply: answer the actual question in line one, ask exactly one qualifying question, state one honest boundary, close with a specific next step.

---

## A. Buyer asks about price

```text
The three tiers cover most of what comes through, and the difference between them is scope, not quality.

Starter Line at $450 is one agent, one direction, a single call flow, live on your number in 5 days. Front Desk at $1,200 adds multiple intents, calendar booking and a CRM write. Production at $2,800 is the full build with the compliance surface, post-call extraction and 21 days to get it right.

Tell me what the agent should be able to finish on its own without a human, and I will tell you which one you actually need, including if that is the cheapest one.

I do not discount the published prices. If the scope is close but not exact, I will add an extra rather than move the number.
```

**Variant, buyer names a budget below $450**

```text
Below $450 I would be selling you a demo rather than a working line, and you would find that out in week two.

What I can do at that number is scope down rather than price down. One intent, one direction, on your number, nothing else. If that is genuinely useful to you, say so and I will send a custom offer for exactly that.

If it is not, I would rather tell you now than take the order.
```

---

## B. Buyer asks about latency or how fast it sounds

```text
Median 761 ms to first audio, measured on simulated calls on 26 August 2026. The vendor stack that build replaced measured 1.64 to 1.9 s across 17 archived production calls.

Two things matter as much as the median. It stops the instant a caller interrupts, and the disclosure at the start is fixed text concatenated outside the model, so it never drifts and never adds a delay that varies call to call.

Those figures are from my own test calls, and I will say so on every number I give you. A number measured on your traffic comes from the tuning period after go-live, not from me before it.

What does your current hold or answer time look like today?
```

---

## C. Buyer asks about compliance

```text
The short version: the agent says it is an AI and that the line is recorded, as the first thing on every call, in fixed text the model never generates and cannot skip or reword.

Underneath that, consent state, quiet hours and Do-Not-Call are code gates rather than instructions in a prompt. That distinction is the whole point. A prompt is a request. A gate is a refusal.

I trained as a lawyer before I built this and I read the statutes myself: TCPA, 47 CFR 64.1200, the FCC's 2024 position that an AI voice is an artificial voice under the TCPA, CIPA 632 and 632.7, and California AB 2905.

This is engineering, not legal advice, and I am not your attorney. Have your own counsel review the consent language before go-live. I will give you the exact text to send them.

Which states do you take calls from?
```

---

## D. Buyer asks about a different vertical

```text
Honest answer: the engine is vertical-agnostic, the expertise is not.

What transfers to any vertical is the telephony, the sub-second response path, the interruption handling, the disclosure and consent architecture, and the post-call extraction into your systems. That is most of the build.

What does not transfer for free is the domain: the intents, the objections, the vocabulary, and what counts as a good outcome on a call. For dealerships and insurance agencies I already have that. For yours I would be learning it from you, which is workable and which I would rather say now than discover in week two.

Tell me the vertical and the three call types you get most. If I think someone else is a better fit, I will say so.
```

---

## Never in a first reply

A price drop. A phone number, email or any off-platform contact path. A promise about timing you have not checked. A number without its measurement basis. A claim about production scale, because no measured figure for that exists. An em dash.
