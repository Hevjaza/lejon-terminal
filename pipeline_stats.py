#!/usr/bin/env python3
"""Build an honest pipeline_stats.json from desk files.

Sources: journal/*.md, leads/, research/screened.txt (optional notes),
positions/ledger.json, positions/*.json, shadow-b/, shadow-c/.

Never invent numbers. Fields that cannot be measured are set to null
and listed under "unknowns" (the UI shows them as "okänt").
PAPER only. No secrets, no RPC URLs, no keys.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

TZ = ZoneInfo("Europe/Stockholm")

# Words that are never token tickers when captured by the name regex.
_NAME_STOP = {
    "new", "only", "all", "the", "and", "disc", "py", "scout", "risk",
    "check", "factory", "equity", "shadow", "others", "other", "near",
    "miss", "misses", "no", "buy", "open", "mark", "cycle", "paper",
    "hard", "kill", "pass", "flag", "previously", "screened", "killed",
    "eligible", "candidates", "candidate", "token", "tokens", "via",
    "rule", "rules", "age", "liq", "liquidity", "both", "already",
    "rest", "unknown", "ok", "sol", "ticket", "sync", "lejon", "b", "c",
    "vs", "is", "on", "of", "in", "at", "or", "to", "for", "from",
    "with", "not", "yes", "re", "run", "rerun", "unchanged",
    "top", "top10", "top15", "creator", "buyers", "wallets", "wallet",
    "migration", "slot", "slot0", "too", "young", "previously", "handled",
    "cannot", "bundling", "signed", "signer", "holder", "holders",
    "funding", "walk", "done", "unresolved", "unverified", "odd",
    "listed", "real", "confirmed", "creates", "sigs", "window", "total",
    "hard", "flag", "miss", "ages", "ratio", "vol", "vol1h", "buy",
    "sell", "pump", "fun", "raydium", "meteora", "pumpswap", "launchlab",
    "slots", "co", "cosigned", "percent", "dev", "rest", "already",
    "screened", "killed", "skipped", "eligible", "candidate", "candidates",
    "near", "misses", "both", "all", "only", "new", "nya", "others",
    "pool",
    "burned",
    "null",
    "create",
    "field",
    "curve",
    "exchange",
    "distributor",
    "origin",
    "budget",
    "unread",
    "history",
    "clear", "but", "however",
    "shitcoin",
    "dca",
    "rpc",
    "rugcheck",
    "files",
    "trader",
    "deployer",
    "impact",
    "authorities",
    "residual",
    "other", "no", "buy", "equity", "shadow", "sync", "lejon",
}


def _now() -> datetime:
    return datetime.now(TZ)


def _safe_read(path: Path) -> str:
    try:
        if path.name == ".env" or "PumpGrok/.env" in str(path):
            return ""
        return path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return ""


def _load_json(path: Path) -> Any:
    t = _safe_read(path)
    if not t:
        return None
    try:
        return json.loads(t)
    except Exception:
        return None


def _truthy(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return value != 0
    if isinstance(value, str):
        return value.strip().lower() in {"true", "yes", "1"}
    return False


def parse_cycle_time(day: str, title: str) -> datetime | None:
    """Parse cycle timestamps in several journal formats (Europe/Stockholm)."""
    # Cycle 353 (2026-11-12 00:06-00:10 Stockholm)  /  (2026-11-12 ~23:53 Stockholm)
    tm = re.search(
        r"(?:\(|\s)(\d{4}-\d{2}-\d{2})\s+~?(\d{1,2}):(\d{2})(?:\s*-\s*~?\d{1,2}:\d{2})?\s*Stockholm",
        title,
    )
    if tm:
        try:
            return datetime(
                int(tm.group(1)[0:4]), int(tm.group(1)[5:7]), int(tm.group(1)[8:10]),
                int(tm.group(2)), int(tm.group(3)), tzinfo=TZ,
            )
        except Exception:
            pass
    # Cycle 727 (~00:06 Stockholm)  /  (~00:15-00:35 Stockholm, 2026-11-14)
    # Cycle 607 (09:33 Stockholm, 2026-11-16)  /  (08:50-08:58 Stockholm, 2026-11-16)
    tm = re.search(
        r"\(?~?(\d{1,2}):(\d{2})(?:\s*-\s*~?\d{1,2}:\d{2})?\s*Stockholm(?:,\s*(\d{4}-\d{2}-\d{2}))?",
        title,
    )
    if tm:
        date = tm.group(3) or day
        try:
            return datetime(
                int(date[0:4]), int(date[5:7]), int(date[8:10]),
                int(tm.group(1)), int(tm.group(2)), tzinfo=TZ,
            )
        except Exception:
            pass
    # Older: "00:00 (23:00Z) paper cycle 5" — first clock is Stockholm
    tm = re.match(r"(\d{1,2}):(\d{2})\s+\(\d{1,2}:\d{2}Z", title)
    if tm:
        try:
            return datetime(int(day[0:4]), int(day[5:7]), int(day[8:10]), int(tm.group(1)), int(tm.group(2)), tzinfo=TZ)
        except Exception:
            pass
    # Older: "20:15Z research cycle 2" — UTC
    tm = re.match(r"(\d{1,2}):(\d{2})Z\b", title)
    if tm:
        try:
            utc = datetime(int(day[0:4]), int(day[5:7]), int(day[8:10]), int(tm.group(1)), int(tm.group(2)), tzinfo=ZoneInfo("UTC"))
            return utc.astimezone(TZ)
        except Exception:
            pass
    return None


def iter_journal_cycles(journal_dir: Path) -> list[dict[str, Any]]:
    out: list[dict[str, Any]] = []
    files = sorted(journal_dir.glob("*.md"))
    for jf in files:
        day = jf.stem
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", day):
            continue
        text = _safe_read(jf)
        parts = re.split(r"^## ", text, flags=re.M)
        for part in parts[1:]:
            lines = part.splitlines()
            if not lines:
                continue
            title = lines[0].strip()
            cm = re.search(r"(?:paper cycle|Cycle)\s+(\d+)", title, re.I)
            if not cm:
                continue
            cycle = int(cm.group(1))
            body = " ".join(ln.strip() for ln in lines[1:] if ln.strip())
            # Flatten whitespace
            body = re.sub(r"\s+", " ", body).strip()
            ts = parse_cycle_time(day, title)
            out.append({
                "day": day,
                "cycle": cycle,
                "title": title,
                "time": ts,
                "body": body,
            })
    out.sort(key=lambda r: (r["time"] or datetime(1970, 1, 1, tzinfo=TZ), r["cycle"]))
    return out


def _clean_name(raw: str) -> str | None:
    if not raw:
        return None
    s = raw.strip().strip("$,;:.")
    s = re.sub(r"\s*#\s*\d+\s*$", "", s).strip()
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"^(only|new|nya)\s+", "", s, flags=re.I).strip()
    if not s or len(s) > 24:
        return None
    if re.fullmatch(r"R\d+", s, re.I) or re.fullmatch(r"c\d+", s, re.I):
        return None
    # Mint-like (mixed case + digits) is not a ticker
    if re.search(r"[A-Z]", s) and re.search(r"[a-z]", s) and re.search(r"\d", s):
        return None
    if not re.fullmatch(r"[A-Za-zÀ-ÿ][A-Za-zÀ-ÿ0-9_.$]{0,23}", s):
        return None
    key = s.lower()
    if key in _NAME_STOP:
        return None
    if s.lower() in {"disc.py", "paperfill.py", "scout_check", "factory_check"}:
        return None
    return s


def _extract_mint(text: str) -> str | None:
    """Public mint prefixes only (truncated with … / ... or full base58). Not English words."""
    m = re.search(r"\b([1-9A-HJ-NP-Za-km-z]{6,})(?:…|\.{2,3})(?:pump)?", text)
    if m:
        return m.group(1)[:12]
    m = re.search(r"\b([1-9A-HJ-NP-Za-km-z]{32,44})(?:pump)?\b", text)
    if m:
        return m.group(1)[:12]
    return None


def _rules_from(text: str) -> list[str]:
    found: set[str] = set()
    t = text or ""
    # Rules 1+2+11 / Rules 1-eq/2-eq/11-eq / Rule 1, Rule 2
    for m in re.finditer(r"Rules?\s+((?:(?:\d+)(?:-eq)?(?:\s*[+/,&]\s*)?)+)", t, re.I):
        for n in re.findall(r"\d+", m.group(1)):
            if n in {"1", "2", "11"}:
                found.add(n)
    for m in re.finditer(r"R(?:ule)?\s*(\d+)(?:-eq)?", t, re.I):
        n = m.group(1)
        if n in {"1", "2", "11"}:
            # Avoid treating "R1 10.23 %" in a PASS as a kill rule unless KILL is nearby
            found.add(n)
    # "1-eq/2-eq/11-eq"
    for n in re.findall(r"\b(\d+)-eq\b", t, re.I):
        if n in {"1", "2", "11"}:
            found.add(n)
    return sorted(found, key=lambda x: int(x))


def _classify_outcome(text: str) -> tuple[str, list[str]]:
    """Return (kind, rules) for a token outcome snippet.

    kind is one of: scout_kill, factory_kill, funding_avoid, risk_other,
    skipped_unverified, bought, filter_age_liq, pass_to_risk, unknown.
    """
    t = text or ""
    tl = t.lower()

    bought = bool(re.search(
        r"(paper buy|paper-köp|simulated paper buy|ticket\s+SOL-\d{8}-\d+)",
        t, re.I,
    ))
    factory = bool(re.search(
        r"factory_check[^\n]{0,180}KILL|launch factory|check 8[^\n]{0,80}KILL",
        t, re.I,
    ))
    funding = bool(re.search(
        r"funding (walk|chain|not (traced|traceable|done|fully|resolved))|"
        r"hidden funding|unresolved funding|funding not resolved|"
        r"origin untraceable|finansiering",
        t, re.I,
    )) and bool(re.search(r"\bAVOID\b", t, re.I))
    # DCTC-style: funding walk not done + AVOID (unverified)
    if re.search(r"funding walk.*(?:not done|not traced)|bundling flag unresolved", t, re.I) and re.search(r"\bAVOID\b", t, re.I):
        funding = True
    scout_kill = bool(re.search(
        r"KILLED-SCOUT|scout_check\s+KILL|scout\s+KILL|KILLED\s+via scout|"
        r"\bKILL(?:ED)?\s+Rules?\s*\d",
        t, re.I,
    ))
    risk_avoid = bool(re.search(r"\bAVOID\b|RISK KILL|RISK check.*KILL", t, re.I))
    skipped = bool(re.search(
        r"skipped unverified|skip(?:ped)? unverified|not pump\.fun|"
        r"Rule 11 BLIND|Rules?\s*2/11 unverifiable|obekräftad",
        t, re.I,
    )) and not scout_kill and not factory and not bought
    # Only treat as age/liq filter when the token was actually not eligible
    age_liq = bool(re.search(
        r"age\s*<?\s*30|too young|near-miss|not eligible|"
        r"liq(?:uidity)?\s*<\s*25|liq\s+\d+(\.\d+)?k\s*<\s*25",
        t, re.I,
    ))
    age_m = re.search(r"age\s*~?\s*(\d{{1,2}})m", t, re.I)
    if age_m and int(age_m.group(1)) < 30:
        age_liq = True

    if bought:
        return "bought", []
    if factory:
        return "factory_kill", []
    if funding:
        return "funding_avoid", []
    if scout_kill:
        rules = _rules_from(t)
        # For a KILL line, Rule mentions are the kill reasons. Drop PASS context R1 percentages:
        # if the snippet also has PASS and then KILL, _rules_from may pick up R1 from PASS.
        # Keep rules only if a Rule/Rules clause is in a KILL clause.
        kill_bit = t
        mk = re.search(r"(KILLED-SCOUT|scout_check\s+KILL|scout\s+KILL).*$", t, re.I)
        if mk:
            rules = _rules_from(mk.group(0))
        return "scout_kill", rules
    if risk_avoid:
        return "risk_other", []
    if skipped:
        return "skipped_unverified", []
    if age_liq:
        return "filter_age_liq", []
    if re.search(r"scout_check\s+PASS", t, re.I):
        return "pass_to_risk", []
    return "unknown", []


def _split_new_items(blob: str) -> list[str]:
    """Split a 'New: A ...; B ...' blob only when the next chunk is a token."""
    if not blob:
        return []
    # Next token starts with a ticker and preferably a mint parenthesis or a verdict verb.
    nxt = r"(?=[A-Za-zÀ-ÿ][A-Za-zÀ-ÿ0-9_.$]{1,30}(?:\s+#\d+)?\s*\()"
    parts = re.split(
        rf"\s*;\s+{nxt}|\s+(?:and|&)\s+{nxt}|(?<=\))\s+{nxt}",
        blob,
    )
    return [p.strip(" .;,") for p in parts if p.strip(" .;,")]



def extract_new_tokens(body: str) -> list[dict[str, Any]]:
    """Extract tokens presented as new eligible (or new vs prior cycle)."""
    items: list[dict[str, Any]] = []
    # Skip pure re-mentions: "only new vs 745 is DCTC ... (previously AVOID"
    if re.search(r"only new vs\s+\d+\s+is\s+", body, re.I) and re.search(
        r"previously\s+(AVOID|KILL|screened)", body, re.I
    ):
        return items

    # Strong end markers so mid-sentence periods (PASS-FLAG. factory_check...) stay in the snippet.
    end_ok = r"(?=\s+(?:Others? previously|Others? already|No buy|Equity|Shadow B|Near-miss)|$)"
    blobs: list[str] = []

    for m in re.finditer(
        rf"\bonly\s+(.+?)\s+new(?:\s+eligible)?\s*(?:->|:)\s*(.+?){end_ok}",
        body,
        re.I,
    ):
        blobs.append(m.group(1) + " " + m.group(2))

    for m in re.finditer(
        rf"\bNEW\s+([A-Za-zÀ-ÿ][A-Za-zÀ-ÿ0-9_.$ ]{{0,30}}?)\s*(\([^)]{{0,240}}\))?\s*[:]\s*(.+?){end_ok}",
        body,
        re.I,
    ):
        blobs.append(m.group(1) + " " + (m.group(2) or "") + " " + m.group(3))

    for m in re.finditer(
        rf"\bNew:\s*(.+?){end_ok}",
        body,
        re.I,
    ):
        blobs.append(m.group(1))

    for m in re.finditer(
        rf"(?:candidates|eligible);\s*new:\s*(.+?){end_ok}",
        body,
        re.I,
    ):
        blobs.append(m.group(1))

    for m in re.finditer(
        rf"\bnew\s+([A-Za-zÀ-ÿ][A-Za-zÀ-ÿ0-9_.$]{{0,30}}(?:\s+#\d+)?)\s*(\([^)]{{0,240}}\))?\s*(?:->|:)\s*(.+?){end_ok}",
        body,
        re.I,
    ):
        blobs.append(m.group(1) + " " + (m.group(2) or "") + " " + m.group(3))

    seen_local: set[str] = set()
    for blob in blobs:
        for snippet in _split_new_items(blob):
            nm = re.match(
                r"([A-Za-zÀ-ÿ][A-Za-zÀ-ÿ0-9_.$]{0,30}(?:\s+#?\d+)?)(?:\s*\(([^)]{0,240})\))?(.*)$",
                snippet.strip(),
            )
            if not nm:
                nm2 = re.match(r"([A-Za-zÀ-ÿ][A-Za-zÀ-ÿ0-9_.$]{0,30})\b(.*)$", snippet.strip())
                if not nm2:
                    continue
                name = _clean_name(nm2.group(1))
                rest = nm2.group(2)
                mint = _extract_mint(snippet)
            else:
                name = _clean_name(nm.group(1))
                mint = _extract_mint(nm.group(2) or "") or _extract_mint(snippet)
                rest = (nm.group(2) or "") + " " + (nm.group(3) or "")
            if not name or name.lower() in {"others", "other", "rest"}:
                continue
            key = name.lower() + "|" + ((mint or "")[:8].lower())
            if key in seen_local:
                continue
            # Ignore trailing "Rest/Others previously screened" and a following other-token sentence
            own = re.sub(r"\.\s+(?:Rest|Others?)\s+previously\b.*", "", snippet, flags=re.I)
            own = re.split(r"\.\s+(?=[A-Z][A-Za-z0-9].{0,50}\b(?:liq|age|near-miss|not eligible))", own, maxsplit=1)[0]
            if re.search(r"previously\s+(AVOID|KILL|screened|killed|handled)", own, re.I):
                continue
            # Explicitly not eligible / near-miss — counted as filter, not a new eligible candidate.
            if re.search(r"near-miss|not eligible|too young", own, re.I) or (
                (m_age := re.search(r"age\s*~?\s*(\d{1,2})m", own, re.I)) and int(m_age.group(1)) < 30
            ):
                continue
            kind, rules = _classify_outcome(own + " " + rest)
            seen_local.add(key)
            items.append({
                "symbol": name,
                "mint": mint,
                "kind": kind,
                "rules": rules,
                "snippet": snippet[:240],
                "source": "journal_new",
            })
    return items



def _split_list_items(blob: str) -> list[str]:
    """Split a comma/semicolon list without cutting inside parentheses."""
    items: list[str] = []
    buf: list[str] = []
    depth = 0
    i = 0
    n = len(blob)
    while i < n:
        ch = blob[i]
        if ch in "([" :
            depth += 1
            buf.append(ch)
        elif ch in ")]" and depth:
            depth -= 1
            buf.append(ch)
        elif depth == 0 and ch in ",;":
            item = "".join(buf).strip(" .")
            if item:
                items.append(item)
            buf = []
        elif depth == 0 and blob[i:i + 5].lower() == " and " and re.match(
            r" and [A-Za-zÀ-ÿ]", blob[i:i + 7], re.I
        ):
            item = "".join(buf).strip(" .")
            if item:
                items.append(item)
            buf = []
            i += 4  # skip ' and', loop +1 adds the space remainder? we'll skip ' and'
        else:
            buf.append(ch)
        i += 1
    item = "".join(buf).strip(" .")
    if item:
        items.append(item)
    return items


def _near_miss_sections(body: str) -> list[str]:
    """Return only the near-miss clauses, not the whole cycle body."""
    secs: list[str] = []
    for m in re.finditer(
        r"near-miss(?:es)?\b[^:]{0,80}:\s*(.+?)(?=\s+(?:No buy|Equity|Shadow B|Others? previously|Others? already|disc\.py)|$)",
        body,
        re.I,
    ):
        secs.append(m.group(1))
    # "near-misses (Billy, KODA age<30m; Doubloon liq<25k) not eligible"
    for m in re.finditer(
        r"near-miss(?:es)?\s*\(([^)]{3,400})\)",
        body,
        re.I,
    ):
        secs.append(m.group(1))
    # "TOKEN ... near-miss" / "TOKEN near-miss age..."
    for m in re.finditer(
        r"\b([A-Za-zÀ-ÿ][A-Za-zÀ-ÿ0-9_.$]{1,30}(?:\s+#\d+)?)"
        r"(?:\s*\([^)]{0,160}\))?"
        r"\s+(?:age[^.,;]{0,40}|liq[^.,;]{0,40})\s+near-miss[^.,;]{0,80}",
        body,
        re.I,
    ):
        secs.append(m.group(0))
    for m in re.finditer(
        r"\b([A-Za-zÀ-ÿ][A-Za-zÀ-ÿ0-9_.$]{1,30}(?:\s+#\d+)?)"
        r"(?:\s*\([^)]{0,160}\))?"
        r"\s+near-miss\s+(?:age|liq)[^.,;]{0,60}",
        body,
        re.I,
    ):
        secs.append(m.group(0))
    # "X liq 20k near-miss"
    for m in re.finditer(
        r"\b([A-Za-zÀ-ÿ][A-Za-zÀ-ÿ0-9_.$]{1,30}(?:\s+#\d+)?)\s+liq\s+\d[\d.]*k\s+near-miss",
        body,
        re.I,
    ):
        secs.append(m.group(0))
    # "NAME (…, age 24m near-miss)" and "NAME (…) liq 24.8k <25k not eligible"
    for m in re.finditer(
        r"\b([A-Za-zÀ-ÿ][A-Za-zÀ-ÿ0-9_.$]{1,30}(?:\s+#\d+)?)\s*\([^)]*age\s*~?\s*\d+m\s+near-miss[^)]*\)[^.]{0,200}",
        body,
        re.I,
    ):
        secs.append(m.group(0))
    for m in re.finditer(
        r"\b([A-Za-zÀ-ÿ][A-Za-zÀ-ÿ0-9_.$]{1,30}(?:\s+#\d+)?)(?:\s*\([^)]{0,160}\))?\s+liq\s+\d[\d.]*k\s*<\s*25[^.;]{0,60}not eligible",
        body,
        re.I,
    ):
        secs.append(m.group(0))
    return secs


def extract_near_misses(body: str) -> list[dict[str, Any]]:
    items: list[dict[str, Any]] = []
    seen: set[str] = set()
    unnamed = False
    sections = _near_miss_sections(body)
    if re.search(r"near-miss", body, re.I) and not sections:
        # A near-miss was mentioned but no clause was isolated.
        if re.search(r"near-miss(?:es)?\s*\((?:age|liq)", body, re.I) or re.search(
            r"near-miss(?:es)?(?:\s+\([^)]*(?:age|liq)[^)]*\))(?!\s*:)", body, re.I
        ):
            unnamed = True

    for blob in sections:
        # Split list items: commas / slashes / semicolons / " and " between names
        parts = _split_list_items(blob)
        got_any = False
        section_is_filter = bool(re.search(r"\b(?:age|liq|30m|25k|too young|not eligible|near-miss)\b", blob, re.I))
        for part in parts:
            part = part.strip(" .")
            if not part:
                continue
            nm = re.match(
                r"([A-Za-zÀ-ÿ][A-Za-zÀ-ÿ0-9_.$]{1,30}(?:\s+#\d+)?)"
                r"(?:\s*\(([^)]{0,200})\))?"
                r"(.*)$",
                part,
            )
            if not nm:
                continue
            name = _clean_name(nm.group(1))
            if not name:
                continue
            rest = (nm.group(2) or "") + " " + (nm.group(3) or "")
            if not (nm.group(2) or section_is_filter or re.search(r"\b(?:age|liq|30m|25k|too young|not eligible|KILL|PASS)\b", rest, re.I)):
                continue
            key = name.lower()
            if key in seen:
                continue
            seen.add(key)
            got_any = True
            kind, rules = _classify_outcome(part)
            items.append({
                "symbol": name,
                "mint": _extract_mint(nm.group(2) or "") or _extract_mint(part),
                "kind": "filter_age_liq",
                "rules": rules if kind == "scout_kill" else [],
                "would_scout_kill": kind == "scout_kill",
                "snippet": part[:240],
                "source": "journal_near_miss",
            })
        if not got_any and re.search(r"age|liq|30m|25k", blob, re.I):
            unnamed = True
    if unnamed:
        items.append({
            "symbol": None,
            "mint": None,
            "kind": "filter_age_liq",
            "rules": [],
            "snippet": "unnamed near-miss",
            "source": "journal_near_miss_unnamed",
            "unnamed": True,
        })
    return items


def extract_extra_outcomes(body: str, already: set[str]) -> list[dict[str, Any]]:
    """Named outcomes with a mint in parentheses, not already captured and not in a near-miss list."""
    items: list[dict[str, Any]] = []
    # Mask near-miss clauses so we do not promote them to new eligible tokens.
    masked = body
    for sec in _near_miss_sections(body):
        if sec:
            masked = masked.replace(sec, " ")
    for m in re.finditer(
        r"\b([A-Za-zÀ-ÿ][A-Za-zÀ-ÿ0-9_.$]{1,30}(?:\s+#\d+)?)\s*"
        r"\(([1-9A-HJ-NP-Za-km-z]{4,}[^)]{0,200})\)\s+"
        r"(?:scout_check\s+KILL|KILLED-SCOUT|scout\s+KILL|scout_check\s+PASS|"
        r"RISK(?:\s+check\s+8)?[^\.]{0,100}(?:KILL|AVOID)|"
        r"factory_check[^\.]{0,100}KILL|Verdict\s+AVOID|"
        r"simulated paper buy|Ticket\s+SOL-\d{8}-\d+)"
        r"[^.]{0,280}",
        masked,
        re.I,
    ):
        name = _clean_name(m.group(1))
        mint_pfx = (_extract_mint(m.group(2) or "") or _extract_mint(m.group(0) or "") or "")[:8].lower()
        if not name:
            continue
        if name.lower() in already or (name.lower() + "|" + mint_pfx) in already:
            continue
        snippet = m.group(0)
        if re.search(r"previously\s+(AVOID|KILL|screened|killed|handled)|near-miss|not eligible|too young", snippet, re.I):
            continue
        kind, rules = _classify_outcome(snippet)
        if kind in {"unknown", "filter_age_liq"}:
            continue
        items.append({
            "symbol": name,
            "mint": _extract_mint(m.group(2) or "") or _extract_mint(snippet),
            "kind": kind,
            "rules": rules,
            "snippet": snippet[:240],
            "source": "journal_extra",
        })
    return items


def eligible_count(body: str) -> int | None:
    m = re.search(r"disc\.py:\s*(\d+)\s+(?:eligible|candidates)\b", body, re.I)
    if m:
        return int(m.group(1))
    if re.search(r"disc\.py:\s*(?:only |no new eligible|no new candidate)", body, re.I):
        # "only X new" without a leading number
        if re.search(r"disc\.py:\s*only\s+", body, re.I):
            return None  # unknown total eligible; new tokens still counted
        if re.search(r"disc\.py:\s*no new (eligible|candidate)", body, re.I):
            return 0  # no *new* eligible — not the same as 0 eligible shown
    return None


def new_eligible_flag_zero(body: str) -> bool:
    return bool(re.search(r"\bno new (eligible|candidate|candidates)\b|\bno new,\s|\ball (?:previously |already )(?:screened|killed)", body, re.I))


def color_for(kind: str) -> str:
    if kind == "bought":
        return "green"
    if kind in {"funding_avoid", "risk_other", "skipped_unverified", "pass_to_risk"}:
        return "yellow"
    return "red"  # scout_kill, factory_kill, filter_age_liq, unknown stop


def label_for(kind: str) -> str:
    return {
        "scout_kill": "stoppad av SCOUT",
        "factory_kill": "stoppad av fabrikskoll",
        "funding_avoid": "undvik (finansiering)",
        "risk_other": "undvik (RISK)",
        "skipped_unverified": "hoppad (obekräftad)",
        "bought": "köpt (paper)",
        "filter_age_liq": "stopp för ålder/likviditet",
        "pass_to_risk": "vidare till RISK",
        "unknown": "okänt",
    }.get(kind, "okänt")


def _position_pnl(d: dict) -> float | None:
    ex = d.get("exit") or {}
    raw = ex.get("realised_pnl_sol")
    if raw is None:
        raw = d.get("realised_pnl_sol")
    try:
        return float(raw)
    except (TypeError, ValueError):
        return None


def _exit_day(d: dict) -> str | None:
    ex = d.get("exit") or {}
    ts = ex.get("stockholm") or ex.get("utc") or d.get("entry_stockholm") or ""
    day = str(ts)[:10]
    return day if len(day) == 10 else None


def parse_stockholm(ts: str | None) -> datetime | None:
    if not ts:
        return None
    s = str(ts).strip().replace("Z", "+00:00")
    try:
        dt = datetime.fromisoformat(s)
    except Exception:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=TZ)
    return dt.astimezone(TZ)


def load_positions(pos_dir: Path) -> list[dict]:
    rows: list[dict] = []
    if not pos_dir.is_dir():
        return rows
    for p in sorted(pos_dir.glob("SOL-*.json")):
        d = _load_json(p)
        if isinstance(d, dict):
            rows.append(d)
    return rows


def load_strategy(root: Path, kind: str) -> dict[str, Any]:
    out: dict[str, Any] = {
        "equity": None, "pnl": None, "closed": None, "wins": None, "losses": None,
        "open": None, "win_rate_pct": None,
    }
    if kind == "A":
        led = _load_json(root / "positions" / "ledger.json") or {}
        positions = load_positions(root / "positions")
    elif kind == "B":
        led = _load_json(root / "shadow-b" / "ledger.json") or {}
        positions = []
        pdir = root / "shadow-b" / "positions"
        if pdir.is_dir():
            for p in pdir.glob("B-*.json"):
                d = _load_json(p)
                if isinstance(d, dict):
                    positions.append(d)
    else:
        led = _load_json(root / "shadow-c" / "ledger.json") or {}
        positions = []
        pdir = root / "shadow-c" / "positions"
        if pdir.is_dir():
            for p in pdir.glob("C-*.json"):
                d = _load_json(p)
                if isinstance(d, dict):
                    positions.append(d)
    if not isinstance(led, dict) or not led:
        return out
    try:
        eq0 = float(led.get("equity_start_sol") or 0)
        pnl = float(led.get("realised_pnl_sol") or 0)
        out["pnl"] = pnl
        out["equity"] = eq0 + pnl
    except Exception:
        pass
    try:
        out["closed"] = int(led.get("trades_closed") or 0)
    except Exception:
        pass
    try:
        w = int(led.get("wins") or 0)
        l = int(led.get("losses") or 0)
        out["wins"] = w
        out["losses"] = l
        if w + l > 0:
            out["win_rate_pct"] = 100.0 * w / (w + l)
    except Exception:
        pass
    out["open"] = sum(1 for d in positions if str(d.get("status", "")).upper() == "OPEN")
    return out


def compute_goals(ledger: dict, positions: list[dict]) -> dict[str, Any]:
    closed = [d for d in positions if str(d.get("status", "")).upper() == "CLOSED"]
    excluded = [d for d in closed if _truthy(d.get("excluded_from_goals"))]
    n_excl = len(excluded)
    excl_pnl = 0.0
    excl_wins = 0
    excl_losses = 0
    excl_by_day: dict[str, float] = {}
    excl_rows: list[dict[str, Any]] = []
    for d in excluded:
        rp = _position_pnl(d)
        ticket = str(d.get("ticket") or "–")
        reason = str(d.get("excluded_from_goals_reason") or "räknas inte i målen").strip()
        excl_rows.append({"ticket": ticket, "reason": reason, "pnl_sol": rp})
        if rp is None:
            continue
        excl_pnl += rp
        if rp > 0:
            excl_wins += 1
        else:
            excl_losses += 1
        day = _exit_day(d)
        if day:
            excl_by_day[day] = excl_by_day.get(day, 0.0) + rp

    eq0 = None
    try:
        if ledger.get("equity_start_sol") is not None:
            eq0 = float(ledger["equity_start_sol"])
    except Exception:
        eq0 = None
    pnl = None
    try:
        if ledger.get("realised_pnl_sol") is not None:
            pnl = float(ledger["realised_pnl_sol"]) - excl_pnl
    except Exception:
        pnl = None

    n_closed = ledger.get("trades_closed")
    try:
        n_closed = int(n_closed) if n_closed is not None else len(closed)
    except Exception:
        n_closed = len(closed)
    n_closed = max(0, n_closed - n_excl)

    wins_i = losses_i = None
    try:
        if ledger.get("wins") is not None:
            wins_i = max(0, int(ledger["wins"]) - excl_wins)
        if ledger.get("losses") is not None:
            losses_i = max(0, int(ledger["losses"]) - excl_losses)
    except Exception:
        wins_i = losses_i = None
    hit = None
    closed_wl = None
    if wins_i is not None and losses_i is not None:
        closed_wl = wins_i + losses_i
        if closed_wl > 0:
            hit = 100.0 * wins_i / closed_wl

    daily = ledger.get("daily") or {}
    worst_pct = None
    days_known = 0
    if isinstance(daily, dict) and eq0 and eq0 > 0:
        for day, info in daily.items():
            if not isinstance(info, dict):
                continue
            try:
                d_pnl = float(info.get("realised_pnl_sol") or 0) - excl_by_day.get(str(day), 0.0)
            except Exception:
                continue
            days_known += 1
            pct = d_pnl / eq0 * 100.0
            if worst_pct is None or pct < worst_pct:
                worst_pct = pct

    book_pnl = None
    try:
        if ledger.get("realised_pnl_sol") is not None:
            book_pnl = float(ledger["realised_pnl_sol"])
    except Exception:
        book_pnl = None
    book_equity = (eq0 + book_pnl) if (eq0 is not None and book_pnl is not None) else None

    return {
        "closed": n_closed,
        "closed_target": 20,
        "wins": wins_i,
        "losses": losses_i,
        "win_rate_pct": hit,
        "goal_pnl_sol": pnl,
        "worst_day_pct": worst_pct,
        "excluded": excl_rows,
        "book_closed": int(ledger.get("trades_closed") or len(closed)) if ledger else None,
        "book_wins": ledger.get("wins"),
        "book_losses": ledger.get("losses"),
        "book_pnl_sol": book_pnl,
        "book_equity_sol": book_equity,
        "equity_start_sol": eq0,
    }


def parse_lead_file(path: Path) -> dict[str, Any] | None:
    text = _safe_read(path)
    if not text:
        return None
    name = path.name
    cm = re.search(r"-c(\d+)\.md$", name)
    cycle = int(cm.group(1)) if cm else None
    # Dates in content: (c747, 2026-11-19) or similar
    day_m = re.search(r"\(c\d+,\s*(\d{4}-\d{2}-\d{2})\)", text)
    day = day_m.group(1) if day_m else None
    # symbol
    sym = None
    m = re.match(r"#\s*KILLED-SCOUT\s+([^\s(]+)", text)
    if m:
        sym = m.group(1)
    if not sym:
        m = re.search(r"#\s*(?:KILLED(?:\s*\([^)]*\))?|WANTED|AVOID)\s+([A-Za-z0-9$]{1,32})", text)
        if m:
            sym = m.group(1)
    if not sym:
        m = re.match(r"KILLED-(?:SCOUT|RISK)-([A-Za-z0-9$]+)", name)
        if m:
            sym = m.group(1)
        elif name.startswith("AVOID-"):
            sym = name.split("-")[1]
    kind, rules = _classify_outcome(text[:1500] + " " + name)
    if name.startswith("KILLED-SCOUT") and kind not in {"scout_kill", "factory_kill"}:
        kind = "scout_kill"
        rules = rules or _rules_from(text[:1500])
    if name.startswith("KILLED-RISK") and kind not in {"factory_kill", "funding_avoid", "risk_other"}:
        if re.search(r"launch factory|factory_check", text, re.I):
            kind = "factory_kill"
        elif re.search(r"funding|AVOID", text, re.I):
            kind = "funding_avoid" if re.search(r"funding", text, re.I) else "risk_other"
        else:
            kind = "risk_other"
    return {
        "symbol": _clean_name(sym) if sym else path.stem,
        "mint": _extract_mint(text[:400]),
        "kind": kind,
        "rules": rules,
        "cycle": cycle,
        "day": day,
        "path": name,
        "snippet": " ".join(text.splitlines()[:3])[:240],
        "source": "lead_file",
    }


def journal_days_present(journal_dir: Path, start: datetime, end: datetime) -> tuple[list[str], list[str]]:
    have: list[str] = []
    missing: list[str] = []
    d = start.date()
    end_d = end.date()
    while d <= end_d:
        ds = d.isoformat()
        if (journal_dir / f"{ds}.md").is_file():
            have.append(ds)
        else:
            missing.append(ds)
        d = d + timedelta(days=1)
    return have, missing


def aggregate_window(
    cycles: list[dict[str, Any]],
    start: datetime,
    end: datetime,
    lead_by_cycle: dict[int, list[dict[str, Any]]],
    positions: list[dict],
    journal_dir: Path,
) -> dict[str, Any]:
    unknowns: list[str] = []
    window_cycles = [c for c in cycles if c["time"] is not None and start <= c["time"] <= end]
    day_from = start.date().isoformat()
    day_to = end.date().isoformat()
    cycles_without_time = [
        c for c in cycles
        if c["time"] is None and day_from <= c["day"] <= day_to
    ]
    if cycles_without_time:
        unknowns.append(
            f"{len(cycles_without_time)} journalrunda(or) i fönstret saknar klockslag och räknas inte med"
        )

    have, missing = journal_days_present(journal_dir, start, end)
    if missing:
        unknowns.append(
            "Ingen journal för " + ", ".join(missing) + " — 7-dagars-/dygnssiffror är bara från dagar som finns."
        )

    events: list[dict[str, Any]] = []
    new_keys: set[str] = set()
    named_filters: set[str] = set()
    unnamed_filter = 0
    eligible_sum = 0
    eligible_known = 0
    eligible_unknown_cycles = 0

    for cyc in window_cycles:
        body = cyc["body"]
        elig = eligible_count(body)
        if elig is None:
            # "disc.py: only X" or "no new eligible" — not a measured eligible total
            if not re.search(r"disc\.py:\s*no new eligible", body, re.I):
                if re.search(r"disc\.py:", body, re.I):
                    eligible_unknown_cycles += 1
        else:
            eligible_sum += elig
            eligible_known += 1

        news = extract_new_tokens(body)
        already = set()
        for n in news:
            if n.get("symbol"):
                already.add(n["symbol"].lower())
                already.add(n["symbol"].lower() + "|" + ((n.get("mint") or "")[:8].lower()))
        extras = extract_extra_outcomes(body, already)
        # Avoid double-counting extras that are the same new token
        misses = extract_near_misses(body)

        # Merge lead files for this cycle if journal missed a token
        lead_items = lead_by_cycle.get(cyc["cycle"], [])

        def _add(ev: dict[str, Any], role: str) -> None:
            ev = dict(ev)
            ev["cycle"] = cyc["cycle"]
            ev["time"] = cyc["time"].strftime("%Y-%m-%d %H:%M") if cyc["time"] else None
            ev["day"] = cyc["day"]
            ev["color"] = color_for(ev.get("kind") or "unknown")
            ev["label"] = label_for(ev.get("kind") or "unknown")
            ev["role"] = role
            events.append(ev)

        seen_here = set()
        for ev in news + extras:
            sym = (ev.get("symbol") or "").lower()
            mint = (ev.get("mint") or "")[:8].lower()
            key = f"{sym}|{mint}" if mint else sym
            if not sym or key in seen_here:
                continue
            seen_here.add(key)
            new_keys.add(key)
            _add(ev, "new")

        for ev in misses:
            if ev.get("unnamed"):
                unnamed_filter += 1
                continue
            key = (ev.get("symbol") or "").lower()
            if not key or key in seen_here or key in named_filters:
                continue
            # If already counted as a new eligible this window, don't also mark as first-time filter
            if key in new_keys:
                continue
            named_filters.add(key)
            seen_here.add(key)
            _add(ev, "filter")

        journal_syms = seen_here
        for ev in lead_items:
            key = (ev.get("symbol") or "").lower()
            if key and key in journal_syms:
                # Fill missing rules/kind if journal was weaker
                continue
            if ev.get("day") and ev["day"] != cyc["day"]:
                continue
            if key:
                journal_syms.add(key)
                if ev.get("kind") == "filter_age_liq":
                    named_filters.add(key)
                else:
                    new_keys.add(key)
            _add(ev, "lead")

    # Positions bought in the window (in case journal wording was missed)
    for d in positions:
        entry = parse_stockholm(d.get("entry_stockholm") or d.get("entry_utc"))
        if entry is None or not (start <= entry <= end):
            continue
        ticket = str(d.get("ticket") or "")
        symbol = None
        # try notes / mint
        mint = str(d.get("mint") or "")[:12] or None
        notes = str(d.get("notes") or d.get("label") or "")
        already = any(
            e.get("kind") == "bought" and (
                (mint and e.get("mint") and str(e["mint"])[:8] == mint[:8])
                or (ticket and ticket in (e.get("snippet") or ""))
            )
            for e in events
        )
        if already:
            continue
        events.append({
            "symbol": ticket or "köp",
            "mint": mint,
            "kind": "bought",
            "rules": [],
            "snippet": f"paper-köp {ticket}",
            "source": "position",
            "cycle": None,
            "time": entry.strftime("%Y-%m-%d %H:%M"),
            "day": entry.strftime("%Y-%m-%d"),
            "color": "green",
            "label": label_for("bought"),
            "role": "position",
        })

    # Unique by symbol+kind (keep first)
    # Counts
    def _tok_key(e: dict[str, Any]) -> str:
        sym = (e.get("symbol") or "").lower()
        mint = (e.get("mint") or "")[:8].lower()
        if mint:
            return f"{sym}|{mint}"
        return sym

    unique_new = {}
    for e in events:
        if e.get("role") == "filter":
            continue
        if (e.get("kind") or "") == "filter_age_liq":
            continue
        key = _tok_key(e)
        if not key or key in {"|"}:
            continue
        if key not in unique_new:
            unique_new[key] = e

    counts = Counter()
    rule_counts = Counter()
    for key, e in unique_new.items():
        kind = e.get("kind") or "unknown"
        counts[kind] += 1
        if kind == "scout_kill":
            for r in e.get("rules") or []:
                rule_counts[r] += 1
            if not e.get("rules"):
                rule_counts["unknown"] += 1

    filter_count = len(named_filters)
    if unnamed_filter:
        unknowns.append(
            f"{unnamed_filter} runda(or) nämner ålder/likviditet-stopp utan tokennamn; "
            f"namngivna filterstopp är {filter_count}."
        )

    if eligible_unknown_cycles:
        unknowns.append(
            f"{eligible_unknown_cycles} rundor har disc.py-text utan ett tydligt antal godkända kandidater."
        )

    # Source split is not in the journal
    unknowns.append(
        "Uppdelning mellan DexScreener och GeckoTerminal går inte att läsa ut ur journalen."
    )

    scout_unknown_rules = int(rule_counts.get("unknown") or 0)
    if scout_unknown_rules:
        unknowns.append(
            f"{scout_unknown_rules} SCOUT-stopp saknar tydlig Regel 1/2/11 i texten."
        )

    # Token dots: unique new + unique named filters, most recent first, cap later in UI
    tokens_out: list[dict[str, Any]] = []
    seen_tok: set[str] = set()
    # newest first
    for e in sorted(events, key=lambda x: (x.get("time") or "", x.get("cycle") or 0), reverse=True):
        sym = e.get("symbol")
        if not sym:
            continue
        k = _tok_key(e)
        if k in seen_tok:
            continue
        seen_tok.add(k)
        tokens_out.append({
            "symbol": sym,
            "mint_prefix": e.get("mint"),
            "kind": e.get("kind"),
            "rules": e.get("rules") or [],
            "color": e.get("color"),
            "label": e.get("label"),
            "cycle": e.get("cycle"),
            "time": e.get("time"),
        })

    killed = {
        "scout_rule1": int(rule_counts.get("1") or 0),
        "scout_rule2": int(rule_counts.get("2") or 0),
        "scout_rule11": int(rule_counts.get("11") or 0),
        "scout_unique": int(counts.get("scout_kill") or 0),
        "scout_rules_unknown": scout_unknown_rules if scout_unknown_rules else 0,
        "age_or_liq_filter": filter_count,
        "age_or_liq_filter_complete": unnamed_filter == 0,
        "factory_kill": int(counts.get("factory_kill") or 0),
        "funding_avoid": int(counts.get("funding_avoid") or 0),
        "risk_other": int(counts.get("risk_other") or 0),
        "skipped_unverified": int(counts.get("skipped_unverified") or 0),
    }

    discovered = {
        "new_tokens": len(unique_new),
        "eligible_appearances": eligible_sum if eligible_known else None,
        "eligible_cycles_measured": eligible_known,
        "sources": {
            "dexscreener": None,
            "geckoterminal": None,
            "note": "disc.py använder båda källorna; journalen säger inte vilken token som kom från vilken.",
        },
    }

    return {
        "from": start.strftime("%Y-%m-%d %H:%M"),
        "to": end.strftime("%Y-%m-%d %H:%M"),
        "timezone": "Europe/Stockholm",
        "cycles": len(window_cycles),
        "journal_days_present": have,
        "journal_days_missing": missing,
        "discovered": discovered,
        "killed": killed,
        "passed_to_buy": int(counts.get("bought") or 0),
        "tokens": tokens_out,
        "unknowns": unknowns,
    }


def equity_series(cycles: list[dict[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for c in cycles:
        em = re.search(r"equity\s+([0-9.]+)\s*SOL", c["body"], re.I)
        if not em:
            continue
        try:
            eq = float(em.group(1))
        except Exception:
            continue
        rows.append({
            "t": c["time"].strftime("%Y-%m-%d %H:%M") if c["time"] else None,
            "cycle": c["cycle"],
            "equity": eq,
        })
    return rows


def build(src: Path) -> dict[str, Any]:
    now = _now()
    unknowns_global: list[str] = []
    journal_dir = src / "journal"
    cycles = iter_journal_cycles(journal_dir)
    if not cycles:
        unknowns_global.append("Ingen journal hittades.")

    lead_by_cycle: dict[int, list[dict[str, Any]]] = defaultdict(list)
    leads_dir = src / "leads"
    if leads_dir.is_dir():
        for p in list(leads_dir.glob("KILLED-*.md")) + list(leads_dir.glob("AVOID-*.md")):
            ev = parse_lead_file(p)
            if ev and ev.get("cycle"):
                lead_by_cycle[int(ev["cycle"])].append(ev)

    # screened.txt is a current exclusion list, not a 24h log — only record its size
    screened_info: dict[str, Any] = {"path": "research/screened.txt", "lines": None, "note": None}
    sp = src / "research" / "screened.txt"
    if sp.is_file():
        lines = [ln.strip() for ln in _safe_read(sp).splitlines() if ln.strip()]
        screened_info["lines"] = len(lines)
        screened_info["note"] = (
            "Det här är en aktuell lista över redan screenade mint-adresser, "
            "inte en logg för 24 timmar eller 7 dagar. Den används inte som antal upptäckta tokens."
        )
    else:
        screened_info["note"] = "research/screened.txt saknas i den här ögonblicksbilden."
        unknowns_global.append("research/screened.txt saknas; den behövs inte för 24h/7d-räkningen.")

    positions = load_positions(src / "positions")
    ledger = _load_json(src / "positions" / "ledger.json") or {}
    goals = compute_goals(ledger, positions)
    stats_a = load_strategy(src, "A")
    stats_b = load_strategy(src, "B")
    stats_c = load_strategy(src, "C")

    win_24h = aggregate_window(cycles, now - timedelta(hours=24), now, lead_by_cycle, positions, journal_dir)
    win_7d = aggregate_window(cycles, now - timedelta(days=7), now, lead_by_cycle, positions, journal_dir)

    series = equity_series(cycles)

    return {
        "generated_at_stockholm": now.strftime("%Y-%m-%d %H:%M"),
        "timezone": "Europe/Stockholm",
        "paper": True,
        "disclaimer": "PAPER – inte riktiga pengar. Inte finansiell rådgivning.",
        "windows": {"24h": win_24h, "7d": win_7d},
        "equity": {
            "start_sol": goals.get("equity_start_sol"),
            "realised_pnl_sol": goals.get("book_pnl_sol"),
            "equity_sol": goals.get("book_equity_sol"),
            "series": series,
        },
        "strategy": {"A": stats_a, "B": stats_b, "C": stats_c},
        "goals": goals,
        "screened_txt": screened_info,
        "unknowns": unknowns_global,
    }


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Build pipeline_stats.json (PAPER, no secrets).")
    p.add_argument("--src", default="/workspace/trading-desk", help="Desk root")
    p.add_argument("--out", required=True, help="Output JSON path")
    args = p.parse_args(argv)
    src = Path(args.src)
    if not src.is_dir():
        print(f"pipeline_stats: missing src {src}", file=sys.stderr)
        return 1
    data = build(src)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    # Never write secrets; compact but readable
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"pipeline_stats: wrote {out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
