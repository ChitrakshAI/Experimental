# Playbook: weekly review

Thirty to forty minutes, same day every week. Suggested: Monday morning, before the inbox is open.

The daily check collects. The weekly review decides. Keeping those separate is the point: decisions made from a single day's numbers are noise, and decisions deferred indefinitely are drift.

---

## 0. Open the numbers first

```bash
cd marketplace-hub
python3 hub.py status
python3 hub.py metrics report
python3 hub.py checklist
```

Read all three before forming an opinion. Reading the report after you have decided what happened is how a bad week becomes a good story.

---

## 1. Blockers (5 minutes)

Every open blocker, out loud, with one of three answers:

- **Cleared this week.** Close it. `--entity blocker --action closed`
- **Still blocked, and here is the next concrete step.** Open a task with a due date.
- **No longer relevant.** Close it with the reason written down.

A blocker that has been open three weeks with no movement is not a blocker. It is a decision nobody has made. Make it.

---

## 2. Overdue next actions (5 minutes)

`status` flags OVERDUE. For each one:

- Do it now if it takes under two minutes.
- Re-due it with a real date if it is still worth doing.
- Close it as `cancelled` if it is not, with the reason.

Never silently carry an overdue task into a fourth week. A task list nobody trusts stops being read.

---

## 3. The funnel, one stage at a time (10 minutes)

Read `metrics report` in funnel order and stop at the first stage that is broken. Fixing a downstream stage while an upstream one leaks is wasted work.

| Stage | Number | What a bad reading means | The fix |
|---|---|---|---|
| Visibility | impressions | The listing is not being surfaced | Tags, title keywords, category, freshness edit |
| Interest | clicks, CTR | It is being surfaced and skipped | The image first, then the title, then the price shown in the card |
| Consideration | messages | Clicked and not contacted | The description's first three lines, the package comparison, the FAQ |
| Conversion | orders | Contacted and not bought | The first reply, qualification, the price ladder |
| Delivery | on-time, revisions | Bought and not smooth | Scope definition, buyer requirements |
| Reputation | rating, private feedback, Success Score | Delivered and not loved | Communication cadence during the order |

**One change per gig per week.** Two changes make the result unattributable, and an unattributable result teaches nothing. Write the change into the ledger with the hypothesis attached:

```bash
python3 hub.py log --platform fiverr --account hanfluxai --entity gig \
  --ref gig1 --action optimised \
  --detail "swapped image 1 for the 761 ms headline. Hypothesis: CTR is the constraint, not impressions. Read again in 7 days." \
  --actor chitraksh
```

Next week, read the same number and say whether the hypothesis held. That sentence is the entire value of the ledger.

---

## 4. Leading indicator flags (5 minutes)

`metrics report` prints flags at the bottom. Each is a prompt, not a verdict. Take each one and either act or write down why not.

The two that outrank everything else:

- **Response time over 1 hour.** Fix it this week. It is a direct ranking input and it costs nothing.
- **Success Score under the level threshold.** Nothing else on the list matters as much. Under 5.0 puts Level 1 out of reach. Under 7.0 keeps the inbound Briefs channel locked, which means search ranking and owned traffic are the only two channels that exist.

"No flags fired" means no rule matched. It does not mean everything is fine. Read the table yourself.

---

## 5. Level progress (5 minutes)

| | Level 1 | Level 2 |
|---|---|---|
| Days active | 60 | 120 |
| Orders / unique clients | 5 / 3 | 20 / 10 |
| Lifetime earnings | $400 | $2,000 |
| Rating | 4.4+ | 4.6+ |
| Response rate | 80% | 90% |
| Success Score | 5.0+ | 7.0+ |

At a $450 to $2,800 ladder the money bars are trivial: one order clears Level 1's $400 and three or four clear Level 2's $2,000. **The binding constraints are the day counters and the order and unique-client counts.** Nothing done in a given week can move the day counter. What a week can move is the order count and the unique-client count, and those are the numbers to watch.

Count unique clients explicitly. Five orders from two clients does not clear a bar that says three.

---

## 6. Pipeline and proof (5 minutes)

- Orders delivered this week: was a case study captured for each? If not, the before numbers are already gone. `playbooks/case-study-capture.md`.
- Quote permissions requested and received.
- Any proof asset that could go into the portfolio now.
- Anything currently published that is no longer accurate. Numbers age. A measured figure from three months ago still needs its date on it.

---

## 7. Spend (2 minutes)

Only if a campaign is live.

- Spend against the daily cap that was actually set on the platform, not the intended one.
- Cost per message and cost per order this week.
- Any kill rule triggered. If one triggered, it fires. A kill rule you talk yourself out of is not a kill rule.

---

## 8. Write it down (3 minutes)

```bash
python3 hub.py export
```

That writes `reports/YYYY-MM-DD.md`: status, checklist, metrics with deltas, the week's events, in one file. Commit it. The value is not this week's snapshot, it is having twelve of them in a row when a question comes up about what actually changed.

Then log the review itself, with the single decision that came out of it:

```bash
python3 hub.py log --platform fiverr --account hanfluxai --entity account \
  --ref weekly-review --action reviewed \
  --detail "week 2026-W41. Decision: gig2 publishes Monday, gig3 slips a week, verification cleared Thursday." \
  --actor chitraksh
```

---

## 9. The four questions to end on

1. What did I learn this week that I did not know last week?
2. What number moved, and do I know why?
3. What is the single binding constraint right now, and is this week's work aimed at it?
4. What am I doing because it is comfortable rather than because it is the constraint?

If the honest answer to question 1 is "nothing", the week was spent on activity rather than on learning, and the next week's plan should be built to produce an answer.
