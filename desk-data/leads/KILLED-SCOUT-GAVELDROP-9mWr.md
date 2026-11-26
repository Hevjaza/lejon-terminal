# KILLED-SCOUT GAVELDROP-9mWr (9mWrj77gDZ7w4rwHF6STYXDZmYRMyf39L4go1mXepump)
Cycle 220 (01:05 Stockholm, 2026-11-05), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 with fixed c6 locator), measured 2026-11-05T00:04:03Z-2026-11-05T00:04:50Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: 9mWrj77gDZ7w4rwHF6STYXDZmYRMyf39L4go1mXepump
- PumpSwap pool: GgGoctYNusmGdFpqmrC9pv8JX6JPG4mkm4RkeNzkakTo (https://dexscreener.com/solana/GgGoctYNusmGdFpqmrC9pv8JX6JPG4mkm4RkeNzkakTo)
- DexScreener/GT ~00:05Z: GAVELDROP, pool GgGoct..., age ~78 min (curve created 2026-11-04 22:44:57Z, MigrateV2+CreatePool 5ak2H4... in the same slot 465474049, signed by the creator 3jedan...), found via DS search + GT: DS liq ~59.7k, GT reserve ~59.6k USD, FDV ~506k, 1h vol ~907k (DS) / ~861k (GT), GT h1 19,150 buys / 6,811 sells by 6,026 buyers / 2,059 sellers. Pattern: whole curve emptied in the creation slot by 7 wallets (100 % of tradable, k30 = 2, dev buy 0.44 %, two 3-signer buy txs) -> rule 1 HIT; migration in creation slot signed by creator -> rule 2 HIT; Rule 11 window 11 buyers 116.97 %, k80 = 4 -> HIT. Same 7-wallet template as c213/c218. (bundle.py picked the later MigrateV2 CbKKrM... by 9C4nRv... at +2 slots, known quirk; rule11.py authoritative.)
- Created: 2026-11-04T22:44:57Z, slot 465474049, tx 4eV7MbK9poNV7ntziGH15vmTvBfbx1mjuNRMkDMri6WWY2uiCTwMkuwaZ1DmVhTJUD7DWmNGiVbtbMQP969cXRaB; curve HSKXdUAsSojVY77TSanp7sTxGUGBLN5XAP6Lx4sFCAoU; creator 3jedanvgSEd4ReVUDnY2uL7SmiGBjwohp41KneKt2g82
- Rule 1: creation slot 7 buying wallets (creator counted, migration tx and pool excluded), 100.0 % of tradable supply, wallets to reach 30 %: 2; slots 0-2: 7 wallets, 100.0 %. **HIT**
- Rule 2: migration 5ak2H4rE3b6NtzYVWVxfi6R4hZL1DdtZayhKy4xprzrP9PjyEpMon9qfWpCjG686fmdU7vmrADZUcWPAD9KebgMk, same slot as creation, creator co-signed. **HIT**
- Rule 11: migration slot 465474049 (+0 slots), window +0..+2: 11 buyers, 116.97 % of tradable supply, wallets to reach 80 %: 4. **HIT**
- Rule hit: **Rule 1, Rule 2, Rule 11**
- Raw: research/raw-20261105/c220/bundle_GAVELDROP-9mWr.json, rule11_GAVELDROP-9mWr.json, b_*.log, r11log_GAVELDROP-9mWr.txt
