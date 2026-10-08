# First replies: Gig 3, n8n AI agent workflows with production error handling and monitoring

Paste-ready. Edit before sending.

This is the volume gig. It exists to accumulate order count and unique clients, which is what gates the levels, and the $250 tier is the only low anchor allowed anywhere in the ladder. Treat the buyer accordingly: fast, specific, and qualified before the order rather than after.

---

## A. Buyer asks about price

```text
Workflow at $250 is one production workflow with retries, a dead-letter path and alerting, in 4 days. Agent System at $750 is a multi-step agent with tools and state, in 8 days. Pipeline at $2,000 is the full build across your integrations with per-run cost telemetry and a runbook, in 15 days.

Send me your integrations list first. I will confirm feasibility before you order, and if one of them has no usable API I would rather tell you that now than after you have paid.

Which systems need to talk to each other, and what triggers the flow?
```

---

## B. Buyer asks about latency or reliability

```text
Latency is rarely the problem in workflow automation. Silent failure is.

Most automations do not break loudly. They break in week three and nobody finds out until a customer does. So every external call gets retry with backoff, everything that still fails lands in a dead-letter path instead of vanishing, and an alert fires the moment it does. Writes are idempotent, so a replayed webhook never double-writes your CRM.

I hold ordinary workflows to the standard I use on live phone infrastructure, where a failed webhook is a customer still on the line.

What happens today when one of your automations fails?
```

---

## C. Buyer asks about compliance

```text
Two parts to this.

If the workflow touches calling, messaging or recording, the same rules as my voice work apply: consent basis, quiet hours, Do-Not-Call, disclosure. I build those as gates in the flow, not as instructions in a prompt.

If it is data movement, the questions are different and I will raise them rather than wait: what personal data moves, where it lands, who can read it, and how long it is kept. I build with row-level security and masked read views by default, and the dashboard reads the masked views rather than the raw tables.

Engineering, not legal advice. Your counsel signs off on the policy. I make the system do what the policy says.
```

---

## D. Buyer asks about a different vertical

```text
Workflow automation is the most portable of the three things I do. The patterns transfer completely: retries, dead-letter handling, idempotency, alerting, per-run cost telemetry, and a runbook your team can follow at 2am.

What I need from you is the integrations list and one sentence on what a failure costs when it happens. That second answer decides how much of the build is machinery and how much is monitoring, and it is the question most people have never been asked.
```

---

## Qualification before accepting

Ask these before the order, not after. A pre-order question that surfaces a mismatch prevents a cancellation, and a cancellation costs more ranking than the order was worth.

- Which systems, and do you have API access and credentials to all of them?
- Self-hosted n8n or cloud? Which version?
- What triggers the flow, and roughly how often does it run?
- What does a failure cost when it happens?
- Is there an existing flow to extend, or is this greenfield?

If any integration is a closed system with no API, say so before the order and adjust the scope in writing.
