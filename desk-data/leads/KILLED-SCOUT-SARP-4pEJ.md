# KILLED-SCOUT SARP-4pEJ (4pEJhmzLxk6PyDK4aKCbyBRR1Z8uMn3ZGiSUgXBVpump)
Cycle 219 (00:05 Stockholm, 2026-11-05), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 with fixed c6 locator), measured 2026-11-04T23:06:02Z-2026-11-04T23:06:35Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: 4pEJhmzLxk6PyDK4aKCbyBRR1Z8uMn3ZGiSUgXBVpump
- PumpSwap pool: F13zXfnRzH7zJ23Z29YDxGD2NcDxJGfzWvSqvtbSNxBU (https://dexscreener.com/solana/F13zXfnRzH7zJ23Z29YDxGD2NcDxJGfzWvSqvtbSNxBU)
- DexScreener/GT ~23:05Z: SARP (different mint from SARP 3q48/HynF), pool F13zXf..., age ~455 min (curve created 2026-11-04 15:30:38Z, MigrateV2+CreatePool 2ojHsP... in the same slot 465352934, signed by the creator Hjps6N...), found via GT (gtslow.py) only: GT reserve ~512k USD, FDV ~39.1M, 1h vol ~28.8k, h1 6,827 buys / 113 sells by only 10 buyers / 10 sellers (bot-like). Pattern: creator bought 100 % of tradable in the create tx (k30 = 1) -> rule 1 HIT; migration in creation slot signed by creator -> rule 2 HIT; Rule 11 window 5 buyers 125.01 %, k80 = 1 -> HIT. (bundle.py picked the later MigrateV2 2ez66j... by 9C4nRv... at +3 slots, known quirk; rule11.py authoritative.)
- Created: 2026-11-04T15:30:38Z, slot 465352934, tx 4HJbYsF8rUJykSSzHtk67xRyXrC77Wb6eJkeD8zEESHFJ9BLWZXtLiYs6GSPmcBrBfC716d3sYA9AeFBTjd3988T; curve EiS5BEihmDQoZFrHWMPE8m4EpXMLsPfL5dsA8RGP65ze; creator Hjps6N6UxKzgpBLGrbf3qxGAMxtSFu9jZ9JrkeoEfDBv
- Rule 1: creation slot 1 buying wallets (creator counted, migration tx and pool excluded), 100.0 % of tradable supply, wallets to reach 30 %: 1; slots 0-2: 1 wallets, 100.0 %. **HIT**
- Rule 2: migration 2ojHsP1q9ctTaTK4bnqkcYXxvGEXWyHzFWyp7dJ64nxBGHsPkJgh49y7orvwCWjwckPZU692etaG5p4PRVfXQ5n9, same slot as creation, creator co-signed. **HIT**
- Rule 11: migration slot 465352934 (+0 slots), window +0..+2: 5 buyers, 125.01 % of tradable supply, wallets to reach 80 %: 1. **HIT**
- Rule hit: **Rule 1, Rule 2, Rule 11**
- Raw: research/raw-20261105/c219/bundle_SARP-4pEJ.json, rule11_SARP-4pEJ.json, b_*.log, r11log_SARP-4pEJ.txt
