# KILLED-SCOUT PEACE-BngA (BngAfLZxaWN2QvpFhRbUHydYGr8zA7YTSA178G8Epump)
Cycle 153 (06:00 Stockholm, 2026-11-02), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 with fixed c6 locator), measured 2026-11-02T05:02:33Z-2026-11-02T05:04:48Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: BngAfLZxaWN2QvpFhRbUHydYGr8zA7YTSA178G8Epump
- PumpSwap pool: B9kecYVZxSVvy56uSSxfiyt6GD7A4w7WEPkB9tNYq7sZ (https://dexscreener.com/solana/B9kecYVZxSVvy56uSSxfiyt6GD7A4w7WEPkB9tNYq7sZ)
- DexScreener/GT ~05:01Z: Symbol PEACE. DS pumpswap pool liquidity ~40.2k USD (GT ~41.1k), FDV ~222-250k USD, 1h volume ~1.0-1.08M USD, h1 +397 %, pool ~64 min old; GT 1h 14283 buys / 11165 sells, 4386 buyers / 3479 sellers. Create signer 2griik... dev buy 8.36 % of tradable; creation slot 464349218: 6 wallets 28.76 % (just under 30 %), slots 0-2: 8 wallets 31.08 % (6 wallets reach 30 %) -> rule 1 hit via the slots 0-2 window. Migration (rule11.py) at +3149 slots signed by EshALR... (not creator). Rule 11 pool walk BLIND (not needed, rule 1 kills). bundle.py's locator did not find a migration in the newest 25 curve txs (known quirk; verdict unaffected)
- Created: 2026-11-02T03:46:48Z, slot 464349218, tx 4y8JW4u2QYN8CEw4hh39BH32gbuYbPrBKTAz19TCJgQHqVw3YRRdn3YCA61LrBtQEgDnY589Eh7UWf3vHS1iTkYS; curve 47Q63jHAqDovyXHhB2aHxpCfKerYm4H4GJkjQpRbm48c; creator HqK2dAt9fQnRaV9Qh7hpcy9D4FGriTN9XnkZp77iKZYa
- Rule 1: creation slot 6 buying wallets (creator counted, migration tx and pool excluded), 28.76 % of tradable supply, wallets to reach 30 %: None; slots 0-2: 8 wallets, 31.08 %. **HIT**
- Rule 2: migration 5C3j8w1K1J3fh88K2N4jaEQ22DdznNojGg5PRzKPoCTX6pB9KHQYohaREBw2oFHGtcpz1wMoKXDADyLCBQhZukT, not same slot, creator not co-signer. Not hit.
- Rule 11: BLIND (migration tx located at slot 464352367, but the pool signature walk did not reach the migration slot; not guessed). Irrelevant to the verdict, rule 1 already kills.
- Rule hit: **Rule 1**
- Raw: research/raw-20261102/c153/bundle_PEACE-BngA.json, rule11_PEACE-BngA.json, log_PEACE-BngA.txt, r11log_PEACE-BngA.txt
