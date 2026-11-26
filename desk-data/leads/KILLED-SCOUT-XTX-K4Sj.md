# KILLED-SCOUT XTX-K4Sj (K4SjYqTswHEZd9aHTJbFyeZ5irGM921Ut8WMXMQpump)
Cycle 204 (09:05 Stockholm, 2026-11-04), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 with fixed c6 locator), measured 2026-11-04T08:08:09Z-2026-11-04T08:08:42Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: K4SjYqTswHEZd9aHTJbFyeZ5irGM921Ut8WMXMQpump
- PumpSwap pool: C8mh98vzCLHbQob4Gf8cV4ib1HtXzvngRYufnghmdCpF (https://dexscreener.com/solana/C8mh98vzCLHbQob4Gf8cV4ib1HtXzvngRYufnghmdCpF)
- DexScreener/GT ~08:07Z: XTX, pool C8mh98..., age ~876 min (created 2026-11-03 17:31:09Z), found via GT only: GT reserve ~1.52M USD vs FDV ~351M USD and h1 3,235 buys / 56 sells / 5 sellers = price/liquidity artefact (XTX family, cf. c200 XTX BWDi); GT 1h vol ~7.6k. Pattern: creator 2VNThN... bought 100 % of tradable in the create tx itself (k30 = 1); MigrateV2 5vPvMX... in the creation slot co-signed by the creator 2VNThN... and BBAAPE... -> rule 2 HIT; Rule 11 window 5 buyers 125.77 %, k80 = 1 -> HIT. (bundle.py picked the later no-op MigrateV2 5vqpUd... by 9C4nRv..., known quirk; rule11.py authoritative; rule11.py getSignaturesForAddress hit one Helius 429, retried OK.)
- Created: 2026-11-03T17:31:09Z, slot 464983480, tx 28WCpEeXrVDWnEnff4t42YnqfpjW9TA3uCp14s9diwf9RdhTqcCLtY3JHjXJqfxVNjkcn7Vio9PpqFJyzJa1dHNC; curve 7ABMKiYvzUCvnenjc8TNCqKoikB5tWYFVJh4E3JhHFL8; creator 2VNThNMrr3wWMNSFARcKw6dCBtcHXJt9DoFrvtJAPvAK
- Rule 1: creation slot 1 buying wallets (creator counted, migration tx and pool excluded), 100.0 % of tradable supply, wallets to reach 30 %: 1; slots 0-2: 1 wallets, 100.0 %. **HIT**
- Rule 2: migration 5vPvMXjFzu2W7wJ7qsLMLdzcKyFVrjoUhSqJH92EyFcCKQWZN3LEhogwVWTvg6mYoMUAYU1xtRZyPvQim9enVwU2, same slot as creation, creator co-signed. **HIT**
- Rule 11: migration slot 464983480 (+0 slots), window +0..+2: 5 buyers, 125.77 % of tradable supply, wallets to reach 80 %: 1. **HIT**
- Rule hit: **Rule 1, Rule 2, Rule 11**
- Raw: research/raw-20261104/c204/bundle_XTX-K4Sj.json, rule11_XTX-K4Sj.json, b_*.log, r11log_XTX-K4Sj.txt
