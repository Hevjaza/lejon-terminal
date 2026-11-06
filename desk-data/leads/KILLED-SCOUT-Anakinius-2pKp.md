# KILLED-SCOUT Anakinius-2pKp (2pKpMwUQXNZeAf93LoomnZSworH3ezFzweCiuvrppump)
Cycle 148 (01:06 Stockholm, 2026-11-02), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 with fixed c6 locator), measured 2026-11-02T00:08:50Z-2026-11-02T00:09:14Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: 2pKpMwUQXNZeAf93LoomnZSworH3ezFzweCiuvrppump
- PumpSwap pool: 9FCA7K7oVCmFDdAjxtoDN4nNnuymskuodSV33LMELu5P (https://dexscreener.com/solana/9FCA7K7oVCmFDdAjxtoDN4nNnuymskuodSV33LMELu5P)
- DexScreener/GT ~00:08Z: Symbol Anakinius. DS liquidity ~41.6-43.7k USD (GT ~42.4k), 1h volume ~286-313k USD (24h ~562k; pair ~73 min old), h1 ~+39 %, FDV ~263-289k USD; GT 1h txs 10733 buys / 2823 sells, 6107 buyers / 1830 sellers; found via DexScreener search (dsretry.py), scan2.py and GT (gtslow.py). Creator 5Y9KnK... (create signer); 3 multi-signer bundle txs (6/7/7 signers) in the creation slot -> 19 wallets bought the whole curve (100 %), 3 wallets reach 30 %; same-slot MigrateV2+CreatePool tx 4DoZsL... co-signed by the creator (bundle.py's locator reported a later no-op MigrateV2 e518Gx... at +4 slots signed by the migration authority 9C4nRv...; the pool was created in 4DoZsL...)
- Created: 2026-11-01T22:54:17Z, slot 464267283, tx 4QcW5XP6XTGgvRSsUro9ZMsUtQnV5ADe5E5Ra22RwPkS9KyUzzJH1jjxZUtJUv3foWHeK6i2GS6Ytowh5v4mAqcG; curve HyknyUvuSsXbmSNSHzAH3RfrVY7EufQED9XXXoyzLnSV; creator 5Y9KnKTNVDom3d9pu7vhhNAJEjGi6Ta49P3CjXfjPTrX
- Rule 1: creation slot 19 buying wallets (creator counted, migration tx and pool excluded), 100.0 % of tradable supply, wallets to reach 30 %: 3; slots 0-2: 19 wallets, 100.0 %. **HIT**
- Rule 2: migration 4DoZsLTvTH2jNtNVv3enSCbDVbjpFqXVioG1LopUztmeJbsBMhnQ5WgigW27TV2mRi7dPsafY8gCeSMjNQT7Rznj, same slot as creation, creator co-signed. **HIT**
- Rule 11: migration slot 464267283 (+0 slots), window +0..+2: 27 buyers, 112.61 % of tradable supply, wallets to reach 80 %: 8. Not hit.
- Rule hit: **Rule 1, Rule 2**
- Raw: research/raw-20261102/c148/bundle_Anakinius-2pKp.json, rule11_Anakinius-2pKp.json, log_Anakinius-2pKp.txt, r11log_Anakinius-2pKp.txt
