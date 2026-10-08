# Template: delivery message

The delivery message is the last thing the buyer reads before they decide what to write in a review and, invisibly, in private feedback. Private feedback is collected after every order and feeds ranking separately from the public star rating, which means a delivery that is technically complete and communicatively thin still costs ranking.

Structure: what was built, how it was measured, what it cannot do, how to operate it, what happens next.

Nothing in a delivery message asks for a review, suggests review wording, or names a rating. That request lives in `templates/review-request.md` and it is deliberately separate.

---

## The message

```text
Delivered. Here is what is in the package and how to check it yourself.

WHAT IS LIVE

[N] agent on [number or channel], handling [intent 1], [intent 2], [intent 3].
Disclosure and recorded-line notice are the first thing on every call, as fixed text outside the model.
[Consent basis, Do-Not-Call, quiet hours and allowlist gates are enforced before a call is placed.]
[Booking writes to [calendar]. Transfers route to [destination]. Post-call extraction writes [N] fields to [system].]

MEASURED, NOT ESTIMATED

Median time to first audio: [N] ms, measured across [N] [simulated / production] calls on [date].
[Second measurement, same treatment.]

Every number above says how it was measured and when. If you measure it differently you will get a different figure, so here is exactly what I did: [one sentence of method].

WHAT IT DOES NOT DO

[Limitation 1, plainly.]
[Limitation 2, including any wall-clock or call-length ceiling.]
[What it hands off to a human, and why that is the right call rather than a gap.]

HOW TO OPERATE IT

[Where to see calls and transcripts.]
[How to change [the thing they will want to change first].]
[Who to contact and what to send if something looks wrong.]
[Runbook attached: what to do at 2am, in order.]

YOUR REVISIONS

You have [N] revisions in this package, and [N] days to use them. A revision is a change to what we agreed. If you want something outside that scope, say so and I will tell you plainly whether it is a small addition I will just do, or a separate piece of work.

WHAT I WOULD DO NEXT, IF IT WERE MINE

[One specific, honest recommendation, including "nothing for 30 days, let it run and gather data" if that is the true answer.]

Compliance work here is engineering, not legal advice. I am not your attorney. Have your own counsel review the consent and disclosure language before you scale this up. The exact text is in the attached file so you can send it to them without retyping anything.
```

---

## Attachments checklist

- [ ] The working system, or credentials and access to it
- [ ] Runbook: failure modes, what to check, in what order
- [ ] The disclosure and consent text as a plain file, ready to send to counsel
- [ ] Measurement method, written down, so the numbers can be reproduced
- [ ] Screenshots, PII masked, solid blocks and not blurs
- [ ] Source or export where the package includes it

---

## Logging

```bash
python3 hub.py log --platform fiverr --account hanfluxai --entity order \
  --ref FO12345 --action delivered \
  --detail "gig1 Front Desk tier, dealership service intake, 3 intents, delivered on day 9 of 10" \
  --metric price=1200 --metric delivery_days=9 --actor chitraksh
```

Then, the same day, run `playbooks/case-study-capture.md`. The before numbers stop existing the moment the new system is live.
