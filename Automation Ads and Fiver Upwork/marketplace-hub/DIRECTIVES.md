# Founder directives

Standing orders from the founders, dated, in force until replaced. Every session applies these on top of `CLAUDE.md` and `accounts.json` `never_do`. When a directive and a never-do rule collide, the never-do rule wins and the session says so.

## D1. Maximise clients first (Chitraksh, 2026-09-14)

The objective in the first 30 days is orders and reviews, not margin. The plan in `STRATEGY.md` stands; this directive sets how aggressively it is executed.

- **Launch pricing is allowed.** The first orders on any new listing may go out below the listed ladder. Rules: the discount is offered as a scoped custom offer or a lower starter tier, never as a "review in exchange" deal; the price is logged with the reason `launch_pricing`; the ladder in `accounts.json` is restored after three delivered orders on that listing, and a session proposes the restore in the weekly review.
- **Over-delivery is allowed and encouraged.** Build beyond the written scope when it makes the buyer's result better (an extra workflow branch, a monitoring alert, a second voice persona, a cleaner handoff doc). Log it as `scope_extra` with what was added and the hours it cost, so the weekly review can see whether it converts into reviews and repeat orders.
- **What stays forbidden, exactly as before:** buying reviews, coaching a review, conditioning any discount or extra on a review, accepting an order that is not really delivered, moving a conversation off-platform. Ask for feedback only with `templates/review-request.md`.
- **Speed is part of this.** Every buyer message answered inside 60 minutes. Every first reply uses the matching template and ends with a concrete next step.
- **When in doubt between winning the order and protecting margin, win the order** and log why. The founders will correct the price later if needed.

## D2. Frankie's Upwork account: no Hanflux (Chitraksh, 2026-09-14)

Hanflux is never mentioned on Frankie's account: not in the name, headline, overview, skills, employment, education, portfolio titles or descriptions, catalog listings, specialized profiles, proposals, messages or attachments. Frankie presents as Frankie Alicea, Oraya, US-based, licensed insurance producer. Full playbook: `playbooks/frankie-upwork-setup.md`; step list: `RUNBOOK-FRANKIE-UPWORK.md`.

Agency name decided (Chitraksh, 2026-09-14): **Oraya Labs**, domain orayalabs.ai, created from Chitraksh's Upwork account. Frankie joins it as business manager, and the membership showing "Oraya Labs" on his profile is consistent with this directive. The earlier working name Hanflux AI is retired for the agency.

**Agency scope (Chitraksh, 2026-09-14): much wider than Oraya's dealer and insurance work.** Oraya Labs is presented as the full studio: AI voice agents and telephony, agentic systems that act on real tools, n8n and custom automation, CRM and back-office integrations, document review and risk flagging, local and private LLM deployments, compliance enforced in code. Dealerships and insurance are case studies and catalog listings inside it, never the top-level identity. Same rule as D4 for the Fiverr profile. The positioning block lives in `accounts.json` under the agency record.

## D3. Cloud-first, any model, any surface (Chitraksh, 2026-09-14)

The hub must be operable from any Claude session in the "Upwork/Fiver Automation" project: claude.ai on the web, Cowork, Claude in Chrome, a phone, a scheduled task, and by a lower-effort model. That means:

- Runbooks are literal: numbered steps with the exact tool call, the check that proves the step worked, the ledger line, and the checkpoint update. A session follows the runbook rather than improvising.
- Every step is checkpointed to a project doc the moment it completes, so a session that is cut off resumes at the next step in a fresh session with nothing lost.
- Images are pulled from the Marketplace Asset Library artifact and pushed into the browser with the upload tool, never by asking for the Mac folder. See `CLOUD-AGENT.md` section 5a.

## D4. Profile positioning (Chitraksh, 2026-09-13)

The Fiverr profile presents Chitraksh as lawyer x engineer covering voice agents, workflows, custom automation, document processing and local LLMs, with voice AI leading. Verticals (dealerships, insurance) live in the individual gigs and case studies, not in the top-level profile. Portfolio is quality over quantity: related workflows clubbed into one project; real dashboard and product screenshots kept.
