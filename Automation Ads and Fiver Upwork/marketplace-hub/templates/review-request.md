# Template: review request

## The two rules, before any wording

1. **Never suggest what a review should say. Never ask for a rating or a number of stars. Never offer anything in exchange for one.** Coaching a review is the fastest route off a marketplace, and it is an account-termination risk rather than a warning.
2. **Ask once.** A second ask reads as pressure, and pressure shows up in private feedback where you will never see it.

Ask for feedback. Do not ask for a good review. The distinction is not a technicality: it is the whole difference between a request and a manipulation.

---

## Send it after the delivery has settled

Not inside the delivery message. Give the buyer a day or two to actually use the thing, then send this.

```text
Checking in now that it has had a few days of real traffic.

Two questions, and neither is rhetorical.

Is it doing what you expected? If anything is off, tell me and I will fix it. That is what the revisions are for and I would rather you use them than live with something that is 80 percent right.

And if it has been useful, would you leave feedback on the order? Whatever you write is yours. I will not suggest wording and I am not going to ask twice.

Either way, thank you for the work. It was a good problem.
```

---

## Variant: when the buyer has already said something positive in the thread

```text
Glad it landed.

If you would be willing to put a version of that on the order as feedback, it helps me more than anything else does at this stage. Entirely your call and entirely your words.

And the offer stands on the revisions: if anything drifts in the next [N] days, send it over.
```

---

## Variant: when the order did not go perfectly

Ask anyway, and ask honestly. A four-star review with a fair comment costs less than a silence that shows up as negative private feedback nobody can answer.

```text
Before I close this out: [the thing that went wrong] was on me, and here is what I changed so it does not happen on the next one: [specific change].

If you have feedback on the order, positive or otherwise, I would rather have it than not. An honest account of what went wrong is more useful to me than a generous one.

If there is anything still outstanding, say so now and I will deal with it before this closes.
```

---

## The anonymised-use request

Separate ask, separate message, because it is a different question and bundling them makes both sound transactional.

```text
One more thing, unrelated to the order.

Would you be open to me describing this build publicly without naming you? It would read as "[a franchise dealership in the Midwest]" or similar, with the numbers we measured together and nothing that could identify the business.

I would send you the exact wording for approval before it goes anywhere, and if the answer is no that is genuinely fine.
```

Log the answer either way, so nobody has to reconstruct permission from a chat thread six months later:

```bash
python3 hub.py log --platform fiverr --account hanfluxai --entity review \
  --ref FO12345 --action quote_permission_granted \
  --detail "anonymised description approved, exact wording confirmed in the order thread on 2026-11-02" \
  --actor chitraksh
```

And when the review lands:

```bash
python3 hub.py log --platform fiverr --account hanfluxai --entity review \
  --ref FO12345 --action received \
  --detail "public review received" --metric stars=5 --actor chitraksh
```

---

## Never

| Never | Because |
|---|---|
| Suggest wording for a review | Review manipulation, termination risk |
| Ask for five stars, or any number | Same |
| Offer a discount, an extra or anything else for a review | Same |
| Ask more than once | Pressure surfaces in private feedback |
| Respond to a critical review defensively | The reply is read by every future buyer, not by the one who wrote it |
| Ask the buyer to remove or edit a review | Named prohibited behaviour on every marketplace that has reviews |
