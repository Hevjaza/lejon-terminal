# KILLED-SCOUT debtdog (FkCsLU7TVDFBex8oubEau2iq1wdLQiagjdBMqv8jpump)
Cycle 279 (16:0x Stockholm, 2026-11-07), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 with fixed c6 locator), measured 2026-11-07T15:10:39Z-2026-11-07T15:10:59Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: FkCsLU7TVDFBex8oubEau2iq1wdLQiagjdBMqv8jpump
- PumpSwap pool: ovdgA3NcfR7zVPc2xszo72VPPy2rSDPhAZHVRJhvcTf (https://dexscreener.com/solana/ovdgA3NcfR7zVPc2xszo72VPPy2rSDPhAZHVRJhvcTf)
- DexScreener/GT ~15:1xZ: debtdog, pool ovdgA3Nc..., age ~36 min at scan (curve created 2026-11-07 14:33:38Z, creator SmoCQPSy...; MigrateV2+CreatePool same slot 466547451 per rule11, creator not co-signer), found via scan2: DS liq ~26.1k, 1h vol ~248k, pc1 +200 %. Creation slot: 11 buying wallets 100 % of tradable (ex-pool), k30 = 3; two 5-signer multiwallet buys in creation slot.
- Created: 2026-11-07T14:33:38Z, slot 466547451, tx 5mmNkJTHYwoyJLn8YMe5cANDsK9obG6vcccK6tSWjVKPBvrwGMc5W1HgUwHRdpQJV5H4MiTbz4zw1vr8J4jbpDe2; curve Ch9u7wm31sg3n1DdFeK8kRSceYMweiqv9MXbLeLbfmUa; creator SmoCQPSyHfGx9qnmvtDqg3TNz93RPogq7bkDFEp7QiQ
- Rule 1: creation slot 11 buying wallets (creator counted, migration tx and pool excluded), 100.0 % of tradable supply, wallets to reach 30 %: 3; slots 0-2: 11 wallets, 100.0 %. **HIT**
- Rule 2: migration 59VvXecLYiHvuu5BPHy2KD8tsP4QFLZ3U9GkcEC29JtijNKUy9DXcoyo8J2T3jUzoTP34Jqr2W1fgbTY8RoMUpfL, same slot as creation, creator not co-signer. Not hit.
- Rule 11: migration slot 466547451 (+0 slots), window +0..+2: 16 buyers, 108.34 % of tradable supply, wallets to reach 80 %: 7. Not hit mechanically (k80>5 or null). Judgment (t39u hard): two 5-signer Buy multiwallet txs in the creation/migration slot bought large share of the curve.
- Rule hit: **Rule 1, Rule 11**
- Raw: research/raw-20261107/c279/bundle_debtdog.json, rule11_debtdog.json, bun_debtdog.log, r11_debtdog.log
