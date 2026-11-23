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
import math
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
.cmp-grid-3 { grid-template-columns:1fr 1fr 1fr; gap:6px; }
.cmp-col { background:#10141c; border:1px solid #1c2230; border-radius:14px; padding:10px; }
.cmp-col h4 { margin:0 0 6px; font-size:0.78rem; color:#fff; }
.cmp-kv { display:flex; justify-content:space-between; font-size:0.68rem; padding:2px 0; color:#c5cad6; }
.cmp-kv b { color:#e8ecf5; font-family:JetBrains Mono, ui-monospace, monospace; }
.d-paper { display:inline-block; font-size:0.62rem; color:#ffd166; border:1px solid #5a4a1a; border-radius:8px; padding:1px 6px; margin-left:6px; }
.d-cat-row { display:grid; grid-template-columns: 1fr 2.2rem 2.6rem 4.4rem; gap:6px; font-size:0.68rem; color:#c5cad6; padding:5px 0; border-bottom:1px solid #161b26; }
.d-cat-row b { font-family:JetBrains Mono, ui-monospace, monospace; color:#e8ecf5; text-align:right; }
.d-cat-head { color:#8b93a7; font-size:0.62rem; }
.d-pos { font-size:0.68rem; color:#c5cad6; padding:4px 0; border-bottom:1px solid #161b26; }
.whale-row { display:grid; grid-template-columns: 4.6rem 2.4rem 1fr; gap:8px; align-items:start; padding:7px 0; border-bottom:1px solid #161b26; }
.whale-row:last-child { border-bottom:none; }
.whale-addr { font-family:JetBrains Mono, ui-monospace, monospace; font-size:0.72rem; color:#e8ecf5; font-weight:700; }
.whale-score { font-family:JetBrains Mono, ui-monospace, monospace; font-size:0.72rem; color:#00e676; text-align:right; }
.whale-reason { font-size:0.68rem; color:#8b93a7; line-height:1.3; }

.goal-foot { margin-top:10px; font-size:0.68rem; color:#8b93a7; line-height:1.35; }
.goal-foot-excl { margin-top:6px; color:#ffd166; }


.wl-line { margin: 4px 0 10px; color:#c5cad6; font-size:0.78rem; }
.wl-line b { color:#fff; font-family:JetBrains Mono, ui-monospace, monospace; }
.circle-note { color:#8b93a7; font-size:0.68rem; line-height:1.4; margin-top:8px; }
.circle-unk { color:#ffd166; font-size:0.68rem; line-height:1.4; margin-top:6px; }

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




def _shadow_dir(desk: Path, name: str) -> Path:
    p = desk / name
    if (p / "ledger.json").is_file():
        return p
    p2 = desk / "desk-data" / name
    if (p2 / "ledger.json").is_file():
        return p2
    return p


def load_strategy_stats(desk: Path, kind: str) -> dict[str, Any]:
    """kind A = main desk positions/; B = shadow-b/; C = shadow-c/; D = shadow-d/ (lösare A, PAPER)."""
    out: dict[str, Any] = {
        "equity": None, "pnl": None, "closed": None, "win_rate": None, "open": None, "label": kind,
    }
    if kind == "A":
        led = load_json(desk / "positions" / "ledger.json") or {}
        pos_glob = str(desk / "positions" / "*.json")
    elif kind == "C":
        root = _shadow_dir(desk, "shadow-c")
        led = load_json(root / "ledger.json") or {}
        pos_glob = str(root / "positions" / "C-*.json")
    elif kind == "D":
        root = _shadow_dir(desk, "shadow-d")
        led = load_json(root / "ledger.json") or {}
        pos_glob = str(root / "positions" / "D-*.json")
    else:
        root = _shadow_dir(desk, "shadow-b")
        led = load_json(root / "ledger.json") or {}
        pos_glob = str(root / "positions" / "B-*.json")
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


def _truthy_flag(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return value != 0
    if isinstance(value, str):
        return value.strip().lower() in {"true", "yes", "1"}
    return False


def excluded_from_goals(d: dict) -> bool:
    """True when a position stays in the ledger/equity but is omitted from 'Mål innan live'."""
    if not isinstance(d, dict):
        return False
    return _truthy_flag(d.get("excluded_from_goals"))


def _position_realised_pnl(d: dict) -> float | None:
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


def goals_exclusion_footnote(positions: list[dict]) -> str:
    rows: list[str] = []
    for d in positions:
        if str(d.get("status", "")).upper() != "CLOSED":
            continue
        if not excluded_from_goals(d):
            continue
        ticket = str(d.get("ticket") or "–")
        reason = str(d.get("excluded_from_goals_reason") or "excluded from goals").strip()
        rows.append(f"{ticket} — {reason}")
    if not rows:
        return ""
    n = len(rows)
    head = "1 stängt paper-köp räknas inte i målen" if n == 1 else f"{n} stängda paper-köp räknas inte i målen"
    return head + " (syns i boken och i equity): " + "; ".join(rows) + "."


def live_goals(ledger: dict, positions: list[dict]) -> list[dict[str, Any]]:
    """Compute read-only 'Mål innan live' from paper ledger/positions only.

    Positions with excluded_from_goals=true stay in the ledger and in paper
    equity, but are omitted from closed-count, win rate, goal P/L and the
    daily-loss goal.
    """
    closed = [d for d in positions if str(d.get("status", "")).upper() == "CLOSED"]
    excluded = [d for d in closed if excluded_from_goals(d)]
    n_excl = len(excluded)
    excl_pnl = 0.0
    excl_wins = 0
    excl_losses = 0
    excl_by_day: dict[str, float] = {}
    for d in excluded:
        rp = _position_realised_pnl(d)
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

    # Prefer ledger trades_closed when present, then subtract exclusions
    n_closed = ledger.get("trades_closed")
    try:
        n_closed = int(n_closed) if n_closed is not None else len(closed)
    except Exception:
        n_closed = len(closed)
    n_closed = max(0, n_closed - n_excl)

    wins = ledger.get("wins")
    losses = ledger.get("losses")
    try:
        wins_i = int(wins) if wins is not None else None
        losses_i = int(losses) if losses is not None else None
    except Exception:
        wins_i = losses_i = None
    if wins_i is not None:
        wins_i = max(0, wins_i - excl_wins)
    if losses_i is not None:
        losses_i = max(0, losses_i - excl_losses)
    closed_wl = None
    hit = None
    if wins_i is not None and losses_i is not None:
        closed_wl = wins_i + losses_i
        if closed_wl > 0:
            hit = 100.0 * wins_i / closed_wl

    # Daily loss vs start equity (2 % limit), excluding goal-excluded trades
    daily = ledger.get("daily") or {}
    worst_pct = None
    days_known = 0
    if isinstance(daily, dict) and eq0 and eq0 > 0:
        for _day, info in daily.items():
            if not isinstance(info, dict):
                continue
            try:
                d_pnl = float(info.get("realised_pnl_sol") or 0) - excl_by_day.get(str(_day), 0.0)
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
            if excluded_from_goals(d):
                continue
            day = _exit_day(d)
            if not day:
                continue
            rp = _position_realised_pnl(d)
            if rp is None:
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



def fmt_known(n: Any, digits: int | None = None) -> str:
    if n is None:
        return "okänt"
    if digits is not None:
        try:
            return f"{float(n):.{digits}f}"
        except Exception:
            return "okänt"
    return fmt_int(n)


def _pipeline_paths() -> list[Path]:
    return [
        DESK / "pipeline_stats.json",
        DESK / "desk-data" / "pipeline_stats.json",
        APP_DIR / "desk-data" / "pipeline_stats.json",
        Path("/workspace/trading-desk/var/pipeline_stats.json"),
    ]


def load_pipeline_stats() -> dict[str, Any] | None:
    for p in _pipeline_paths():
        d = load_json(p)
        if isinstance(d, dict) and d.get("windows"):
            return d
    # Fallback: rebuild from the full desk when the helper is present
    try:
        import importlib.util
        helper = Path("/workspace/trading-desk/pipeline_stats.py")
        if helper.is_file() and (DESK / "journal").is_dir():
            spec = importlib.util.spec_from_file_location("pipeline_stats_desk", helper)
            if spec and spec.loader:
                mod = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(mod)
                return mod.build(DESK if (DESK / "journal").is_dir() else Path("/workspace/trading-desk"))
    except Exception:
        return None
    return None


def _sv_unknowns(items: list[str] | None) -> list[str]:
    """Short, simple Swedish notes. Never invent a number here."""
    out: list[str] = []
    for raw in items or []:
        s = str(raw)
        sl = s.lower()
        if "dexscreener" in sl or "geckoterminal" in sl:
            out.append("Uppdelning mellan DexScreener och GeckoTerminal: okänt.")
        elif "ingen journal" in sl:
            # Keep the date(s)
            out.append(s.replace(" — 7-dagars-/dygnssiffror är bara från dagar som finns.", ".").replace(" 7-dagars-/dygnssiffror är bara från dagar som finns.", "."))
        elif "utan tokennamn" in sl or "saknar tokennamn" in sl:
            out.append("Några stopp för ålder eller likviditet saknar namn, så den siffran kan vara högre.")
        elif "utan ett tydligt antal" in sl:
            out.append("Några rundor saknar ett tydligt antal godkända tokens.")
        elif "saknar tydlig regel" in sl or "saknar tydlig Regel" in s:
            out.append("Några SCOUT-stopp saknar tydlig regel i texten.")
        elif "saknar klockslag" in sl:
            out.append("Några journalrader saknar klockslag och räknas inte med.")
        else:
            out.append(s)
    # unique preserve order
    seen: set[str] = set()
    uniq: list[str] = []
    for s in out:
        if s not in seen:
            seen.add(s)
            uniq.append(s)
    return uniq


def agent_circle_figure(window: dict[str, Any], strategy: dict[str, Any]) -> "go.Figure | None":
    if go is None or not isinstance(window, dict):
        return None
    killed = window.get("killed") or {}
    discovered = window.get("discovered") or {}
    tokens = window.get("tokens") or []
    if not isinstance(tokens, list):
        tokens = []

    def _n(val: Any) -> int | None:
        if val is None:
            return None
        try:
            return int(val)
        except Exception:
            return None

    new_n = _n((discovered or {}).get("new_tokens"))
    filter_n = _n(killed.get("age_or_liq_filter"))
    r1 = _n(killed.get("scout_rule1"))
    r2 = _n(killed.get("scout_rule2"))
    r11 = _n(killed.get("scout_rule11"))
    scout_u = _n(killed.get("scout_unique"))
    fac = _n(killed.get("factory_kill"))
    fund = _n(killed.get("funding_avoid"))
    risk_o = _n(killed.get("risk_other"))
    skipped = _n(killed.get("skipped_unverified")) or 0
    risk_other_n = (risk_o or 0) + skipped
    # If both risk_o and skipped are missing entirely, show okänt
    risk_other_val: int | None
    if killed.get("risk_other") is None and killed.get("skipped_unverified") is None:
        risk_other_val = None
    else:
        risk_other_val = risk_other_n
    buys = _n(window.get("passed_to_buy"))

    def _st(kind: str) -> dict[str, Any]:
        d = (strategy or {}).get(kind) or {}
        return d if isinstance(d, dict) else {}

    sa, sb, sc, sd = _st("A"), _st("B"), _st("C"), _st("D")

    # Layout: center + 6 groups on a ring, sub-nodes further out
    def xy(r: float, deg: float) -> tuple[float, float]:
        th = math.radians(deg)
        return r * math.cos(th), r * math.sin(th)  # 0=right, 90=up

    # Angles (0 = right, 90 = up)
    groups = [
        {"id": "upptackt", "label": "Upptäckt", "sub": "DexScreener och GeckoTerminal", "angle": 90, "color": "#3ddeb0", "count": new_n},
        {"id": "scout", "label": "SCOUT", "sub": "Regel 1, 2 och 11", "angle": 30, "color": "#6b9bff", "count": scout_u},
        {"id": "risk", "label": "RISK", "sub": "Fabrik, finans, övriga", "angle": 330, "color": "#d291ff", "count": (None if fac is None and fund is None and risk_other_val is None else (fac or 0) + (fund or 0) + (risk_other_val or 0))},
        {"id": "a", "label": "Strategi A", "sub": "paper-köp", "angle": 270, "color": "#00e676", "count": buys},
        {"id": "d", "label": "Skugga D", "sub": "lösare A", "angle": 235, "color": "#ff9f6b", "count": None},
        {"id": "b", "label": "Skugga B", "sub": "följer trenden", "angle": 200, "color": "#ffd166", "count": None},
        {"id": "c", "label": "Skugga C", "sub": "följer valar", "angle": 150, "color": "#4dd0e1", "count": None},
    ]
    # Sub-counts are shown in the list under the figure (too tight on a phone if drawn here).
    subs: list[dict] = []
    # A/B/C: snapshot equity as a sub-label, not a counted kill
    def eq_lbl(stt: dict[str, Any]) -> str:
        eq = stt.get("equity")
        op = stt.get("open")
        cl = stt.get("closed")
        parts = []
        if eq is not None:
            try:
                parts.append(f"{float(eq):.3f} SOL")
            except Exception:
                pass
        if op is not None or cl is not None:
            parts.append(f"öppna {fmt_known(op)} · stängda {fmt_known(cl)}")
        return " · ".join(parts) if parts else "okänt"

    group_xy = {g["id"]: xy(0.82, g["angle"]) for g in groups}
    parent_of = {g["id"]: g for g in groups}
    sub_xy = []
    for s in subs:
        p = parent_of[s["parent"]]
        sub_xy.append((s, xy(1.22, p["angle"] + s["dangle"])))

    def size_for(count: int | None, base: float = 18, extra: float = 14) -> float:
        if not count:
            return base
        return base + min(extra, math.sqrt(max(0, count)) * 2.4)

    # Token dots clustered near the stage that handled them
    def token_angle(kind: str | None) -> float:
        k = kind or ""
        if k == "scout_kill":
            return 30
        if k in {"factory_kill", "funding_avoid", "risk_other", "skipped_unverified"}:
            return 330
        if k == "bought":
            return 270
        if k == "filter_age_liq":
            return 90
        return 60

    token_cap = 40
    shown = [tok for tok in tokens if isinstance(tok, dict) and tok.get("symbol")][:token_cap]
    # Spread tokens around their stage
    by_ang: dict[float, list[dict]] = {}
    for tok in shown:
        by_ang.setdefault(token_angle(tok.get("kind")), []).append(tok)
    token_pts: list[tuple[dict, float, float]] = []
    for ang, group in by_ang.items():
        n = len(group)
        for i, tok in enumerate(group):
            spread = (i - (n - 1) / 2) * (10 if n < 10 else 6)
            rr = 1.42 + (i % 3) * 0.10
            token_pts.append((tok, *xy(rr, ang + spread)))

    fig = go.Figure()
    cx, cy = 0.0, 0.0

    def add_glow_line(x0, y0, x1, y1, color: str, width: float = 1.4) -> None:
        fig.add_trace(go.Scatter(
            x=[x0, x1], y=[y0, y1], mode="lines",
            line=dict(color=color, width=width * 4),
            opacity=0.18, hoverinfo="skip", showlegend=False,
        ))
        fig.add_trace(go.Scatter(
            x=[x0, x1], y=[y0, y1], mode="lines",
            line=dict(color=color, width=width),
            opacity=0.85, hoverinfo="skip", showlegend=False,
        ))

    # Core to groups
    for g in groups:
        x, y = group_xy[g["id"]]
        add_glow_line(cx, cy, x, y, g["color"], 1.6)
    # Groups to subs
    for s, (x, y) in sub_xy:
        px, py = group_xy[s["parent"]]
        add_glow_line(px, py, x, y, parent_of[s["parent"]]["color"], 1.1)
    # Tokens to stage group
    kind_group = {
        "scout_kill": "scout",
        "factory_kill": "risk",
        "funding_avoid": "risk",
        "risk_other": "risk",
        "skipped_unverified": "risk",
        "bought": "a",
        "filter_age_liq": "upptackt",
    }
    color_map = {"red": "#ff6b6b", "yellow": "#ffd166", "green": "#00e676"}
    for tok, x, y in token_pts:
        gid = kind_group.get(str(tok.get("kind") or ""), "upptackt")
        px, py = group_xy[gid]
        col = color_map.get(str(tok.get("color") or "red"), "#ff6b6b")
        add_glow_line(px, py, x, y, col, 0.7)

    # Core node
    fig.add_trace(go.Scatter(
        x=[cx], y=[cy], mode="markers+text",
        marker=dict(size=46, color="#062414", line=dict(color="#00e676", width=3)),
        text=["🦁"], textfont=dict(size=18),
        hovertext="Lejon kärna · PAPER", hoverinfo="text", showlegend=False,
    ))

    # Group nodes
    gx = [group_xy[g["id"]][0] for g in groups]
    gy = [group_xy[g["id"]][1] for g in groups]
    gsize = [size_for(g["count"], 22, 16) for g in groups]
    gcol = [g["color"] for g in groups]
    ghover = []
    for g in groups:
        cnt = "okänt" if g["count"] is None else str(g["count"])
        extra = ""
        if g["id"] == "a":
            extra = f"<br>{eq_lbl(sa)}"
        elif g["id"] == "b":
            extra = f"<br>{eq_lbl(sb)}"
        elif g["id"] == "c":
            extra = f"<br>{eq_lbl(sc)}"
        elif g["id"] == "d":
            extra = f"<br>{eq_lbl(sd)}<br>PAPER – inte riktiga pengar"
        ghover.append(f"{g['label']}<br>{g['sub']}<br>antal: {cnt}{extra}")
    fig.add_trace(go.Scatter(
        x=gx, y=gy, mode="markers",
        marker=dict(size=gsize, color="#0a2416", line=dict(color=gcol, width=2.5)),
        hovertext=ghover, hoverinfo="text", showlegend=False,
    ))

    # Sub nodes
    sx = [xy_[0] for _, xy_ in sub_xy]
    sy = [xy_[1] for _, xy_ in sub_xy]
    ssize = [size_for(s["count"], 14, 12) for s, _ in sub_xy]
    scol = [parent_of[s["parent"]]["color"] for s, _ in sub_xy]
    shover = [
        f"{s['label']}: {'okänt' if s['count'] is None else s['count']}"
        for s, _ in sub_xy
    ]
    fig.add_trace(go.Scatter(
        x=sx, y=sy, mode="markers",
        marker=dict(size=ssize, color="#07180e", line=dict(color=scol, width=2)),
        hovertext=shover, hoverinfo="text", showlegend=False,
    ))

    # Token dots
    if token_pts:
        tx = [x for _, x, _ in ((t, x, y) for t, x, y in token_pts)]
        # unpack properly
        tx, ty, tcol, thov = [], [], [], []
        for tok, x, y in token_pts:
            tx.append(x); ty.append(y)
            tcol.append(color_map.get(str(tok.get("color") or "red"), "#ff6b6b"))
            rules = tok.get("rules") or []
            rule_s = f" · regel {', '.join(str(r) for r in rules)}" if rules else ""
            when = tok.get("time") or ""
            cyc = tok.get("cycle")
            cyc_s = f" · runda {cyc}" if cyc is not None else ""
            thov.append(f"{tok.get('symbol')}{cyc_s}<br>{tok.get('label') or ''}{rule_s}<br>{when}")
        fig.add_trace(go.Scatter(
            x=tx, y=ty, mode="markers",
            marker=dict(size=8, color=tcol, line=dict(color="#04120a", width=0.6), opacity=0.95),
            hovertext=thov, hoverinfo="text", showlegend=False,
        ))

    annotations = [
        dict(x=0, y=-0.18, text="Lejon kärna", showarrow=False,
             font=dict(color="#d8ffe9", size=11, family="Inter, sans-serif")),
    ]
    for g in groups:
        x, y = group_xy[g["id"]]
        cnt = "okänt" if g["count"] is None else str(g["count"])
        # Place the name between the core and the node so it is not clipped.
        lx, ly = xy(0.58, g["angle"])
        shown = g["label"] if g["id"] in {"b", "c", "d"} or g["count"] is None else f"{g['label']}  {cnt}"
        annotations.append(dict(
            x=lx, y=ly, text=shown, showarrow=False,
            font=dict(color=g["color"], size=10, family="Inter, sans-serif"),
        ))
    for s, (x, y) in sub_xy:
        cnt = "okänt" if s["count"] is None else str(s["count"])
        annotations.append(dict(
            x=x, y=y - 0.13, text=f"{s['label']} {cnt}", showarrow=False,
            font=dict(color="#9aa7a0", size=8, family="Inter, sans-serif"),
        ))
    # A/B/C equity under the group label
    for gid, stt in (("a", sa), ("b", sb), ("c", sc), ("d", sd)):
        g = parent_of[gid]
        eq = stt.get("equity")
        if eq is None:
            continue
        try:
            txt = f"{float(eq):.3f} SOL"
        except Exception:
            continue
        ex, ey = xy(1.08, g["angle"])
        annotations.append(dict(
            x=ex, y=ey, text=txt, showarrow=False,
            font=dict(color="#8b93a7", size=8, family="JetBrains Mono, monospace"),
        ))

    fig.update_layout(
        paper_bgcolor="#04120a",
        plot_bgcolor="#04120a",
        margin=dict(l=10, r=10, t=28, b=28),
        height=520,
        xaxis=dict(visible=False, range=[-1.75, 1.75], constrain="domain"),
        yaxis=dict(visible=False, range=[-1.75, 1.75], scaleanchor="x", scaleratio=1),
        showlegend=False,
        annotations=annotations,
        hoverlabel=dict(bgcolor="#0a2416", font_size=11, font_color="#d8ffe9"),
    )
    return fig



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



# ----- agentcirkel -----
pipe = load_pipeline_stats()
# W/L under equity, from live goals (DACT excluded) when available
_goals_pre = live_goals(ledger, positions)
_wl_wins = _wl_losses = None
_goal_pnl = None
_goal_closed = None
_goal_hit = None
for _g in _goals_pre:
    if _g.get("title", "").startswith("Träffsäkerhet"):
        # "40 % (2/5)"
        _m = re.search(r"(\d+)\s*/\s*(\d+)", str(_g.get("sub") or ""))
        if _m:
            _wl_wins, _closed_wl = int(_m.group(1)), int(_m.group(2))
            _wl_losses = _closed_wl - _wl_wins
        _goal_hit = _g.get("sub")
    if _g.get("title", "").startswith("Totalt resultat"):
        _goal_pnl = _g.get("sub")
    if _g.get("title", "").startswith("Minst 20"):
        _goal_closed = _g.get("sub")
_book_w = ledger.get("wins")
_book_l = ledger.get("losses")
_wl_bits = []
if _wl_wins is not None and _wl_losses is not None:
    _wl_bits.append(f"<b>{_wl_wins}</b> vinster · <b>{_wl_losses}</b> förluster i målen (utan DACT)")
if _book_w is not None and _book_l is not None:
    _wl_bits.append(f"bok {_book_w} vinster / {_book_l} förluster")
if _wl_bits:
    st.markdown('<div class="wl-line">' + " · ".join(_wl_bits) + "</div>", unsafe_allow_html=True)
_goal_bits = [x for x in (_goal_closed, _goal_hit, _goal_pnl) if x]
if _goal_bits:
    st.markdown(
        '<div class="wl-line">Mål innan live: ' + " · ".join(_goal_bits) + "</div>",
        unsafe_allow_html=True,
    )

st.markdown(
    """
<div class="card">
  <h3>Agentcirkel <span class="meta">riktiga paper-siffror</span></h3>
  <div class="meta">PAPER – inte riktiga pengar · inte finansiell rådgivning</div>
</div>
""",
    unsafe_allow_html=True,
)
_win_label = st.radio(
    "Tidsfönster",
    ("Senaste 24 timmarna", "Senaste 7 dagarna"),
    horizontal=True,
    label_visibility="collapsed",
    key="lejon_circle_window",
)
_win_key = "24h" if _win_label.startswith("Senaste 24") else "7d"
_win = None
if isinstance(pipe, dict):
    _win = (pipe.get("windows") or {}).get(_win_key)
if not isinstance(_win, dict):
    st.caption("Pipeline-siffror: okänt (ingen pipeline_stats.json i ögonblicksbilden).")
else:
    _from = _win.get("from") or "okänt"
    _to = _win.get("to") or "okänt"
    _cyc = fmt_known(_win.get("cycles"))
    _disc = (_win.get("discovered") or {}).get("new_tokens")
    _buy = _win.get("passed_to_buy")
    st.caption(f"{_from} – {_to} Europe/Stockholm · {_cyc} rundor · {fmt_known(_disc)} nya tokens · {fmt_known(_buy)} paper-köp")
    _strat = (pipe or {}).get("strategy") if isinstance(pipe, dict) else {}
    if not isinstance(_strat, dict):
        _strat = {}
    _fig = agent_circle_figure(_win, _strat)
    if _fig is not None:
        st.plotly_chart(_fig, use_container_width=True, config={"displayModeBar": False, "staticPlot": False})
    elif go is None:
        st.caption("Cirkeln behöver plotly.")
    _k = _win.get("killed") or {}
    _d = _win.get("discovered") or {}
    def _kv(label, val):
        return f'<div class="cmp-kv"><span>{label}</span><b>{fmt_known(val)}</b></div>'
    _sa = ((_strat or {}).get("A") or {})
    _sb = ((_strat or {}).get("B") or {})
    _sc = ((_strat or {}).get("C") or {})
    _sd = ((_strat or {}).get("D") or {})
    def _eq(stt):
        if not isinstance(stt, dict) or stt.get("equity") is None:
            return "okänt"
        try:
            return f"{float(stt['equity']):.3f} SOL · öppna {fmt_known(stt.get('open'))} · stängda {fmt_known(stt.get('closed'))}"
        except Exception:
            return "okänt"
    st.markdown(
        '<div class="card" style="margin-top:0">'
        '<h3>Siffror i cirkeln <span class="meta">samma fönster</span></h3>'
        + _kv("Upptäckt, nya tokens", _d.get("new_tokens"))
        + _kv("Stopp för ålder eller likviditet", _k.get("age_or_liq_filter"))
        + _kv("SCOUT, unika stopp", _k.get("scout_unique"))
        + _kv("— regel 1", _k.get("scout_rule1"))
        + _kv("— regel 2", _k.get("scout_rule2"))
        + _kv("— regel 11", _k.get("scout_rule11"))
        + _kv("RISK, fabrikskoll", _k.get("factory_kill"))
        + _kv("RISK, finansiering (undvik)", _k.get("funding_avoid"))
        + _kv("RISK, övriga", (_k.get("risk_other") or 0) + (_k.get("skipped_unverified") or 0) if (_k.get("risk_other") is not None or _k.get("skipped_unverified") is not None) else None)
        + _kv("Paper-köp i fönstret (A)", _win.get("passed_to_buy"))
        + f'<div class="cmp-kv"><span>Skugga B nu</span><b>{_eq(_sb)}</b></div>'
        + f'<div class="cmp-kv"><span>Skugga C nu</span><b>{_eq(_sc)}</b></div>'
        + f'<div class="cmp-kv"><span>Skugga D nu (paper)</span><b>{_eq(_sd)}</b></div>'
        + "</div>",
        unsafe_allow_html=True,
    )
    _toks = _win.get("tokens") or []
    _shown_n = min(40, len(_toks)) if isinstance(_toks, list) else 0
    _tot_n = len(_toks) if isinstance(_toks, list) else 0
    if _tot_n > _shown_n:
        st.caption(f"Visar de {_shown_n} senaste av {_tot_n} namngivna tokens.")
    st.markdown(
        '<div class="circle-note">Röd prick = stoppad. Gul prick = undvik. Grön prick = paper-köp. '
        "B, C och D visar nuvarande paper-saldo, inte antal i fönstret.</div>",
        unsafe_allow_html=True,
    )
    _unk = _sv_unknowns(list(_win.get("unknowns") or []) + list((pipe or {}).get("unknowns") or []))
    if _unk:
        st.markdown('<div class="circle-unk">Okänt / ofullständigt:<br>' + "<br>".join(_unk) + "</div>", unsafe_allow_html=True)


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
excl_note = goals_exclusion_footnote(positions)
excl_html = f'<div class="goal-foot-excl">{excl_note}</div>' if excl_note else ""
st.markdown(
    f"""
<div class="card">
  <h3>Mål innan live <span class="meta">paper-bevis</span></h3>
  {''.join(goal_rows)}
  <div class="goal-foot">Live slås på först när alla är ✅ och Hevar godkänner. Endast paper.{excl_html}</div>
</div>
""",
    unsafe_allow_html=True,
)


# ----- A vs B vs C comparison -----
stats_a = load_strategy_stats(DESK, "A")
stats_b = load_strategy_stats(DESK, "B")
stats_c = load_strategy_stats(DESK, "C")
stats_d = load_strategy_stats(DESK, "D")

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

def _cmp_col(title: str, stt: dict) -> str:
    return (
        f"<div class=\"cmp-col\"><h4>{title}</h4>"
        f"<div class=\"cmp-kv\"><span>Equity</span><b>{_cmp_val(stt.get('equity'),'sol')} SOL</b></div>"
        f"<div class=\"cmp-kv\"><span>P/L</span><b>{_cmp_val(stt.get('pnl'),'pnl')} SOL</b></div>"
        f"<div class=\"cmp-kv\"><span>Stängda</span><b>{_cmp_val(stt.get('closed'))}</b></div>"
        f"<div class=\"cmp-kv\"><span>Träffsäkerhet</span><b>{_cmp_val(stt.get('win_rate'),'pct')}</b></div>"
        f"<div class=\"cmp-kv\"><span>Öppna</span><b>{_cmp_val(stt.get('open'))}</b></div>"
        f"</div>"
    )

st.markdown(
    f"""
<div class="card">
  <h3>Jämförelse A, B, C och D <span class="meta">paper</span></h3>
  <div class="cmp-grid">
    {_cmp_col("A · desk", stats_a)}
    {_cmp_col("B · shadow", stats_b)}
    {_cmp_col("C · valar", stats_c)}
    {_cmp_col("D · lösare A", stats_d)}
  </div>
</div>
""",
    unsafe_allow_html=True,
)

# ----- Skugga D (lösare A) -----
_d_root = _shadow_dir(DESK, "shadow-d")
_d_led = load_json(_d_root / "ledger.json") or {}
_d_pos = []
for _p in sorted(glob.glob(str(_d_root / "positions" / "D-*.json"))):
    _x = load_json(Path(_p))
    if isinstance(_x, dict):
        _d_pos.append(_x)
_D_CAT_SV = {"a": "Regel 1 nära gränsen", "b": "Finansiering via stor hub", "c": "Likviditet 20–25k"}
_d_cats = _d_led.get("by_category") if isinstance(_d_led, dict) else None
if not isinstance(_d_cats, dict):
    _d_cats = {}
_d_rows = ['<div class="d-cat-row d-cat-head"><span>Mjuk regel som släpptes</span><b>köp</b><b>V/F</b><b>P/L SOL</b></div>']
for _k in ("a", "b", "c"):
    _c = _d_cats.get(_k) or {}
    try:
        _pl = f"{float(_c.get('realised_pnl_sol') or 0):+.4f}"
    except Exception:
        _pl = "–"
    _d_rows.append(
        f'<div class="d-cat-row"><span>{_k} · {_c.get("label_sv") or _D_CAT_SV[_k]}</span>'
        f'<b>{fmt_known(_c.get("bought"))}</b><b>{fmt_known(_c.get("wins"))}/{fmt_known(_c.get("losses"))}</b><b>{_pl}</b></div>'
    )
_d_open_html = []
_d_closed_html = []
for _x in sorted(_d_pos, key=lambda z: str(z.get("entry_utc") or ""), reverse=True):
    _sym = _x.get("symbol") or str(_x.get("mint") or "")[:6]
    _cat = _x.get("d_category") or "?"
    if str(_x.get("status", "")).upper() == "OPEN":
        _lm = _x.get("last_mark") or {}
        _mult = _lm.get("multiple")
        _d_open_html.append(f'<div class="d-pos">🟡 {_x.get("ticket")} · {_sym} · kategori {_cat} · '
                            f'{(str(_mult) + "x") if _mult is not None else "ingen kurs än"} · köpt {_x.get("entry_stockholm") or "–"}</div>')
    elif len(_d_closed_html) < 8:
        _ex = _x.get("exit") or {}
        try:
            _r = float(_ex.get("realised_pnl_sol"))
            _icon = "🟢" if _r > 0 else ("🔴" if _r < 0 else "⚪")
            _rs = f"{_r:+.4f} SOL ({float(_ex.get('realised_pnl_pct') or 0):+.1f} %)"
        except Exception:
            _icon, _rs = "⚪", "–"
        _d_closed_html.append(f'<div class="d-pos">{_icon} {_x.get("ticket")} · {_sym} · kategori {_cat} · {_rs} · {_ex.get("stockholm") or "–"}</div>')
_d_eq = stats_d.get("equity")
_d_head = (f"{float(_d_eq):.4f} SOL" if _d_eq is not None else "väntar på start")
_d_wl = f"{fmt_known(_d_led.get('wins') if isinstance(_d_led, dict) else None)}/{fmt_known(_d_led.get('losses') if isinstance(_d_led, dict) else None)}"
st.markdown(
    f"""
<div class="card">
  <h3>Skugga D · lösare A <span class="d-paper">PAPER – inte riktiga pengar</span></h3>
  <div class="cmp-kv"><span>Saldo (start 10 SOL)</span><b>{_d_head}</b></div>
  <div class="cmp-kv"><span>Öppna / max</span><b>{fmt_known(stats_d.get('open'))} / 3</b></div>
  <div class="cmp-kv"><span>Stängda · vinst/förlust</span><b>{fmt_known(stats_d.get('closed'))} · {_d_wl}</b></div>
  <div style="margin-top:8px">{''.join(_d_rows)}</div>
  <div style="margin-top:8px">{''.join(_d_open_html) or '<div class="d-pos">Inga öppna D-köp.</div>'}</div>
  <div style="margin-top:4px">{''.join(_d_closed_html)}</div>
  <div class="goal-foot">D köper bara tokens som A stoppade för exakt en mjuk regel. Hårda stopp (fabrik, dold finansiering, regel 2 och 11) gäller fullt ut. D räknas inte i "Mål innan live" och skickar inga notiser. Inte finansiell rådgivning.</div>
</div>
""",
    unsafe_allow_html=True,
)

# ----- Valar (C) -----
_wh_root = _shadow_dir(DESK, "shadow-c")
whales_blob = load_json(_wh_root / "whales.json") or {}
whale_rows = whales_blob.get("reviewed") or whales_blob.get("qualified") or []
if not isinstance(whale_rows, list):
    whale_rows = []
whale_html = []
for r in whale_rows[:10]:
    if not isinstance(r, dict):
        continue
    short = r.get("short") or "–"
    score = r.get("score")
    score_s = str(score) if score is not None else "–"
    reason = r.get("reason") or "–"
    whale_html.append(
        f'<div class="whale-row"><div class="whale-addr">{short}</div>'
        f'<div class="whale-score">{score_s}</div>'
        f'<div class="whale-reason">{reason}</div></div>'
    )
if not whale_html:
    whale_html.append('<div class="whale-reason">Inga valar just nu. C köper inget förrän någon klarar kraven.</div>')
n_ok = len(whales_blob.get("qualified") or []) if isinstance(whales_blob.get("qualified"), list) else 0
st.markdown(
    f"""
<div class="card">
  <h3>Valar <span class="meta">godkända {n_ok} · paper</span></h3>
  {''.join(whale_html)}
</div>
""",
    unsafe_allow_html=True,
)

# C day equity line (grows over the Stockholm day)
eq_day = load_json(_wh_root / "equity-day.json") or {}
c_pts = eq_day.get("points") if isinstance(eq_day, dict) else None
c_ys = []
c_xs = []
if isinstance(c_pts, list):
    for pt in c_pts:
        if not isinstance(pt, dict):
            continue
        try:
            c_ys.append(float(pt.get("equity")))
            c_xs.append(str(pt.get("t") or ""))
        except Exception:
            continue
st.markdown(
    '<div class="card"><h3>C idag <span class="meta">val-strategi · paper</span></h3>',
    unsafe_allow_html=True,
)
if go and c_ys:
    fig_c = go.Figure(
        go.Scatter(
            x=c_xs or list(range(len(c_ys))),
            y=c_ys,
            mode="lines+markers",
            line=dict(color="#00e676", width=2),
            marker=dict(size=5, color="#00e676"),
            hoverinfo="skip",
        )
    )
    fig_c.update_layout(
        paper_bgcolor="#0c0f14",
        plot_bgcolor="#0c0f14",
        margin=dict(l=8, r=8, t=8, b=24),
        height=140,
        xaxis=dict(visible=True, showgrid=False, tickfont=dict(color="#8b93a7", size=10), color="#8b93a7"),
        yaxis=dict(visible=True, showgrid=True, gridcolor="#161b26", tickfont=dict(color="#8b93a7", size=10), color="#8b93a7"),
        showlegend=False,
    )
    st.plotly_chart(fig_c, use_container_width=True, config={"displayModeBar": False})
elif c_ys:
    st.line_chart(c_ys, height=140)
else:
    st.caption("C-kurva idag: väntar på första mätningen.")
st.markdown("</div>", unsafe_allow_html=True)

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
    f'öppna {open_n}/10 · endast läsning · inga nycklar<br>'
    f'Desk {DESK} · uppdaterad {dt.datetime.now():%Y-%m-%d %H:%M} Europe/Stockholm</div>',
    unsafe_allow_html=True,
)
