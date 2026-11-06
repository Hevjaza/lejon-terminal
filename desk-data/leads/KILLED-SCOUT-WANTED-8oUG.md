# KILLED-SCOUT WANTED-8oUG (8oUGdPdyxVaCSJSZpcVZuxqoyiZAmc2Z22FsDRZ3pump)
Cycle 174 (03:05 Stockholm, 2026-11-03), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11), measured 2026-11-03T02:08:00Z-2026-11-03T02:08:35Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: 8oUGdPdyxVaCSJSZpcVZuxqoyiZAmc2Z22FsDRZ3pump
- PumpSwap pool: 46jo5tmE2ZpvqQ3ndHCNEwWTbdtQvqFmcSYxGgB9262M (https://dexscreener.com/solana/46jo5tmE2ZpvqQ3ndHCNEwWTbdtQvqFmcSYxGgB9262M)
- DexScreener/GT ~02:07Z: Wanted, age ~77 min, DS liq ~47.6k, 1h vol ~249k, h1 +69.9 %, FDV ~354k.
- Created: 2026-11-03T00:50:37Z, slot 464703040, tx 4VPNS3HRNC1LhrnMnuJwnL5KRHHLgPjgpx2mxox7NXi1rdn99hvW13s44a51eeCnDWAS2coi2g4WCxWxSbYuPSwx; curve J3gSM3v8zY1TCLHUs6iw58GXfEP4zPoXZDHs1v9X8opz; creator 2njWaF4RD3Mm53NuZQDmrbFwDgGJ57wh3amAhe3v74vg
- Rule 1: creation slot 19 buying wallets (creator counted, migration tx and pool excluded), 100.0 % of tradable supply (top-15 90.08 %), wallets to reach 30 %: 5; slots 0-2: 19 wallets, 100.0 %. **HIT**
- Rule 2: migration 2EskeLy7yqXwFbyJFann1vYdXsGfZabSj3V5dKmCZY6e9MzgGxB1x7Yb7tGKmMf5KjL5Mm2WWnhrqJuEBeZSsUjU slot 464703040 (+0 slots), signers ['2njWaF4RD3Mm53NuZQDmrbFwDgGJ57wh3amAhe3v74vg', '9f1judfM7nyJE1xqD2HvShrK3m1KBWhgTb7fh1BaYsKK']: same slot as creation, creator co-signed, 6-/7-signer multi-wallet buy txs in creation slot -> HIT
- Rule 11: migration slot 464703040, window +0..+2: 24 buyers, 111.14 % of tradable supply, wallets to reach 80 %: 13 (broad cluster, not hit by the k80 precedent of ZERO c171; moot).
- bundle.py's migration locator picked a later no-op MigrateV2 (4wYsWeje..., +2 slots, migration authority 9C4nRv...) = known quirk; rule11.py authoritative; verdict unaffected.
- Rule hit: **Rule 1, Rule 2**
- Raw: research/raw-20261103/c174/bundle_WANTED.json, rule11_WANTED.json, b_WANTED.log, r_WANTED.log
