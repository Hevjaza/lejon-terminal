# KILLED-SCOUT AIB-EwHV (EwHV6XfuMmBirGSiDVSypVkHcw7jD7Mho1s5xGwjpump)
Cycle 212 (17:12 Stockholm, 2026-11-04), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 with fixed c6 locator), measured 2026-11-04T16:13:51Z-2026-11-04T16:15:44Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: EwHV6XfuMmBirGSiDVSypVkHcw7jD7Mho1s5xGwjpump
- PumpSwap pool: 2F2DVuZeGs2dUmQdAaEHWF6cdwRX4GtLJHLWVoJkyVzW (https://dexscreener.com/solana/2F2DVuZeGs2dUmQdAaEHWF6cdwRX4GtLJHLWVoJkyVzW)
- DexScreener/GT ~16:12Z: AIB, pool 2F2DVu..., age ~45 min (curve created 2026-11-04 15:26:23Z, MigrateV2+CreatePool 4ShPCX... at +556 slots, 15:28:22Z, signed by 9C4nRv..., not creator), found via DS (scan2.py) and GT: DS liq ~30.9k USD, FDV ~132k, 1h vol ~903k, h1 +251 %; GT h1 10,203 buys / 7,463 sells, 3,149 buyers / 2,394 sellers. Pattern: creation slot 465351743: 6 buying wallets 41.01 % of tradable, k30 = 4 (create tx signer 2JxPmU..., curve creator m2r4P6..., dev buy 18.96 %; plus a 3-signer and a 2-signer multi-wallet buy tx) -> rule 1 HIT. Rule 11 BLIND (pool walk did not reach the migration slot). (bundle.py picked MigrateV2 by 9C4nRv... at slot 465352300, +1 vs rule11.py, known quirk.)
- Created: 2026-11-04T15:26:23Z, slot 465351743, tx 4esfX8d8RsP6HgqrNiwjraQfeTfK1XikKZayPfgfYiV6Zm11M8vnHaDjLuUG28nLMtfkQnGLS4eUAjUQMF4yUvij; curve BBeZDX9v8i6iFrD3Ghx3vVvFEZ6ssPDBHnE9WFSUpL2L; creator m2r4P6VtLEeJTAN2qGX3hsUfVem2TS1vxEQaYXrmphR
- Rule 1: creation slot 6 buying wallets (creator counted, migration tx and pool excluded), 41.01 % of tradable supply, wallets to reach 30 %: 4; slots 0-2: 6 wallets, 41.01 %. **HIT**
- Rule 2: migration 4ShPCXdJPnLbNKS8hp9qPiqYKx6dGyBfi252zv4D7JqbB61jDz4FktMmGqByrGjJAjxgRogedp3vogPzyv46QYf8, not same slot, creator not co-signer. Not hit.
- Rule 11: BLIND (migration tx located at slot 465352299, but the pool signature walk did not reach the migration slot; not guessed). Irrelevant to the verdict, rule 1 already kills.
- Rule hit: **Rule 1**
- Raw: research/raw-20261104/c212/bundle_AIB-EwHV.json, rule11_AIB-EwHV.json, b_*.log, r11log_AIB-EwHV.txt
