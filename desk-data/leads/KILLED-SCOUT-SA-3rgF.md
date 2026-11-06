# KILLED-SCOUT SA-3rgF (3rgFUpCG4Vs2twJordBqLgUtuzdr7yckJNP33fQypump)
Cycle 194 (23:08 Stockholm, 2026-11-03), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 with fixed c6 locator), measured 2026-11-03T22:08:57Z-2026-11-03T22:09:26Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: 3rgFUpCG4Vs2twJordBqLgUtuzdr7yckJNP33fQypump
- PumpSwap pool: 4kM4wu8NA28qqay9GnMuNknzXVfefqPYH3cZySE1JLwv (https://dexscreener.com/solana/4kM4wu8NA28qqay9GnMuNknzXVfefqPYH3cZySE1JLwv)
- DexScreener/GT ~22:08Z: SA, pool 4kM4wu..., age ~262 min (pool created 2026-11-03 17:46:43Z), DS liq ~61.2k, FDV ~559k, 1h vol ~27.6k, h24 vol ~813k. Pattern: creator 9jcRnH... (dev buy 0.57 %) plus 18 other wallets bought 100 % of tradable supply in the creation slot (k30 = 3, top 3 39.44 %) via multi-wallet buy txs (6/7/7/2 signers); MigrateV2 23inmd... in the creation slot co-signed by the creator and 8HB7wU...; Rule 11 window 25 buyers 110.53 %, k80 = 8 (not counted strictly). bundle.py picked the later no-op MigrateV2 3VhRPc... (9C4nRv..., +2 slots) = known quirk; rule11.py authoritative.
- Created: 2026-11-03T17:46:43Z, slot 464987835, tx 2ZLAZgNun2nskXTVmK8ow2eMLGyRdzuWBUqfk7xG2wuzAjdJMfVQRS6Bz2qX4F18oFxwhegQ66gXt21K755WtMXj; curve AQNi7s5RP9Pz9PG9mt4H1iKTvcsNM5yBKY9521D6Qspv; creator 9jcRnHezo8HXgPAU19MnYj5iZJ8gKZQZkmwpHwuDzVEZ
- Rule 1: creation slot 19 buying wallets (creator counted, migration tx and pool excluded), 100.0 % of tradable supply, wallets to reach 30 %: 3; slots 0-2: 19 wallets, 100.0 %. **HIT**
- Rule 2: migration 23inmdoPmQntPtFSnJouv6CoqZYGtaFDuY2YMDd31z68NkCqBCkw6K1XbkxpxK5SAySYCZS9VcxEbYJhdBJDA9Rq, same slot as creation, creator co-signed. **HIT**
- Rule 11: migration slot 464987835 (+0 slots), window +0..+2: 25 buyers, 110.53 % of tradable supply, wallets to reach 80 %: 8. Not hit.
- Rule hit: **Rule 1, Rule 2**
- Raw: research/raw-20261103/c194/bundle_SA-3rgF.json, rule11_SA-3rgF.json, b_*.log, r11log_SA-3rgF.txt
