# KILLED-SCOUT METEORITE-67RB (67RBmGztx8ciVyWr8yi6R8fwrc3EG86XejYT7mespump)
Cycle 177 (06:08 Stockholm, 2026-11-03), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11), measured 2026-11-03T05:09:33Z-2026-11-03T05:10:04Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: 67RBmGztx8ciVyWr8yi6R8fwrc3EG86XejYT7mespump
- PumpSwap pool: 8qfdKTa5Mub2DxLVyXkAq6c3skV6sdba5WGNChmQRVk4 (https://dexscreener.com/solana/8qfdKTa5Mub2DxLVyXkAq6c3skV6sdba5WGNChmQRVk4)
- Market data: METEORITE, age ~71 min, DS liq ~33.9k, 1h vol ~271.1k, h24 vol ~393.5k, FDV ~179k (DexScreener ~05:08Z)
- Created: 2026-11-03T03:56:44Z, slot 464755280, tx 3hvA5oWtNCG3cULyXEaEKuLJqAnfzCCjpCfQ5Da5Vy2z5rqTH47ZXyLvbxNHEbeTudPixGSGo3ncWJTW2t46gBTt; curve 8KndFyWYsWKFZQXPEAEWKfjj5rMkdFQRVBHwA6LnAjww; curve creator GBdqBdatwPHbvvp1eiJNEKRsVz9YCRDSrgvYrQ786hQj; create signers ['GBdqBdatwPHbvvp1eiJNEKRsVz9YCRDSrgvYrQ786hQj', '67RBmGztx8ciVyWr8yi6R8fwrc3EG86XejYT7mespump']
- Rule 1: creation slot 1 buying wallets (creator counted, migration tx and pool excluded), 84.79 % of tradable supply (top-15 84.79 %), wallets to reach 30 %: 1; slots 0-2: 1 wallets, 84.79 %. **HIT** (the creator/create signer GBdqBd... alone bought 84.79 % of tradable supply = most of the curve in its own create tx)
- Rule 2: migration 4QX1iTwY... at +350 slots (~75 s) signed by 9cY4Li... (not the creator) -> rule 2 not hit
- Rule 11: **HIT (judgment, t39u)**: pre-migration curve concentration: one wallet (creator GBdqBd...) bought 84.79 % of tradable supply of the curve before migration (MUTTAPE precedent); migration window +0..+2 itself 5 buyers 0.3 %
- bundle.py's migration locator picked the later no-op MigrateV2 (+2 slots, migration authority 9C4nRv...) where applicable = known quirk; rule11.py authoritative; verdict unaffected.
- Rule hit: **Rule 1, Rule 11 (pre-migration curve concentration, hard per t39u)**
- Raw: research/raw-20261103/c177/bundle_METEORITE.json, rule11_METEORITE.json, b_METEORITE.log, r11log_METEORITE.txt
