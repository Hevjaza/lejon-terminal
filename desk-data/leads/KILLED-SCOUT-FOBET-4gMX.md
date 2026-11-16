# KILLED-SCOUT FOBET-4gMX (4gMXHewBS7B4qbUuNw9LLeq1DjBCuuZy3B76VJq6pump)
Cycle 174 (03:05 Stockholm, 2026-11-03), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11), measured 2026-11-03T02:08:19Z-2026-11-03T02:10:36Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: 4gMXHewBS7B4qbUuNw9LLeq1DjBCuuZy3B76VJq6pump
- PumpSwap pool: 9oKbruCw9ot3yUMNPirvMMAkuzvpKqCcTAt8YzE3gs14 (https://dexscreener.com/solana/9oKbruCw9ot3yUMNPirvMMAkuzvpKqCcTAt8YzE3gs14)
- DexScreener/GT ~02:07Z: FOBET, age ~745 min, DS liq ~42.9k, 1h vol ~0.5k, h24 vol ~426k, FDV ~290k.
- Created: 2026-11-02T13:42:14Z, slot 464516025, tx 3kzbkGNNEMEvi6bBa78nK5Y1jJXynpjQvxYdUwoQtDdvZvT5DpHEyefKVrFtUtXVLRKwqK3ohwDhoXxgvksawjKH; curve FaGwNES4nMhxTtq8F73ZjSPbdLKj3FmGeNMn3kuWoUWK; creator GMDj3RpddapCUU5GxKaRaTXRCvW2e72LRbMkceJ91TxM
- Rule 1: creation slot 16 buying wallets (creator counted, migration tx and pool excluded), 100.93 % of tradable supply (top-15 100.75 %), wallets to reach 30 %: 3; slots 0-2: 16 wallets, 100.93 %. **HIT**
- Rule 2: migration 2WT4yDp9K52vBtWppKSyM6B6tkhdphuF7ZF9KCo7F9Zfj5KuRejaCSiAjhG5u82rZbRmLgws3yw9tDL1WEJKV2Jj slot 464516025 (+0 slots), signers ['GMDj3RpddapCUU5GxKaRaTXRCvW2e72LRbMkceJ91TxM', 'DD2gxEQ54CJXD7KEhffTCmWo3wCnxAxX42SeEXC1mTuu']: same slot as creation, creator co-signed, 5-/6-signer multi-wallet buy txs in creation slot -> HIT
- Rule 11: migration slot 464516025, window +0..+2: 23 buyers, 110.0 % of tradable supply, wallets to reach 80 %: 8 (broad cluster, not hit by the k80 precedent of ZERO c171; moot).
- bundle.py's migration locator picked a later no-op MigrateV2 (4qVJLqUn..., +2 slots, migration authority 9C4nRv...) = known quirk; rule11.py authoritative; verdict unaffected.
- Rule hit: **Rule 1, Rule 2**
- Raw: research/raw-20261103/c174/bundle_FOBET.json, rule11_FOBET.json, b_FOBET.log, r_FOBET.log
