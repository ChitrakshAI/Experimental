# Playbook: Frankie's Upwork account, from any Claude session

For sessions where Frankie is the one talking. Cloud-first: nothing here needs the Mac folder. Images come from the Asset Library artifact (see `assets/ASSET-INDEX.md`), copy comes from the project docs, and every step is logged with `actor frankie`.

Base rules are in `playbooks/upwork-account-setup.md` section 2 and `accounts.json` (`never_do`). This file adds what is specific to Frankie's account.

---

## 0. The one rule specific to this account

**Hanflux is never mentioned on Frankie's Upwork account.** Not in the name, headline, overview, skills, employment history, education, portfolio titles or descriptions, Project Catalog listings, specialized profiles, proposals, messages or attachments. Before anything is saved or sent from this account, search the text for "Hanflux" and "hanflux" and remove it. The cover image (`assets/gig-images/cover.png`) is checked for the word before use.

Frankie presents as: **Frankie Alicea, co-founder and CEO of Oraya, US-based, licensed insurance producer.** Oraya is the company on this profile. The engineering is described as Oraya's, delivered by Oraya's team.

The Upwork agency is **Oraya Labs** (orayalabs.ai), created from Chitraksh's account (decided 2026-09-14). Frankie accepts the business-manager invitation from his own account once it arrives (`playbooks/upwork-account-setup.md` section 3). Until the invitation exists, his profile simply has no agency yet; nothing on his side waits for it.

---

## 1. What Frankie does himself (Claude never does these)

On his own device, his own browser, his own payment method and his own withdrawal account. Chitraksh never logs into this account and Frankie never logs into Chitraksh's.

1. Sign up at upwork.com as a freelancer with the name he uses in everyday life and his real US business address.
2. Identity verification, the same day. It gates Rising Talent.
3. US location verification. This is the whole point of the account: only US freelancers see "U.S. only" job posts.
4. Tax form: W-9, as a US person.
5. Withdrawal method, separate from anything Chitraksh uses.
6. Freelancer Plus ($19.99 a month) on day 1: 100 Connects, competitor bid visibility, and it unlocks the 50-Connect new-freelancer bonus.
7. Availability Badge on, hard cap 100 Connects a month for the first 60 days. Zero invitations in 14 days: turn it off.
8. Status set to Available.

Claude asks for the real handle and the creation date as soon as the account exists, and writes them into `accounts.json` (replace `TODO-frankie`, set `status` to `active`, set `created`), then logs:

```
python3 hub.py log --platform upwork --account <handle> --entity account --ref account --action created \
  --detail "Upwork freelancer account opened, US, own device and payment method." --actor frankie
```

---

## 2. What Claude builds with Frankie

Ask for these once, at the start, and do not guess any of them: profile photo (a real headshot of Frankie), employment history entries in his words (employer names, titles, dates), education, languages, hourly rate he is comfortable publishing, and the city on the profile. Everything else below is already written.

### Headline (general profile)
AI Voice and Compliance Systems for Insurance Agencies and Dealerships, US-based

### Overview, working draft
Write it in Frankie's voice, first person, under Upwork's overview limit, from these cleared facts only:
- Co-founder and CEO of Oraya, which builds AI voice agents and the workflows around them for US insurance agencies and car dealerships.
- About three years as a licensed life insurance producer helping families protect their homes. The licence is his own credential; Oraya is not a licensed insurance entity and the copy never implies it is.
- Measured median 761 ms time-to-first-audio on simulated calls (26 Aug 2026), against a prior-vendor production p50 of 1.64 to 1.9 s. State the method and the date.
- Compliance enforced in code, not in a prompt: recorded-line disclosure locked as the first thing every caller hears, outbound allowlist, consent, quiet hours and DNC checked in code. Engineering, not legal advice.
- What a buyer gets: a scoped build, a working demo line, a compliance audit table, and the workflows that turn calls into booked appointments.
- No phone number, no email, no website, no off-platform contact route. No Hanflux.

### Skills
AI voice agents, conversational AI, Twilio, telephony, TCPA compliance, insurance lead generation, automotive retail, n8n, workflow automation, CRM integration. Pick from Upwork's list; do not type free text where the field offers a picker.

### Portfolio, from the Asset Library
Same four cleared entries as Fiverr, titles and descriptions rewritten in Frankie's voice with Oraya as the builder. No client named, no Hanflux.

| Order | Image path in the artifact | Title |
|---|---|---|
| 1 | `assets/portfolio-final/portfolio-2-voice-control-center.png` | AI voice control center for a dealership line |
| 2 | `assets/portfolio-final/portfolio-3-compliance-audit-ab2905.png` | Compliance audit: AI voice disclosure enforced in code |
| 3 | `assets/portfolio-final/portfolio-4-governance-enforced-in-code.png` | Governance gates enforced in code, not prompts |
| 4 | `assets/portfolio-final/portfolio-1-n8n-outbound-pipeline.png` | Post-call outbound pipeline built in n8n |

Pull each file with `Artifact action:read_file` and hand it to Frankie with `SendUserFile`, or upload through the browser tool when one is connected. Upwork's portfolio image dimensions are read from the upload dialog at the time, not assumed.

### Specialized profile (one, not two, on this account)
Insurance-vertical: **AI Voice Agents for Insurance Agencies, Licensed Producer, Compliance in Code.** Portfolio subset: entries 1 to 3. The dealership work stays on the general profile.

### Project Catalog
Mirror Gig 1 and Gig 2 only (voice receptionist; TCPA-gated cold calling), priced at or above the Fiverr ladder ($450 / $1,200 / $2,800 and $350 / $1,200 / $2,800). Copy rewritten from `research/fiverr-profile-package.md` sections 2 and 3 into Upwork's fields. Gig 3 (n8n) stays on Chitraksh's account.

---

## 3. Proposals from this account

- Filter first: posted in the last hour where possible, client payment verified, budget $1,000 plus, inside the eight ranked niches (`research/marketplace-expansion.md` section 1.9), client lifetime spend ideally $1,000 to $5,000, not a whale. Include US-only posts, which only this account sees.
- Structure and worked examples: `templates/upwork-proposal-skeleton.md`. Chitraksh supplies the technical answer when a post needs one; Frankie sends.
- Cadence: week 1 is 18 proposals over days 3 to 7, about 230 Connects. Boosts only on $1,500 plus jobs with named vertical proof, at most 25% of proposals, capped at 30 Connects.
- Log every proposal (`--entity message --action proposal_sent`) with the job title, budget, Connects spent and whether it was boosted. The interview rate is unknowable otherwise.

---

## 4. Frankie day-1 checklist

- [ ] Account created, own device, own payment method
- [ ] ID verification submitted
- [ ] US location verification submitted
- [ ] W-9 submitted
- [ ] Withdrawal method added, separate from Chitraksh's
- [ ] Freelancer Plus subscribed
- [ ] Availability Badge on, 100-Connect cap
- [ ] Headline, overview, skills, rate, photo, employment, education, languages: profile at 100%
- [ ] Four portfolio entries uploaded from the Asset Library, no client named
- [ ] "Hanflux" search on every field returns nothing
- [ ] Oraya Labs agency invitation accepted (when Chitraksh sends it)
- [ ] Specialized insurance profile created
- [ ] Project Catalog availability checked and logged
- [ ] Status Available
- [ ] `accounts.json` updated with the real handle and creation date
- [ ] Every step above logged with `--actor frankie` and written back to the project
