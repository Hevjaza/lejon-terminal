# KILLED-SCOUT OTC-Fa24 (Fa24xN13pzjmcx1dtKP9nBMMFCwLtXCJrtP5hSPKpump)
Cycle 62, bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 with fixed c6 locator), measured 2026-10-29T09:03:24Z-2026-10-29T09:04:04Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: Fa24xN13pzjmcx1dtKP9nBMMFCwLtXCJrtP5hSPKpump
- PumpSwap pool: 6Wfuyx4DvKykPnGaNguAJii7or1A4Xmr5m8DnN2Bdh1T (https://dexscreener.com/solana/6Wfuyx4DvKykPnGaNguAJii7or1A4Xmr5m8DnN2Bdh1T)
- DexScreener ~09:02-09:03Z: liquidity 25967 USD, 1h volume 258227.26 USD
- Created: 2026-10-29T07:43:04Z, slot 462800877, tx 4mjW1zSPVpiQBNDjX1cTUxGY2o23wy6Wr8QPr8VxujRHfHbXdCw8vdZQuJpDZgs8arrBv68WSMmewFgYdPEEojVm; curve GKHBy4HvUNgWRQrXRC5QNfBsCo8d1zL58d1LmH1Poh9M; creator FTaeCBK9fhv1rsnx91yAPKLax5RoHvAZb1n8HMb2zu3
- Rule 1: creation slot 0 buying wallets (creator counted, migration tx and pool excluded), 0.0 % of tradable supply, wallets to reach 30 %: None; slots 0-2: 16 wallets, 90.33 %. **HIT**
- Rule 2: migration 5r8bmp9ViDpqiYo8NszuBMmxX3b1zstwCfxADAvHid9bWYUYQoCnvVU9ZdFnjLHBXsPKVu8d4kUTeLxTkqA7gAAV, not same slot, creator not co-signer. Not hit.
- Rule 11: migration slot 462801818 (+941 slots), window +0..+2: 12 buyers, 1.38 % of tradable supply, wallets to reach 80 %: None. Not hit.
- Rule hit: **Rule 1**
- Raw: research/raw-20261029/c62/bundle_OTC-Fa24.json, rule11_OTC-Fa24.json, log_OTC-Fa24.txt, r11log_OTC-Fa24.txt
- Note: the CreateV2 tx and all early buys landed in slot 462800878 (located create_slot 462800877 is one slot earlier), so the "creation slot" figure above reads 0; the slots 0-2 window covers the real creation slot: 16 wallets (creator FTaeCB... dev buy 1.34 % counted), 90.33 % of tradable supply, 1 wallet (JCt7RH..., 288.9M = 36.4 %) reaches 30 %. Rule 1 hit either way.
