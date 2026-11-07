# KILLED-SCOUT Alice (7tSMEsYfx2vdPSmnmqBRbFuaPUMmVuiCVsmpFtfLpump)
Cycle 271 (07:0x Stockholm, 2026-11-07), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 with fixed c6 locator), measured 2026-11-07T07:06:05Z-2026-11-07T07:06:17Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: 7tSMEsYfx2vdPSmnmqBRbFuaPUMmVuiCVsmpFtfLpump
- PumpSwap pool: 7tjjmqNrGt1pySMrpKTxVknXMAutgqvXDtzLJBe7SZVE (https://dexscreener.com/solana/7tjjmqNrGt1pySMrpKTxVknXMAutgqvXDtzLJBe7SZVE)
- DexScreener/GT ~07:05Z: Alice, pool 7tjjmqNr..., age ~33 min at scan (curve created 2026-11-07 06:32:51Z, creation slot 466412805, creator EzRXSeYZ...; MigrateV2 3zLpaUAS... in the SAME slot, signer 5Prrtb4b..., creator not co-signer), found via scan2: DS liq ~26.2k, 1h vol ~397k, h1 +197 %, FDV ~112k. Creation slot: 11 wallets bought 100 % of tradable, two 5-signer buy txs (4nPJ/32k2/9JXb/BZJT/GW9k and 9PsR/3J2v/6Eb7/7onQ/Aibf), k30 = 3 -> Rule 1 HIT. Rule 2 not hit (same slot but creator not co-signer). Rule 11: window 16 buyers 109.77 %, k80 = 7 (mechanically not hit) but judgment HIT: two 5-signer BuyV3 bundles bought the whole curve in the creation/migration slot (hard KILL per t39u, same template as c224 CI).
- Created: 2026-11-07T06:32:51Z, slot 466412805, tx 5Wkzro2icgsNJ3P1WfZDypR9MdD4ySYAs3Ldqy8NDNsuALFYpHs1XxdyV3Q2D6X1ejzbRnarMPH1cZ61799FrGFw; curve 6QKxDorEHb52XkCSfe9UazAFfWcqtv6mvSJHGPZ3KMYY; creator EzRXSeYZz8YdvBZupN7rZnW7RyUUmNTjy8L84EgCEAjT
- Rule 1: creation slot 11 buying wallets (creator counted, migration tx and pool excluded), 100.0 % of tradable supply, wallets to reach 30 %: 3; slots 0-2: 11 wallets, 100.0 %. **HIT**
- Rule 2: migration 3zLpaUAS2QtELu4GaPRB8D3zz6u5bgjZ7c1Tytc6naL4PM9H1fMV7qX4Wq2V7yhu8AxtaUfHXzX4Ssjr2qjDjhne, same slot as creation, creator not co-signer. Not hit.
- Rule 11: migration slot 466412805 (+0 slots), window +0..+2: 16 buyers, 109.77 % of tradable supply, wallets to reach 80 %: 7. Not hit mechanically (k80>5).
- Rule hit: **Rule 1, Rule 11 (judgment: two 5-signer BuyV3 = 100 % of curve in creation/migration slot)**
- Raw: research/raw-20261107/c271/bundle_Alice.json, rule11_Alice.json, bun_Alice.log, r11_Alice.log
