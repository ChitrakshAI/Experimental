# Playbook: build and publish a Fiverr gig

Audience: whoever is sitting in front of the Fiverr gig editor. This is the exact order of operations, including the interface quirks that waste an hour the first time and thirty seconds every time after.

Copy source: the paste-ready profile package. This file is the **how**, not the **what**. Never retype copy from memory into the editor. Paste it.

Log every step. If it is not in `ledger/events.jsonl`, it did not happen.

---

## 0. Before you open the editor

| Check | Why it is first |
|---|---|
| ID verification passed | Nothing publishes without it |
| W-8BEN submitted | Payout gate for a non-US person |
| India GST declaration submitted | Publishing gate |
| Payout method connected | Confirm it, do not assume it |
| Gig images rendered at 1280 x 769, 72 DPI | The image is the ad. Uploading a placeholder "for now" is how a placeholder ships |
| Copy open in a second window | You will paste seven times per gig |

```bash
python3 hub.py checklist
```

Do the gates first. Every hour spent polishing copy on a listing that cannot publish is an hour spent on nothing.

---

## 1. The five screens, in order

Fiverr's gig editor is five steps: **Overview, Pricing, Description and FAQ, Requirements, Gallery**. It saves per step. You can leave and come back, and a half-finished gig sits as a draft indefinitely.

Log after each screen saves:

```bash
python3 hub.py log --platform fiverr --account hanfluxai --entity gig \
  --ref gig2 --action overview_saved --detail "title, category, service type, five tags" \
  --actor chitraksh
```

---

## 2. Screen 1: Overview

### 2.1 Title

Type only the portion after "I will ". Fiverr prepends it automatically and it counts toward the 80 characters.

Two things lock the moment you save this screen for the first time, and neither can ever be undone:

1. **The URL slug.** It is generated from the title text at first save and is permanent. Save the keyword-exact title first. If you want a friendlier title later, edit the title afterwards: the slug keeps the keywords.
2. **The category.** Categories cannot be changed after publishing. Read the breadcrumb out loud before you save.

Immediately after the first save, **read the URL out of the browser address bar and write the real slug into `accounts.json`.** Do not reconstruct it from the title by hand, because Fiverr's slugification of punctuation is not something to guess at.

### 2.2 Category, the dropdown quirk

The category and subcategory selectors are **custom dropdown widgets, not native `<select>` elements**. Consequences:

- Typing the first letter does not jump to an option.
- Keyboard tab-and-enter is unreliable.
- Automation must **find the option element and click it**, not set a value. A value set programmatically on a custom dropdown looks correct on screen and submits nothing.
- After clicking, confirm the visible label changed before moving on. The click can register on the wrapper instead of the option.

The same pattern applies to service type, metadata dropdowns, delivery time and revisions. Find, click, verify the label, then continue.

### 2.3 Service type and metadata

Select everything you can genuinely deliver and nothing you cannot. Metadata drives filter inclusion. Appearing in a filter you then fail on produces a cancellation, and a cancellation costs far more ranking than the impression was worth.

Note that Gig 3 uses service type **N8n Automation**, not AI Agents. That is deliberate: it is what puts the gig in the workflow-tool filter chip.

### 2.4 Tagline and short fields, the punctuation quirk

**The tagline field rejects punctuation.** Commas, colons, full stops and ampersands are silently stripped or refused depending on the field, and the error message, when there is one, does not say which character caused it. Write taglines as plain words with spaces. If a field refuses a string you believe is valid, remove the punctuation one character at a time before you start doubting the length.

Related: several short fields count characters differently from what you see. Trust the on-screen counter over any number written in a copy document, including this repo's own.

### 2.5 Search tags

Five slots. Fill all five.

- **Tags must match Fiverr's autocomplete.** A tag typed freehand that does not match a suggestion may be accepted into the box and then do nothing for reach. Type a few letters, wait for the suggestion list, pick from it. If your intended phrase never appears in autocomplete, it is not a live keyword: choose the nearest one that is.
- Do not duplicate words already in the title. Tags extend reach, they do not reinforce it.
- Each tag is 20 characters or fewer.

The same autocomplete rule applies to the **skills** list on the profile: skills must be selected from the autocomplete list, not typed as free text. A skill that does not resolve to a real entry is decoration.

---

## 3. Screen 2: Pricing

Three tiers. Enter them exactly as written in the package source.

Quirks:

- **Package name caps at roughly 20 characters** and the counter is easy to miss. Every planned name is 13 characters or fewer, so this should never bite.
- **Package description caps at 100 characters.** Long descriptions are truncated in the comparison table without warning.
- At least one revision option is required per package.
- Delivery time and revisions are the same custom dropdowns as the category. Find, click, verify.
- **Extras title caps at 20 characters.** Several of the planned extra titles in the copy source are written long, for example `30 days of tuning and weekly latency report`. They will not fit. Shorten to fit the 20-character field and keep the full sentence for the description and the delivery message:

| Full intent | 20-char field |
|---|---|
| Extra call flow or intent branch | `Extra call flow` |
| Outbound module, consent and DNC gated | `Outbound module` |
| 30 days of tuning and weekly latency report | `30 days tuning` |
| Second campaign flow, configured and gated | `Second campaign flow` |
| State-by-state calling matrix | `State calling matrix` |
| Consent and disclosure audit trail dashboard | `Consent audit trail` |
| Custom MCP server, source included | `Custom MCP server` |
| 30 days of monitoring and on-call fixes | `30 days monitoring` |

Count them yourself in the editor. Do not trust the table above blind.

- **Extra fast delivery:** enable it only on the `gig3` Workflow tier. Never on a telephony build. A telephony cutover cannot be safely compressed and a missed fast-delivery clock is a late delivery on your permanent record.

Pricing discipline, which is a positioning rule and not a preference:

- Never discount a published package price. Not once.
- Concede scope, not price. Add an extra for free instead of lowering the number.
- Anything above the top tier goes out as a custom offer, not as a fourth published package.

---

## 4. Screen 3: Description and FAQ

### 4.1 Description

**Hard cap 1,200 characters.** This is the single most common surprise, because the paste-ready copy reads short and counts long.

- Paste, then read the counter. If it is over, cut whole sentences, never adjectives. Cutting adjectives produces limp copy at 1,199 characters.
- The editor's rich-text controls insert markup that counts. Paste as plain text where the option exists.
- Line breaks count.
- No phone number, no email, no URL anywhere in the description. That is a named denial trigger, not a style note.
- Every gig description states that the build is configured for one client. Selling a product rather than a per-client service is a named denial reason.

### 4.2 FAQ

Up to 10 entries. Question caps at roughly 70 characters, answer at roughly 300.

Required FAQs, because each one defuses a specific denial or cancellation risk:

- "Is this a template you resell?" answered by distinguishing the reused engine from the per-client configuration.
- The engineering-not-legal-advice line, first FAQ on Gig 2, with an explicit instruction that the buyer's own counsel reviews the consent language.
- The agent identifies itself as AI on every call, in fixed text outside the model.
- Voice cloning of a real person only with that person's recorded consent, otherwise licensed stock voices.
- The call-length ceiling, disclosed before the order rather than after.

---

## 5. Screen 4: Requirements

Buyer requirement questions cap at roughly 200 characters each.

The requirements screen is a qualification filter, not paperwork. A pre-order question that surfaces a mismatch before the order exists prevents a cancellation, and a cancellation costs more ranking than the order was worth. Gig 2's consent-basis question exists entirely for that reason.

---

## 6. Screen 5: Gallery

- Up to three images, 1280 x 769 at 72 DPI recommended.
- Video 20 to 60 seconds. The platform limit wins over any SEO guidance suggesting longer. Cut to 55 to 60 seconds.
- Thumbnail canvas is 550 x 370. Bold text, clean contrast, visible sample work.
- **Mask the dialed number in every frame and never speak it.** Numbers on screen are a denial trigger.
- PII-masked dashboard views only.
- Upload is slow and occasionally silently fails. Refresh the page and confirm all three images are actually attached before you consider the screen done.

---

## 7. Publish

Publish gigs **staggered**, not all at once: Gig 1 alone in the morning, Gig 2 about four hours later, Gig 3 the next morning. Each gets its own impression pool instead of competing with the others on day one.

The moment a gig is live, verify the slug, then start owned traffic. New gigs get elevated visibility for 48 hours to several weeks while the platform collects data, and orders landed in that window compound into permanent ranking.

```bash
python3 hub.py log --platform fiverr --account hanfluxai --entity gig \
  --ref gig1 --action published --detail "live, slug verified against accounts.json" \
  --actor chitraksh
```

---

## 8. After publishing

| Cadence | Action |
|---|---|
| Every message | Reply inside 60 minutes between 08:00 and 23:00 IST. Response time is a direct ranking input |
| Daily | `monitoring/daily-check.md`, then `hub.py metrics add` |
| Weekly | `playbooks/weekly-review.md`, then `hub.py metrics report` and `hub.py export` |
| Every 45 to 60 days | A small edit to each gig. Freshness is a signal |
| Going quiet | Use Vacation Mode. Genuine inactivity suppresses promotion, Vacation Mode does not |

---

## 9. Quirk index, for fast lookup

| Quirk | Behaviour | Handling |
|---|---|---|
| Category and other dropdowns | Custom widgets, not native selects | Find the option element and click it, then verify the label changed |
| Tagline field | Rejects or strips punctuation | Plain words and spaces only |
| Search tags | Freehand tags can be accepted but do nothing | Pick from autocomplete only |
| Profile skills | Same as tags | Pick from autocomplete only |
| Description | 1,200 character hard cap, markup counts | Paste plain, read the counter, cut sentences |
| Package name | About 20 characters | Keep names at 13 or fewer |
| Package description | 100 characters | Already inside |
| Extras title | 20 characters | Use the short forms in section 3 |
| FAQ | About 70 question, 300 answer, 10 max | Check the counter |
| Requirements | About 200 characters per question | Check the counter |
| URL slug | Locks permanently at first save | Save keyword-exact, then read the real slug from the address bar into accounts.json |
| Category | Cannot be changed after publishing | Read the breadcrumb aloud before saving |
| Gallery upload | Can fail silently | Refresh and confirm all three are attached |
| Video length | 20 to 60 seconds, platform cap | Cut to 55 to 60 |

---

## 10. Denial and warning triggers, each mapped to a rule above

| Trigger | Where it is handled |
|---|---|
| Contact details in a gig | Section 4.1 and section 6. No number, email or URL anywhere, including the video |
| Product instead of a service | Section 4.1. Every description states per-client configuration |
| Copied description | All copy is original to the source package |
| Unclear or misleading packages | Every package states a countable scope. No unbounded promises |
| Taking business off-platform | No off-platform path in any gig field, and none offered in any message |
| Sharing or selling personal data | No lead lists, no scraping, on any gig |
| Unauthorized voice or likeness | Cloning only with the person's recorded consent, stated in an FAQ |
| AI impersonating a human | The agent discloses it is AI, in fixed text outside the model |
| Fabricated metrics | Every number carries its measurement basis and date, or it does not ship |
| Review or order manipulation | Ask for the order, never for what the review says |
