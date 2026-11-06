# KILLED-SCOUT XTO-v3DN (v3DNinEcVoHw9xawuGTQJDZtE6qo35cbdiSrVTrpump)
Cycle 189 (18:13 Stockholm, 2026-11-03), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11), measured 2026-11-03T17:14:13Z-17:14:36Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: v3DNinEcVoHw9xawuGTQJDZtE6qo35cbdiSrVTrpump
- PumpSwap pool: Ahm67oTNe7b5enVDgckP7wULgt5of3XZXxgy2HprRYF5 (https://dexscreener.com/solana/Ahm67oTNe7b5enVDgckP7wULgt5of3XZXxgy2HprRYF5)
- Market data (GeckoTerminal gtslow ~17:13Z: age ~704 min, liq ~1.58M USD, 1h vol ~7.8k USD (24h ~909k), FDV ~381M, 1h 3,170 buys / 51 sells from 2,487 buyers / 4 sellers (bot-style churn, same AODF/XTO clone pattern).)
- Created: 2026-11-03T05:29:28Z, slot 464781351; curve AcegWkYn...; curve creator CMm2j1vL5eypCaCyWnhcjrfmCr8Vedu54Mr6CMBwe7mE (dev buy 100.0 %); create tx signers 3; 5 curve sigs.
- Rule 1: creator CMm2j1... alone bought the ENTIRE bonding curve (793.1M = 100 % of tradable) in the create tx; wallets to reach 30 %: 1. **HIT**
- Rule 2: MigrateV2+CreatePool 3voJmz... in the creation slot (+0) signed by the creator CMm2j1... (+ CdDdFX...) -> **HIT**
- Rule 11: window +0..+2: 4 buyers, 125.72 %, wallets to reach 80 %: 1. **HIT**
- bundle.py's migration locator picked the later no-op MigrateV2 (+2 slots, 9C4nRv...) = known quirk; rule11.py authoritative; verdict unaffected.
- Rule hit: **Rule 1, Rule 2, Rule 11**
- Raw: research/raw-20261103/c189/bundle_XTO.json, rule11_XTO.json, b_XTO.log, r11log_XTO.txt
