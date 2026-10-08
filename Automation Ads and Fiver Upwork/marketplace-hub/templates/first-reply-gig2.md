# First replies: Gig 2, AI cold calling agents with TCPA, DNC and quiet hours gating

Paste-ready. Edit before sending.

This gig attracts two kinds of buyer: the one who wants the calling and has not thought about consent, and the one who has been told by counsel that they need to. The first needs the gates explained as a feature. The second needs them explained as an architecture. Read which one you have before you answer.

---

## A. Buyer asks about price

```text
Audit at $350 is a written review of your current calling setup against TCPA and the state rules, plus the consent and disclosure script text, in 3 days. It is standalone and useful even if you never build anything with me.

Gated Dialer at $1,200 is the working outbound agent with consent basis, Do-Not-Call, quiet hours and allowlist gating in code, in 12 days. Full Pipeline at $2,800 adds the second campaign flow, the consent and disclosure audit trail, and the CRM integration.

Most people should start with the Audit. It usually changes what the build should be, and it is cheaper to change your mind at $350 than at $1,200.

What is your consent basis on the list today?
```

---

## B. Buyer asks about latency

```text
Median 868 ms to first audio on the outbound orchestrator, measured on simulated calls on 26 August 2026.

On outbound the number that decides the outcome is not the median anyway. It is what happens in the first two seconds after the connect: the disclosure has to land, cleanly and identically, every single time, before anything else happens. That text is concatenated outside the model, so it is the same on call one and on call ten thousand.

A fast agent that drifts on the disclosure is a worse outcome than a slower one that does not.
```

---

## C. Buyer asks about compliance

```text
This is the part of the gig that is actually the gig.

Four gates run before the dialer is allowed to place a call: consent basis on file, Do-Not-Call clear, local time inside quiet hours in the callee's own time zone, and allowlist pass. Fail any one and the call does not get placed. They are code, not a line in a prompt the model can talk itself past.

Written from TCPA, 47 CFR 64.1200, the FCC's 2024 artificial-voice ruling, CIPA 632 and 632.7, California AB 2905, and the 5-year record retention requirement at 16 CFR 310.5.

Two boundaries, stated up front. I do not sell or source lead data: you bring the list and the consent records, and I build the machine that calls them safely. And this is engineering, not legal advice. Your counsel reviews the consent language, and I will hand you the exact text for that review.

Where does the consent on your current list come from?
```

**Variant, buyer says they do not have consent records**

```text
Then the build is not the first problem, and I would be doing you no favours by starting with it.

The Audit tier at $350 exists for exactly this. You get a written read on what basis you actually have, what the gates would need to check, and the consent and disclosure language, in 3 days. If the answer is that the current list cannot be called the way you were planning, you will know that for $350 instead of finding out later.

Engineering, not legal advice. Your counsel makes the call on the basis. I tell you what the system would have to enforce.
```

---

## D. Buyer asks about a different vertical

```text
The gating is vertical-neutral, which is unusual and is why this gig exists. Consent basis, Do-Not-Call, quiet hours and allowlist are the same four checks whether you are calling dealership service customers or clinic patients.

What changes by vertical is which rules stack on top. Some verticals carry a whole second regime, and if yours is one of them I will tell you that before you order rather than after.

Tell me the vertical, the states you call into, and where the consent comes from. If there is a regime I would be learning rather than one I already know, you will hear it from me first.
```

---

## Requests to decline on this gig

| Request | Reply position |
|---|---|
| Buy or scrape a lead list | Decline. Sharing personal data and social scraping are prohibited services, and it is not the business either way |
| Skip or shorten the AI disclosure | Decline. The disclosure is the architecture, not a setting |
| Clone a named person's voice | Only with that person's recorded consent, reviewed before go-live. Otherwise licensed stock voices |
| Call outside quiet hours "just for a test" | Decline. A gate that has an exception is not a gate |
| Confirm that a given calling plan is legal | Decline the framing. Describe what the system enforces, tell them their counsel makes the call, and offer the audit |
