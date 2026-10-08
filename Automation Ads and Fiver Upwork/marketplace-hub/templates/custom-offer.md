# Template: custom offer

Use a custom offer for anything the published ladder does not fit. Never add a fourth published package: the ladder is the positioning, and a fourth tier blurs it.

Rules that hold on every custom offer:

- **Price at or above the nearest published tier.** A custom offer priced below the published ladder tells every future buyer what the real rate is.
- **Countable scope.** Numbers of agents, flows, intents, integrations and revisions. No "unlimited" anything.
- **State one exclusion explicitly.** An honest exclusion buys more trust than another inclusion.
- **Delivery time you can hold on a bad week**, not a good one.
- Nothing off-platform. No phone number, no email, no external payment path.

---

## The offer description field

```text
SCOPE

[N] voice agent[s], [inbound / outbound / direction-aware], on [N] number[s].
[N] call flow[s] covering: [intent 1], [intent 2], [intent 3].
Disclosure and recorded-line notice as fixed first-utterance text, outside the model.
[Consent basis, Do-Not-Call, quiet hours and allowlist gating in code.]
[Calendar booking / warm transfer / CRM write] into [system].
Post-call structured extraction, [N] fields, delivered to [destination].
[N] revisions within [N] days of delivery.

NOT INCLUDED

[The one thing they might assume is in and is not. Say it plainly.]

DELIVERY

[N] days from the day I have [the specific thing you need from them].

WHAT I NEED FROM YOU BEFORE THE CLOCK STARTS

1. [Access or credential]
2. [Content, script or list]
3. [The decision only they can make]

Every figure I quote carries how it was measured and the date. Compliance work here is engineering, not legal advice: your counsel reviews the consent language, and I will give you the exact text to send them.
```

---

## The message that accompanies it

```text
Sent the offer.

Two things worth flagging before you accept.

First, [the honest constraint: a limitation, a dependency, or a thing that could slip]. I would rather you know now.

Second, the clock starts when I have [the specific dependency], not when you accept. If that takes a week to arrange, the delivery date moves by a week and I will say so rather than quietly absorb it.

If anything in the scope is wrong, tell me and I will resend. I would rather rewrite it twice than deliver the wrong thing once.
```

---

## Scope-concession message, when a buyer pushes on price

Never lower the number. Add scope instead. The order value on record stays where it is, and the published price stays the published price.

```text
I hold the published prices, so I am not going to move the number. What I will do is widen what you get for it.

At $[published price] I will add [extra: an additional intent branch / a second week of tuning / a written latency report on your existing line] at no charge. That is worth $[extra price] on the gig and it is the part of the build that usually matters most in month two.

If that still is not the right shape, tell me what you are actually solving for and I will tell you honestly whether I am the right person for it.
```

---

## Logging

```bash
python3 hub.py log --platform fiverr --account hanfluxai --entity proposal \
  --ref offer-2026-10-14-a --action sent \
  --detail "custom offer, dealership group, 3 rooftops, direction-aware agent plus CRM write" \
  --metric price=4200 --metric delivery_days=24 --actor chitraksh
```
