# KILLED-SCOUT FOTF-gi2r (gi2rCdj8JSCSKzBpFDHQbMy2oeYg8qHUi7KQ7t6pump)
Cycle 204 (09:05 Stockholm, 2026-11-04), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 with fixed c6 locator), measured 2026-11-04T08:08:09Z-2026-11-04T08:08:43Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: gi2rCdj8JSCSKzBpFDHQbMy2oeYg8qHUi7KQ7t6pump
- PumpSwap pool: 5orMHC7da3xGQBvLzLyCuY9w5Eta1mafA2dzQ3sTXGXn (https://dexscreener.com/solana/5orMHC7da3xGQBvLzLyCuY9w5Eta1mafA2dzQ3sTXGXn)
- DexScreener/GT ~08:07Z: FOTF, pool 5orMHC..., age ~914 min (created 2026-11-03 16:53:41Z), found via GT only (not on DS lists): GT reserve ~2.15M USD vs FDV ~707M USD and h1 3,240 buys / 55 sells / 4 sellers = price/liquidity artefact (FOTF/XTX family, cf. c191 PumpFun artefact); GT 1h vol ~7.6k. Pattern: creator F3ZHYG... bought 100 % of tradable in the create tx itself (k30 = 1); MigrateV2 42zLVM... in the creation slot co-signed by the creator F3ZHYG... and AYoGwc... -> rule 2 HIT; Rule 11 window 4 buyers 125.82 %, k80 = 1 -> HIT. (bundle.py picked the later no-op MigrateV2 5RnKXH... by 9C4nRv..., known quirk; rule11.py authoritative.)
- Created: 2026-11-03T16:53:41Z, slot 464973009, tx 3gLd2BRpZXKYdRy1FTN6JQLFffxepPJKNqCNKbuEsVvGsJzS37yupUF2gg9UhVEdp8JrnSkcjk938R9RAGY5BgTv; curve DxzKbZfxPDhgqZwcBNeCnECdDhqmQZiBiCjcpyzkcktx; creator F3ZHYGtx83N3E7ypwnChzbDX2quaz2V4SDhK7T6Drtfm
- Rule 1: creation slot 1 buying wallets (creator counted, migration tx and pool excluded), 100.0 % of tradable supply, wallets to reach 30 %: 1; slots 0-2: 1 wallets, 100.0 %. **HIT**
- Rule 2: migration 42zLVMPovtrEWSdicNGyqQv1xffLZanFqsmx7QdMu6dMxqWBriWXHTws8R4fLwPsmcMA4LRtbVDhVtJ6tWKGjY66, same slot as creation, creator co-signed. **HIT**
- Rule 11: migration slot 464973009 (+0 slots), window +0..+2: 4 buyers, 125.82 % of tradable supply, wallets to reach 80 %: 1. **HIT**
- Rule hit: **Rule 1, Rule 2, Rule 11**
- Raw: research/raw-20261104/c204/bundle_FOTF-gi2r.json, rule11_FOTF-gi2r.json, b_*.log, r11log_FOTF-gi2r.txt
