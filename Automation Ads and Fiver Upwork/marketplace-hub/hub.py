#!/usr/bin/env python3
"""Marketplace Hub CLI.

The operating system for Oraya / Hanflux AI freelance-marketplace go-to-market.
Fiverr today, Upwork next, more platforms after that.

Design rules:
  1. The ledger is append-only. Nothing is ever edited in place or deleted.
     Corrections are new events. History is the point.
  2. Every command is idempotent. Re-running a seed, a log with an explicit id,
     or a metrics snapshot for a date already recorded does not corrupt state.
  3. Python 3 standard library only. No install step, no virtualenv, no network.
  4. No em dashes. Ever. See WRITING-RULES in the source repo.

Run `python3 hub.py --help` for the command list.
"""

import argparse
import hashlib
import json
import os
import sys
from datetime import datetime, timezone, date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LEDGER_DIR = ROOT / "ledger"
EVENTS_PATH = LEDGER_DIR / "events.jsonl"
METRICS_PATH = LEDGER_DIR / "metrics.jsonl"
REPORTS_DIR = ROOT / "reports"
ACCOUNTS_PATH = ROOT / "accounts.json"
CAMPAIGNS_PATH = ROOT / "ads" / "campaigns.json"

# The seven entity types named in the hub spec, plus four operational types
# the ledger needs to be able to answer "what is blocking us" and "what is due".
CORE_ENTITIES = ["profile", "gig", "proposal", "ad", "order", "review", "message"]
OPS_ENTITIES = ["account", "task", "blocker", "campaign"]
ENTITIES = CORE_ENTITIES + OPS_ENTITIES

# Action to state, for anything that has a lifecycle: profile, gig, proposal, ad.
STATE_ACTIONS = {
    "not_started": "not-started",
    "draft_started": "draft",
    "draft_saved": "draft",
    "draft_complete": "draft",
    "submitted_for_review": "pending-verification",
    "awaiting_verification": "pending-verification",
    "denied": "draft",
    "published": "live",
    "live": "live",
    "paused": "paused",
    "unpaused": "live",
    "resumed": "live",
    "archived": "archived",
    "withdrawn": "archived",
}

STATE_ORDER = ["not-started", "draft", "pending-verification", "live", "paused", "archived"]

# Every metric named in research/marketplace-expansion.md section 6, plus the Fiverr
# set from fiverr-market.md section 4.1. Where a number lives in the platform UI is
# recorded in monitoring/daily-check.md, not here.
METRIC_FIELDS = [
    # --- Fiverr, gig analytics and seller dashboard ---
    "impressions",
    "clicks",
    "ctr",
    "views",
    "orders",
    "conversion_rate",
    "messages",
    "response_rate",
    "response_time_h",
    "success_score",
    "rating",
    "cancellations",
    "unique_clients",
    "earnings_lifetime",
    # --- Upwork, Stats and trends ---
    "profile_views",
    "invitations",
    "proposals_sent",
    "proposals_viewed",
    "interviews",
    "hires",
    "boosted_proposals",
    "connects_spent",
    "connects_balance",
    "jss",
    "earnings_12mo",
    # --- pipeline input, counted by hand ---
    "jobs_identified",
    # --- paid channels ---
    "ad_spend",
    "ad_clicks",
    # Paid impressions are kept separate from organic gig impressions on purpose.
    # Summing them into one column would quietly inflate the CTR denominator.
    "ad_impressions",
    "ad_leads",
]

# Fields that sum across a week. Everything else is a level or a rate and is averaged.
SUM_FIELDS = {
    "impressions",
    "clicks",
    "views",
    "orders",
    "messages",
    "cancellations",
    "profile_views",
    "invitations",
    "proposals_sent",
    "proposals_viewed",
    "interviews",
    "hires",
    "boosted_proposals",
    "connects_spent",
    "jobs_identified",
    "ad_spend",
    "ad_clicks",
    "ad_impressions",
    "ad_leads",
}
# A level or a rate. Averaged across the week, never summed. Lifetime and balance
# figures are levels too: summing seven daily readings of a balance is nonsense.
AVG_FIELDS = {
    "ctr",
    "conversion_rate",
    "response_rate",
    "response_time_h",
    "success_score",
    "rating",
    "jss",
    "connects_balance",
    "earnings_12mo",
    "earnings_lifetime",
    "unique_clients",
}

# Fields typed as float on the CLI. Everything else is an int.
FLOAT_FIELDS = {
    "ctr",
    "conversion_rate",
    "response_rate",
    "response_time_h",
    "success_score",
    "rating",
    "jss",
    "earnings_12mo",
    "earnings_lifetime",
    "ad_spend",
}


# ---------------------------------------------------------------------------
# small helpers
# ---------------------------------------------------------------------------


def now_iso():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def today_str():
    return date.today().isoformat()


def coerce(value):
    """Turn a CLI string into an int or float where that is lossless."""
    if value is None:
        return None
    text = str(value).strip()
    if text == "":
        return None
    try:
        if text.lower() in ("true", "false"):
            return text.lower() == "true"
        if "." in text or "e" in text.lower():
            return float(text)
        return int(text)
    except ValueError:
        return text


def read_jsonl(path):
    if not path.exists():
        return []
    rows = []
    with path.open("r", encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, 1):
            line = line.strip()
            if not line or line.startswith("//"):
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as err:
                print("warning: %s line %d is not valid JSON, skipped (%s)" % (path.name, line_no, err), file=sys.stderr)
    return rows


def append_jsonl(path, record):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False, sort_keys=False) + "\n")


def load_json(path, default):
    if not path.exists():
        return default
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def event_id(record):
    basis = "|".join(
        str(record.get(k, ""))
        for k in ("ts", "platform", "account", "entity", "ref", "action", "detail")
    )
    return "evt-" + hashlib.sha1(basis.encode("utf-8")).hexdigest()[:12]


def fingerprint(record):
    """Identity of an event ignoring its timestamp. Used by --once."""
    basis = "|".join(
        str(record.get(k, ""))
        for k in ("platform", "account", "entity", "ref", "action", "detail")
    )
    return hashlib.sha1(basis.encode("utf-8")).hexdigest()[:12]


def table(headers, rows, indent=0):
    """Plain fixed-width table. No dependencies, copy-pastes into markdown fine."""
    if not rows:
        return " " * indent + "(none)"
    cols = len(headers)
    widths = [len(str(h)) for h in headers]
    clean = []
    for row in rows:
        cells = [("" if c is None else str(c)) for c in list(row) + [""] * (cols - len(row))][:cols]
        clean.append(cells)
        for i, cell in enumerate(cells):
            widths[i] = max(widths[i], len(cell))
    pad = " " * indent
    out = [pad + "  ".join(str(h).ljust(widths[i]) for i, h in enumerate(headers)).rstrip()]
    out.append(pad + "  ".join("-" * widths[i] for i in range(cols)))
    for cells in clean:
        out.append(pad + "  ".join(cells[i].ljust(widths[i]) for i in range(cols)).rstrip())
    return "\n".join(out)


def heading(text, char="="):
    return "\n" + text + "\n" + char * len(text)


# ---------------------------------------------------------------------------
# ledger index
# ---------------------------------------------------------------------------


class Ledger:
    """Read-only projection of the append-only event log into current state."""

    def __init__(self):
        self.events = sorted(read_jsonl(EVENTS_PATH), key=lambda e: (e.get("ts") or "", e.get("id") or ""))
        self.metrics = read_jsonl(METRICS_PATH)
        self.accounts = load_json(ACCOUNTS_PATH, {"accounts": []})

    # === events ===

    def ids(self):
        return {e.get("id") for e in self.events if e.get("id")}

    def fingerprints(self):
        return {fingerprint(e) for e in self.events}

    def by(self, **filters):
        out = []
        for event in self.events:
            if all(event.get(k) == v for k, v in filters.items()):
                out.append(event)
        return out

    def has(self, **filters):
        return len(self.by(**filters)) > 0

    def last(self, **filters):
        rows = self.by(**filters)
        return rows[-1] if rows else None

    # === derived state ===

    def entity_state(self, platform, account, entity, ref):
        """Latest lifecycle state for one profile, gig, proposal or ad."""
        state = "not-started"
        last_ts = None
        last_action = None
        for event in self.events:
            if event.get("platform") != platform or event.get("account") != account:
                continue
            if event.get("entity") != entity or event.get("ref") != ref:
                continue
            mapped = STATE_ACTIONS.get(event.get("action"))
            last_ts = event.get("ts")
            last_action = event.get("action")
            if mapped:
                state = mapped
        return state, last_action, last_ts

    def open_blockers(self, platform=None, account=None):
        opened = {}
        for event in self.events:
            if event.get("entity") != "blocker":
                continue
            if platform and event.get("platform") not in (platform, "all"):
                continue
            if account and event.get("account") not in (account, "all", None):
                continue
            key = (event.get("platform"), event.get("account"), event.get("ref"))
            if event.get("action") in ("opened", "reopened"):
                opened[key] = event
            elif event.get("action") in ("closed", "resolved"):
                opened.pop(key, None)
        return list(opened.values())

    def open_tasks(self, platform=None, account=None):
        opened = {}
        for event in self.events:
            if event.get("entity") != "task":
                continue
            if platform and event.get("platform") not in (platform, "all"):
                continue
            if account and event.get("account") not in (account, "all", None):
                continue
            key = (event.get("platform"), event.get("account"), event.get("ref"))
            if event.get("action") in ("opened", "reopened"):
                opened[key] = event
            elif event.get("action") in ("done", "closed", "cancelled"):
                opened.pop(key, None)
        rows = list(opened.values())
        rows.sort(key=lambda e: (e.get("due") or "9999-12-31", e.get("ref") or ""))
        return rows

    def blocker_closed(self, ref):
        state = False
        for event in self.events:
            if event.get("entity") == "blocker" and event.get("ref") == ref:
                if event.get("action") in ("opened", "reopened"):
                    state = False
                elif event.get("action") in ("closed", "resolved"):
                    state = True
        return state

    def blocker_exists(self, ref):
        return any(e.get("entity") == "blocker" and e.get("ref") == ref for e in self.events)

    # === metrics ===

    def metric_snapshots(self):
        """Last write wins per (date, platform, account, gig, source). Append-only, so a
        correction is just a later line with the same key. Source is part of the key so an
        ad snapshot never overwrites that day's organic reading for the same gig."""
        keyed = {}
        for row in self.metrics:
            key = (row.get("date"), row.get("platform"), row.get("account"),
                   row.get("gig") or "-", row.get("source") or "manual")
            keyed[key] = row
        rows = list(keyed.values())
        rows.sort(key=lambda r: (r.get("date") or "", r.get("platform") or "", r.get("gig") or ""))
        return rows


# ---------------------------------------------------------------------------
# accounts
# ---------------------------------------------------------------------------


def gig_registry(accounts_blob):
    """Flatten accounts.json into (account_record, gig_record) pairs."""
    pairs = []
    for account in accounts_blob.get("accounts", []):
        for gig in account.get("gigs", []):
            pairs.append((account, gig))
    return pairs


# ---------------------------------------------------------------------------
# launch checklist
# ---------------------------------------------------------------------------

# Each item: key, group, label, and a rule that reads the ledger.
# An item is also marked done by an explicit event:
#   entity=task action=done ref=<key>
CHECKLIST = [
    ("account_created", "Account", "Fiverr account created and username locked",
     lambda L: L.has(entity="account", action="created")),
    ("profile_live", "Account", "Seller profile published (display name, tagline, description)",
     lambda L: L.entity_state("fiverr", "hanfluxai", "profile", "seller-profile")[0] == "live"),
    ("education_entry", "Account", "Education entry completed (graduation year confirmed)",
     lambda L: L.blocker_closed("education-graduation-year")),
    ("seller_plus_decision", "Account", "Seller Plus Kickstart decision made (yes or no, in writing)",
     lambda L: L.blocker_closed("seller-plus-kickstart")),
    ("id_verification", "Compliance gate", "ID verification passed",
     lambda L: L.blocker_closed("id-verification")),
    ("w8ben", "Compliance gate", "W-8BEN submitted and accepted",
     lambda L: L.blocker_closed("w8ben")),
    ("india_gst", "Compliance gate", "India GST declaration form submitted",
     lambda L: L.blocker_closed("india-gst")),
    ("payout_setup", "Compliance gate", "Payout method connected",
     lambda L: L.blocker_closed("payout-setup")),
    ("gig1_draft", "Gig 1 voice receptionist", "Draft complete in the Fiverr editor",
     lambda L: L.has(entity="gig", ref="gig1", action="draft_complete")),
    ("gig1_images", "Gig 1 voice receptionist", "Three gig images uploaded at 1280 x 769",
     lambda L: L.has(entity="gig", ref="gig1", action="images_uploaded")),
    ("gig1_video", "Gig 1 voice receptionist", "Gig video uploaded, 55 to 60 seconds, number masked",
     lambda L: L.has(entity="gig", ref="gig1", action="video_uploaded")),
    ("gig1_published", "Gig 1 voice receptionist", "Published and URL slug verified",
     lambda L: L.entity_state("fiverr", "hanfluxai", "gig", "gig1")[0] == "live"),
    ("gig2_draft", "Gig 2 cold calling", "Draft complete (overview, pricing, description, FAQ, requirements)",
     lambda L: L.has(entity="gig", ref="gig2", action="draft_complete")),
    ("gig2_images", "Gig 2 cold calling", "Three gig images uploaded",
     lambda L: L.has(entity="gig", ref="gig2", action="images_uploaded")),
    ("gig2_published", "Gig 2 cold calling", "Published and URL slug verified",
     lambda L: L.entity_state("fiverr", "hanfluxai", "gig", "gig2")[0] == "live"),
    ("gig3_draft", "Gig 3 n8n workflows", "Draft started in the Fiverr editor",
     lambda L: L.entity_state("fiverr", "hanfluxai", "gig", "gig3")[0] != "not-started"),
    ("gig3_published", "Gig 3 n8n workflows", "Published and URL slug verified",
     lambda L: L.entity_state("fiverr", "hanfluxai", "gig", "gig3")[0] == "live"),
    ("portfolio", "Proof", "Portfolio projects uploaded, PII masked, no client named",
     lambda L: L.has(entity="profile", action="portfolio_uploaded")),
    ("sla_templates", "Operations", "First-reply templates loaded into Fiverr Quick Responses",
     lambda L: L.has(entity="message", action="quick_responses_saved")),
    ("mobile_app", "Operations", "Fiverr mobile app installed with notifications on (response SLA)",
     lambda L: L.has(entity="account", action="mobile_app_configured")),
    ("first_metrics", "Operations", "First daily metrics snapshot logged",
     lambda L: len(L.metric_snapshots()) > 0),
    ("first_order", "Traction", "First paid order delivered",
     lambda L: L.has(entity="order", action="delivered")),
    ("five_orders", "Traction", "Five orders from three or more unique clients (Level 1 bar)",
     lambda L: len({e.get("ref") for e in L.by(entity="order", action="delivered")}) >= 5),
]


def checklist_state(ledger):
    explicit_done = {
        e.get("ref") for e in ledger.by(entity="task", action="done")
    }
    rows = []
    for key, group, label, rule in CHECKLIST:
        try:
            derived = bool(rule(ledger))
        except Exception:
            derived = False
        done = derived or key in explicit_done
        rows.append({"key": key, "group": group, "label": label, "done": done})
    return rows


# ---------------------------------------------------------------------------
# commands
# ---------------------------------------------------------------------------


def cmd_log(args):
    metrics = {}
    for pair in args.metric or []:
        if "=" not in pair:
            print("error: --metric expects key=value, got %r" % pair, file=sys.stderr)
            return 2
        key, value = pair.split("=", 1)
        metrics[key.strip()] = coerce(value)

    record = {
        "id": None,
        "ts": args.ts or now_iso(),
        "platform": args.platform,
        "account": args.account,
        "entity": args.entity,
        "ref": args.ref,
        "action": args.action,
        "detail": args.detail or "",
        "metrics": metrics,
        "actor": args.actor,
    }
    if args.due:
        record["due"] = args.due

    record["id"] = args.id or event_id(record)

    ledger = Ledger()
    if record["id"] in ledger.ids():
        print("skip: event %s already in ledger (idempotent)" % record["id"])
        return 0
    if args.once and fingerprint(record) in ledger.fingerprints():
        print("skip: an identical event already exists and --once was passed")
        return 0

    append_jsonl(EVENTS_PATH, record)
    print("logged %s  %s/%s  %s:%s  %s" % (
        record["id"], record["platform"], record["account"],
        record["entity"], record["ref"] or "-", record["action"]))
    return 0


def cmd_status(args):
    ledger = Ledger()
    out = []
    out.append("MARKETPLACE HUB STATUS   read %s" % now_iso())
    out.append("ledger: %d events, %d metric snapshots" % (len(ledger.events), len(ledger.metric_snapshots())))

    for account in ledger.accounts.get("accounts", []):
        platform = account.get("platform")
        handle = account.get("handle")
        if args.platform and platform != args.platform:
            continue
        out.append(heading("%s / %s   [%s]" % (platform.upper(), handle, account.get("status", "unknown"))))
        out.append("  owner: %s   jurisdiction: %s   created: %s" % (
            account.get("owner", "-"), account.get("jurisdiction", "-"), account.get("created", "-")))
        out.append("  purpose: %s" % account.get("purpose", "-"))
        verification = account.get("verification_state", {})
        if verification:
            vrows = [[k, str(v)] for k, v in sorted(verification.items())]
            out.append("")
            out.append("  Verification")
            out.append(table(["gate", "state"], vrows, indent=4))

        listings = account.get("gigs", []) or account.get("profiles", [])
        rows = []
        for gig in listings:
            ref = gig.get("ref")
            state, last_action, last_ts = ledger.entity_state(platform, handle, "gig", ref)
            if state == "not-started" and gig.get("declared_state"):
                state = gig.get("declared_state")
            # Gig records carry `short`. Upwork profile records carry `headline` instead,
            # and no price ladder, so fall through rather than printing an empty cell.
            label = gig.get("short") or gig.get("title") or gig.get("headline") or ""
            rows.append([
                ref,
                label[:44],
                state,
                gig.get("price_ladder") or gig.get("kind") or "-",
                last_action or "-",
                (last_ts or "-")[:10],
            ])
        out.append("")
        out.append("  Listings")
        out.append(table(["ref", "listing", "state", "ladder", "last action", "on"], rows, indent=4))

        blockers = ledger.open_blockers(platform=platform, account=handle)
        brows = [[b.get("ref"), (b.get("detail") or "")[:64], (b.get("ts") or "")[:10]] for b in blockers]
        out.append("")
        out.append("  Open blockers (%d)" % len(brows))
        out.append(table(["blocker", "detail", "opened"], brows, indent=4))

        tasks = ledger.open_tasks(platform=platform, account=handle)
        today = today_str()
        trows = []
        for task in tasks:
            due = task.get("due") or "-"
            flag = ""
            if due != "-" and due < today:
                flag = "OVERDUE"
            elif due == today:
                flag = "DUE TODAY"
            trows.append([task.get("ref"), (task.get("detail") or "")[:56], due, flag])
        out.append("")
        out.append("  Next actions (%d open)" % len(trows))
        out.append(table(["task", "detail", "due", "flag"], trows, indent=4))

    # Account-agnostic blockers, for example anything logged against platform "all".
    globals_open = [b for b in ledger.open_blockers() if b.get("platform") == "all"]
    if globals_open:
        out.append(heading("CROSS-PLATFORM BLOCKERS"))
        out.append(table(
            ["blocker", "detail", "opened"],
            [[b.get("ref"), (b.get("detail") or "")[:64], (b.get("ts") or "")[:10]] for b in globals_open],
            indent=2))

    done = sum(1 for item in checklist_state(ledger) if item["done"])
    out.append(heading("LAUNCH CHECKLIST"))
    out.append("  %d of %d complete. Run `python3 hub.py checklist` for the item list." % (done, len(CHECKLIST)))
    out.append("")

    text = "\n".join(out)
    print(text)
    return 0


def cmd_checklist(args):
    ledger = Ledger()
    rows = checklist_state(ledger)
    out = ["LAUNCH CHECKLIST   read %s" % now_iso()]
    current_group = None
    for item in rows:
        if item["group"] != current_group:
            current_group = item["group"]
            out.append("")
            out.append("  " + current_group)
        mark = "[x]" if item["done"] else "[ ]"
        out.append("    %s %-22s %s" % (mark, item["key"], item["label"]))
    done = sum(1 for item in rows if item["done"])
    out.append("")
    out.append("  %d of %d complete." % (done, len(rows)))
    out.append("  Mark an item done by logging the real action, or explicitly:")
    out.append("    python3 hub.py log --platform fiverr --account hanfluxai --entity task \\")
    out.append("      --ref <key> --action done --detail \"what happened\" --actor chitraksh")
    out.append("")
    text = "\n".join(out)
    print(text)
    return 0


def cmd_metrics_add(args):
    record = {
        "ts": now_iso(),
        "date": args.date or today_str(),
        "platform": args.platform,
        "account": args.account,
        "gig": args.gig or "-",
        "source": args.source or "manual",
        "actor": args.actor,
        "note": args.note or "",
    }
    for field in METRIC_FIELDS:
        record[field] = getattr(args, field, None)

    if record.get("ctr") is None and record.get("impressions") and record.get("clicks") is not None:
        try:
            record["ctr"] = round(100.0 * float(record["clicks"]) / float(record["impressions"]), 3)
        except (TypeError, ZeroDivisionError):
            record["ctr"] = None

    # Conversion rate is orders over clicks, which is the dominant Fiverr ranking signal.
    # Computed only when both were actually read, never inferred from one of them.
    if record.get("conversion_rate") is None and record.get("clicks") and record.get("orders") is not None:
        try:
            record["conversion_rate"] = round(100.0 * float(record["orders"]) / float(record["clicks"]), 3)
        except (TypeError, ZeroDivisionError):
            record["conversion_rate"] = None

    ledger = Ledger()
    key = (record["date"], record["platform"], record["account"], record["gig"], record["source"])
    existing = {
        (r.get("date"), r.get("platform"), r.get("account"), r.get("gig") or "-", r.get("source") or "manual"): r
        for r in ledger.metrics
    }
    prior = existing.get(key)
    if prior:
        same = all(prior.get(f) == record.get(f) for f in METRIC_FIELDS)
        if same:
            print("skip: identical snapshot for %s already recorded (idempotent)" % (key,))
            return 0
        print("note: a snapshot for %s exists. Appending a correction, last line wins." % (key,))
        print("      A correction must reuse the same --source, or it lands as a separate reading.")

    append_jsonl(METRICS_PATH, record)
    filled = [f for f in METRIC_FIELDS if record.get(f) is not None]
    print("recorded %s  %s/%s  gig=%s  fields: %s" % (
        record["date"], record["platform"], record["account"], record["gig"],
        ", ".join(filled) or "(none)"))
    return 0


def week_key(date_string):
    try:
        parsed = date.fromisoformat(date_string)
    except (TypeError, ValueError):
        return "unknown"
    iso = parsed.isocalendar()
    return "%04d-W%02d" % (iso[0], iso[1])


def rollup(rows):
    """Sum counters, average rates, over a list of snapshot rows."""
    out = {}
    for field in METRIC_FIELDS:
        values = [r.get(field) for r in rows if isinstance(r.get(field), (int, float))]
        if not values:
            out[field] = None
        elif field in SUM_FIELDS:
            out[field] = round(sum(values), 2)
        else:
            out[field] = round(sum(values) / len(values), 2)
    if out.get("impressions") and out.get("clicks") is not None:
        try:
            out["ctr"] = round(100.0 * out["clicks"] / out["impressions"], 2)
        except ZeroDivisionError:
            pass
    if out.get("clicks") and out.get("orders") is not None:
        try:
            out["conversion_rate"] = round(100.0 * out["orders"] / out["clicks"], 2)
        except ZeroDivisionError:
            pass
    return out


def rate(numerator, denominator):
    """Percentage, or None when either side was not read. Never guesses a denominator."""
    if not isinstance(numerator, (int, float)) or not isinstance(denominator, (int, float)):
        return None
    if not denominator:
        return None
    return round(100.0 * numerator / denominator, 2)


def delta_cell(current, previous):
    if current is None:
        return "-"
    if previous is None:
        return "%s (new)" % fmt_num(current)
    change = current - previous
    if abs(change) < 1e-9:
        return "%s (0)" % fmt_num(current)
    sign = "+" if change > 0 else ""
    return "%s (%s%s)" % (fmt_num(current), sign, fmt_num(change))


def fmt_num(value):
    if value is None:
        return "-"
    if isinstance(value, float) and abs(value - round(value)) < 1e-9:
        return str(int(round(value)))
    if isinstance(value, float):
        return "%.2f" % value
    return str(value)


def leading_flags(current, previous):
    """Leading-indicator reads.

    The seven ranked indicators are in research/marketplace-expansion.md section 6.4 and
    in STRATEGY.md section (i). Every one of these is a decision prompt, not a verdict.
    Indicators are checked in the research's own priority order: the earliest-moving,
    most-fixable signal first.
    """
    flags = []

    def got(field):
        return isinstance(current.get(field), (int, float))

    def prev(field):
        return isinstance(previous.get(field), (int, float)) if previous else False

    # --- 1. Upwork proposal view rate. The earliest signal in the system, moving
    # within 24 hours of a send, and fixable the same day. ---
    view_rate = rate(current.get("proposals_viewed"), current.get("proposals_sent"))
    if view_rate is not None and current.get("proposals_sent", 0) >= 10 and view_rate < 30.0:
        flags.append(
            "LEAD 1, PROPOSAL VIEW RATE %.1f PERCENT on %s proposals: they are not being opened at all. "
            "The problem is the first two lines and the profile headline, not the offer. Fixable today."
            % (view_rate, fmt_num(current.get("proposals_sent"))))

    # --- 2. Upwork interview rate. Baseline 7.45 percent, 13.77 percent with the full
    # template. Below 5 percent after 20 proposals is the documented stop-and-rewrite. ---
    interview_rate = rate(current.get("interviews"), current.get("proposals_sent"))
    if interview_rate is not None and current.get("proposals_sent", 0) >= 20:
        if interview_rate < 5.0:
            flags.append(
                "LEAD 2, INTERVIEW RATE %.1f PERCENT over %s proposals: below the 5 percent stop line. "
                "Stop bidding for one day, rewrite the two opening lines, record a new Loom, then resume."
                % (interview_rate, fmt_num(current.get("proposals_sent"))))
        elif interview_rate >= 13.0:
            flags.append(
                "LEAD 2, INTERVIEW RATE %.1f PERCENT over %s proposals: at or above the 13.77 percent "
                "template target. The template is working. Raise volume before changing anything else."
                % (interview_rate, fmt_num(current.get("proposals_sent"))))
        elif interview_rate >= 7.0:
            flags.append(
                "LEAD 2, INTERVIEW RATE %.1f PERCENT: above the 7.45 percent platform baseline and no hire yet. "
                "Change nothing. 20 to 80 serious proposals is the documented range to a first client."
                % interview_rate)

    if got("impressions") and got("clicks") and prev("impressions") and prev("clicks"):
        imp_up = current["impressions"] > previous["impressions"] * 1.15
        clicks_flat = current["clicks"] <= previous["clicks"] * 1.05
        if imp_up and clicks_flat:
            flags.append("IMPRESSIONS UP, CLICKS FLAT: thumbnail, title or price is losing the click. Fix the image first.")

    # --- 3. Fiverr click-through rate. Moves within 48 hours of publishing because of the
    # honeymoon impression boost. 2 to 5 percent is typical, 8 to 15 percent is strong. ---
    if got("ctr") and got("impressions") and current["impressions"] >= 200:
        if current["ctr"] < 1.0:
            flags.append("LEAD 3, CTR %.2f PERCENT at %s impressions: the listing is visible and being skipped. "
                         "The thumbnail and the title are the fix, in that order."
                         % (current["ctr"], fmt_num(current["impressions"])))
        elif current["ctr"] < 2.0:
            flags.append("LEAD 3, CTR %.2f PERCENT, under the 2 percent floor with impressions arriving: "
                         "the thumbnail and title are wrong. If impressions were absent instead, the category and tags would be."
                         % current["ctr"])

    # --- 4. Response time and response rate. The only indicator fully within our control,
    # and an explicit ranking input on both platforms. ---
    if got("response_time_h") and current["response_time_h"] > 1.0:
        flags.append("LEAD 4, RESPONSE TIME %s HOURS, over the 1 hour line: a direct ranking input on both platforms "
                     "and the cheapest lever on the list. Same-day fix, not a weekly discussion."
                     % fmt_num(current["response_time_h"]))

    if got("response_rate") and current["response_rate"] < 90.0:
        note = "Level 1 requires 80 percent, Level 2 requires 90 percent."
        if current["response_rate"] < 80.0:
            note = "Below the 80 percent Level 1 bar. Urgent."
        flags.append("LEAD 4, RESPONSE RATE %s PERCENT: %s" % (fmt_num(current["response_rate"]), note))

    # --- 5. Upwork invitations. The purest signal that the profile itself converts,
    # independent of any proposal. ---
    if got("invitations") and current["invitations"] == 0 and got("connects_spent") and current["connects_spent"] > 0:
        flags.append("LEAD 5, ZERO INVITATIONS in a week with Connects spent: if the Availability Badge has now run "
                     "14 days with no invitation, turn it off. Invited jobs convert better because the shortlist is shorter.")

    # --- 6. Fiverr conversion rate, orders over clicks. The lagging half of the funnel
    # and the dominant Fiverr ranking signal. ---
    if got("conversion_rate") and got("clicks") and current["clicks"] >= 30:
        if current["conversion_rate"] < 2.0:
            flags.append("LEAD 6, CONVERSION RATE %.2f PERCENT on %s clicks: under 2 percent with healthy click volume "
                         "means the packages, the price ladder or the description are failing, not the discovery."
                         % (current["conversion_rate"], fmt_num(current["clicks"])))

    # --- 7. Pipeline input. Not a platform metric, and the one that invalidates every
    # other number when it fails. ---
    if got("jobs_identified") and current["jobs_identified"] < 21:
        flags.append("LEAD 7, ONLY %s QUALIFYING JOBS IDENTIFIED this week, under the 3 a day floor: the niche filters "
                     "are wrong and no amount of proposal quality compensates."
                     % fmt_num(current["jobs_identified"]))

    # --- Secondary reads: funnel breaks and level gates. ---
    if got("clicks") and got("orders") and current["clicks"] >= 30 and current["orders"] == 0:
        flags.append("CLICKS WITHOUT ORDERS: the gig page is not converting. Read the description and the first package.")

    if got("messages") and got("orders") and current["messages"] >= 5 and current["orders"] == 0:
        flags.append("MESSAGES WITHOUT ORDERS: qualification or pricing objection. Check the first-reply template.")

    if got("success_score") and current["success_score"] < 5.0:
        flags.append("SUCCESS SCORE UNDER 5.0: Level 1 is gated on 5.0. Check private feedback and cancellations.")

    if got("success_score") and 5.0 <= current["success_score"] < 7.0:
        flags.append("SUCCESS SCORE UNDER 7.0: Briefs stay locked until 7.0. There is no inbound apply motion yet.")

    if got("rating") and current["rating"] < 4.6:
        flags.append("RATING UNDER 4.6: Level 2 is gated on 4.6 and Rising Talent on Upwork needs 4.8. "
                     "One bad order costs more ranking than it earned.")

    if got("cancellations") and current["cancellations"] > 0:
        flags.append("CANCELLATION RECORDED: log the reason. On Upwork a freelancer-initiated cancellation is a very "
                     "strong JSS negative. Negotiate a reduced-scope close instead, always.")

    if got("jss") and current["jss"] < 90.0:
        note = "Top Rated and Rising Talent both need 90 percent."
        if current["jss"] < 75.0:
            note = "Below 75, response rates collapse. This is the emergency threshold."
        flags.append("JSS %s PERCENT: %s Remember it displays every 14 days, so this may be a stale read."
                     % (fmt_num(current["jss"]), note))

    if got("ad_spend") and current["ad_spend"] > 0 and got("ad_clicks") and current["ad_clicks"] == 0:
        flags.append("AD SPEND WITHOUT CLICKS: pause the campaign and check targeting before the next cycle.")

    if got("ad_spend") and current["ad_spend"] > 0 and got("ad_clicks") and current["ad_clicks"] > 0:
        if got("messages") and current["messages"] == 0 and got("ad_leads") and current["ad_leads"] == 0:
            flags.append("PAID CLICKS WITH ZERO MESSAGES AND ZERO LEADS: the kill rule is 7 days of this. "
                         "Check how many days it has now been before spending another dollar.")

    if got("connects_spent") and got("interviews") and current["connects_spent"] > 0 and current["interviews"] == 0:
        flags.append("CONNECTS SPENT WITHOUT INTERVIEWS: cost per interview is undefined. Tighten the filter before spending more.")

    if got("boosted_proposals") and got("proposals_sent") and current["proposals_sent"] > 0:
        boost_share = rate(current.get("boosted_proposals"), current.get("proposals_sent"))
        if boost_share is not None and boost_share > 30.0:
            flags.append("BOOSTING %.0f PERCENT OF PROPOSALS, above the 25 to 30 percent discipline line: "
                         "boost only 1,500 dollar plus jobs where we hold named vertical proof." % boost_share)

    return flags


def cmd_metrics_report(args):
    ledger = Ledger()
    rows = ledger.metric_snapshots()
    if args.platform:
        rows = [r for r in rows if r.get("platform") == args.platform]
    if args.account:
        rows = [r for r in rows if r.get("account") == args.account]
    if args.gig:
        rows = [r for r in rows if (r.get("gig") or "-") == args.gig]

    out = ["WEEKLY METRICS REPORT   read %s" % now_iso()]
    scope = " / ".join(x for x in [args.platform, args.account, args.gig] if x) or "all platforms, all accounts"
    out.append("scope: %s" % scope)

    if not rows:
        out.append("")
        out.append("  No metric snapshots recorded yet.")
        out.append("  Pull the numbers from monitoring/daily-check.md, then run:")
        out.append("    python3 hub.py metrics add --platform fiverr --account hanfluxai --gig gig1 \\")
        out.append("      --impressions 0 --clicks 0 --orders 0 --messages 0 --response-time-h 0.5")
        out.append("")
        print("\n".join(out))
        return 0

    weeks = {}
    for row in rows:
        weeks.setdefault(week_key(row.get("date")), []).append(row)
    ordered = sorted(weeks.keys())
    limit = args.weeks if args.weeks else 8
    shown = ordered[-limit:]

    rolled = {week: rollup(weeks[week]) for week in ordered}

    headers = ["week", "days", "impr", "clicks", "ctr%", "orders", "msgs", "resp h", "score", "ads $", "ad clk"]
    body = []
    for i, week in enumerate(shown):
        current = rolled[week]
        idx = ordered.index(week)
        previous = rolled[ordered[idx - 1]] if idx > 0 else None
        days = len({r.get("date") for r in weeks[week]})
        body.append([
            week,
            days,
            delta_cell(current.get("impressions"), previous.get("impressions") if previous else None),
            delta_cell(current.get("clicks"), previous.get("clicks") if previous else None),
            delta_cell(current.get("ctr"), previous.get("ctr") if previous else None),
            delta_cell(current.get("orders"), previous.get("orders") if previous else None),
            delta_cell(current.get("messages"), previous.get("messages") if previous else None),
            fmt_num(current.get("response_time_h")),
            fmt_num(current.get("success_score")),
            delta_cell(current.get("ad_spend"), previous.get("ad_spend") if previous else None),
            delta_cell(current.get("ad_clicks"), previous.get("ad_clicks") if previous else None),
        ])
    out.append("")
    out.append(table(headers, body, indent=2))

    upwork_rows = [r for r in rows if r.get("platform") == "upwork"]
    if upwork_rows:
        uweeks = {}
        for row in upwork_rows:
            uweeks.setdefault(week_key(row.get("date")), []).append(row)
        uordered = sorted(uweeks.keys())
        ubody = []
        for week in uordered[-limit:]:
            current = rollup(uweeks[week])
            idx = uordered.index(week)
            previous = rollup(uweeks[uordered[idx - 1]]) if idx > 0 else None
            view_rate = rate(current.get("proposals_viewed"), current.get("proposals_sent"))
            interview_rate = rate(current.get("interviews"), current.get("proposals_sent"))
            ubody.append([
                week,
                delta_cell(current.get("proposals_sent"), previous.get("proposals_sent") if previous else None),
                delta_cell(current.get("proposals_viewed"), previous.get("proposals_viewed") if previous else None),
                "-" if view_rate is None else "%.1f" % view_rate,
                delta_cell(current.get("interviews"), previous.get("interviews") if previous else None),
                "-" if interview_rate is None else "%.1f" % interview_rate,
                delta_cell(current.get("hires"), previous.get("hires") if previous else None),
                delta_cell(current.get("invitations"), previous.get("invitations") if previous else None),
                delta_cell(current.get("connects_spent"), previous.get("connects_spent") if previous else None),
                fmt_num(current.get("jss")),
            ])
        out.append("")
        out.append("  Upwork funnel. Interview rate baseline is 7.45 percent, template target 13.77 percent,")
        out.append("  stop-and-rewrite line 5 percent after 20 proposals.")
        out.append(table(
            ["week", "sent", "viewed", "view%", "interviews", "intvw%", "hires", "invites", "connects", "JSS"],
            ubody, indent=4))

    paid_rows = [r for r in rows if isinstance(r.get("ad_spend"), (int, float))]
    if paid_rows:
        pweeks = {}
        for row in paid_rows:
            pweeks.setdefault(week_key(row.get("date")), []).append(row)
        pordered = sorted(pweeks.keys())
        pbody = []
        for week in pordered[-limit:]:
            current = rollup(pweeks[week])
            spend = current.get("ad_spend")
            clicks = current.get("ad_clicks")
            cpc = "-"
            if isinstance(spend, (int, float)) and isinstance(clicks, (int, float)) and clicks:
                cpc = "%.2f" % (spend / clicks)
            pbody.append([
                week,
                fmt_num(current.get("ad_spend")),
                fmt_num(current.get("ad_impressions")),
                fmt_num(current.get("ad_clicks")),
                cpc,
            ])
        out.append("")
        out.append("  Paid channels, kept separate from organic so the CTR denominator stays honest")
        out.append(table(["week", "spend $", "paid impr", "paid clicks", "cost/click $"], pbody, indent=4))

    latest = rolled[ordered[-1]]
    prior = rolled[ordered[-2]] if len(ordered) > 1 else None
    flags = leading_flags(latest, prior)
    out.append("")
    out.append("  Leading indicators, week %s" % ordered[-1])
    if flags:
        for flag in flags:
            out.append("    ! " + flag)
    else:
        out.append("    No flags fired. That means no rule matched, not that everything is fine.")
    out.append("")
    text = "\n".join(out)
    print(text)
    return 0


# ---------------------------------------------------------------------------
# next: the single next action per account
# ---------------------------------------------------------------------------

# Ordered build steps per account track, from STRATEGY.md section (d) and the
# build_order block in accounts.json. Each step is (label, done_predicate). The first
# step whose predicate is false is that account's next action, unless an open blocker
# or an overdue task outranks it, which they always do.
#
# The track key is the account handle with any leading "TODO-" stripped, so a record
# keeps its track when the placeholder handle is replaced with the real one.
BUILD_STEPS = {
    "hanfluxai": [
        ("Submit ID verification, W-8BEN and the India GST form in one sitting. Nothing publishes until these clear",
         lambda L, h: L.blocker_closed("id-verification") and L.blocker_closed("w8ben") and L.blocker_closed("india-gst")),
        ("Connect the payout method",
         lambda L, h: L.blocker_closed("payout-setup")),
        ("Finish Gig 2: description, 7 FAQs, 4 buyer requirements, then images gig2-a/b/c",
         lambda L, h: L.has(account=h, entity="gig", ref="gig2", action="draft_complete")),
        ("Record the real Gig 2 slug from the URL bar into accounts.json. It locks permanently on first save",
         lambda L, h: L.has(account=h, entity="gig", ref="gig2", action="slug_recorded")),
        ("Build Gig 3 from research/fiverr-profile-package.md section 4. Service type is N8n Automation, not AI Agents",
         lambda L, h: L.entity_state("fiverr", "hanfluxai", "gig", "gig3")[0] != "not-started"),
        ("Upload three images on Gig 1 at 1280 x 769",
         lambda L, h: L.has(account=h, entity="gig", ref="gig1", action="images_uploaded")),
        ("Record all three gig videos in one sitting, 55 to 60 seconds, dialed number masked in every frame",
         lambda L, h: L.has(account=h, entity="gig", ref="gig1", action="video_uploaded")),
        ("Publish Gig 1 in the morning, Gig 2 four hours later, Gig 3 the next morning",
         lambda L, h: L.entity_state("fiverr", "hanfluxai", "gig", "gig1")[0] == "live"),
        ("Decide Seller Plus Kickstart, and write the reason in the ledger either way",
         lambda L, h: L.blocker_closed("seller-plus-kickstart")),
        ("Upload the six portfolio projects, PII masked, no client named",
         lambda L, h: L.has(account=h, entity="profile", action="portfolio_uploaded")),
        ("Load the first-reply templates into Fiverr Quick Responses",
         lambda L, h: L.has(account=h, entity="message", action="quick_responses_saved")),
        ("Start the daily metrics series. A gap in the series cannot be compared to anything",
         lambda L, h: len(L.metric_snapshots()) > 0),
    ],
    "chitraksh": [
        ("Open the Upwork freelancer account, India. Real name, real business address",
         lambda L, h: L.has(account=h, platform="upwork", entity="account", action="created")),
        ("Complete Upwork ID verification. It gates Rising Talent and unverified information risks suspension",
         lambda L, h: L.has(account=h, platform="upwork", entity="account", ref="id-verification", action="closed")),
        ("Take the profile to 100 percent. It is a Rising Talent prerequisite and 10 to 15 percent of the search algorithm",
         lambda L, h: L.has(account=h, platform="upwork", entity="profile", ref="general", action="completed")),
        ("Create the two specialized profiles: voice and telephony, workflow automation and AI integration",
         lambda L, h: L.has(account=h, platform="upwork", entity="profile", ref="spec-voice", action="created")),
        ("Populate the portfolio. The highest-leverage four hours of the month",
         lambda L, h: L.has(account=h, platform="upwork", entity="profile", action="portfolio_uploaded")),
        ("Record the 90-second Loom: a live call with the latency readout on screen. Largest measured proposal lift at 3.70pp",
         lambda L, h: L.has(account=h, entity="profile", ref="loom", action="recorded")),
        ("Check Project Catalog availability in the dashboard and log the answer. Upwork does not publish the gate",
         lambda L, h: L.has(account=h, platform="upwork", entity="profile", ref="project-catalog", action="checked")),
        ("Create the three Project Catalog listings mirroring the Fiverr gigs",
         lambda L, h: L.has(account=h, platform="upwork", entity="gig", ref="cat1", action="published")),
    ],
    "frankie": [
        ("Open the US Upwork freelancer account. Own device, own payment method, own withdrawal account",
         lambda L, h: L.has(account=h, platform="upwork", entity="account", action="created")),
        ("Complete ID verification and US location verification. The US flag is what unlocks US-only job posts",
         lambda L, h: L.has(account=h, platform="upwork", entity="account", ref="us-location-verification", action="closed")),
        ("Take the profile to 100 percent",
         lambda L, h: L.has(account=h, platform="upwork", entity="profile", ref="frankie-general", action="completed")),
        ("Subscribe to Freelancer Plus on this account: 100 Connects and competitor bid visibility",
         lambda L, h: L.has(account=h, platform="upwork", entity="account", ref="freelancer-plus", action="subscribed")),
        ("Turn the Availability Badge on with a hard cap of 100 Connects, about 15 dollars a month",
         lambda L, h: L.has(account=h, platform="upwork", entity="account", ref="availability-badge", action="enabled")),
        ("Put the LinkedIn Services page live with the free-consultation toggle on",
         lambda L, h: L.has(account=h, entity="profile", ref="linkedin-services", action="published")),
        ("Start bidding: 3 proposals on day 3, ramping to 5 a day. Under 250 words, zero cliches, Loom offered",
         lambda L, h: L.has(account=h, platform="upwork", entity="proposal", action="sent")),
    ],
    "orayalabs-agency": [
        ("Create the Oraya Labs agency from Chitraksh's freelancer account. One agency per freelancer, so get it right first time",
         lambda L, h: L.has(account=h, platform="upwork", entity="account", ref="agency", action="created")),
        ("Subscribe to Agency Plus, about 19.99 a month. Required before any member can be added",
         lambda L, h: L.has(account=h, platform="upwork", entity="account", ref="agency-plus", action="subscribed")),
        ("Invite Frankie as a business manager. He can then bid for the agency and is the only role that can accept an offer",
         lambda L, h: L.has(account=h, platform="upwork", entity="account", ref="agency-member-frankie", action="added")),
        ("Write the founder revenue-split agreement. Upwork does not facilitate agency-to-member payments",
         lambda L, h: L.has(account=h, entity="account", ref="founder-split-agreement", action="signed")),
    ],
    "agency": [
        ("BLOCKED until a third in-house member exists. Fiverr agencies require a minimum of 3 team members. "
         "Do not attempt a second Fiverr account as a workaround",
         lambda L, h: False),
    ],
}


# Lower number means it is answered first. Publishing and payout gates outrank
# everything, because a listing that cannot go live has no ranking to optimise and a
# spending decision can wait a day without costing anything.
BLOCKER_PRIORITY = {
    "id-verification": 0,
    "w8ben": 1,
    "india-gst": 2,
    "payout-setup": 3,
    "us-location-verification": 4,
    "education-graduation-year": 20,
    "seller-plus-kickstart": 30,
}


def track_of(handle):
    if not handle:
        return ""
    return handle[5:] if handle.startswith("TODO-") else handle


def account_next(ledger, account):
    """One next action for one account. Blockers beat overdue tasks beat due tasks beat
    the build order. Returns (source, text, due)."""
    platform = account.get("platform")
    handle = account.get("handle")
    today = today_str()

    tasks = ledger.open_tasks(platform=platform, account=handle)
    overdue = [t for t in tasks if (t.get("due") or "9999-12-31") < today]
    if overdue:
        task = overdue[0]
        return ("OVERDUE TASK", "%s: %s" % (task.get("ref"), task.get("detail") or ""), task.get("due"))

    blockers = ledger.open_blockers(platform=platform, account=handle)
    if blockers:
        # A gate that stops a listing publishing outranks a cosmetic gap, whatever order
        # they were logged in. A gig that cannot publish has no ranking to optimise.
        blockers.sort(key=lambda b: (BLOCKER_PRIORITY.get(b.get("ref"), 50), b.get("ts") or ""))
        blocker = blockers[0]
        return ("BLOCKER", "%s: %s" % (blocker.get("ref"), blocker.get("detail") or ""), None)

    if tasks:
        task = tasks[0]
        return ("TASK", "%s: %s" % (task.get("ref"), task.get("detail") or ""), task.get("due"))

    for label, done in BUILD_STEPS.get(track_of(handle), []):
        try:
            finished = bool(done(ledger, handle))
        except Exception:
            finished = False
        if not finished:
            return ("BUILD ORDER", label, None)

    return ("CLEAR", "No open blocker, no open task, and every build step logged. "
                     "Pull today's numbers and send today's proposals.", None)


def cmd_next(args):
    ledger = Ledger()
    out = ["NEXT ACTION PER ACCOUNT   read %s" % now_iso()]
    out.append("one action each, ranked: overdue task, then open blocker, then next due task, then the STRATEGY build order")
    rows = []
    for account in ledger.accounts.get("accounts", []):
        if args.platform and account.get("platform") != args.platform:
            continue
        if args.account and account.get("handle") != args.account:
            continue
        source, text, due = account_next(ledger, account)
        rows.append([
            "%s/%s" % (account.get("platform"), account.get("handle")),
            account.get("status", "-"),
            source,
            due or "-",
            text[:96],
        ])
    out.append("")
    out.append(table(["account", "state", "from", "due", "next action"], rows, indent=2))
    out.append("")
    out.append("  Owners: Chitraksh builds and delivers. Frankie sells, fronts the US, and holds the US Upwork")
    out.append("  account that is the only key to US-only job posts. See STRATEGY.md section (d).")
    out.append("")
    print("\n".join(out))
    return 0


# ---------------------------------------------------------------------------
# handoff: a resume brief for a fresh session
# ---------------------------------------------------------------------------


def cmd_handoff(args):
    ledger = Ledger()
    path = ROOT / (args.out or "NEXT-SESSION.md")

    status_text = capture(cmd_status, Bag(platform=None))
    next_text = capture(cmd_next, Bag(platform=None, account=None))
    checklist_rows = checklist_state(ledger)
    done = sum(1 for item in checklist_rows if item["done"])
    pending = [item for item in checklist_rows if not item["done"]]
    blockers = ledger.open_blockers()
    tasks = ledger.open_tasks()
    today = today_str()
    overdue = [t for t in tasks if (t.get("due") or "9999-12-31") < today]

    body = []
    add = body.append
    add("# NEXT SESSION")
    add("")
    add("Resume brief for a fresh Claude session with no memory of this one. Written by "
        "`python3 hub.py handoff` on %s. Everything below is derived from the ledger, "
        "`accounts.json` and `STRATEGY.md`, so it is current as of that run and not a moment later." % now_iso())
    add("")
    add("**Read these first, in this order:** `STRATEGY.md`, then `README.md`, then this file. "
        "The research behind every number is in `research/`, indexed in `research/INDEX.md`.")
    add("")
    add("**Writing rules that apply to everything you produce, including ledger detail text:** "
        "no em dashes, no U+2014, ever. An en dash only inside a numeric range. No invented numbers. "
        "Every figure carries its measurement basis and the date it was read. No fabricated metrics, "
        "no fake social proof, no invented client stories. Anonymise client data. "
        "Compliance framing is engineering, not legal advice.")
    add("")

    add("## 1. Who and what")
    add("")
    add("Oraya / Hanflux AI. Two founders. **Chitraksh Mayank**, graduate lawyer based in India, builds "
        "and delivers. **Frankie Alicea**, US-based licensed insurance producer, sells, fronts the US, "
        "and holds the US Upwork account that is the only key to US-only job posts.")
    add("")
    add("Three assets nobody else in the competitive set holds: a measured median **761 ms** time-to-first-audio "
        "on simulated calls, 26 August 2026, against a prior-vendor production p50 of **1.64 to 1.9 s**; "
        "**compliance enforced in code** rather than in a prompt; and **real dealership and insurance experience**.")
    add("")
    add("The 30-day objective is **five orders**, not revenue.")
    add("")

    add("## 2. Account state")
    add("")
    for account in ledger.accounts.get("accounts", []):
        add("- **%s / %s** [%s] owner %s. %s" % (
            account.get("platform"), account.get("handle"), account.get("status"),
            account.get("owner"), account.get("purpose") or ""))
    add("")
    add("Full verification state, listing states and the never-do list are in `accounts.json`. "
        "The registry is the source of truth for what exists; the ledger is the source of truth for what happened.")
    add("")

    add("## 3. What is built")
    add("")
    add("```")
    images = 0
    for path_obj in sorted(ROOT.rglob("*")):
        if not path_obj.is_file() or str(path_obj).endswith(".pyc"):
            continue
        relative = str(path_obj.relative_to(ROOT))
        if "gig-images" in relative:
            images += 1
            continue
        add(relative)
    add("research/gig-images/   (%d rendered PNGs, not listed individually)" % images)
    add("```")
    add("")
    add("Launch checklist: **%d of %d complete.** Run `python3 hub.py checklist` for the live version." % (done, len(checklist_rows)))
    add("")

    add("## 4. Exactly where the browser work stopped")
    add("")
    add("**Chrome is disconnected.** The last session ended mid-build in the Fiverr gig editor. "
        "Reconnect Chrome to an already authenticated Fiverr session before touching any of this. "
        "Never attempt to log in and never accept credentials.")
    add("")
    add("| Surface | State | Resume point |")
    add("|---|---|---|")
    add("| Fiverr seller profile | Live | Display name Chitraksh M. Education entry still incomplete, pending a confirmed graduation year |")
    add("| **Fiverr Gig 1**, voice receptionist | Draft complete | Slug locked as `build-ai-voice-receptionist-for-car-dealerships-and-insurance-agencies`. "
        "Three images and the video are still pending. Cannot publish until the verification gates clear |")
    add("| **Fiverr Gig 2**, compliance-gated outbound | **Paused at the Description step** | Overview and pricing are saved. "
        "Still to enter: the **description**, **7 FAQs**, **4 buyer requirements**, then upload images **gig2-a**, **gig2-b**, **gig2-c**. "
        "All copy is paste-ready in `research/fiverr-profile-package.md` section 3. Images are at `research/gig-images/gig2-a.png`, `gig2-b.png`, `gig2-c.png`. "
        "**Read the URL bar after the first save and write the real slug into `accounts.json`: it locks permanently** |")
    add("| **Fiverr Gig 3**, n8n workflows | **Not started** | Full paste-ready copy is in `research/fiverr-profile-package.md` section 4. "
        "Service type is **N8n Automation**, not AI Agents, which is what puts it in the workflow filter chip |")
    add("| **Upwork, all three entities** | **Not opened** | Chitraksh freelancer, Oraya Labs agency, Frankie US freelancer. "
        "Step-by-step click path is in `playbooks/upwork-account-setup.md`. Open on day 1: the 90-day Top Rated clock starts at first project |")
    add("| Ads | No spend, zero dollars | Campaigns registered and planned in `ads/campaigns.json`. Fiverr Promoted Gigs is not eligible in month 1 |")
    add("")

    add("## 5. Gates only the user can clear")
    add("")
    add("Do not attempt any of these. Flag them and stop. Each one needs the account holder in person.")
    add("")
    add("| Gate | Why it is user-only | Blocks |")
    add("|---|---|---|")
    add("| **ID verification** | Identity document and a liveness check | Fiverr publishing, and Upwork Rising Talent |")
    add("| **W-8BEN** | A tax declaration signed by the taxpayer | Fiverr payouts |")
    add("| **India GST declaration form** | A tax declaration signed by the taxpayer | Fiverr publishing |")
    add("| **Education graduation year** | A fact only Chitraksh knows | Profile completeness, which is a Rising Talent prerequisite on Upwork |")
    add("| **Seller Plus Kickstart decision** | A 15 dollar a month spending decision | Nothing hard. It buys keyword data and no ranking. Refundable within 48 hours |")
    add("| Payout method | Bank credentials | Fiverr payouts, and a valid withdrawal method is a Rising Talent requirement |")
    add("")

    add("## 6. Open blockers and overdue tasks")
    add("")
    if blockers:
        for blocker in blockers:
            add("- **BLOCKER** `%s` (%s): %s" % (blocker.get("ref"), (blocker.get("ts") or "")[:10], blocker.get("detail") or ""))
    else:
        add("- No open blockers.")
    add("")
    if overdue:
        for task in overdue:
            add("- **OVERDUE** `%s` due %s: %s" % (task.get("ref"), task.get("due"), task.get("detail") or ""))
    else:
        add("- No overdue tasks.")
    add("")
    add("Pending checklist items: %s" % (", ".join(item["key"] for item in pending) or "none"))
    add("")

    add("## 7. The first 10 steps, in order")
    add("")
    add("```bash")
    add("cd marketplace-hub")
    add("")
    add("# 1. Read the state. Nothing is done from memory.")
    add("python3 hub.py status")
    add("")
    add("# 2. Read the one next action per account.")
    add("python3 hub.py next")
    add("")
    add("# 3. Read what is still pending on the launch checklist.")
    add("python3 hub.py checklist")
    add("")
    add("# 4. Read the plan. STRATEGY.md sections (d) build order and (i) leading indicators.")
    add("#    Then playbooks/fiverr-gig-build.md for the Fiverr interface quirks.")
    add("")
    add("# 5. Ask the user to clear the user-only gates in section 5 above. Do not attempt them.")
    add("#    Log each one as it clears:")
    add("python3 hub.py log --platform fiverr --account hanfluxai --entity blocker \\")
    add("  --ref id-verification --action closed --detail \"ID verification passed\" --actor chitraksh")
    add("")
    add("# 6. Resume Fiverr Gig 2 at the Description step. Copy is in")
    add("#    research/fiverr-profile-package.md section 3. Paste the description, then the 7 FAQs,")
    add("#    then the 4 buyer requirements. Check the character counter before every save.")
    add("python3 hub.py log --platform fiverr --account hanfluxai --entity gig \\")
    add("  --ref gig2 --action description_saved --detail \"pasted the description, checked the counter\" --actor chitraksh")
    add("")
    add("# 7. Read the gig URL from the browser bar after the first save and write the real slug")
    add("#    into accounts.json. It locks permanently and is currently TODO.")
    add("python3 hub.py log --platform fiverr --account hanfluxai --entity gig \\")
    add("  --ref gig2 --action slug_recorded --detail \"real slug written into accounts.json\" --actor chitraksh")
    add("")
    add("# 8. Upload gig2-a, gig2-b and gig2-c from research/gig-images/ at 1280 x 769.")
    add("python3 hub.py log --platform fiverr --account hanfluxai --entity gig \\")
    add("  --ref gig2 --action images_uploaded --detail \"three images uploaded\" --actor chitraksh")
    add("")
    add("# 9. Build Gig 3 from research/fiverr-profile-package.md section 4.")
    add("#    Service type is N8n Automation, NOT AI Agents.")
    add("")
    add("# 10. Log the day and refresh the report.")
    add("python3 hub.py metrics add --platform fiverr --account hanfluxai --gig gig1 \\")
    add("  --impressions 0 --clicks 0 --orders 0 --messages 0 --source fiverr-gig-analytics")
    add("python3 hub.py export")
    add("python3 hub.py handoff")
    add("```")
    add("")
    add("**When Upwork is next on the list** rather than Fiverr, the click path is "
        "`playbooks/upwork-account-setup.md` and the first-week bidding cadence is its section 7. "
        "Open all three Upwork entities on the same day: the 90-day Top Rated clock starts at first project, "
        "and Rising Talent clears on a single 250 dollar order.")
    add("")

    add("## 8. Current next action per account")
    add("")
    add("```")
    add(next_text.rstrip())
    add("```")
    add("")
    add("## 9. Full status at handoff time")
    add("")
    add("```")
    add(status_text.rstrip())
    add("```")
    add("")
    add("## 10. Before anything ships")
    add("")
    add("Run the dash scan from `README.md` and confirm `total banned dash characters: 0`. "
        "Run it against text baked into images too, including SVG labels and JavaScript template strings. "
        "Then log what you did. If it is not in the ledger, it did not happen.")
    add("")

    text = "\n".join(body)
    path.write_text(text, encoding="utf-8")
    print("wrote %s  (%d bytes)" % (path, len(text.encode("utf-8"))))
    return 0


def cmd_ads_list(args):
    blob = load_json(CAMPAIGNS_PATH, {"campaigns": []})
    rows = []
    for campaign in blob.get("campaigns", []):
        rows.append([
            campaign.get("id"),
            campaign.get("channel"),
            campaign.get("status"),
            campaign.get("target_gig", "-"),
            campaign.get("budget_note", "TODO"),
            (campaign.get("audience") or "-")[:40],
        ])
    print("AD CAMPAIGN REGISTRY   %s" % CAMPAIGNS_PATH.name)
    print("")
    print(table(["id", "channel", "status", "gig", "budget", "audience"], rows, indent=2))
    print("")
    print("  Everything marked TODO is unverified. Do not invent a number to fill it.")
    print("")
    return 0


def cmd_ads_log(args):
    blob = load_json(CAMPAIGNS_PATH, {"campaigns": []})
    known = {c.get("id"): c for c in blob.get("campaigns", [])}
    campaign = known.get(args.campaign)
    if campaign is None:
        print("error: campaign %r is not in ads/campaigns.json. Add it there first, so spend always has a home."
              % args.campaign, file=sys.stderr)
        print("known ids: %s" % ", ".join(sorted(k for k in known if k)), file=sys.stderr)
        return 2

    snapshot_date = args.date or today_str()
    platform = campaign.get("platform") or args.platform or "fiverr"
    account = campaign.get("account") or args.account or "hanfluxai"
    gig = campaign.get("target_gig") or args.gig or "-"

    metrics_record = {
        "ts": now_iso(),
        "date": snapshot_date,
        "platform": platform,
        "account": account,
        "gig": gig,
        "source": "ads:%s" % args.campaign,
        "actor": args.actor,
        "note": args.note or "",
    }
    for field in METRIC_FIELDS:
        metrics_record[field] = None
    metrics_record["ad_spend"] = args.spend
    metrics_record["ad_clicks"] = args.clicks
    metrics_record["ad_impressions"] = args.impressions

    ledger = Ledger()
    key = (snapshot_date, platform, account, gig, "ads:%s" % args.campaign)
    duplicate = any(
        (r.get("date"), r.get("platform"), r.get("account"), r.get("gig"), r.get("source")) == key
        and r.get("ad_spend") == args.spend and r.get("ad_clicks") == args.clicks
        for r in ledger.metrics
    )
    if duplicate:
        print("skip: identical ad snapshot for %s on %s already recorded (idempotent)" % (args.campaign, snapshot_date))
        return 0

    append_jsonl(METRICS_PATH, metrics_record)

    event = {
        "id": None,
        "ts": now_iso(),
        "platform": platform,
        "account": account,
        "entity": "ad",
        "ref": args.campaign,
        "action": "spend_recorded",
        "detail": args.note or ("spend and clicks for %s" % snapshot_date),
        "metrics": {"ad_spend": args.spend, "ad_clicks": args.clicks, "impressions": args.impressions},
        "actor": args.actor,
    }
    event["id"] = event_id(event)
    if event["id"] not in ledger.ids():
        append_jsonl(EVENTS_PATH, event)

    print("ads: %s on %s  spend=%s clicks=%s impressions=%s  -> metrics.jsonl and events.jsonl" % (
        args.campaign, snapshot_date, fmt_num(args.spend), fmt_num(args.clicks), fmt_num(args.impressions)))
    return 0


def capture(fn, args):
    """Run a command that prints, and return what it printed."""
    import io
    buffer = io.StringIO()
    stdout = sys.stdout
    sys.stdout = buffer
    try:
        fn(args)
    finally:
        sys.stdout = stdout
    return buffer.getvalue()


class Bag:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __getattr__(self, name):
        return None


def cmd_export(args):
    report_date = args.date or today_str()
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    path = REPORTS_DIR / ("%s.md" % report_date)

    status_text = capture(cmd_status, Bag(platform=args.platform))
    checklist_text = capture(cmd_checklist, Bag())
    metrics_text = capture(cmd_metrics_report, Bag(platform=args.platform, account=None, gig=None, weeks=8))

    ledger = Ledger()
    recent = [e for e in ledger.events if (e.get("ts") or "")[:10] >= (date.fromisoformat(report_date) - timedelta(days=7)).isoformat()]
    recent_rows = [[
        (e.get("ts") or "")[:10],
        "%s/%s" % (e.get("platform"), e.get("account")),
        "%s:%s" % (e.get("entity"), e.get("ref") or "-"),
        e.get("action"),
        (e.get("detail") or "")[:70],
    ] for e in recent[-40:]]

    body = []
    body.append("# Marketplace Hub report, %s" % report_date)
    body.append("")
    body.append("Generated by `python3 hub.py export`. Source of truth is `ledger/events.jsonl` and `ledger/metrics.jsonl`, both append-only.")
    body.append("")
    body.append("## Status")
    body.append("")
    body.append("```")
    body.append(status_text.rstrip())
    body.append("```")
    body.append("")
    body.append("## Launch checklist")
    body.append("")
    body.append("```")
    body.append(checklist_text.rstrip())
    body.append("```")
    body.append("")
    body.append("## Metrics")
    body.append("")
    body.append("```")
    body.append(metrics_text.rstrip())
    body.append("```")
    body.append("")
    body.append("## Events in the last 7 days")
    body.append("")
    body.append("```")
    body.append(table(["date", "account", "entity", "action", "detail"], recent_rows, indent=0))
    body.append("```")
    body.append("")
    body.append("## What a reader should do with this")
    body.append("")
    body.append("1. Clear every open blocker above before touching anything cosmetic. A gig that cannot publish has no ranking to optimise.")
    body.append("2. Work the overdue next actions top to bottom. Due dates are set when the action is logged, not invented at review time.")
    body.append("3. Act on the leading-indicator flags, one change per week per gig, so the effect is attributable.")
    body.append("")

    text = "\n".join(body)
    path.write_text(text, encoding="utf-8")
    print("wrote %s  (%d bytes)" % (path, len(text.encode("utf-8"))))
    return 0


# ---------------------------------------------------------------------------
# argument parser
# ---------------------------------------------------------------------------


def build_parser():
    parser = argparse.ArgumentParser(
        prog="hub.py",
        description="Marketplace Hub: append-only operating ledger for marketplace go-to-market.",
        epilog="Every action taken on any marketplace gets logged. If it is not in the ledger, it did not happen.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = parser.add_subparsers(dest="command")

    # log
    p_log = sub.add_parser("log", help="append one structured event to ledger/events.jsonl")
    p_log.add_argument("--platform", required=True, help="fiverr, upwork, meta, google, all")
    p_log.add_argument("--account", required=True, help="account handle, for example hanfluxai")
    p_log.add_argument("--entity", required=True, choices=ENTITIES,
                       help="what the event is about: " + ", ".join(ENTITIES))
    p_log.add_argument("--ref", default=None, help="which one: gig1, seller-profile, id-verification, order id")
    p_log.add_argument("--action", required=True,
                       help="what happened: draft_saved, published, opened, closed, delivered, sent, replied")
    p_log.add_argument("--detail", default="", help="one sentence of plain English, no em dashes")
    p_log.add_argument("--metric", action="append", default=[], metavar="KEY=VALUE",
                       help="repeatable numeric context, for example --metric price=450")
    p_log.add_argument("--actor", default=os.environ.get("HUB_ACTOR", "chitraksh"),
                       help="who did it (default: $HUB_ACTOR or chitraksh)")
    p_log.add_argument("--due", default=None, help="for entity=task, the due date as YYYY-MM-DD")
    p_log.add_argument("--ts", default=None, help="override the timestamp, ISO 8601 UTC")
    p_log.add_argument("--id", default=None, help="explicit event id, so re-running the same command is a no-op")
    p_log.add_argument("--once", action="store_true",
                       help="skip if an identical event already exists, ignoring timestamp")
    p_log.set_defaults(func=cmd_log)

    # status
    p_status = sub.add_parser("status", help="print the dashboard: accounts, listing states, blockers, next actions")
    p_status.add_argument("--platform", default=None, help="limit to one platform")
    p_status.set_defaults(func=cmd_status)

    # next
    p_next = sub.add_parser("next", help="print the single next action per account, from the ledger and the STRATEGY build order")
    p_next.add_argument("--platform", default=None, help="limit to one platform")
    p_next.add_argument("--account", default=None, help="limit to one account handle")
    p_next.set_defaults(func=cmd_next)

    # handoff
    p_handoff = sub.add_parser("handoff", help="write NEXT-SESSION.md, a complete resume brief for a fresh session")
    p_handoff.add_argument("--out", default=None, help="output filename, relative to the hub root (default NEXT-SESSION.md)")
    p_handoff.set_defaults(func=cmd_handoff)

    # checklist
    p_check = sub.add_parser("checklist", help="print the launch checklist with done and pending read from the ledger")
    p_check.set_defaults(func=cmd_checklist)

    # metrics
    p_metrics = sub.add_parser("metrics", help="daily snapshots and the weekly rollup")
    m_sub = p_metrics.add_subparsers(dest="metrics_command")

    p_add = m_sub.add_parser("add", help="append one daily metric snapshot to ledger/metrics.jsonl")
    p_add.add_argument("--platform", required=True)
    p_add.add_argument("--account", required=True)
    p_add.add_argument("--gig", default=None, help="gig ref, or leave off for an account-level snapshot")
    p_add.add_argument("--date", default=None, help="YYYY-MM-DD, defaults to today")
    p_add.add_argument("--source", default=None, help="where the numbers came from, for example fiverr-gig-analytics")
    p_add.add_argument("--note", default=None)
    p_add.add_argument("--actor", default=os.environ.get("HUB_ACTOR", "chitraksh"))
    for field in METRIC_FIELDS:
        flag = "--" + field.replace("_", "-")
        kind = float if field in FLOAT_FIELDS else int
        p_add.add_argument(flag, dest=field, type=kind, default=None)
    p_add.set_defaults(func=cmd_metrics_add)

    p_report = m_sub.add_parser("report", help="weekly rollup with week-over-week deltas and leading-indicator flags")
    p_report.add_argument("--platform", default=None)
    p_report.add_argument("--account", default=None)
    p_report.add_argument("--gig", default=None)
    p_report.add_argument("--weeks", type=int, default=8, help="how many weeks to show (default 8)")
    p_report.set_defaults(func=cmd_metrics_report)

    # ads
    p_ads = sub.add_parser("ads", help="ad campaign registry and spend logging")
    a_sub = p_ads.add_subparsers(dest="ads_command")

    p_ads_list = a_sub.add_parser("list", help="print the campaign registry from ads/campaigns.json")
    p_ads_list.set_defaults(func=cmd_ads_list)

    p_ads_log = a_sub.add_parser("log", help="log campaign spend and clicks into metrics and the event ledger")
    p_ads_log.add_argument("--campaign", required=True, help="campaign id from ads/campaigns.json")
    p_ads_log.add_argument("--date", default=None, help="YYYY-MM-DD, defaults to today")
    p_ads_log.add_argument("--spend", type=float, default=None, help="spend in USD for that day")
    p_ads_log.add_argument("--clicks", type=int, default=None)
    p_ads_log.add_argument("--impressions", type=int, default=None)
    p_ads_log.add_argument("--platform", default=None, help="override the campaign's platform")
    p_ads_log.add_argument("--account", default=None)
    p_ads_log.add_argument("--gig", default=None)
    p_ads_log.add_argument("--note", default=None)
    p_ads_log.add_argument("--actor", default=os.environ.get("HUB_ACTOR", "chitraksh"))
    p_ads_log.set_defaults(func=cmd_ads_log)

    # export
    p_export = sub.add_parser("export", help="write a markdown report to reports/YYYY-MM-DD.md")
    p_export.add_argument("--date", default=None, help="report date, defaults to today")
    p_export.add_argument("--platform", default=None)
    p_export.set_defaults(func=cmd_export)

    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)

    if not getattr(args, "func", None):
        # A group was named without a subcommand, or nothing was named at all.
        if getattr(args, "command", None) == "metrics":
            print("metrics needs a subcommand: add or report. Try `python3 hub.py metrics --help`.", file=sys.stderr)
            return 2
        if getattr(args, "command", None) == "ads":
            print("ads needs a subcommand: list or log. Try `python3 hub.py ads --help`.", file=sys.stderr)
            return 2
        parser.print_help()
        return 0

    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
