# KILLED-SCOUT 0DAY (85mEALGuRCMmmMo7YD51pMfEjWisbHHRwZX8t7Bpump)
Cycle 263 (23:0x Stockholm, 2026-11-06), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11), measured 2026-11-06T22:04:49Z-2026-11-06T22:06:07Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: 85mEALGuRCMmmMo7YD51pMfEjWisbHHRwZX8t7Bpump
- PumpSwap pool: 6qLMg6Pz7ESJVz3i7MP4ARQknLkDy4NCAnZsu8NnnofA (https://dexscreener.com/solana/6qLMg6Pz7ESJVz3i7MP4ARQknLkDy4NCAnZsu8NnnofA)
- DexScreener ~22:04Z: 0DAY, found via gtslow.py: DS liq ~58,380, 1h vol ~24,302, age ~468 min, pc1 +10.9 %.
- Created: 2026-11-06T14:16:42Z, slot 466139855, tx 35YbkycYdAhmBrb3ZbY1G2eFfDYjFUEUMGZ8CqGrwu8HkasbcxeJeznm575KPk62b82JfuzrmmBGqzmsjAg2Qy4r; curve CnMmCMbeCQMTbamMtNyQYBufNweDkPVWBKvJuXsjXgkv; creator D9kSDUeKgG3GW3BRsczAimqycsTAoJ3ZkaUjvgfudxmU
- Rule 1: creation slot 16 buying wallets (creator counted, r1 after excl mig), 100 % of tradable supply, wallets to reach 30 %: 3; slots 0-2: 16 wallets, 100 %. Raw w_slot0 18 wallets 126.09 %, top15 119.56 %, k30=3. Multi-wallet txs in slot0: two 7-signer buys. **HIT**
- Rule 2: migration 5MasKJsHP4aBJXP1W9FnkkiP9m74itRbojd1RZL5HJag4bnmUTtUw98vwXEQ8pdmHRhUyMgyJhtVS8xJgnaPHZUm, same slot as create (dslot 0) but creator D9kS… not co-signer (signer A9jM…). Not hit.
- Rule 11: migration window +0..+2: 21 buyers, 100.01 % of tradable, k80=10. Not hit (mechanical k80<=5).
- Rule hit: **Rule 1**
- Raw: research/raw-20261106/c263/bundle_0DAY.json, rule11_0DAY.json, bun_0DAY.log, r11_0DAY.log
