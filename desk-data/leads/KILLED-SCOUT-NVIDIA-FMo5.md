# KILLED-SCOUT NVIDIA-FMo5 (FMo5TRkMan9AUjDZGNEB7eMR6EXwMZgvTNpTtFELpump)
Cycle 180 (09:05 Stockholm, 2026-11-03), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11), measured 2026-11-03T08:05:46Z-2026-11-03T08:06:12Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: FMo5TRkMan9AUjDZGNEB7eMR6EXwMZgvTNpTtFELpump
- PumpSwap pool: 45BQDDwDdsqCWFWjXXwKUisP4ytmatgsNn5q6v8rUjZx (https://dexscreener.com/solana/45BQDDwDdsqCWFWjXXwKUisP4ytmatgsNn5q6v8rUjZx)
- Market data: NVIDIA, GT reserve ~44.3k, 1h vol ~87.5k, h24 ~102.0k, FDV ~316k, age ~70 min (GeckoTerminal ~08:05Z)
- Created: 2026-11-03T06:55:25Z, slot 464805499, tx 32hM4jcwrLhUigeJTgJe2uuxsKvYx4YYLyGS1FnVVksqYPuGXim9QM6zkAYGB7E5cSzmGafffnawcZKAVgt7eugS; curve H5Xw6DcPaA4WAFvNk6Y1MBYCvpP7taZEBBkLDAHdq4QK; curve creator EZbp5WYC3rGxL7gChpCBvzKFNQCBY7JBKFUgGr4YPpE5; create signers ['EZbp5WYC3rGxL7gChpCBvzKFNQCBY7JBKFUgGr4YPpE5', 'FMo5TRkMan9AUjDZGNEB7eMR6EXwMZgvTNpTtFELpump']
- Rule 1: creation slot 7 buying wallets (creator counted, migration tx and pool excluded), 100.0 % of tradable supply (top-15 100.0 %), wallets to reach 30 %: 2; slots 0-2: 7 wallets, 100.0 %. 2 multi-signer buy txs in slot 0. **HIT**
- Rule 2: migration MigrateV2+CreatePool 4dJ4sEZo... in the creation slot (+0 slots) signed by the creator EZbp5W... -> **HIT** (coordinated creation-slot buys incl. 2 multi-signer buy txs + same-slot creator migration)
- Rule 11: window +0..+2: 20 buyers, 110.86 % of tradable, wallets to reach 80 %: 5 -> **HIT**
- bundle.py's migration locator picked the later no-op MigrateV2 (+2 slots, migration authority 9C4nRv...) = known quirk; rule11.py authoritative; verdict unaffected.
- Rule hit: **Rule 1, Rule 2, Rule 11**
- Raw: research/raw-20261103/c180/bundle_NVIDIA.json, rule11_NVIDIA.json, b_NVIDIA.log, r11log_NVIDIA.txt
