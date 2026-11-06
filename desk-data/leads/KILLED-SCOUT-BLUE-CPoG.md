# KILLED-SCOUT BLUE-CPoG (CPoGSmcjprCvzA2MFYLJMpQkGjmgVzKg4RVwMdrzpump)
Cycle 127 (04:00 Stockholm), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 with fixed c6 locator), measured 2026-11-01T03:02:10Z-2026-11-01T03:04:42Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: CPoGSmcjprCvzA2MFYLJMpQkGjmgVzKg4RVwMdrzpump
- PumpSwap pool: BzomHwB33RGwuyWdm8sQFi3ZDNaUWnpmHRaiQaLQNZiA (https://dexscreener.com/solana/BzomHwB33RGwuyWdm8sQFi3ZDNaUWnpmHRaiQaLQNZiA)
- DexScreener ~03:01Z: liquidity ~67.9k USD (GT ~69.6k), 1h volume ~1.31M USD (GT ~1.49M; h1 price +1010 %), age ~77 min, GT h1 txns 17,911 buys vs 13,275 sells, FDV ~606k USD; found in DS dsretry/scan2 and GT pumpswap lists. Migration ~505 slots after creation; Rule 11 pool walk did not reach the migration slot (BLIND)
- Created: 2026-11-01T01:42:42Z, slot 463911085, tx 31yZE4mqtAj64yxu6tZ2HUspMmFoXcytQH9b7PijMBqbfe2W8kLcXqBRTWdC4XmGXh24NRt62cn1z1kThuKggsKi; curve ETZY7DAHETwFno5MFteZ8fAXLrRrhjcsSvKLTAn5y2jS; creator BUtVEDrdgGhP5evYd7RUY4tzWP8koL4AVDjrxdjYHHWS
- Rule 1: creation slot 2 buying wallets (creator counted, migration tx and pool excluded), 32.75 % of tradable supply, wallets to reach 30 %: 2; slots 0-2: 6 wallets, 40.82 %. **HIT**
- Rule 2: migration 5MrvFrkAETzEAEtRRhBxVo8iixcQgDYz12hhDDReCRt95gcH7CFtRWMPkRw2CzsFBRMFUst4R8N1PaB1KVVQ6pSG, not same slot, creator not co-signer. Not hit.
- Rule 11: BLIND (migration tx located at slot 463911590, but the pool signature walk did not reach the migration slot; not guessed). Irrelevant to the verdict, rule 1 already kills.
- Rule hit: **Rule 1**
- Raw: research/raw-20261101/c127/bundle_BLUE-CPoG.json, rule11_BLUE-CPoG.json, log_BLUE-CPoG.txt, r11log_BLUE-CPoG.txt
