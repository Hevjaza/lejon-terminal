# KILLED-SCOUT debtdog (4gyubJ7sqYDySUDmVFEfSdvvC43F1eWLUXgEHDDWpump)
Cycle 278 (14:1x Stockholm, 2026-11-07), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 with fixed c6 locator), measured 2026-11-07T14:10:56Z-2026-11-07T14:12:20Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: `4gyubJ7sqYDySUDmVFEfSdvvC43F1eWLUXgEHDDWpump`
- PumpSwap pool: `FJSMvMR5bysnMZUkQgjadYFk4fpR3VRPCXbFbEaFXZQ1` (https://dexscreener.com/solana/FJSMvMR5bysnMZUkQgjadYFk4fpR3VRPCXbFbEaFXZQ1)
- DexScreener ~14:10Z: debtdog, pool FJSMvMR5..., age ~52 min at scan (curve created 2026-11-07T12:59:31Z, creator DchVdUAosPG1fqY9rX6W6u69CPcQv5vFz4fWmamGs9o4; MigrateV2 2026-11-07T13:18:46Z, +5357 slots, creator not co-signer), found via scan2: DS liq ~29.9k, 1h vol ~408k, h1 +266 %, fdv ~138k. Dev buy in create tx 19.33 % of tradable (wallet 7ufmve7Z…, not the curve_creator pubkey itself).
- Created: 2026-11-07T12:59:31Z, slot 466521098, tx `ziU6DBfkHhMQQzSaMiN2m4mqmH2hqWPb843CmEmMyTFYZcx81qAaBUpBaBSUG9pTBza7kk2RmF7jd9paKjWasDL`; curve `36XUEAe6Z3DUUAKmZ7MA4FDqXWuxg25vodjxuaLYe2fL`; creator `DchVdUAosPG1fqY9rX6W6u69CPcQv5vFz4fWmamGs9o4`
- Rule 1: creation slot 8 buying wallets (creator counted, migration tx and pool excluded), 46.21 % of tradable supply, wallets to reach 30 %: 3; slots 0-2: 8 wallets, 46.21 %. **HIT** (k30=3 ≤ 15 and pct ≥ 30).
- Rule 2: migration `T6rScAW1ZWQCPAzahMMY99zWRBegyUNudBR7Hg5Ff4riYmEDzWztrL4DpwNfJVhuxB3radiCMSNUGFw72mdHvEd`, +5357 slots, creator not co-signer. Not hit.
- Rule 11: migration slot 466526455 (+5357 slots), window +0..+2: 10 buyers, 3.16 % of tradable supply, wallets to reach 80 %: None. Not hit mechanically (k80 null / >5). No Rule 11 judgment (only one 2-signer multiwallet buy in creation slot; migration window 3.16 % — not a critical-mass graduation bundle).
- Soft flag: n/a (hard KILL).
- Verdict: **KILLED in SCOUT** (Rule 1). No RISK, no LEAD, no ticket, no paper buy.
- Saved: leads/KILLED-SCOUT-debtdog-4gyu.md; research/raw-20261107/c278/bundle_debtdog.json, rule11_debtdog.json.
