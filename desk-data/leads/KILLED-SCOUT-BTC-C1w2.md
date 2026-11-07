# KILLED-SCOUT BTC (C1w2cSCc4GmXfUL2y5amkGLhDPsJT7Ts7VyS71inpump)
Cycle 267 (04:0x Stockholm, 2026-11-07), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 with fixed c6 locator), measured 2026-11-07T03:02:41Z-2026-11-07T03:03:09Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: C1w2cSCc4GmXfUL2y5amkGLhDPsJT7Ts7VyS71inpump
- PumpSwap pool: 7Nw3tQdCkz92P77VaFToF5yJmN2CSAtHuC8pEvSNEvWV (https://dexscreener.com/solana/7Nw3tQdCkz92P77VaFToF5yJmN2CSAtHuC8pEvSNEvWV)
- DexScreener/GT ~03:0xZ: BTC, pool 7Nw3tQdC..., age ~68 min at scan (curve created 2026-11-07 01:54:27Z, creation slot 466334782, creator 2CUGMx...; migrated in the SAME slot), found via scan2 (dsretry 0 / gtslow 0 new): DS liq ~30.7k, 1h vol ~92k, h1 +34 %, FDV ~158k. Creation slot: CreateV2 + multiwallet Buys (5-signer CreateV2 + two 7-signer Buy txs) -> r1 (ex-pool) 18 wallets 100 % of tradable, k30 = 3 -> Rule 1 HIT. Authoritative MigrateV2/CreatePool 2oNwN8... same slot, co-signed by the creator 2CUGMx... (+FrxTYU...) -> Rule 2 HIT. Rule 11: window 28 buyers 110.21 %, k80 = 9 (mechanical cap 5 not hit); same-slot multiwallet BuyV3 pattern (5+7+7 signers) with top10 89.04 % of tradable in migration window -> Rule 11 judgment HIT (hard KILL per t39u). bundle.py locator picked a later no-op Migrate by 9C4nRv... (+4 slots, known quirk); rule11.py authoritative.
- Created: 2026-11-07T01:54:27Z, slot 466334782, tx 5P1XDkwceYzxfAH16L5JYj7oHFACnUKMC2EhpVTRb4SFLUMUid7dY22UgWzJ2ooWSv9iYLHZFUshwW7bfQq1JWCN; curve 8bTdFidARpQvWwz8UFwQxQc6f4REuC8AGXodQzB2zJmN; creator 2CUGMxDpPBB2qxguPhTkqSHSB7vemL8277SMQxobUutk
- Rule 1: creation slot 18 buying wallets (creator counted, migration tx and pool excluded), 100.0 % of tradable supply, wallets to reach 30 %: 3; slots 0-2: 18 wallets, 100.0 %. **HIT**
- Rule 2: migration 2oNwN8DUr4CcmLroLWCyCAeZPuq5B1R5xcUreKUvz5Paao4gt3P4cMUEKMvZqHJtVvehKegT4ChQZTWLeBAR2y4m, same slot as creation, creator co-signed. **HIT**
- Rule 11: migration slot 466334782 (+0 slots), window +0..+2: 28 buyers, 110.21 % of tradable supply, wallets to reach 80 %: 9. Not hit mechanically (k80>5).
- Rule hit: **Rule 1, Rule 2, Rule 11 (judgment: same-slot 5+7+7-signer BuyV3 multiwallet = top10 89.04 % in migration window)**
- Raw: research/raw-20261107/c267/bundle_BTC.json, rule11_BTC.json, bun_BTC.log, r11_BTC.log
