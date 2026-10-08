# Runbook: Frankie's Upwork account, step by step

Literal steps for any Claude session, any model. Follow them in order. Do not improvise, do not skip the checkpoint. The checkpoint doc is `marketplace-hub/checkpoints/frankie-upwork.json`; the playbook with the reasoning is `playbooks/frankie-upwork-setup.md`; the directives are `DIRECTIVES.md`.

**Resume rule.** At the start of every session: `project_read marketplace-hub/checkpoints/frankie-upwork.json`, find `current_step`, and continue from there. If the checkpoint says a step is `in_progress`, verify in the browser whether it actually completed (the session may have died after the click and before the write), then mark it and move on.

**Checkpoint rule.** After every step: set that step's `status` to `done`, `done_at` to now (ISO UTC), `note` to one line of what was observed, set `current_step` to the next step, `project_write` the JSON back. Then append the ledger line with `hub.py log` (or manually, shape in `CLOUD-AGENT.md` section 3) and `project_write` the ledger. Two writes per step, every step. A step is not done until both writes succeed.

**Hanflux rule.** Before any Save, Publish or Send on this account, search every field you filled for `hanflux` (case-insensitive). If found, remove it and re-check. Log a `hanflux_scan` event with `clean=true`.

**Founder-only steps.** Anything involving sign-in, identity documents, tax forms, payment or withdrawal details is done by Frankie himself. Claude reads the resulting state from the page to verify, never types into those forms.

---

## Phase A: session boot

### A1. Identify who you are working with
Do: if the person has not said, ask once: "Are you Frankie, or Chitraksh working on Frankie's account?" Only Frankie may be signed into this account.
Check: answer received.
Log: none.
Checkpoint: `inputs.actor`.

### A2. Load state
Do: `project_read marketplace-hub/checkpoints/frankie-upwork.json` and `project_read marketplace-hub/NEXT-SESSION.md`. Hydrate `hub.py` and its four data files per `CLOUD-AGENT.md` section 3 if the session can run Python; otherwise log manually.
Check: `current_step` known.
Log: `--entity account --ref session --action session_started --detail "Resumed at <step>" --actor claude`.

### A3. Detect the browser
Do: check which browser tools exist in this session.
- `mcp__claude-in-chrome__*` present: mode **CHROME** (full control, file uploads supported). Call `tabs_context_mcp` once, then `tabs_create_mcp` for a fresh tab.
- Only `mcp__remote-devices__Claude_Browser__*` present: mode **BUILTIN** (full control, no file upload tool; images go through Frankie's own file picker, see step D0).
- Neither: mode **PASTE** (Claude writes every field's text in the reply, Frankie pastes and confirms; Claude logs on confirmation).
Check: mode chosen and written to `inputs.browser_mode`.
Log: `--action browser_mode --detail "<mode>"`.

### A4. Open Upwork and confirm the account
Do (CHROME/BUILTIN): navigate to `https://www.upwork.com/nx/find-work/` . If a login page appears, stop and ask Frankie to sign in himself in that tab; wait; do not type credentials. Then `navigate` to `https://www.upwork.com/freelancers/settings/contactInfo` and `read_page` (or `get_page_text`) to read the name and the profile URL.
Check: signed-in name is Frankie Alicea. If the name is anyone else, stop: wrong account, do not continue.
Log: `--action account_confirmed --detail "Signed in as <name>, profile URL <url>"`.
Checkpoint: `inputs.handle` (the part after `/freelancers/` in the profile URL), `inputs.profile_url`.

---

## Phase B: founder gates (Frankie does, Claude verifies and logs)

For each gate: ask Frankie its state, or read it from the settings pages when in CHROME/BUILTIN mode. Log the state. Do not block later phases on B2 to B7 except where noted.

| Step | Gate | Where to read it | Blocks |
|---|---|---|---|
| B1 | Account exists, own device and payment method | A4 | everything |
| B2 | Identity verification submitted | `https://www.upwork.com/freelancers/settings/identity` or the banner on the profile | publishing the profile in some regions; Rising Talent |
| B3 | US location verification | same page or the profile location badge | US-only job visibility |
| B4 | W-9 submitted | `https://www.upwork.com/freelancers/settings/taxInfo` | withdrawals |
| B5 | Withdrawal method added (separate from Chitraksh's) | `https://www.upwork.com/freelancers/settings/getPaid` | withdrawals |
| B6 | Freelancer Plus subscribed | `https://www.upwork.com/freelancers/settings/membership` | nothing; do on day 1 |
| B7 | Availability Badge on, cap 100 Connects a month | same membership or Connects page | nothing |

Log each as `--entity blocker --ref <gate-id> --action opened|closed --detail "<state read from page or from Frankie>"`. If a URL above has moved, use the Settings menu in the left navigation and note the new URL in the checkpoint `notes`.

---

## Phase C: profile fields

### C0. Collect Frankie's own inputs once
Do: ask for, in one message: a headshot photo (attached in chat), employment history (employer, title, dates, one line each), education, languages, hourly rate he will publish, city on the profile. Save the photo to `/mnt/user-data/outputs/frankie-headshot.<ext>` when it arrives.
Check: all six received. If some are missing, continue with what exists and leave the missing steps `pending`.
Checkpoint: `inputs.*`.

### C1. Profile photo
Do (CHROME): open `https://www.upwork.com/freelancers/<handle>` , click the edit control on the photo, `find` "file input", `file_upload` with `/mnt/user-data/outputs/frankie-headshot.<ext>` and the input's ref. Crop if the dialog asks, Save.
Do (BUILTIN/PASTE): tell Frankie to upload the headshot himself in the photo dialog; confirm when done.
Check: screenshot shows the new photo.
Log: `--entity profile --ref photo --action saved`.

### C2. Headline
Text: `AI Voice and Compliance Systems for Insurance Agencies and Dealerships, US-based`
Do: edit title on the profile page, `form_input` the text, Save. Respect the counter under the field; if it is over, drop ", US-based" first.
Check: page shows the headline.
Log: `--ref headline --action saved`.

### C3. Overview
Do: write the overview in Frankie's voice from the cleared facts in `playbooks/frankie-upwork-setup.md` section 2 (first person, no phone, no email, no URL, no Hanflux, numbers with method and date). Show it to Frankie in the reply before saving; one round of edits max. Then `form_input` into the overview field, Save.
Check: saved text matches; Hanflux scan clean.
Log: `--ref overview --action saved` and `--ref overview --action hanflux_scan --metric clean=1`.

### C4. Skills
Do: add from Upwork's picker, in this order, until the cap: AI Voice Agents (or closest), Conversational AI, Twilio, Telephony, TCPA Compliance, Insurance Lead Generation, Automotive, n8n, Workflow Automation, CRM Integration, AI Agent Development. Type each into the picker, choose the suggestion, never free text.
Check: skills list shows them.
Log: `--ref skills --action saved --detail "<n> skills"`.

### C5. Employment history, C6. Education, C7. Languages, C8. Hourly rate, C9. Location
Do: enter exactly what Frankie supplied in C0. Employment entries describe Oraya as "AI voice agents and workflow automation for insurance agencies and car dealerships" and the insurance role as "licensed life insurance producer". No Hanflux.
Check: each section shows the entry.
Log: one event per section.

### C10. Profile completeness
Do: read the completeness indicator on the profile page.
Check: 100%. If not, the page names what is missing; do that item and re-check.
Log: `--ref completeness --action read --metric percent=<n>`.

---

## Phase D: portfolio (four entries)

### D0. Get the image into the session
Do, for the entry's file:
1. `Artifact action:read_file url:https://claude.ai/artifact/DwQewSj5StuW76xF7MG3bw path:<path from the table>`. The tool prints where it saved the file.
2. Copy it: `cp "<saved path>" /mnt/user-data/outputs/<filename>` (Bash). This is the path the browser upload tool accepts.
3. CHROME: on the portfolio form, `find` "file input" or "upload image", then `file_upload paths:["/mnt/user-data/outputs/<filename>"] ref:<ref> tabId:<tab>`. Never click the upload button itself; it opens a native dialog you cannot see.
4. BUILTIN or PASTE: `SendUserFile` the file so Frankie can download it, tell him the exact filename, and ask him to choose it in the upload dialog. Confirm from a screenshot or his reply.

| Entry | Path in the artifact | Filename | Title | Description source |
|---|---|---|---|---|
| D1 | `assets/portfolio-final/portfolio-2-voice-control-center.png` | `portfolio-2-voice-control-center.png` | AI voice control center for a dealership line | Fiverr P1 text, rewritten in Frankie's voice, Oraya as builder |
| D2 | `assets/portfolio-final/portfolio-3-compliance-audit-ab2905.png` | `portfolio-3-compliance-audit-ab2905.png` | Compliance audit: AI voice disclosure enforced in code | Fiverr P2 text |
| D3 | `assets/portfolio-final/portfolio-4-governance-enforced-in-code.png` | `portfolio-4-governance-enforced-in-code.png` | Governance gates enforced in code, not prompts | Fiverr P3 text |
| D4 | `assets/portfolio-final/portfolio-1-n8n-outbound-pipeline.png` | `portfolio-1-n8n-outbound-pipeline.png` | Post-call outbound pipeline built in n8n | Fiverr P4 text |

Fiverr portfolio text: `research/fiverr-profile-package.md` section 5. Description rules: no client named, Dealer A and Dealer B stay as they are in the image, every number with method and date, no Hanflux, no contact details.

### D1 to D4. Add each entry
Do: on the profile page, Portfolio section, click Add. Fill title, description, role (Oraya, co-founder), completion date (from the Fiverr entry), skills (pick 3 from the C4 list), upload the image per D0, mark it public, Publish or Save.
Check: the entry appears in the portfolio with the image thumbnail. Take one screenshot.
Log: `--entity profile --ref portfolio-<n> --action portfolio_uploaded --detail "<title>, image <filename>"`.
Checkpoint after each entry, not after all four.

---

## Phase E: specialized profile

### E1. Create the insurance specialized profile
Do: Settings, Specialized profiles (or the "Add a specialized profile" control on the profile page). Category: closest to AI and Machine Learning or Automation. Title: `AI Voice Agents for Insurance Agencies, Licensed Producer, Compliance in Code`. Overview: the C3 overview trimmed to the insurance half. Portfolio: D1, D2, D3. Rate: same as general unless Frankie says otherwise.
Check: specialized profile listed and published.
Log: `--ref specialized-insurance --action published`.

---

## Phase F: Project Catalog

### F1. Availability
Do: navigate to `https://www.upwork.com/nx/create-project/` (or Project Catalog under the Find Work menu). Read whether the account may create a project.
Check: yes or no, with the reason shown.
Log: `--entity listing --ref catalog --action availability_checked --detail "<yes|no>: <reason>"`. If no, set F2 and F3 to `blocked` and continue to Phase G.

### F2. Listing 1: AI Voice Receptionist for Car Dealerships and Insurance Agencies
Copy: `research/fiverr-profile-package.md` section 2, rewritten into Upwork's fields (title, description, tiers, requirements, gallery). Tiers $450 / $1,200 / $2,800, or a launch tier below that per `DIRECTIVES.md` D1 if Frankie wants it. Gallery images: `assets/gig-images/gig1-a.png`, `gig1-b.png`, `gig1-c.png` via the D0 recipe.
Check: listing submitted for review or published.
Log: `--entity listing --ref catalog-1 --action submitted`.

### F3. Listing 2: TCPA-Compliant AI Cold Calling Agent with Consent and DNC Gating
Copy: section 3. Tiers $350 / $1,200 / $2,800. Images: `gig2-a.png`, `gig2-b.png`, `gig2-c.png`.
Log: `--ref catalog-2 --action submitted`.

---

## Phase G: go live

### G0. Agency invitation
Do: if Chitraksh has sent the Oraya Labs agency invitation, Frankie accepts it from his own account (Settings, Agencies, or the invitation email). Claude verifies the agency appears on the profile. If no invitation yet, mark `skipped` with note "awaiting invitation" and continue.
Log: `--ref agency-membership --action accepted` or `--action pending`.

### G1. Availability
Do: set profile status to Available (profile page, availability control).
Log: `--ref availability --action set_available`.

### G2. Registry
Do: in `accounts.json`, replace `TODO-frankie` with the real handle, set `status: active`, `created`, `profile_url`, and update `verification_state` from Phase B. `project_write` it.
Log: `--ref registry --action updated`.

### G3. Handoff
Do: `python3 hub.py handoff`, `project_write` `NEXT-SESSION.md`, the ledger, and the checkpoint. Tell Frankie in one paragraph what is live and what is still his to do.

---

## Phase H: daily loop (after go live)

Once per day, any session: `playbooks/upwork-proposal.md` and `templates/upwork-proposal-skeleton.md` for proposals (Frankie sends; log each), `playbooks/response-sla.md` for replies, `monitoring/daily-check.md` for numbers. Apply `DIRECTIVES.md` D1: win the order, log the price reason, over-deliver, ask for feedback only with the template.

---

## If something is different from this runbook

Upwork changes its UI. When a page, URL or control is not where this says: take a screenshot, find the equivalent control, do the step, and write what you found into the checkpoint `notes` so the next session does not rediscover it. Never guess a form value; never complete a CAPTCHA or human check (stop and ask Frankie); never type credentials, ID numbers or payment details.
