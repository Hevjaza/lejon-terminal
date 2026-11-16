# KILLED-SCOUT ATI-419P (419P2wrVug9cW5hMwsjEEdhM5aLBt7YFnwn1p7dypump)
Cycle 110 (11:12 Stockholm), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 with fixed c6 locator), measured 2026-10-31T10:10:20Z-2026-10-31T10:10:50Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: 419P2wrVug9cW5hMwsjEEdhM5aLBt7YFnwn1p7dypump
- PumpSwap pool: Hjcgmfy7XAhXGLtgs4NSid2aXQtsrU9r7F8MADhQ2W1H (https://dexscreener.com/solana/Hjcgmfy7XAhXGLtgs4NSid2aXQtsrU9r7F8MADhQ2W1H)
- DexScreener ~10:10Z: liquidity 44821 USD, 1h volume 707883.06 USD
- Created: 2026-10-31T08:38:51Z, slot 463624130, tx 3tcTfbRHaRcqGLtoDCt1gbdNgfwUo8RBCh4KJoCymNU459i9qKLqvtfUvkznZcp4gfTbg94tof8iSZwhPRtCwCVk; curve Fb64pBRPcnARdvaY48qEhvXKN9mVHGZrMguzNUhpzRFZ; creator 9QB9kANE6kXcJC6P5hxq26GX9ErEm6jtt9CxvSzTs7Yy
- Rule 1: creation slot 11 buying wallets (creator counted, migration tx and pool excluded), 100.0 % of tradable supply, wallets to reach 30 %: 3; slots 0-2: 11 wallets, 100.0 %. **HIT**
- Rule 2: migration 57g99j9VfmJWEw7hwxr6GZTGZhiTi2aAkv8BRuSNEdpNsSRLBXKiA3PT9CVa9CFof93Gu1d9YiXPfkPgmLYCn3x, same slot as creation, creator not co-signer. Not hit.
- Rule 11: migration slot 463624130 (+0 slots), window +0..+2: 17 buyers, 106.48 % of tradable supply, wallets to reach 80 %: 7. Not hit.
- Rule hit: **Rule 1**
- Raw: research/raw-20261031/c110/bundle_ATI-419P.json, rule11_ATI-419P.json, log_ATI-419P.txt, r11log_ATI-419P.txt
- Notes: creation slot had 2 multi-wallet buy txs with 5 signers / 5 recipients each (2gLhQk..., 3MKc31...) plus a 3-signer buy (3S9YZi...). The real migration tx 57g99j... (MigrateV2 + CreatePool, creation slot) was signed by Fy2p7R..., which is also a creation-slot buy fee payer (not the creator, so rule 2 is not formally hit). bundle.py's first locator picked a later MigrateV2-only tx (4ygkjD..., slot +2); getTransaction cross-check (chkmig) confirms the rule11.py locator. Dev buy 2.19 % of tradable supply.
