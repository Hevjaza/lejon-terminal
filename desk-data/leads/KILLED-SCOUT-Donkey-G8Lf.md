# KILLED-SCOUT Donkey-G8Lf (G8Lf8uthQp5YHoswQZDRdeRxaWiUqnNFNoZ45y68pump)
Cycle 213 (18:10 Stockholm, 2026-11-04), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 with fixed c6 locator), measured 2026-11-04T17:11:47Z-2026-11-04T17:13:55Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: G8Lf8uthQp5YHoswQZDRdeRxaWiUqnNFNoZ45y68pump
- PumpSwap pool: ESCdnqaEAyUsxUy5hAdqogQYykJiAFAYXgchuDhDgxAN (https://dexscreener.com/solana/ESCdnqaEAyUsxUy5hAdqogQYykJiAFAYXgchuDhDgxAN)
- DexScreener/GT ~17:10Z: Donkey (different mint from Donkey APj5, c212), pool ESCdnq..., age ~147 min (curve created 2026-11-04 14:39:13Z, MigrateV2+CreatePool 3zJSCo... at +1,255 slots, 14:43:42Z, signed by 9C4nRv..., not creator), found via DS (scan2.py) only: DS liq ~27.3k USD, FDV ~99k, 1h vol ~221k, h24 ~1.23M, h1 +45 %. Pattern: creation slot 4 buying wallets 34.62 % of tradable, k30 = 4 (top Dqv8wh... 15.9 %); slots 0-2 9 wallets 45.04 %, k30 = 3 -> rule 1 HIT. Rule 11 BLIND (pool walk did not reach the migration slot). (bundle.py picked MigrateV2 by 9C4nRv... at +5 slots, known quirk.)
- Created: 2026-11-04T14:39:13Z, slot 465338544, tx 2ChoHBnkBp8L3ER1AEwhBvtmh7vz7hhBB8khgBfe1wkgDrZCz3D9BV7xiv9mMgpRsoZA1WSrPn9vaqmH4BuABXrS; curve 6qXMeKknyEY9voj5UU24tzzLMhrYVs8hDo7jrN5QEaDa; creator 4FDNhaz443183ExeXarqjsyB8KikE8vEM5PG12HVfPp1
- Rule 1: creation slot 4 buying wallets (creator counted, migration tx and pool excluded), 34.62 % of tradable supply, wallets to reach 30 %: 4; slots 0-2: 9 wallets, 45.04 %. **HIT**
- Rule 2: migration 3zJSCozE5MRB2UNaaJpzqdPLbT7LJ2KHW7BguK7sP77XvK1aBc4WY5J5nzZwu6yJfQ2jAPGFnbT2hiB3SPxoZmxb, not same slot, creator not co-signer. Not hit.
- Rule 11: BLIND (migration tx located at slot 465339799, but the pool signature walk did not reach the migration slot; not guessed). Irrelevant to the verdict, rule 1 already kills.
- Rule hit: **Rule 1**
- Raw: research/raw-20261104/c213/bundle_Donkey-G8Lf.json, rule11_Donkey-G8Lf.json, b_*.log, r11log_Donkey-G8Lf.txt
