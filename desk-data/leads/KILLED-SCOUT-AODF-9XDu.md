# KILLED-SCOUT AODF-9XDu (9XDuPo32gHEPNyRnuM8sdUeFh7p9VoreihoCME7Bpump)
Cycle 149 (02:00 Stockholm, 2026-11-02), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 with fixed c6 locator), measured 2026-11-02T01:02:38Z-2026-11-02T01:03:45Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: 9XDuPo32gHEPNyRnuM8sdUeFh7p9VoreihoCME7Bpump
- PumpSwap pool: 3dCL5paRBuoxqFeWPqupFr1nnQUrC3bxYkkFFXJTixv9 (https://dexscreener.com/solana/3dCL5paRBuoxqFeWPqupFr1nnQUrC3bxYkkFFXJTixv9)
- DexScreener/GT ~01:02Z: Symbol AODF. Not in DexScreener scans; GT (gtslow.py) pumpswap pool liquidity ~2.87M USD, FDV ~1.25B USD, 1h volume ~22.0k USD (24h ~667k), pool ~700 min old; GT 1h txs 3694 buys / 65 sells but only 55 buyers / 51 sellers (bot-style churn). Creator 8kyvQ7... (create signer) bought the ENTIRE bonding curve (793.1M = 100 % of tradable supply) in the create tx, and the MigrateV2 tx 2JZaZ3... in the same creation slot 464107201 was signed by the creator (rule11.py decode; bundle.py's locator reported a later MigrateV2 5Sjx7Q... at +4 slots signed by the migration authority 9C4nRv..., known quirk)
- Created: 2026-11-01T13:22:14Z, slot 464107201, tx 3hQ5uNGb2njHNPd7wDCq8JHweVMzpGprdbSLdZzPugLyTyiPt4deaJT8UggvQfVBzkJdUwksxbuwZsaTKJgELi97; curve 5DjyEYSJ9THdc8wvy9BZH9ugmadDe6A5Qekmzf8kDrKv; creator 8kyvQ7dzp5kJCUf38ZzpXPg4xTuiWYAEoLQmbS4oqo25
- Rule 1: creation slot 1 buying wallets (creator counted, migration tx and pool excluded), 100.0 % of tradable supply, wallets to reach 30 %: 1; slots 0-2: 1 wallets, 100.0 %. **HIT**
- Rule 2: migration 2JZaZ3P7xptC1qetJcpWZP1ALHaApqyyCNJAjTkeaDjxFe2BZzHxAWRxnB8a66V9KrLFVbvnTwt8zWU5s2o6nQsX, same slot as creation, creator co-signed. **HIT**
- Rule 11: migration slot 464107201 (+0 slots), window +0..+2: 5 buyers, 125.87 % of tradable supply, wallets to reach 80 %: 1. **HIT**
- Rule hit: **Rule 1, Rule 2, Rule 11**
- Raw: research/raw-20261102/c149/bundle_AODF-9XDu.json, rule11_AODF-9XDu.json, log_AODF-9XDu.txt, r11log_AODF-9XDu.txt
