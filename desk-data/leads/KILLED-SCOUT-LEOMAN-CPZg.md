# KILLED-SCOUT LEOMAN-CPZg (CPZguakzrJSPZDvyB2BY7wdk25eKFwuwtYxSPYHmpump)
Cycle 211 (16:10 Stockholm, 2026-11-04), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 with fixed c6 locator), measured 2026-11-04T15:11:42Z-2026-11-04T15:12:29Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: CPZguakzrJSPZDvyB2BY7wdk25eKFwuwtYxSPYHmpump
- PumpSwap pool: 4d6z9aPYpX8iVJ7msRirpwLhfVbStcCQY6c8tprEdg2R (https://dexscreener.com/solana/4d6z9aPYpX8iVJ7msRirpwLhfVbStcCQY6c8tprEdg2R)
- DexScreener/GT ~15:11Z: LEOMAN, pool 4d6z9a..., age ~171 min / ~2.9 h (curve created 2026-11-04 12:20:19Z, MigrateV2+CreatePool 3YLXzF... in the same slot 465299670), found via DS (scan2.py) only: DS liq ~36.4k USD (188.5 SOL quote), FDV ~197k, 1h vol ~48.4k, h24 ~387k, DS h1 1,633 buys / 1,600 sells, h1 +43 %. Pattern: whole bonding curve emptied in the creation slot: CreateV2 by creator 9d5Q3M... (5-signer create+buy tx) + two 7-signer multi-wallet buy txs, 18 buying wallets 100 % of tradable, k30 = 2; migration 3YLXzF... in the creation slot co-signed by the creator 9d5Q3M... -> rule 2 hit. Rule 11 window 24 buyers 110.27 %, k80 = 10 -> mechanical k80 <= 5 not hit, noted as concern (rules 1+2 already hard-KILL). (bundle.py picked the later MigrateV2 58gqRr... by 9C4nRv... at +6 slots, known quirk; rule11.py authoritative.)
- Created: 2026-11-04T12:20:19Z, slot 465299670, tx 3XxvF7D3ZPMUq9hu4E3hDKRXwvn9cbgqhVccJSeCrbyaiJY4nrpCfvTaob85AYSLH9x8DE2Z5ZEXFgeQuVYg4igg; curve 7rYdYr9WN7fTbA4zLhx8jRmiKv61Hbp1KWjmFHtPzvmG; creator 9d5Q3Mssv4fLJoAboXzBRDV87p867bFttCYD2nqSSYNB
- Rule 1: creation slot 18 buying wallets (creator counted, migration tx and pool excluded), 100.0 % of tradable supply, wallets to reach 30 %: 2; slots 0-2: 18 wallets, 100.0 %. **HIT**
- Rule 2: migration 3YLXzFSPuWKoYPFm6zEmFqDAc72m3EKWRkv2mKse8DEzx3V32eGFjmdre5mD9K8ABM2XwnJd4HVqLTy1oRHpdNGU, same slot as creation, creator co-signed. **HIT**
- Rule 11: migration slot 465299670 (+0 slots), window +0..+2: 24 buyers, 110.27 % of tradable supply, wallets to reach 80 %: 10. Not hit.
- Rule hit: **Rule 1, Rule 2**
- Raw: research/raw-20261104/c211/bundle_LEOMAN-CPZg.json, rule11_LEOMAN-CPZg.json, b_*.log, r11log_LEOMAN-CPZg.txt
