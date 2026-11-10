# KILLED-SCOUT PRESIDENT (3LPTanzycRAjguU6VAXE7T2Fd12LePQLpHATXXs9pump)
Cycle 3, bundler pre-check (scout-bundler-rules.md), measured 2026-10-26T21:08:01Z-2026-10-26T21:09:13Z (Stockholm UTC+1). Engagement: research. No lead ID, no RISK file.

- Mint: 3LPTanzycRAjguU6VAXE7T2Fd12LePQLpHATXXs9pump
- PumpSwap pool: 4a4VAe5qmggjqtu2TcWt5pJYq6dXi7H1a5FJxr2KaMhD (https://dexscreener.com/solana/4a4VAe5qmggjqtu2TcWt5pJYq6dXi7H1a5FJxr2KaMhD)
- DexScreener at 2026-10-26T20:31:57Z: age 1408 min, liquidity 39,221 USD, 1h volume 23,235 USD
- Created: 2026-10-25T20:28:26Z, slot 461392969, tx 4sJNJYARiYZcDQUb17CauY6dvPX6odmLxYChifjmyjSBk16uvm5k5h1SFanYtPMz8NRgmXTxDKjZkssboxn7wTtW (https://solscan.io/tx/4sJNJYARiYZcDQUb17CauY6dvPX6odmLxYChifjmyjSBk16uvm5k5h1SFanYtPMz8NRgmXTxDKjZkssboxn7wTtW)
- Bonding curve: HfaKCq6H2ZGud5j8NF5oHLz1wWEoei2nc3Dzu1h1n1WC; curve signatures 4431; first 3 slots: 59 sigs (44 failed), all successful txs decoded via RPC getTransaction
- Creation slot: 2 buying wallets, 33.51 % of tradable supply (793.1M), top-10 33.51 %, top-15 33.51 %, wallets needed for 30 %: 2
- First 2 slots: 2 wallets, 33.51 %; first 3 slots: 2 wallets, 33.51 %
- Rule hit: **Rule 1**
- Why: 2 wallets bought 33.51 % of tradable supply in the creation slot (creator/dev 25.34 % in the create tx + 9qz7cW... 8.17 %). No migration within the first 3 slots (rule 2 not met); exact migration tx not located in the newest 25 curve txs. Note: excluding the dev buy, 1 wallet = 8.17 % (would be PASS).
- Raw: research/raw-20261026/c3/bundle_PRESIDENT.json, c3_bundler_precheck_summary.json, slot0_migrations.json
