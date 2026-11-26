# KILLED-SCOUT MrBeast-6Hdd (6HddHsUvKvfgGjkxn9vdPAswwJC3mwa9k8YB52ubpump)
Cycle 218 (23:10 Stockholm, 2026-11-04), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 with fixed c6 locator), measured 2026-11-04T22:11:54Z-2026-11-04T22:12:50Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: 6HddHsUvKvfgGjkxn9vdPAswwJC3mwa9k8YB52ubpump
- PumpSwap pool: NHCcmvWSwGh3qSjNSs8HHcWv4Lt3Xg6osmg6aDeAqvQ (https://dexscreener.com/solana/NHCcmvWSwGh3qSjNSs8HHcWv4Lt3Xg6osmg6aDeAqvQ)
- DexScreener/GT ~22:11Z: MrBeast, pool NHCcmv..., age ~109 min (curve created 2026-11-04 20:22:01Z, MigrateV2+CreatePool 4GTN96... in the same slot 465434114, signed by the creator 9dKRhz...), found via GT (gtslow.py) only (not in DS search results): GT reserve ~55.2k, DS liq ~56.1k USD, FDV ~479k, 1h vol ~44.6k (GT) / ~46.3k (DS), h1 22,431 buys / 22,030 sells by 147 buyers / 138 sellers (wash-like). Pattern: whole curve emptied in the creation slot by 7 wallets (100 % of tradable, k30 = 2, dev buy 0.22 %, two 3-signer buy txs) -> rule 1 HIT; migration in creation slot signed by creator -> rule 2 HIT; Rule 11 window 12 buyers 110.77 %, k80 = 5 -> HIT. Same 7-wallet template as ChatGPT 4y4Q / TikTok DMVM / Robinhood GkhL (c213). (bundle.py picked the later MigrateV2 2N3G3K... by 9C4nRv... at +1 slot, known quirk; rule11.py authoritative.)
- Created: 2026-11-04T20:22:01Z, slot 465434114, tx 4XxDw1k18APLLq9sH9yWi9Ys8m4nzZ39muQ2HwqHKHfwpeuhYHAu4RFdA6S7VSFENsC9NuKBqfSQbijfwaKAMmRx; curve 8FEcSTC8RwDziUP3oqZUHH3btF8DMnJ3FpDjtXXdjn38; creator 9dKRhzJnvLNwje8LdCPpwQUBCm4J7U1iv1RtWgoNqe5V
- Rule 1: creation slot 7 buying wallets (creator counted, migration tx and pool excluded), 100.0 % of tradable supply, wallets to reach 30 %: 2; slots 0-2: 7 wallets, 100.0 %. **HIT**
- Rule 2: migration 4GTN96xcJAQBwqbYsMJrqkhvgUvqvwAXYSaMvgcEXfP9SMEEoXtdygFxjZc4EE3WrvjdRZKWsa5ayqxcY6vGQHV7, same slot as creation, creator co-signed. **HIT**
- Rule 11: migration slot 465434114 (+0 slots), window +0..+2: 12 buyers, 110.77 % of tradable supply, wallets to reach 80 %: 5. **HIT**
- Rule hit: **Rule 1, Rule 2, Rule 11**
- Raw: research/raw-20261104/c218/bundle_MrBeast-6Hdd.json, rule11_MrBeast-6Hdd.json, b_*.log, r11log_MrBeast-6Hdd.txt
