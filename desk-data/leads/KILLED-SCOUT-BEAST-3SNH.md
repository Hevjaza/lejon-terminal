# KILLED-SCOUT BEAST-3SNH (3SNHYnySMkFY5p4c1Ykf8ATf9WRByNCGP3Wjdp7Qpump)
Cycle 103 (04:10 Stockholm), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 with fixed c6 locator), measured 2026-10-31T03:19:42Z-2026-10-31T03:20:15Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: 3SNHYnySMkFY5p4c1Ykf8ATf9WRByNCGP3Wjdp7Qpump
- PumpSwap pool: 4GsrsFtVmDHJwCKKiBUk7A5EaDpXC9e96WAtoo6NKCKF (https://dexscreener.com/solana/4GsrsFtVmDHJwCKKiBUk7A5EaDpXC9e96WAtoo6NKCKF)
- DexScreener ~03:19Z: liquidity 30904 USD, 1h volume 40286 USD, age 32 min (SOL-quoted PumpSwap). Found via GT trending 1h WebFetch fallback at ~03:10Z (age 22 min, liq ~22k, below thresholds) and re-checked once at 03:19Z when it crossed 30 min.
- Migration cross-check (chkmig.py getTransaction): 5hK6mJ... slot 463525856 = MigrateV2 + CreatePool, signed by creator GBGrg...; bundle.py locator picked 4xs4up... (slot +2, MigrateV2-only no-op, signer 9C4n...). rule11.py locator authoritative.
- Created: 2026-10-31T02:47:48Z, slot 463525856, tx 7rogFLBbvD64KSvhV58ZKuGP67FZLvdDYtuBuhueQ3eax7F5MKqPjN7Z1MDEbNe6pydYqxg2oiyzsaBQHdsMKFJ; curve Dr8p1tD7KXtsvss2cfprYNfj2x7FyRc957fxpS7hAbDZ; creator GBGrg1yuBUsmTokJbtfpLaMiXsNNAybGtSXuzkZ4AdGo
- Rule 1: creation slot 7 buying wallets (creator counted, migration tx and pool excluded), 100.0 % of tradable supply, wallets to reach 30 %: 2; slots 0-2: 7 wallets, 100.0 %. **HIT**
- Rule 2: migration 5hK6mJs7kRUnhH2b5VousUSKJbsUfFv57nFSuu9wveUp3YCxaEujGnNKdcznhhfxAYrD9eWuu4iAasKX4savYRym, same slot as creation, creator co-signed. **HIT**
- Rule 11: migration slot 463525856 (+0 slots), window +0..+2: 18 buyers, 100.93 % of tradable supply, wallets to reach 80 %: 5. **HIT**
- Rule hit: **Rule 1, Rule 2, Rule 11**
- Raw: research/raw-20261031/c103/bundle_BEAST-3SNH.json, rule11_BEAST-3SNH.json, log_BEAST-3SNH.txt, r11log_BEAST-3SNH.txt
