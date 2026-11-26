# KILLED-SCOUT UODF-oJkW (oJkWFSotDuP2d9M4hhv9XupCsqSnzjMkRi6h9sWpump)
Cycle 156 (09:03 Stockholm, 2026-11-02), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 with fixed c6 locator), measured 2026-11-02T08:05:13Z-2026-11-02T08:05:38Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: oJkWFSotDuP2d9M4hhv9XupCsqSnzjMkRi6h9sWpump
- PumpSwap pool: FkCmPdj3ioqPJbCMF66WQFL6uuF6cRFGLv6DdL8NjFRS (https://dexscreener.com/solana/FkCmPdj3ioqPJbCMF66WQFL6uuF6cRFGLv6DdL8NjFRS)
- DexScreener/GT ~08:04Z: Symbol UODF. Not a DS candidate; GT (gtslow.py) pumpswap pool liquidity ~1.06M USD, FDV ~168M USD, 1h volume ~6.2k USD (24h ~598k), pool ~1103 min old; GT 1h 2204 buys / 67 sells, 1921 buyers / 2 sellers (bot-style churn, same pattern as earlier XTO/UODF/AODF clones). Creator 5W5dZF... bought the ENTIRE bonding curve (793.1M = 100 % of tradable) in the create tx and MigrateV2 4cKHqZ2M... in the same creation slot 464112549 was co-signed by the creator (bundle.py locator picked later MigrateV2 2Ts67M... +3 slots, known quirk; rule11.py authoritative)
- Created: 2026-11-01T13:41:18Z, slot 464112549, tx 4qjMbw1RxgjozXKo1ctoamXFFGq4xrYdH6qPLsvifEPEGdV3vhro8c4m2LYiuyxAbh8NLThsUzx9HMkJ9XkPyxk8; curve BhbjFhPcHE7bwPDsJnFW3c1epJUJZiXFCTCkiQw7rF2r; creator 5W5dZFqkwSLu2uEp1nJCJ3Zgpm4ht1ZRW3mpNGALFv1
- Rule 1: creation slot 1 buying wallets (creator counted, migration tx and pool excluded), 100.0 % of tradable supply, wallets to reach 30 %: 1; slots 0-2: 1 wallets, 100.0 %. **HIT**
- Rule 2: migration 4cKHqZ2MXeXFpdkPKyytMSPfStniCcJRPoRBFHyYMbnVszPeHAeSRXKA4L1JHooba1BSaL23Uj5LULLFErC5Luyo, same slot as creation, creator co-signed. **HIT**
- Rule 11: migration slot 464112549 (+0 slots), window +0..+2: 4 buyers, 125.65 % of tradable supply, wallets to reach 80 %: 1. **HIT**
- Rule hit: **Rule 1, Rule 2, Rule 11**
- Raw: research/raw-20261102/c156/bundle_UODF-oJkW.json, rule11_UODF-oJkW.json, log_UODF-oJkW.txt, r11log_UODF-oJkW.txt
