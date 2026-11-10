# KILLED-SCOUT AAPL-5Afz (5Afz2mwDXjasvHXZHTT8anNxpec2QYdCiHHhubAWpump)
Cycle 100 (01:05 Stockholm), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 with fixed c6 locator), measured 2026-10-31T00:09:07Z-2026-10-31T00:09:24Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: 5Afz2mwDXjasvHXZHTT8anNxpec2QYdCiHHhubAWpump
- PumpSwap pool: 31bUMZx7Y9N9G2iQNvYNvzbSova6ft7LrAKyeRY1V4HX (https://dexscreener.com/solana/31bUMZx7Y9N9G2iQNvYNvzbSova6ft7LrAKyeRY1V4HX)
- DexScreener ~00:08Z: liquidity ~38-40k USD, 1h volume ~118-133k USD (pair ~31 min old)
- Created: 2026-10-30T23:38:26Z, slot 463472867, tx 2A3xqL2zWgbqa5ZM5QYfkStWJYxPVVemJDgV9v4MWXEo8BdXMBfX4EDWEsVRsz3JHZFZaLs6tXCpff4JLXp92uHB; curve CMv8NWW2UZkbuoPCS1nodB4YZMtkXt86gcadGNKhJ7gw; creator E8NBpd46ByjimsHCmVkZwhMg4D4jubbKLp8tykGayXuW
- Rule 1: creation slot 18 buying wallets (creator counted, migration tx and pool excluded), 100.0 % of tradable supply, wallets to reach 30 %: 4; slots 0-2: 18 wallets, 100.0 %. **HIT**
- Rule 2: migration 587GnoLQTk1x2k6AuBLwAtrdBi5SGktFGboDq9NHGzkzHcQ9VmtoqrA42QeCrb9wa4nDyvweQzP2GiqCHKqKnXmn, same slot as creation, creator co-signed. **HIT**
- Rule 11: migration slot 463472867 (+0 slots), window +0..+2: 24 buyers, 113.47 % of tradable supply, wallets to reach 80 %: 10. Not hit.
- Rule hit: **Rule 1, Rule 2**
- Raw: research/raw-20261031/c100/bundle_AAPL-5Afz.json, rule11_AAPL-5Afz.json, log_AAPL-5Afz.txt, r11log_AAPL-5Afz.txt
- Data note: bundle.py places a second migration tx (4Nj3Jr...) at create+2 slots not co-signed vs rule11.py same-slot tx 587Gno... signed by creator E8NB... (known locator discrepancy); slot 0 has multi-wallet buy txs with 10 and 7 signers (coordinated). Rule 1 kills on its own.
