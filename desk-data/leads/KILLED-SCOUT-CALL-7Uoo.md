# KILLED-SCOUT CALL-7Uoo (7UooapEDmXmP5hRJPoYvXqYDWMVh15Gi59gYu7hopump)
Cycle 221 (02:05 Stockholm, 2026-11-05), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 with fixed c6 locator), measured 2026-11-05T01:05:56Z-2026-11-05T01:09:40Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: 7UooapEDmXmP5hRJPoYvXqYDWMVh15Gi59gYu7hopump
- PumpSwap pool: 77hsvm1D3fu4MpoDCvL4cwXG7KgMrVyJrnxFNoE9cyBx (https://dexscreener.com/solana/77hsvm1D3fu4MpoDCvL4cwXG7KgMrVyJrnxFNoE9cyBx)
- DexScreener/GT ~01:05Z: CALL, pool 77hsvm..., age ~65 min (curve created 2026-11-04 23:54:12Z by create signer Hufy2k... (curve creator field B1yzjR...); MigrateV2 3ekdEe... at slot 465495321, 2026-11-05 00:01:04Z, +1,929 slots, signed by AwfBEu..., not creator-cosigned), found via DS (scan2.py) + GT: DS liq ~36.8k, GT reserve ~37.1k USD, FDV ~186k, 1h vol ~795k (DS) / ~876k (GT), h1 +517 %, GT h1 11,147 buys / 8,628 sells by 3,279 buyers / 2,725 sellers. Pattern: create signer Hufy2k... bought 52.06 % of tradable in the create tx (dev buy, k30 = 1); creation slot 2 wallets 54.28 % -> rule 1 HIT; slots 0-2: 16 wallets 64.68 %, k30 = 1. Rule 2 not hit (migration not same slot, not creator-signed). Rule 11 pool walk BLIND (200k pool sigs did not reach migration slot; curve-side window 1 buyer 2.03 %); irrelevant, rule 1 kills.
- Created: 2026-11-04T23:54:12Z, slot 465493392, tx 4vZSckkz2ZtkGX9xDPs9mtY2Wr6sQNmD2L4zUQeH9ftsDZfWY2bX1o38G4StsZHtCfbGMkoL9hV5xbXRJKazeXuP; curve CDJDGVEyifnUrH6R5zaDGkNRf5g7DZVZu2Kvgd3LQzNo; creator B1yzjRGRbv5hbRMkKcD5fDCWcCNZZ9RpumoYmUqYjnfi
- Rule 1: creation slot 2 buying wallets (creator counted, migration tx and pool excluded), 54.28 % of tradable supply, wallets to reach 30 %: 1; slots 0-2: 16 wallets, 64.68 %. **HIT**
- Rule 2: migration 3ekdEejeRQDTpdt7iN5WVNXLqjngJ4b1fHLUYHCs5fnNDn66Gq5rXW2dBYMHh3tCVxi4aXDNXhWTXhtKq1dYhWYz, not same slot, creator not co-signer. Not hit.
- Rule 11: BLIND (migration tx located at slot 465495321, but the pool signature walk did not reach the migration slot; not guessed). Irrelevant to the verdict, rule 1 already kills.
- Rule hit: **Rule 1**
- Raw: research/raw-20261105/c221/bundle_CALL-7Uoo.json, rule11_CALL-7Uoo.json, b_*.log, r11log_CALL-7Uoo.txt
