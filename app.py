"""Lejon Terminal - READ-ONLY mobile-first PAPER dashboard for the PumpGrok desk.
No wallet, no keys, no orders. Reads only files under the desk directory.
Password via SPIDER_PASSWORD / LEJON_PASSWORD / st.secrets / .spider_password / .lejon_password."""
from __future__ import annotations

import glob
import hmac
import json
import os
import re
import datetime as dt
from collections import Counter
from pathlib import Path
from typing import Any

import streamlit as st

try:
    import plotly.graph_objects as go
except Exception:  # pragma: no cover
    go = None

FORBIDDEN = ("/workspace/PumpGrok/.env",)
APP_DIR = Path(__file__).resolve().parent


def resolve_desk() -> Path:
    env = os.environ.get("SPIDER_DESK_DIR")
    if env:
        return Path(env)
    in_place = Path("/workspace/trading-desk")
    if in_place.is_dir():
        return in_place
    local = APP_DIR / "desk-data"
    if local.is_dir():
        return local
    parent = APP_DIR.parent
    if (parent / "positions" / "ledger.json").exists() or (parent / "desk.md").exists():
        return parent
    return local


DESK = resolve_desk()

st.set_page_config(
    page_title="Lejon Terminal · PAPER",
    page_icon="🦁",
    layout="centered",
    initial_sidebar_state="collapsed",
)

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');
html, body, .stApp { background:#000 !important; color:#f2f4f8;
  font-family: Inter, system-ui, -apple-system, sans-serif !important; }
.block-container { max-width: 430px !important; padding: 0.6rem 0.75rem 2.5rem !important; }
header, #MainMenu, footer { visibility:hidden; height:0; }
.banner {
  background:#00e676; color:#000; font-weight:800; text-align:center;
  padding:8px 10px; border-radius:999px; font-size:0.72rem; letter-spacing:0.06em;
  text-transform:uppercase; margin:4px 0 12px;
}
.topbar { display:flex; align-items:flex-start; justify-content:space-between; gap:10px; margin-bottom:4px; }
.brand { display:flex; flex-direction:column; gap:2px; }
.brand .name { font-size:1.35rem; font-weight:800; color:#fff; letter-spacing:-0.02em; }
.brand .sub { font-size:0.72rem; color:#8b93a7; }
.pill {
  display:inline-flex; align-items:center; padding:4px 10px; border-radius:999px;
  font-size:0.68rem; font-weight:700; letter-spacing:0.04em;
}
.pill-paper { background:#12301f; color:#00e676; border:1px solid #1f6b45; }
.pill-live { background:#301212; color:#ff6b6b; border:1px solid #6b1f1f; } /* unused – PAPER only */
.pill-count { background:#161a22; color:#d7dbe7; border:1px solid #2a3140; font-family:JetBrains Mono, monospace; }
.pill-red { background:#2a1212; color:#ff6b6b; border:1px solid #5a2020; font-family:JetBrains Mono, monospace; }
.equity-wrap { margin:14px 0 6px; }
.equity-big { font-size:2.55rem; font-weight:800; color:#fff; letter-spacing:-0.03em; line-height:1; }
.equity-sub { margin-top:6px; display:flex; align-items:center; gap:8px; flex-wrap:wrap; }
.pnl-pos { color:#00e676; font-weight:700; font-size:0.95rem; }
.pnl-neg { color:#ff6b6b; font-weight:700; font-size:0.95rem; }
.card {
  background:#0c0f14; border:1px solid #1c2230; border-radius:22px;
  padding:14px 14px 10px; margin:12px 0;
}
.card h3 {
  margin:0; font-size:0.95rem; font-weight:700; color:#fff;
  display:flex; justify-content:space-between; align-items:center; gap:8px;
}
.card .meta { color:#8b93a7; font-size:0.72rem; font-weight:500; }
.agent-row {
  display:grid; grid-template-columns: 36px 1fr auto; gap:10px; align-items:center;
  padding:10px 0; border-bottom:1px solid #161b26;
}
.agent-row:last-child { border-bottom:none; }
.agent-icon {
  width:34px; height:34px; border-radius:11px; display:flex; align-items:center;
  justify-content:center; font-size:0.95rem; font-weight:800; color:#fff;
}
.ic-scout { background:#1b4fff; }
.ic-filter { background:#ff7a1a; }
.ic-analyst { background:#7b5cff; }
.ic-executor { background:#00c853; }
.ic-risk { background:#c44dff; }
.ic-logger { background:#00bcd4; }
.agent-name { font-size:0.88rem; font-weight:700; color:#fff; }
.agent-desc { font-size:0.68rem; color:#8b93a7; }
.agent-latest { font-size:0.68rem; color:#c5cad6; margin-top:2px;
  font-family:JetBrains Mono, monospace; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; max-width:190px; }
.log-line {
  font-family:JetBrains Mono, monospace; font-size:0.68rem; padding:5px 0;
  border-bottom:1px solid #141924; display:flex; gap:6px; flex-wrap:wrap;
}
.log-line:last-child { border-bottom:none; }
.log-time { color:#6b7385; min-width:2.6rem; }
.ag-SCOUT { color:#6b9bff; } .ag-FILTER { color:#ff9a4d; } .ag-ANALYST { color:#b39bff; }
.ag-EXECUTOR { color:#5dff9a; } .ag-RISK { color:#e09bff; } .ag-LOGGER { color:#6be7f0; }
.reason-row { display:grid; grid-template-columns: 1fr auto; gap:8px; align-items:center; padding:6px 0; }
.reason-label { font-size:0.78rem; color:#d7dbe7; }
.reason-bar-wrap { display:flex; align-items:center; gap:8px; }
.reason-bar { height:6px; border-radius:99px; background:#ff4d4d; min-width:4px; }
.reason-n { font-family:JetBrains Mono, monospace; font-size:0.72rem; color:#ff8e8e; min-width:2.2rem; text-align:right; }

.goal-row { display:grid; grid-template-columns: 1.4rem 1fr; gap:8px; align-items:start; padding:8px 0; border-bottom:1px solid #161b26; }
.goal-row:last-child { border-bottom:none; }
.goal-mark { font-size:0.9rem; line-height:1.2; }
.goal-title { font-size:0.82rem; font-weight:600; color:#e8ecf5; }
.goal-sub { font-size:0.68rem; color:#8b93a7; margin-top:2px; }
.goal-bar-bg { margin-top:6px; height:6px; border-radius:99px; background:#1a2030; overflow:hidden; }
.goal-bar-fg { height:100%; border-radius:99px; background:#00e676; }
.goal-bar-fg.bad { background:#ff6b6b; }
.goal-bar-fg.mid { background:#ffd166; }

.cmp-grid { display:grid; grid-template-columns:1fr 1fr; gap:8px; margin-top:8px; }
.cmp-col { background:#10141c; border:1px solid #1c2230; border-radius:14px; padding:10px; }
.cmp-col h4 { margin:0 0 6px; font-size:0.78rem; color:#fff; }
.cmp-kv { display:flex; justify-content:space-between; font-size:0.68rem; padding:2px 0; color:#c5cad6; }
.cmp-kv b { color:#e8ecf5; font-family:JetBrains Mono, ui-monospace, monospace; }

.goal-foot { margin-top:10px; font-size:0.68rem; color:#8b93a7; line-height:1.35; }

.login-box { background:#0c0f14; border:1px solid #1c2230; border-radius:22px; padding:18px; margin:18px 0; }
.foot { color:#5c6578; font-size:0.68rem; text-align:center; margin-top:14px; }
div[data-testid="stMetric"] { background:transparent; border:none; padding:0; }
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)


def safe_read(p: Path):
    try:
        if str(p.resolve()) in FORBIDDEN or p.name == ".env":
            return None
        return p.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return None


def redact(s: str) -> str:
    needle = "api" + "-key="
    return re.sub(rf"({re.escape(needle)})[^\s&\"']+", r"\1***", s or "")


def load_json(p: Path):
    t = safe_read(p)
    try:
        return json.loads(t) if t else None
    except Exception:
        return None


def expected_password() -> str | None:
    for key in ("SPIDER_PASSWORD", "LEJON_PASSWORD"):
        env_pw = os.environ.get(key)
        if env_pw is not None and env_pw != "":
            return env_pw
    try:
        secrets = st.secrets
        for key in ("SPIDER_PASSWORD", "LEJON_PASSWORD"):
            if key in secrets:
                val = str(secrets[key])
                if val:
                    return val
    except Exception:
        pass
    for fname in (".spider_password", ".lejon_password"):
        pw_file = APP_DIR / fname
        try:
            if pw_file.is_file():
                val = pw_file.read_text(encoding="utf-8").strip()
                if val:
                    return val
        except Exception:
            pass
    return None


def require_login() -> None:
    expected = expected_password()
    st.markdown(
        '<div class="banner">PAPER MODE – inga riktiga pengar · endast läsning</div>',
        unsafe_allow_html=True,
    )
    if not expected:
        st.markdown('<div class="brand"><div class="name">🦁 Lejon</div></div>', unsafe_allow_html=True)
        st.error("Inget lösenord är konfigurerat. Appen visar ingen data förrän du sätter ett.")
        st.markdown(
            """
**Sätt lösenord (välj ett):**
1. `SPIDER_PASSWORD` (alias `LEJON_PASSWORD`)
2. `.streamlit/secrets.toml`
3. `.spider_password` / `.lejon_password` bredvid `app.py`
"""
        )
        st.stop()
    if st.session_state.get("authenticated") is True:
        return
    st.markdown('<div class="brand"><div class="name">🦁 Lejon – inloggning</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    with st.form("lejon_login"):
        pwd = st.text_input("Lösenord", type="password", autocomplete="current-password")
        submitted = st.form_submit_button("Logga in")
    st.markdown("</div>", unsafe_allow_html=True)
    if submitted:
        ok = bool(pwd) and hmac.compare_digest(str(pwd), str(expected))
        if ok:
            st.session_state.authenticated = True
            st.rerun()
        st.error("Fel lösenord.")
        st.stop()
    st.caption("PAPER only. Ingen plånbok, inga nycklar, inga order.")
    st.stop()


def fmt_int(n: Any) -> str:
    if n is None:
        return "–"
    try:
        return f"{int(n):,}".replace(",", " ")
    except Exception:
        return "–"


def fmt_sol(n: Any, digits: int = 6) -> str:
    if n is None:
        return "–"
    try:
        return f"{float(n):.{digits}f}"
    except Exception:
        return "–"




def load_strategy_stats(desk: Path, kind: str) -> dict[str, Any]:
    """kind A = main desk positions/; B = shadow-b/."""
    out: dict[str, Any] = {
        "equity": None, "pnl": None, "closed": None, "win_rate": None, "open": None, "label": kind,
    }
    if kind == "A":
        led = load_json(desk / "positions" / "ledger.json") or {}
        pos_glob = str(desk / "positions" / "*.json")
    else:
        led = load_json(desk / "shadow-b" / "ledger.json") or {}
        # also allow desk-data/shadow-b for Cloud snapshot
        if not led:
            led = load_json(desk / "desk-data" / "shadow-b" / "ledger.json") or {}
        pos_glob = str(desk / "shadow-b" / "positions" / "B-*.json")
        if not glob.glob(pos_glob):
            pos_glob = str(desk / "desk-data" / "shadow-b" / "positions" / "B-*.json")
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
        w = int(led.get("wins") or 0); l = int(led.get("losses") or 0)
        if w + l > 0:
            out["win_rate"] = 100.0 * w / (w + l)
        elif out["closed"] == 0:
            out["win_rate"] = None
    except Exception:
        pass
    open_n = 0
    for p in glob.glob(pos_glob):
        if p.endswith("ledger.json"):
            continue
        d = load_json(Path(p))
        if isinstance(d, dict) and str(d.get("status", "")).upper() == "OPEN":
            open_n += 1
    out["open"] = open_n
    return out


def live_goals(ledger: dict, positions: list[dict]) -> list[dict[str, Any]]:
    """Compute read-only 'Mål innan live' from paper ledger/positions only."""
    eq0 = None
    try:
        if ledger.get("equity_start_sol") is not None:
            eq0 = float(ledger["equity_start_sol"])
    except Exception:
        eq0 = None
    pnl = None
    try:
        if ledger.get("realised_pnl_sol") is not None:
            pnl = float(ledger["realised_pnl_sol"])
    except Exception:
        pnl = None

    closed = [d for d in positions if str(d.get("status", "")).upper() == "CLOSED"]
    # Prefer ledger trades_closed when present
    n_closed = ledger.get("trades_closed")
    try:
        n_closed = int(n_closed) if n_closed is not None else len(closed)
    except Exception:
        n_closed = len(closed)

    wins = ledger.get("wins")
    losses = ledger.get("losses")
    try:
        wins_i = int(wins) if wins is not None else None
        losses_i = int(losses) if losses is not None else None
    except Exception:
        wins_i = losses_i = None
    closed_wl = None
    hit = None
    if wins_i is not None and losses_i is not None:
        closed_wl = wins_i + losses_i
        if closed_wl > 0:
            hit = 100.0 * wins_i / closed_wl

    # Daily loss vs start equity (2 % limit)
    daily = ledger.get("daily") or {}
    worst_pct = None
    days_known = 0
    if isinstance(daily, dict) and eq0 and eq0 > 0:
        for _day, info in daily.items():
            if not isinstance(info, dict):
                continue
            try:
                d_pnl = float(info.get("realised_pnl_sol") or 0)
            except Exception:
                continue
            days_known += 1
            pct = d_pnl / eq0 * 100.0
            if worst_pct is None or pct < worst_pct:
                worst_pct = pct
    # Also fold closed-position exit days if ledger.daily empty
    if days_known == 0 and eq0 and eq0 > 0:
        by_day: dict[str, float] = {}
        for d in closed:
            ex = d.get("exit") or {}
            ts = ex.get("stockholm") or ex.get("utc") or d.get("entry_stockholm") or ""
            day = str(ts)[:10]
            if len(day) < 10:
                continue
            try:
                rp = float(ex.get("realised_pnl_sol"))
            except Exception:
                continue
            by_day[day] = by_day.get(day, 0.0) + rp
        for _day, d_pnl in by_day.items():
            days_known += 1
            pct = d_pnl / eq0 * 100.0
            if worst_pct is None or pct < worst_pct:
                worst_pct = pct

    goals = []
    # 1 closed count
    g1_ok = n_closed >= 20
    g1_frac = min(1.0, (n_closed / 20.0) if n_closed is not None else 0.0)
    goals.append({
        "ok": g1_ok,
        "title": "Minst 20 stängda paper-köp",
        "sub": f"{n_closed}/20" if n_closed is not None else "–",
        "frac": g1_frac,
    })
    # 2 hit rate
    if hit is None:
        goals.append({"ok": False, "title": "Träffsäkerhet > 50 %", "sub": "–", "frac": 0.0, "unknown": True})
    else:
        goals.append({
            "ok": hit > 50.0,
            "title": "Träffsäkerhet > 50 %",
            "sub": f"{hit:.0f} % ({wins_i}/{closed_wl})",
            "frac": min(1.0, hit / 100.0),
        })
    # 3 total PnL plus
    if pnl is None:
        goals.append({"ok": False, "title": "Totalt resultat plus", "sub": "–", "frac": 0.0, "unknown": True})
    else:
        goals.append({
            "ok": pnl > 0,
            "title": "Totalt resultat plus",
            "sub": f"{pnl:+.6f} SOL",
            "frac": 1.0 if pnl > 0 else 0.0,
        })
    # 4 no day loss > 2%
    if worst_pct is None:
        goals.append({"ok": False, "title": "Ingen dag med förlust > 2 %", "sub": "–", "frac": 0.0, "unknown": True})
    else:
        ok4 = worst_pct > -2.0  # loss not worse than -2%
        goals.append({
            "ok": ok4,
            "title": "Ingen dag med förlust > 2 %",
            "sub": f"sämsta dag {worst_pct:+.2f} %",
            "frac": 1.0 if ok4 else max(0.0, 1.0 + worst_pct / 10.0),
        })
    # 5 audit static
    goals.append({
        "ok": False,
        "title": "Oberoende granskning gjord",
        "sub": "inte gjord",
        "frac": 0.0,
        "static": True,
    })
    return goals


def count_candidates(journals: list[str]) -> int | None:
    total = 0
    found = False
    for jf in journals:
        t = safe_read(Path(jf)) or ""
        for sec in re.split(r"^## ", t, flags=re.M)[1:]:
            m = re.search(r"(\d+)\s+distinct candidates", sec, re.I)
            if not m:
                m = re.search(r"[Dd]iscovery[^\n]*?\b(\d+)\s+candidates", sec)
            if m:
                total += int(m.group(1))
                found = True
            elif re.search(r"\b0 candidates\b|No candidate\b", sec):
                found = True
    return total if found else None


def equity_series(journals: list[str]) -> list[float]:
    ys: list[float] = []
    for jf in journals:
        t = safe_read(Path(jf)) or ""
        for sec in re.split(r"^## ", t, flags=re.M)[1:]:
            em = re.search(r"equity\s+([0-9.]+)\s*SOL", sec, re.I)
            if em:
                ys.append(float(em.group(1)))
    return ys


def parse_last_cycle(desk_md: str) -> dict[str, Any]:
    out: dict[str, Any] = {"cycle": None, "time": None, "ds_pairs": None, "candidates": None}
    m = re.search(r"^Last cycle:\s*(.*)$", desk_md or "", re.M)
    if not m:
        return out
    line = redact(m.group(1))
    head = re.match(r"(\d+)\s+at\s+([0-9\- :]+)", line)
    if head:
        out["cycle"] = int(head.group(1))
        out["time"] = head.group(2).strip()
    dm = re.search(r"DS\s+(\d+)\s+pairs", line)
    if dm:
        out["ds_pairs"] = int(dm.group(1))
    cm = re.search(r"discovery\s+(\d+)\s+candidates", line, re.I)
    if cm:
        out["candidates"] = int(cm.group(1))
    return out


def latest_journal_meta(journals: list[str]) -> dict[str, Any]:
    info: dict[str, Any] = {"cycle": None, "time": None, "title": None}
    if not journals:
        return info
    jf = journals[-1]
    t = safe_read(Path(jf)) or ""
    secs = re.split(r"^## ", t, flags=re.M)
    if len(secs) < 2:
        return info
    title = secs[-1].splitlines()[0]
    info["title"] = title
    cm = re.search(r"paper cycle\s+(\d+)", title, re.I)
    if cm:
        info["cycle"] = int(cm.group(1))
    tm = re.match(r"([0-9:.\-]+)", title)
    if tm:
        info["time"] = f"{Path(jf).stem} {tm.group(1)}"
    return info


def killed_token(path: Path) -> str:
    t = safe_read(path) or ""
    m = re.match(r"#\s*KILLED-SCOUT\s+([^\s(]+)", t)
    if m:
        return m.group(1)
    return path.stem.replace("KILLED-SCOUT-", "").replace("KILLED-", "")


def kill_reason_short(path: Path) -> str:
    t = "\n".join((safe_read(path) or "").splitlines()[:40])
    m = re.search(r"HARD KILL[^\n]{0,70}", t, re.I)
    if m:
        return redact(m.group(0).strip())[:56]
    m = re.search(r"rule[s]?\s+[0-9 +]+", t, re.I)
    if m:
        return redact(m.group(0).strip())[:56]
    return "SCOUT hard-kill"


def reason_counts(desk: Path, desk_md: str, journals: list[str]) -> list[tuple[str, int]]:
    c: Counter[str] = Counter()
    for f in desk.glob("leads/KILLED-*.md"):
        t = "\n".join((safe_read(f) or "").splitlines()[:45])
        ns: set[str] = set()
        for m in re.finditer(r"HARD KILL[^\n]{0,90}", t, re.I):
            ns |= set(re.findall(r"\d+", m.group(0)))
        for m in re.finditer(r"\brule\s+(\d+)\b", t, re.I):
            ns.add(m.group(1))
        if re.search(r"Rule\s*11", t):
            ns.add("11")
        if "1" in ns:
            c["Rule 1"] += 1
        if "2" in ns:
            c["Rule 2"] += 1
        if "11" in ns:
            c["Rule 11"] += 1
    # unique RISK kills from desk + journals
    seen: set[str] = set()
    blobs = [desk_md] + [(safe_read(Path(j)) or "") for j in journals]
    for src in blobs:
        for m in re.finditer(
            r"(LEAD\s+SOL-\d{8}-\d+|SOL-\d{8}-\d+|[A-Za-z0-9$]{2,16}\s+[A-Za-z0-9]{3,6}).{0,40}RISK KILL([^\n]{0,100})",
            src,
            re.I,
        ):
            key = m.group(0)[:80]
            if key in seen:
                continue
            seen.add(key)
            s = m.group(0).lower()
            if "launch factory" in s or "launch-factory" in s:
                c["launch factory"] += 1
            elif "hidden" in s or "pass-through" in s or "durable-nonce" in s or "nonce" in s:
                c["hidden funding"] += 1
            elif "liquidity" in s or "25k" in s or "25,000" in s:
                c["liquidity <25k"] += 1
            elif "top-10" in s or "top 10" in s:
                c["top-10 holders"] += 1
            else:
                c["RISK övrigt"] += 1
    order = [
        "Rule 1",
        "Rule 2",
        "Rule 11",
        "launch factory",
        "hidden funding",
        "liquidity <25k",
        "top-10 holders",
        "RISK övrigt",
    ]
    out = [(k, c[k]) for k in order if c.get(k)]
    for k, v in c.most_common():
        if k not in dict(out):
            out.append((k, v))
    return out


def build_logger_events(
    kfiles: list[Path],
    lead_files: list[Path],
    risk_ids: set[str],
    positions: list[dict],
) -> list[dict[str, str]]:
    events: list[dict[str, str]] = []
    for f in kfiles[:12]:
        ts = dt.datetime.fromtimestamp(os.path.getmtime(f))
        events.append(
            {
                "sort": ts.timestamp(),
                "time": ts.strftime("%H:%M"),
                "agent": "FILTER",
                "text": f"dödade ${killed_token(f)} · {kill_reason_short(f)}",
            }
        )
    for f in lead_files[:8]:
        ts = dt.datetime.fromtimestamp(os.path.getmtime(f))
        body = safe_read(f) or ""
        lid_m = re.search(r"LEAD-ID:\s*(SOL-\d{8}-\d+)", body)
        mint_m = re.search(r"Mint:\s*\S+\s*\(([^)]+)\)", body)
        lid = lid_m.group(1) if lid_m else f.stem
        tok = mint_m.group(1) if mint_m else lid
        if lid in risk_ids:
            events.append(
                {
                    "sort": ts.timestamp(),
                    "time": ts.strftime("%H:%M"),
                    "agent": "RISK",
                    "text": f"dödade {tok} · RISK KILL · {lid}",
                }
            )
        else:
            events.append(
                {
                    "sort": ts.timestamp(),
                    "time": ts.strftime("%H:%M"),
                    "agent": "ANALYST",
                    "text": f"LEAD {tok} · {lid}",
                }
            )
    for d in positions:
        ex = d.get("exit") or {}
        entry = d.get("entry_stockholm") or d.get("entry_utc") or ""
        sort_v = 0.0
        try:
            sort_v = dt.datetime.fromisoformat(str(d.get("entry_utc", "")).replace("Z", "+00:00")).timestamp()
        except Exception:
            pass
        mint = (d.get("mint") or "")[:10]
        ticket = d.get("ticket") or "–"
        if str(d.get("status", "")).upper() == "CLOSED":
            events.append(
                {
                    "sort": sort_v,
                    "time": str(entry)[11:16] if len(str(entry)) >= 16 else "–",
                    "agent": "RISK",
                    "text": f"exit {ticket} · {redact(str(ex.get('reason') or 'stängd'))[:48]}",
                }
            )
            events.append(
                {
                    "sort": sort_v - 1,
                    "time": str(entry)[11:16] if len(str(entry)) >= 16 else "–",
                    "agent": "EXECUTOR",
                    "text": f"paper-köp {ticket} · {d.get('size_sol', '–')} SOL · ${mint}",
                }
            )
        else:
            events.append(
                {
                    "sort": sort_v,
                    "time": str(entry)[11:16] if len(str(entry)) >= 16 else "–",
                    "agent": "EXECUTOR",
                    "text": f"öppen {ticket} · {d.get('size_sol', '–')} SOL",
                }
            )
    # scout hint from newest kill mtime cluster
    if kfiles:
        ts = dt.datetime.fromtimestamp(os.path.getmtime(kfiles[0]))
        events.append(
            {
                "sort": ts.timestamp() + 0.5,
                "time": ts.strftime("%H:%M"),
                "agent": "SCOUT",
                "text": f"senaste kandidat ${killed_token(kfiles[0])}",
            }
        )
    events.sort(key=lambda e: e["sort"], reverse=True)
    return events[:6]


# ----- auth -----
require_login()

# ----- load -----
ledger = load_json(DESK / "positions" / "ledger.json") or {}
eq0 = float(ledger["equity_start_sol"]) if ledger.get("equity_start_sol") is not None else None
pnl = float(ledger["realised_pnl_sol"]) if ledger.get("realised_pnl_sol") is not None else None
equity = (eq0 + pnl) if (eq0 is not None and pnl is not None) else None
pnl_pct = (pnl / eq0 * 100.0) if (eq0 and pnl is not None) else None

desk_md = safe_read(DESK / "desk.md") or ""
journals = sorted(glob.glob(str(DESK / "journal" / "*.md")))
last = parse_last_cycle(desk_md)
jmeta = latest_journal_meta(journals)
cycle = jmeta.get("cycle") or last.get("cycle")

kfiles = sorted(Path(DESK / "leads").glob("KILLED-*.md"), key=os.path.getmtime, reverse=True)
lead_files = sorted(Path(DESK / "leads").glob("SOL-*.md"), key=os.path.getmtime, reverse=True)
killed_n = len(kfiles)
lead_n = len(lead_files)
scanned = count_candidates(journals)

positions: list[dict] = []
for p in sorted(glob.glob(str(DESK / "positions" / "*.json"))):
    if p.endswith("ledger.json"):
        continue
    d = load_json(Path(p))
    if isinstance(d, dict):
        positions.append(d)
traded_n = len(positions)
open_n = sum(1 for d in positions if str(d.get("status", "")).upper() == "OPEN")

risk_ids: set[str] = set()
for src in [desk_md] + [(safe_read(Path(j)) or "") for j in journals]:
    risk_ids |= set(re.findall(r"LEAD\s+(SOL-\d{8}-\d+)\s*->\s*RISK KILL", src or ""))
    risk_ids |= set(re.findall(r"(SOL-\d{8}-\d+)\s*\([^)]*\):\s*RISK KILL", src or ""))

reasons = reason_counts(DESK, desk_md, journals)
reason_total = sum(v for _, v in reasons) if reasons else None
eq_ys = equity_series(journals)
logger_events = build_logger_events(kfiles, lead_files, risk_ids, positions)

# Agent row latest snippets
scout_latest = f"${killed_token(kfiles[0])}" if kfiles else "–"
scout_pill = f"{fmt_int(last.get('ds_pairs'))} par" if last.get("ds_pairs") is not None else "–"
filter_pct = None
if killed_n and (killed_n + lead_n):
    filter_pct = 100.0 * killed_n / (killed_n + lead_n)
filter_latest = f"${killed_token(kfiles[0])} · {kill_reason_short(kfiles[0])}" if kfiles else "–"
filter_pill = (
    f"{fmt_int(killed_n)} · {filter_pct:.0f}%" if filter_pct is not None else fmt_int(killed_n)
)
if lead_files:
    body = safe_read(lead_files[0]) or ""
    mint_m = re.search(r"Mint:\s*\S+\s*\(([^)]+)\)", body)
    lid_m = re.search(r"LEAD-ID:\s*(SOL-\d{8}-\d+)", body)
    lid = lid_m.group(1) if lid_m else lead_files[0].stem
    tok = mint_m.group(1) if mint_m else lid
    if lid in risk_ids:
        analyst_latest = f"${tok} · RISK KILL"
    else:
        analyst_latest = f"${tok} · LEAD"
else:
    analyst_latest = "–"
analyst_pill = f"{fmt_int(lead_n)} granskade"

if positions:
    d0 = positions[0]
    executor_latest = f"{d0.get('ticket')} · {d0.get('size_sol', '–')} SOL · {d0.get('status')}"
else:
    executor_latest = "–"
executor_pill = "max 0.2 SOL"

risk_latest = "–"
if positions:
    ex = positions[0].get("exit") or {}
    if ex.get("reason"):
        risk_latest = redact(str(ex.get("reason")))[:48]
    else:
        risk_latest = "stop −30 % · BE efter TP1"
elif risk_ids:
    risk_latest = f"{next(iter(sorted(risk_ids, reverse=True)))} · RISK KILL"
risk_pill = "−30% · BE"

logger_latest = logger_events[0]["text"] if logger_events else "–"
logger_pill = fmt_int(reason_total) if reason_total else "–"

pnl_cls = "pnl-neg" if (pnl is not None and pnl < 0) else "pnl-pos"
pnl_txt = f"{pnl:+.6f} SOL" if pnl is not None else "–"
pct_txt = f"({pnl_pct:+.2f} %)" if pnl_pct is not None else ""

# ----- header -----
st.markdown(
    f"""
<div class="topbar">
  <div class="brand">
    <div class="name">🦁 Lejon</div>
    <div class="sub">Solana memes · strikt RM · PAPER</div>
  </div>
  <span class="pill pill-paper">PAPER</span>
</div>
""",
    unsafe_allow_html=True,
)

c1, c2 = st.columns(2)
with c1:
    if st.button("🔄 Uppdatera", use_container_width=True):
        st.rerun()
with c2:
    if st.button("Logga ut", use_container_width=True):
        st.session_state.authenticated = False
        st.rerun()

# ----- equity -----
st.markdown(
    f"""
<div class="equity-wrap">
  <div class="equity-big">{fmt_sol(equity)} <span style="font-size:1rem;color:#8b93a7">SOL</span></div>
  <div class="equity-sub"><span class="{pnl_cls}">{pnl_txt} {pct_txt}</span>
  <span class="pill pill-count">start {fmt_sol(eq0)}</span></div>
</div>
""",
    unsafe_allow_html=True,
)

if go and eq_ys:
    fig = go.Figure(
        go.Scatter(
            y=eq_ys,
            mode="lines",
            line=dict(color="#00e676" if (pnl is None or pnl >= 0) else "#ff6b6b", width=2),
            hoverinfo="skip",
        )
    )
    fig.update_layout(
        paper_bgcolor="#000",
        plot_bgcolor="#000",
        margin=dict(l=0, r=0, t=4, b=0),
        height=64,
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
        showlegend=False,
    )
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})
elif eq_ys:
    st.line_chart(eq_ys, height=64)
else:
    st.caption("Equity-kurva: –")


# ----- mål innan live -----
goals = live_goals(ledger, positions)
goal_rows = []
for g in goals:
    mark = "✅" if g.get("ok") else ("–" if g.get("unknown") else "❌")
    if g.get("unknown"):
        mark = "❌"
    frac = float(g.get("frac") or 0.0)
    width = int(max(0, min(100, round(frac * 100))))
    bar_cls = "goal-bar-fg" if g.get("ok") else ("goal-bar-fg mid" if width > 0 else "goal-bar-fg bad")
    goal_rows.append(
        f'<div class="goal-row"><div class="goal-mark">{mark}</div><div>'
        f'<div class="goal-title">{g["title"]}</div>'
        f'<div class="goal-sub">{g["sub"]}</div>'
        f'<div class="goal-bar-bg"><div class="{bar_cls}" style="width:{width}%"></div></div>'
        f'</div></div>'
    )
st.markdown(
    f"""
<div class="card">
  <h3>Mål innan live <span class="meta">paper-bevis</span></h3>
  {''.join(goal_rows)}
  <div class="goal-foot">Live slås på först när alla är ✅ och Hevar godkänner. Endast paper.</div>
</div>
""",
    unsafe_allow_html=True,
)


# ----- A vs B comparison -----
stats_a = load_strategy_stats(DESK, "A")
stats_b = load_strategy_stats(DESK, "B")

def _cmp_val(v, kind="num"):
    if v is None:
        return "–"
    if kind == "sol":
        return f"{float(v):.6f}"
    if kind == "pnl":
        return f"{float(v):+.6f}"
    if kind == "pct":
        return f"{float(v):.0f} %"
    return str(v)

st.markdown(
    f"""
<div class="card">
  <h3>Jämförelse A vs B <span class="meta">paper</span></h3>
  <div class="cmp-grid">
    <div class="cmp-col">
      <h4>A · desk</h4>
      <div class="cmp-kv"><span>Equity</span><b>{_cmp_val(stats_a.get('equity'),'sol')} SOL</b></div>
      <div class="cmp-kv"><span>P/L</span><b>{_cmp_val(stats_a.get('pnl'),'pnl')} SOL</b></div>
      <div class="cmp-kv"><span>Stängda</span><b>{_cmp_val(stats_a.get('closed'))}</b></div>
      <div class="cmp-kv"><span>Träffsäkerhet</span><b>{_cmp_val(stats_a.get('win_rate'),'pct')}</b></div>
      <div class="cmp-kv"><span>Öppna</span><b>{_cmp_val(stats_a.get('open'))}</b></div>
    </div>
    <div class="cmp-col">
      <h4>B · shadow</h4>
      <div class="cmp-kv"><span>Equity</span><b>{_cmp_val(stats_b.get('equity'),'sol')} SOL</b></div>
      <div class="cmp-kv"><span>P/L</span><b>{_cmp_val(stats_b.get('pnl'),'pnl')} SOL</b></div>
      <div class="cmp-kv"><span>Stängda</span><b>{_cmp_val(stats_b.get('closed'))}</b></div>
      <div class="cmp-kv"><span>Träffsäkerhet</span><b>{_cmp_val(stats_b.get('win_rate'),'pct')}</b></div>
      <div class="cmp-kv"><span>Öppna</span><b>{_cmp_val(stats_b.get('open'))}</b></div>
    </div>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# ----- desk agents -----
scan_trade = f"{fmt_int(scanned)} skannade · {fmt_int(traded_n)} handlade"
st.markdown(
    f"""
<div class="card">
  <h3>Desk · 6 agenter <span class="meta">{scan_trade}</span></h3>
  <div class="agent-row">
    <div class="agent-icon ic-scout">S</div>
    <div>
      <div class="agent-name">Scout</div>
      <div class="agent-desc">nya par</div>
      <div class="agent-latest">{scout_latest}</div>
    </div>
    <span class="pill pill-count">{scout_pill}</span>
  </div>
  <div class="agent-row">
    <div class="agent-icon ic-filter">F</div>
    <div>
      <div class="agent-name">Filter</div>
      <div class="agent-desc">kills {f'{filter_pct:.0f} %' if filter_pct is not None else '–'}</div>
      <div class="agent-latest">{filter_latest}</div>
    </div>
    <span class="pill pill-count">{filter_pill}</span>
  </div>
  <div class="agent-row">
    <div class="agent-icon ic-analyst">A</div>
    <div>
      <div class="agent-name">Analyst</div>
      <div class="agent-desc">LEAD / RISK-granskade</div>
      <div class="agent-latest">{analyst_latest}</div>
    </div>
    <span class="pill pill-count">{analyst_pill}</span>
  </div>
  <div class="agent-row">
    <div class="agent-icon ic-executor">E</div>
    <div>
      <div class="agent-name">Executor</div>
      <div class="agent-desc">paper-köp, max 0.2 SOL</div>
      <div class="agent-latest">{executor_latest}</div>
    </div>
    <span class="pill pill-count">{executor_pill}</span>
  </div>
  <div class="agent-row">
    <div class="agent-icon ic-risk">R</div>
    <div>
      <div class="agent-name">Risk</div>
      <div class="agent-desc">stop −30 % · break-even efter TP1</div>
      <div class="agent-latest">{risk_latest}</div>
    </div>
    <span class="pill pill-count">{risk_pill}</span>
  </div>
  <div class="agent-row">
    <div class="agent-icon ic-logger">L</div>
    <div>
      <div class="agent-name">Logger</div>
      <div class="agent-desc">antal orsaker</div>
      <div class="agent-latest">{logger_latest}</div>
    </div>
    <span class="pill pill-count">{logger_pill}</span>
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# ----- logger feed -----
log_html = []
for ev in logger_events:
    ag = ev["agent"]
    log_html.append(
        f'<div class="log-line"><span class="log-time">{ev["time"]}</span>'
        f'<span class="ag-{ag}">{ag}</span>'
        f'<span>{ev["text"]}</span></div>'
    )
if not log_html:
    log_html.append('<div class="log-line">Inga händelser.</div>')

st.markdown(
    f"""
<div class="card">
  <h3>Logger <span class="pill pill-red">{fmt_int(killed_n)} dödade</span></h3>
  {''.join(log_html)}
</div>
""",
    unsafe_allow_html=True,
)

# ----- why they died -----
max_r = max((v for _, v in reasons), default=1) or 1
reason_html = []
for label, n in reasons:
    width = max(8, int(120 * n / max_r))
    reason_html.append(
        f'<div class="reason-row"><div class="reason-label">{label}</div>'
        f'<div class="reason-bar-wrap"><div class="reason-bar" style="width:{width}px"></div>'
        f'<div class="reason-n">{fmt_int(n)}</div></div></div>'
    )
best_worst = "–"
if positions:
    pnls = []
    for d in positions:
        ex = d.get("exit") or {}
        if ex.get("realised_pnl_sol") is not None:
            pnls.append(float(ex["realised_pnl_sol"]))
        elif d.get("realised_pnl_sol") is not None:
            pnls.append(float(d["realised_pnl_sol"]))
    if pnls:
        best_worst = f"bäst {max(pnls):+.4f} · sämst {min(pnls):+.4f}"

st.markdown(
    f"""
<div class="card">
  <h3>Varför de dog <span class="meta">{best_worst}</span></h3>
  {''.join(reason_html) if reason_html else '<div class="meta">–</div>'}
</div>
""",
    unsafe_allow_html=True,
)

st.markdown(
    f'<div class="foot">🦁 Lejon Terminal · PAPER · cykel {fmt_int(cycle)} · '
    f'öppna {open_n}/3 · endast läsning · inga nycklar<br>'
    f'Desk {DESK} · uppdaterad {dt.datetime.now():%Y-%m-%d %H:%M} Europe/Stockholm</div>',
    unsafe_allow_html=True,
)
