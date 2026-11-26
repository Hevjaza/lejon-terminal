# KILLED-SCOUT GTA-9vrE (9vrEeQSTctTPSCdzbiHWLrb4xcjSn91YcoJFLDyopump)
Cycle 241 (22:10 Stockholm, 2026-11-05), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 with fixed c6 locator), measured 2026-11-05T21:11:44Z-2026-11-05T21:12:05Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: 9vrEeQSTctTPSCdzbiHWLrb4xcjSn91YcoJFLDyopump
- PumpSwap pool: 4XBsV7YFtzzEaXdjK77SGTeAS1MEhWBb73gHuWhvJ8Sg (https://dexscreener.com/solana/4XBsV7YFtzzEaXdjK77SGTeAS1MEhWBb73gHuWhvJ8Sg)
- DexScreener/GT ~21:10Z: GTA, pool 4XBsV7YF..., age ~40 min at scan (curve created 2026-11-05 20:30:46Z, creation slot 465840800, creator CCHr6z...; migrated in the SAME slot), found via scan2.py: DS liq ~36.0k, 1h vol ~166k, h1 +392 %, FDV ~216k. Creation slot: CreateV2 (1.31 %) + one 7-signer BuyV3 tx (50.62 %) + one 10-signer BuyV3 tx (48.06 %) -> 18 wallets 100 % of tradable, k30 = 4 -> Rule 1 HIT. Authoritative MigrateV2 3gppqU... same slot, signed by the creator CCHr6z... -> Rule 2 HIT. Rule 11: window 28 buyers 112.74 %, k80 = 10 (mechanical cap 5 not hit); premig.py: 7-signer + 10-signer BuyV3 = 98.68 % of the curve in migration slot -> Rule 11 judgment HIT (hard KILL per t39u). bundle.py locator picked a later no-op MigrateV2 by 9C4nRv... (+2 slots, known quirk); rule11.py authoritative.
- Created: 2026-11-05T20:30:46Z, slot 465840800, tx 4ekNZKEpGUV2EPFizzHPh8RxBJvmBoAQmNteu7ycWHSudBsrDS3JhEhJcePFYt2HCmCCeBM3mx85QC5mYFD1XtMj; curve HNaA7EcfV6AaYw9pUjpcSJpqf65ByBtdcGUNawqbvWRN; creator CCHr6zuDFaS4LW9etiycXY8iEw1rC22WZwhRnKq9FFqb
- Rule 1: creation slot 18 buying wallets (creator counted, migration tx and pool excluded), 100.0 % of tradable supply, wallets to reach 30 %: 4; slots 0-2: 18 wallets, 100.0 %. **HIT**
- Rule 2: migration 3gppqUvMm8tQxPCX5gjwUizX7ww1y8dU6XxhBEXJmV22uev4eQrVWxTp3azzrtgwdAgC27DsCNYGwgsaG3MgMSQw, same slot as creation, creator co-signed. **HIT**
- Rule 11: migration slot 465840800 (+0 slots), window +0..+2: 28 buyers, 112.74 % of tradable supply, wallets to reach 80 %: 10. Not hit.
- Rule hit: **Rule 1, Rule 2, Rule 11 (judgment: 7-signer + 10-signer BuyV3 = 98.68 % in migration slot)**
- Raw: research/raw-20261105/c241/bundle_GTA-9vrE.json, rule11_GTA-9vrE.json, b_*.log, r11log_GTA-9vrE.txt
