# Playbook: case study capture

Run this at delivery, every time, on every order. Not later, not "when there is a lull".

Two reasons the timing is not negotiable. First, the before numbers stop existing the moment the new system is live, and nobody can reconstruct them afterwards. Second, the client is never more willing to say something generous than in the hour they see the thing work.

A marketplace account with no proof is a price negotiation. A marketplace account with measured proof is a credential.

---

## 1. Capture at kickoff, not at delivery

The before numbers have to be collected **before anything ships**. Put this in the first message after the order starts.

| Capture | Why | Source |
|---|---|---|
| Calls per week, inbound and outbound split | Denominator for everything else | Client's phone system or CRM export |
| Answer rate, or unanswered call count | The single most persuasive before number in this vertical | Same |
| Average time to first response on a lead | Speed is the whole argument | CRM |
| After-hours and weekend call volume | Where the agent earns its keep | Phone system |
| What happens today when nobody picks up | Qualitative, one sentence | Ask |
| Headcount currently on the phone | Cost framing, never used to promise a headcount cut | Ask |
| Existing vendor and its measured latency, if any | The only fair comparison basis | Archived call recordings |

Record it as an event so it is not sitting in a chat thread:

```bash
python3 hub.py log --platform fiverr --account hanfluxai --entity order \
  --ref FO12345 --action baseline_captured \
  --detail "pre-build baseline collected from the client's phone system export, week of 2026-10-06" \
  --metric calls_per_week=480 --metric answer_rate_pct=58 --actor chitraksh
```

---

## 2. Capture at delivery

| Capture | Rule |
|---|---|
| The same metrics, measured the same way | A different measurement method makes the comparison worthless. Say how it was measured, both times |
| Time to first audio, median, with the sample size | State whether it was simulated calls or production calls. Never blur the two |
| What the agent completed without a human | Countable: bookings, transfers, CRM writes |
| What it handed off and why | The honest half. This is what makes the rest believable |
| Known limitations still present | Stated plainly |
| Date every number was read | On the same line as the number, always |

---

## 3. Screenshots

Collect these at delivery, while the environment still looks the way it did:

- Call detail view showing a real logged call, masked.
- Dashboard KPI tiles.
- Latency waterfall, per-stage.
- Compliance panel showing disclosure and consent state.
- The workflow canvas or flow diagram, if one applies.

### Masking rules, applied before the file leaves the machine

Mask at capture. A masked copy and an unmasked copy in the same folder is how the unmasked one ships.

| Must be masked or removed | Method |
|---|---|
| Phone numbers, every digit, including the dialed number and any caller ID | Solid block, not a blur. Blur is reversible enough to be a problem |
| Caller names, email addresses, street addresses | Solid block |
| Account numbers, VINs, policy numbers, claim numbers | Solid block |
| Client business name, logo, domain, branded colours in the UI chrome | Crop out or replace with a neutral label |
| Staff names in assignment fields | Replace with a role label, for example "Advisor 1" |
| URLs containing a tenant id or client subdomain | Crop the address bar entirely |
| Timestamps precise enough to identify a single real customer | Keep the date, drop the seconds, or shift the whole set consistently |

Use the product's PII-masked dashboard views wherever they exist. That is what they are for.

Then look at the finished image one more time, deliberately, before it goes anywhere. Reflections in screenshots, browser tab titles, notification toasts and autocomplete dropdowns have all leaked a client name at least once for somebody.

---

## 4. The client quote request

Send it at delivery, in the delivery message or right after. Not weeks later.

> Two things before I close this out.
>
> First, would you be open to me describing this build publicly without naming you? It would read as "a franchise dealership in the Midwest" or similar, with the numbers we measured together and nothing that identifies the business. I will send you the exact wording for approval before it goes anywhere.
>
> Second, if the result was useful, a sentence or two on what changed would help me more than anything else. Whatever you write is yours. I will not suggest wording, and if you would rather not, that is genuinely fine.

**The two rules inside that message are not stylistic.**

1. **Never suggest wording for a review, and never ask for a specific rating.** Coaching a review is the fastest route off a marketplace. Ask for the order, deliver the work, and say nothing about what the review should contain.
2. **Public use is opt-in and the client approves the exact wording.** Not a general permission, the actual sentences.

Log the answer either way:

```bash
python3 hub.py log --platform fiverr --account hanfluxai --entity review \
  --ref FO12345 --action quote_permission_granted \
  --detail "client approved the anonymised description, approved wording saved in the order thread" \
  --actor chitraksh
```

---

## 5. Anonymisation rule

The standing rule, and it holds even when the client has said yes:

- **No client, dealership, agency or individual is ever named in public copy.** Not in a gig, a portfolio entry, a proposal, an ad, a post, or a message to another buyer.
- A vertical descriptor is allowed where it is genuinely generic: "a Mercedes-Benz franchise dealership" describes a brand franchise, not a business identity. "Dave's Mercedes of Springfield" is a business identity. The test is whether a reader could find them.
- Region goes no finer than a large region. "Midwest" yes. "a suburb of Columbus" no.
- Numbers that would identify the business by size get rounded or banded.
- If the client is the only business in their category with that characteristic, the characteristic comes out, even if it is the interesting part.

**Oraya never implies licensure.** Any insurance-side case study states that the licensed producer fronts licensed activity, or it does not mention licensed activity at all.

---

## 6. The hard rule on numbers

Every published figure is either measured and labelled with its method and date, or it does not appear.

- Measured on simulated calls says "measured on simulated calls", with the date.
- Measured on production calls says so, with the sample size.
- A design target is never quoted to a buyer. A target published as a claim is a fabricated metric with extra steps.
- No answer rate, booking rate, calls-handled or customers-served figure appears anywhere until one exists as a measured number.
- Anything that lives outside a folder that has actually been read stays out of the portfolio, however good it sounds. Publishing an unverified number on an account whose entire premise is measurement is the one mistake that cannot be walked back.

---

## 7. The output

One markdown file per delivery, in the repo, containing:

1. Vertical and anonymised descriptor.
2. The problem, in the client's framing.
3. Before numbers, with method and date.
4. What was built, as countable deliverables.
5. After numbers, same method, same rigour, with date.
6. Limitations still present.
7. Masked screenshots, listed by file.
8. Approved client quote, if any, with the date permission was given.
9. Which gig or proposal this proof belongs to.

Then log it, so the proof is discoverable from the ledger rather than from memory:

```bash
python3 hub.py log --platform fiverr --account hanfluxai --entity order \
  --ref FO12345 --action case_study_captured \
  --detail "anonymised case study written, 4 masked screenshots, client quote approved 2026-11-02" \
  --actor chitraksh
```
