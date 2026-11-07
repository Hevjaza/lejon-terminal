# KILLED-SCOUT SCAMCHI (FhtLRwmMfuZAghT8HQ3hhvFYBV3Cw7duGyvjnU7Apump)
Cycle 267 (04:0x Stockholm, 2026-11-07), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 with fixed c6 locator), measured 2026-11-07T03:02:40Z-2026-11-07T03:03:10Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: FhtLRwmMfuZAghT8HQ3hhvFYBV3Cw7duGyvjnU7Apump
- PumpSwap pool: 2sxSUbpjRXfYLBdqDyCmfi7RetJGdVufcP6zRnt6UrdY (https://dexscreener.com/solana/2sxSUbpjRXfYLBdqDyCmfi7RetJGdVufcP6zRnt6UrdY)
- DexScreener/GT ~03:0xZ: SCAMCHI, pool 2sxSUbpj..., age ~33 min at scan (curve created 2026-11-07 02:28:59Z, creation slot 466344433, creator J6YWvR...; migrated in the SAME slot), found via scan2 (dsretry 0 / gtslow 0 new): DS liq ~25.0k, 1h vol ~248k, h1 +180 %, FDV ~107k. Creation slot: CreateV2 + multiwallet Buys (two 5-signer Buy txs) -> r1 (ex-pool) 11 wallets 100 % of tradable, k30 = 3 -> Rule 1 HIT. Authoritative MigrateV2/CreatePool 5h8guJ... same slot, creator J6YWvR... NOT co-signer (fee-payer EJ8yBt...) -> Rule 2 not hit. Rule 11: window 18 buyers 104.13 %, k80 = 8 (mechanical cap 5 not hit); same-slot multiwallet Buy pattern (5+5 signers) with top10 97.81 % of tradable in migration window -> Rule 11 judgment HIT (hard KILL per t39u). bundle.py locator picked a later no-op Migrate by 9C4nRv... (+2 slots, known quirk); rule11.py authoritative.
- Created: 2026-11-07T02:28:59Z, slot 466344433, tx 2PanjE7TbgNwbELp1Wa3BNRa3413YWYA4oKcDFs4KeHqaXJpNzkj6Cd2qtJFSY8zuQPpg21XijusLa4KrXdzMDYV; curve 9L15nHN3ivkVeUzaqn6bsRCLE14yzHwdK3e7TtbQEo2G; creator J6YWvRWDkeCM9ivKeYZzMRxQZwaoE6BiSdR9m5fYq4dB
- Rule 1: creation slot 11 buying wallets (creator counted, migration tx and pool excluded), 100.0 % of tradable supply, wallets to reach 30 %: 3; slots 0-2: 11 wallets, 100.0 %. **HIT**
- Rule 2: migration 5h8guJmwF6YjftHHVjHf8MRZ82penNkmwkmdj48k7cNVCME7sYEhTGL16ergRuBFsyAfeUet8JT1YRhSCRaMr3SH, same slot as creation, creator not co-signer. Not hit.
- Rule 11: migration slot 466344433 (+0 slots), window +0..+2: 18 buyers, 104.13 % of tradable supply, wallets to reach 80 %: 8. Not hit mechanically (k80>5).
- Rule hit: **Rule 1, Rule 11 (judgment: same-slot 5+5-signer Buy multiwallet = top10 97.81 % in migration window)**
- Raw: research/raw-20261107/c267/bundle_SCAMCHI.json, rule11_SCAMCHI.json, bun_SCAMCHI.log, r11_SCAMCHI.log
