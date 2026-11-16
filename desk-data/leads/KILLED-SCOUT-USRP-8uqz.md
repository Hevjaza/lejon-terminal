# KILLED-SCOUT USRP-8uqz (8uqzQqUkSbHTkWCq2At3yS43wpCaLwyGDNj6d7zpump)
Cycle 239 (20:08 Stockholm, 2026-11-05), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 with fixed c6 locator), measured 2026-11-05T19:09:20Z-2026-11-05T19:09:48Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: 8uqzQqUkSbHTkWCq2At3yS43wpCaLwyGDNj6d7zpump
- PumpSwap pool: BGCU76vMG4BghSx7uQBT8Sr9ZQEWAkK4emJ82PRVzrew (https://dexscreener.com/solana/BGCU76vMG4BghSx7uQBT8Sr9ZQEWAkK4emJ82PRVzrew)
- DexScreener/GT ~19:08Z: USRP, pool BGCU76vM..., age ~467 min at scan (curve created 2026-11-05 11:21:34Z, creation slot 465686664, creator 78MfAQ...; migrated in the SAME slot), found via gtslow.py: GT reserve ~1.33M, FDV ~281M, 1h vol ~11.4k (4,641 buys / 873 sells by 9 buyers / 8 sellers). Creator 78MfAQ... bought 100 % of tradable in the create tx, k30 = 1 -> Rule 1 HIT. Same-slot MigrateV2+CreatePool 4HM7eH... signed by ryfbhb..., not the creator -> Rule 2 not hit. Rule 11: window 5 buyers 125.75 %, k80 = 1 -> HIT. Same single-creator template as AODT c236 / NADF c230 / PAD c233. bundle.py locator picked a later no-op MigrateV2 282hTP... by 9C4nRv... (+1 slot, known quirk); rule11.py authoritative.
- Created: 2026-11-05T11:21:34Z, slot 465686664, tx 5h9cez4nw4z7GtRAauBSaxrxwS6ov1dXhTN96iGW3akXkTGLY3U2VCHHhDQfXk12cpWN7CC1JvB2ZPkFgUtJmh71; curve VDLNjZqeQk8tuNzTXWTviUZqA5MLpz5NEzior97Prp2; creator 78MfAQjb5TBsJeC5MXWLocscgNkSuNnPinW929BuZ2j8
- Rule 1: creation slot 1 buying wallets (creator counted, migration tx and pool excluded), 100.0 % of tradable supply, wallets to reach 30 %: 1; slots 0-2: 1 wallets, 100.0 %. **HIT**
- Rule 2: migration 4HM7eHP1f2kjfzHoarSFcWTdLNeuNaDgX9e2oJ6gTu9FCMJoCSgymnJ2EQq27CTQcWhhgdwEFi4ur6sewZbFNPj7, same slot as creation, creator not co-signer. Not hit.
- Rule 11: migration slot 465686664 (+0 slots), window +0..+2: 5 buyers, 125.75 % of tradable supply, wallets to reach 80 %: 1. **HIT**
- Rule hit: **Rule 1, Rule 11**
- Raw: research/raw-20261105/c239/bundle_USRP-8uqz.json, rule11_USRP-8uqz.json, b_*.log, r11log_USRP-8uqz.txt
