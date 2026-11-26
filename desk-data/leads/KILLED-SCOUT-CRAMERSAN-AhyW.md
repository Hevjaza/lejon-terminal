# KILLED-SCOUT CRAMERSAN-AhyW (AhyWCaBF1U1ssTWgjFRrEvqNQdy4NsFCvLYRSJKppump)
Cycle 108 (09:10 Stockholm), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 with fixed c6 locator), measured 2026-10-31T08:10:21Z-2026-10-31T08:11:18Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: AhyWCaBF1U1ssTWgjFRrEvqNQdy4NsFCvLYRSJKppump
- PumpSwap pool: Dt8efo2CFoXELeeF6VE9FTpicQzAAbWPiX3okwszJ3jc (https://dexscreener.com/solana/Dt8efo2CFoXELeeF6VE9FTpicQzAAbWPiX3okwszJ3jc)
- DexScreener ~08:10Z: liquidity 25868 USD, 1h volume 281719.97 USD
- Created: 2026-10-31T07:19:18Z, slot 463601844, tx 3r3XrVVAAL8qnHDhyHRKptdS9WmDRqH6RgL9GgbJhAdKkPDeoYU8VZ3bf3TzquW1m7LYmR5otzbDpYXSHsq9kFBJ; curve 9aQWxJ8tcNz4vJsSVV4nof51jnLCveXYaPhF1JCtWEwG; creator 2zETudM25HVW8enSU1sts85TiBhNBxRjkmjcDfBpYHR4
- Rule 1: creation slot 11 buying wallets (creator counted, migration tx and pool excluded), 100.0 % of tradable supply, wallets to reach 30 %: 3; slots 0-2: 11 wallets, 100.0 %. **HIT**
- Rule 2: migration 5rbNiFG6p8nLjBnFtxPZ4BW6es19TZjApedVK2jNkjNdfcYhCp6SsMpNRzn2GQ3GToA6bH9Y4mn6mvtK1ZbCrTk8, same slot as creation, creator not co-signer. Not hit.
- Rule 11: migration slot 463601844 (+0 slots), window +0..+2: 18 buyers, 109.97 % of tradable supply, wallets to reach 80 %: 8. Not hit.
- Rule hit: **Rule 1**
- Raw: research/raw-20261031/c108/bundle_CRAMERSAN-AhyW.json, rule11_CRAMERSAN-AhyW.json, log_CRAMERSAN-AhyW.txt, r11log_CRAMERSAN-AhyW.txt
- Notes: creation slot had 2 multi-wallet buy txs with 5 signers / 5 recipients each (5kAngD..., 3yZ7jb...). The real migration tx 5rbNiF... (MigrateV2 + CreatePool, creation slot) was signed by 58noXn..., which is also a creation-slot buy fee payer (not the creator, so rule 2 is not formally hit). bundle.py's first locator picked a later MigrateV2-only tx (4weazT..., slot +3); getTransaction cross-check (chkmig) confirms the rule11.py locator.
