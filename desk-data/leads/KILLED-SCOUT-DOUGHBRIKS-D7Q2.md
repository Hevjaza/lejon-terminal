# KILLED-SCOUT DOUGHBRIKS-D7Q2 (D7Q2ApyCUfAm9Vay3wC2g1tDBtrKdomYCLdiSPaNpump)
Cycle 118 (19:12 Stockholm), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 with fixed c6 locator), measured 2026-10-31T18:11:55Z-2026-10-31T18:14:39Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: D7Q2ApyCUfAm9Vay3wC2g1tDBtrKdomYCLdiSPaNpump
- PumpSwap pool: 3JRZdCY3BAdFwdzU5JB7EdP6G624mVYDNoScf2y8MmG9 (https://dexscreener.com/solana/3JRZdCY3BAdFwdzU5JB7EdP6G624mVYDNoScf2y8MmG9)
- DexScreener ~18:11Z (tokens endpoint): liquidity 45265 USD, 1h volume 87662 USD, age ~103 min
- Created: 2026-10-31T16:28:55Z, slot 463755917, tx AW5M8eqft9mS1MWyZdqwLQJiUnHhodRMgNBuwMi3HX8fCcp7NiTA7wGjbnTwuB8MG6su1Lm3t14rDkMK7TsGkfj; curve 61osVtVBfXXVEx4LPqFDjf9E2hDH3GMJyGnZVsuJerfZ; creator BDSATBHuKsPRPweN484jZGE9PwevLinxWPDgBTmkkwVL
- Rule 1: creation slot 4 buying wallets (creator counted, migration tx and pool excluded), 101.3 % of tradable supply, wallets to reach 30 %: 1; slots 0-2: 4 wallets, 101.3 %. **HIT**
- Rule 2: migration 62rTYoPmfAStUj7WLJgwaQ14R33mZott2xGxdihDsmh1jqSkE5UaYWqSkkUfgmY7S2TQKo6zPS4vyxSbgzactTkZ, same slot as creation, creator not co-signer. Not hit.
- Rule 11: BLIND (migration tx located at slot 463755917, but the pool signature walk did not reach the migration slot; not guessed). Irrelevant to the verdict, rule 1 already kills.
- Rule hit: **Rule 1**
- Raw: research/raw-20261031/c118/bundle_DOUGHBRIKS-D7Q2.json, rule11_DOUGHBRIKS-D7Q2.json, log_DOUGHBRIKS-D7Q2.txt, r11log_DOUGHBRIKS-D7Q2.txt
- Note (c118): creation-slot dev buy by create signer DqeVuNmy... = 794.1M tokens (~100 % of tradable supply, 1 wallet reaches 30 %); 4 buying wallets in slots 0-2 (5 before excluding the migration tx). Two MigrateV2-tagged txs in the early window: 62rTYo... in the creation slot signed by the create signer DqeVuNmy... (curve creator field BDSATBHu... differs, so the script's rule 2 "creator co-signed" test reads not hit) and 5Eev41... at +2 slots signed by 9C4nRv... (the common migrator). Rule 2 is moot: rule 1 alone is a HARD KILL. Source: GeckoTerminal trending 1h via WebFetch (not in DexScreener search results this cycle); GT ~18:10Z liq ~43.7k USD, 1h vol ~87.9k USD.
