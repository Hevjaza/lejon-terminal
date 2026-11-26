# KILLED-SCOUT XTO-A7rd (A7rdP4KehZA1jjgYQrtKfN7AzG5zPh2z2ECXJzv4pump)
Cycle 155 (08:07 Stockholm, 2026-11-02), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 with fixed c6 locator), measured 2026-11-02T07:09:21Z-2026-11-02T07:09:48Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: A7rdP4KehZA1jjgYQrtKfN7AzG5zPh2z2ECXJzv4pump
- PumpSwap pool: 17kLCdzVVfJVUeg5D5qs4SQqN5pEhV5xhDhX27avAFh (https://dexscreener.com/solana/17kLCdzVVfJVUeg5D5qs4SQqN5pEhV5xhDhX27avAFh)
- DexScreener/GT ~07:09Z: Symbol XTO. Not a DS candidate; GT (gtslow.py) pumpswap pool liquidity ~528k USD, FDV ~42.1M USD, 1h volume ~17.8k USD (24h ~1.76M), pool ~677 min old; GT 1h 2848 buys / 994 sells, 1906 buyers / 644 sellers (bot-style churn, same pattern as earlier XTO/AODF clones). Creator GwuwaR... bought the ENTIRE bonding curve (793.1M = 100 % of tradable) in the create tx and the MigrateV2 tx 4L7VYA... in the same creation slot 464216158 was co-signed by the creator (bundle.py locator picked later MigrateV2 JSBXMa... +2 slots signed by migration authority 9C4nRv..., known quirk; rule11.py authoritative)
- Created: 2026-11-01T19:51:30Z, slot 464216158, tx 2hodd9JFDdMTknrXDkiQpZkdxF2Ej2nU4tRLacySUbxQJEAB3P1wfDx88PBWebpcmHGoJmXcck4hHSH5gkGoGTVw; curve BFe7XHkg3jkkb9tTVDNynq7DwfKooKFGrfD8eSzXBBQX; creator GwuwaRuta4xkqCy6qFpawkNV7oG5Tph9dig5WzUZVAM6
- Rule 1: creation slot 1 buying wallets (creator counted, migration tx and pool excluded), 100.0 % of tradable supply, wallets to reach 30 %: 1; slots 0-2: 1 wallets, 100.0 %. **HIT**
- Rule 2: migration 4L7VYATvxWfpU21CgY9Bmmrev99J9tASCD4mq8ggTkVmRr9KPnZtcSsarqA6gSR12w5Cn8RHwoU4xF4t4o2A3Z1, same slot as creation, creator co-signed. **HIT**
- Rule 11: migration slot 464216158 (+0 slots), window +0..+2: 3 buyers, 125.65 % of tradable supply, wallets to reach 80 %: 1. **HIT**
- Rule hit: **Rule 1, Rule 2, Rule 11**
- Raw: research/raw-20261102/c155/bundle_XTO-A7rd.json, rule11_XTO-A7rd.json, log_XTO-A7rd.txt, r11log_XTO-A7rd.txt
