# KILLED-SCOUT AODF-vDuC (vDuCB8fRgzZ1Pgm5hcZdaDafLTkgf4WLUBWrFVHpump)
Cycle 194 (23:08 Stockholm, 2026-11-03), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 with fixed c6 locator), measured 2026-11-03T22:08:57Z-2026-11-03T22:09:24Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: vDuCB8fRgzZ1Pgm5hcZdaDafLTkgf4WLUBWrFVHpump
- PumpSwap pool: 3S7j9GjAfo7kkqP1eBYHzXXDFcTqt8CLguvwnG9Doduh (https://dexscreener.com/solana/3S7j9GjAfo7kkqP1eBYHzXXDFcTqt8CLguvwnG9Doduh)
- DexScreener/GT ~22:08Z: AODF, pool 3S7j9G..., age ~1148 min (created 2026-11-03 03:00:17Z), GT reserve ~3.48M (price artefact, not real depth), FDV ~1.83B, 1h vol ~5.6k, h24 ~1.84M; GT h1 1243 buys / 48 sells (1156 buyers / 3 sellers) - extreme one-sided flow, same pattern as earlier AODF clones. Pattern: creator 5P9g75... alone bought the whole curve in the create tx (k30 = 1); MigrateV2+CreatePool 5d8Jef... in the creation slot co-signed by the creator and 7mQ4Sn..., which took a further ~20 % from the pool in the same slot; Rule 11 4 buyers 125.65 %, k80 = 1. bundle.py picked the later no-op MigrateV2 3viaom... (9C4nRv..., +2 slots) = known quirk; rule11.py authoritative.
- Created: 2026-11-03T03:00:17Z, slot 464739430, tx 4ndxLzuim88nNoVu9kXFg7Q9QT2QUGUXqYYhvkb8mTMgQv2687z1M1ny8upwGRiPY6bVaQS22QN2wEoajuBcE78T; curve HXvgeKuRcuVdKJDGL8pZHzLq59xFsaxapY27nXKecEE1; creator 5P9g75ZKx3FVFsr4NB2i8tNojrbqGNy1fDnY3j3vZ3ro
- Rule 1: creation slot 1 buying wallets (creator counted, migration tx and pool excluded), 100.0 % of tradable supply, wallets to reach 30 %: 1; slots 0-2: 1 wallets, 100.0 %. **HIT**
- Rule 2: migration 5d8JefcqaPufA6cTUrq6wsq6edvhvGjG6aqAWyTBF32nEVs6gGCqSi18Z5sBRQWWKkZVotnozfrV26cKq5X14Lmm, same slot as creation, creator co-signed. **HIT**
- Rule 11: migration slot 464739430 (+0 slots), window +0..+2: 4 buyers, 125.65 % of tradable supply, wallets to reach 80 %: 1. **HIT**
- Rule hit: **Rule 1, Rule 2, Rule 11**
- Raw: research/raw-20261103/c194/bundle_AODF-vDuC.json, rule11_AODF-vDuC.json, b_*.log, r11log_AODF-vDuC.txt
