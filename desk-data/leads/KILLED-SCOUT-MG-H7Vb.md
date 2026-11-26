# KILLED-SCOUT MG-H7Vb (H7VbWMbeZYqxPJekix8GMsfLH4ApvedmgDXfcHT1pump)
Cycle 178 (07:05 Stockholm, 2026-11-03), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 + premig per-tx decode), measured 2026-11-03T06:06:10Z-2026-11-03T06:07Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: H7VbWMbeZYqxPJekix8GMsfLH4ApvedmgDXfcHT1pump
- PumpSwap pool: 7fLb5yHNNVjtcCqCy78Skf1HP9rqwjDLUQ4bNL8QueGV (https://dexscreener.com/solana/7fLb5yHNNVjtcCqCy78Skf1HP9rqwjDLUQ4bNL8QueGV)
- Market data: MG, pool age ~1,221 min, GT reserve ~45.8k, 1h vol ~3.8k, h24 vol ~164.2k, FDV ~347k; GT h1 939 buys / 914 sells (GeckoTerminal ~06:05Z)
- Created: 2026-11-01T06:12:09Z, slot 463986587; curve 6LtHhNzvZ9hncwYiKZxs5qzqDT54pBRqyC8KuQpzpoyP; creator / create signer 9J3i2PE6YBoBAed7aw4teDKRGfUWk9nopMy3bzuUks3V
- Rule 1: creation slot 2 buying wallets (creator counted) 14.47 % of tradable; slots 0-2: 3 wallets 14.54 %; k30 none -> not hit (below the 15 % soft-flag band)
- Rule 2: MigrateV2+CreatePool 4EV6Kutg... at slot 464449429 (2026-11-02T09:44:25Z, +462,842 slots after creation) signed by 6hb5Q41A... (not the creator) -> not hit
- Rule 11: **HIT**. In the migration slot itself 5 wallets bought 82.79 % of tradable supply (k30 = 2, k80 = 5): two 2-signer curve buy txs that completed the curve, 4hEN36Nk... (9YvL3D... 231.8M + 6hb5Q4... 124.1M = 44.87 %) and 4wyMjqF6... (2G2TEa... 77.3M + 5JwHZ4... 52.8M = 16.40 %), plus CqzSpd... 170.7M (21.5 %) from the new pool in the same slot. The migration signer 6hb5Q4... is itself one of the co-signing curve buyers (insider-run graduation). Slots +1/+2: only dust buys. Cluster of 5 wallets > 80 % of tradable in the graduation slot = hard KILL (no soft flag for Rule 11; also hard per t39u).
- bundle.py's migration locator picked the later no-op MigrateV2 (3N7wzBMY..., +2 slots, 9C4nRv...) = known quirk; rule11.py + premig.py authoritative; verdict unaffected.
- Rule hit: **Rule 11**
- Raw: research/raw-20261103/c178/bundle_MG.json, rule11_MG.json, premig_MG.json, b_MG.log, r11log_MG.txt
