# KILLED-SCOUT HODL (DKtofLM6bhb54GQy5YFSWQjQmGiZqAkjzkQJ1LTopump)
Cycle 265 (02:0x Stockholm, 2026-11-07), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 with fixed c6 locator), measured 2026-11-07T01:11:55Z-2026-11-07T01:12:56Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: DKtofLM6bhb54GQy5YFSWQjQmGiZqAkjzkQJ1LTopump
- PumpSwap pool: ANS69UDTbMCWbW7ZuCYXLZ4HMCQkvzPMtCW9zjPZQGKR (https://dexscreener.com/solana/ANS69UDTbMCWbW7ZuCYXLZ4HMCQkvzPMtCW9zjPZQGKR)
- DexScreener/GT ~01:1xZ: HODL, pool ANS69UDT..., age ~121 min at scan (curve created 2026-11-06 23:09:39Z, creation slot 466288699, creator 9NkVW5...; migrated in the SAME slot), found via dsretry+scan2+gtslow: DS liq ~144k, 1h vol ~450k, h1 +102 %, FDV ~3.1M. Creation slot: CreateV2 + multiwallet Buys (5-signer + two 7-signer Buy txs) -> r1 (ex-pool) 18 wallets 100 % of tradable, k30 = 3 -> Rule 1 HIT. Authoritative MigrateV2/CreatePool 3zM9dN... same slot, co-signed by the creator 9NkVW5... (+955mud...) -> Rule 2 HIT. Rule 11: window 25 buyers 110.89 %, k80 = 8 (mechanical cap 5 not hit); same-slot multiwallet BuyV3 pattern (5+7+7 signers) with top10 90.25 % of tradable in migration window -> Rule 11 judgment HIT (hard KILL per t39u). bundle.py locator picked a later no-op Migrate by 9C4nRv... (+2 slots, known quirk); rule11.py authoritative.
- Created: 2026-11-06T23:09:39Z, slot 466288699, tx 63p2sx4HAHHfAi79E3D96akfga8v9c4LtRHGyrn2Hg1THJHnB9PrRW5DiqMXJUoMhNNN2fDDUawhnfTMYoCuz2pt; curve 4Umi6xkTYp1EBzwzD7n7oUrMVP8SLzfieqU7S7VBMT1U; creator 9NkVW544fKy2kkU5ZxJFa1xy6C7LssPKZAW5XWbK5XG5
- Rule 1: creation slot 18 buying wallets (creator counted, migration tx and pool excluded), 100.0 % of tradable supply, wallets to reach 30 %: 3; slots 0-2: 18 wallets, 100.0 %. **HIT**
- Rule 2: migration 3zM9dNgcn9ShTV7FrvWXaHYw5J9cKtp4ydaswFYnkqEbJTxVz6rvDhiHRbUf46XPH1h3zYu1pmEwXa8y6tAdGC14, same slot as creation, creator co-signed. **HIT**
- Rule 11: migration slot 466288699 (+0 slots), window +0..+2: 25 buyers, 110.89 % of tradable supply, wallets to reach 80 %: 8. Not hit mechanically (k80>5).
- Rule hit: **Rule 1, Rule 2, Rule 11 (judgment: same-slot 5+7+7-signer BuyV3 multiwallet = top10 90.25 % in migration window)**
- Raw: research/raw-20261107/c265/bundle_HODL.json, rule11_HODL.json, bun_HODL.log, r11_HODL.log
