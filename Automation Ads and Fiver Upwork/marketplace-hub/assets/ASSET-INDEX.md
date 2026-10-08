# Asset index

Every image held for the Fiverr and Upwork profiles. Hosted copy: the **Marketplace Asset Library** artifact, https://claude.ai/artifact/DwQewSj5StuW76xF7MG3bw . A Claude session lists paths with `Artifact action:list_files` on that URL and pulls one with `action:read_file` and the path below. Masters on Chitraksh's Mac: `marketplace-hub/Gallery/portfolio-final/` and `marketplace-hub/research/gig-images/`.

Clearance levels: **Cleared** (upload as is), **Redact first** (contains a live number, client name or browser chrome), **Reference** (never uploaded), **Excluded** (not on the cloud, do not use).

## Portfolio masters, redacted, cleared

Live on Fiverr since 13 Sep 2026. Reuse as the Upwork portfolio on both founders' accounts. Redaction applied: outbound line masked, dealerships renamed Dealer A and Dealer B, browser chrome and bookmarks cropped.

| Path | Size | Shows | Fiverr entry | Clearance |
|---|---|---|---|---|
| `assets/portfolio-final/portfolio-1-n8n-outbound-pipeline.png` | 1920 x 1039 | n8n fan-out canvas, insurance post-call outbound workflow | P4 Post-call outbound pipeline built in n8n (Sep 2026, 7 to 30 days, 750) | Cleared |
| `assets/portfolio-final/portfolio-2-voice-control-center.png` | 1920 x 1039 | Oraya Voice Control Center: call register, masked views, agents on the line, 30-day activity | P1 AI voice control center for a dealership line (Aug 2026, 1 to 3 months, 2800) | Cleared |
| `assets/portfolio-final/portfolio-3-compliance-audit-ab2905.png` | 1920 x 1501 | Compliance audit drawer: law, requirement, mechanism, evidence in code, status; California AB 2905 row compliant | P2 Compliance audit, AI voice disclosure in code (Sep 2026, 7 to 30 days, 350) | Cleared |
| `assets/portfolio-final/portfolio-4-governance-enforced-in-code.png` | 1148 x 1592 | Governance panel: recording, 90-day retention, outbound allowlist, SMS and email gates, caller privacy | P3 Governance gates enforced in code, not prompts (Sep 2026, 7 to 30 days, 1200) | Cleared |

Portfolio entry text lives on the Fiverr profile and in `research/fiverr-profile-package.md` section 5. Two further entries (the three-workflow lead-to-booked-call n8n system, and the SMS agent with lint backstop and watchdog) were illustrated with custom architecture diagrams that are not in this folder; ask Chitraksh for those files before reusing them.

## Gig images, 1280 x 769, cleared

Three per gig, in Fiverr's required 1280 x 769. Reuse as Upwork Project Catalog thumbnails and specialized-profile visuals. Copy per gig: `research/fiverr-profile-package.md` sections 2 to 4.

| Path | Gig | Note |
|---|---|---|
| `assets/gig-images/gig1-a.png`, `gig1-b.png`, `gig1-c.png` | Gig 1, AI voice receptionist for dealerships and insurance agencies | a is primary |
| `assets/gig-images/gig2-a.png`, `gig2-b.png`, `gig2-c.png` | Gig 2, TCPA and DNC gated AI cold calling | a is primary |
| `assets/gig-images/gig3-a.png`, `gig3-b.png`, `gig3-c.png` | Gig 3, production n8n AI workflows with error handling and monitoring | a is primary |
| `assets/gig-images/cover.png` | Profile cover | Carries the Oraya mark. Check wording before use on Frankie's account: no Hanflux |
| `assets/gig-images/contact-sheet.png` | All of the above on one sheet (1240 x 2094) | Reference only |

## Source screenshots, redact first

Raw captures from 13 Sep 2026 with browser chrome, bookmarks and the live demo line visible. Redact per `playbooks/case-study-capture.md` before any use.

| Path | Size | Shows | Became |
|---|---|---|---|
| `assets/source-screenshots/shot-1.png` | 2940 x 1912 | n8n editor, Insurance Post-Call Final (outbound) | portfolio-1 |
| `assets/source-screenshots/shot-2.png` | 2940 x 1912 | Voice Control Center with the live line number | portfolio-2 |
| `assets/source-screenshots/shot-3.png` | 2940 x 1912 | Compliance audit drawer with the line number in the header | portfolio-3 |
| `assets/source-screenshots/shot-5.png` | 1148 x 1722 | Governance panel with browser chrome | portfolio-4 |

## Excluded, on the Mac only

| File | Why |
|---|---|
| `Gallery/shot-4.png` (Frankie's CRM campaign page, `frankiealicea.com/crm/campaigns`) | Shows partner ad-account billing totals, a personal domain and zero-lead rows. Ledger event evt-08f8d57af6fc records the decision not to use it |
| `Gallery/Screenshot 2026-09-13 at *.png` (5 files) | Byte-identical duplicates of shot-1 to shot-5 |

## Adding an asset

1. Save the file in the working directory under `assets/<group>/<kebab-name>.png`.
2. Redact if it shows a client, a phone number, an email, a billing figure or browser chrome.
3. Republish the Asset Library artifact with `url` set to the URL above and the new file in `files`; add a figure to `gallery.html`.
4. Add a row here and `project_write` this doc.
5. Log it: `hub.py log --entity profile --ref portfolio --action asset_added --detail "<what and where>"`.
