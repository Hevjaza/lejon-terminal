# KILLED-SCOUT ARNOLD-nG3j (nG3jfPQHU2ZQhPERkTZD8YPSAsrrWiePPDcm9jxpump)
Cycle 104 (05:10 Stockholm), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 with fixed c6 locator), measured 2026-10-31T04:05:50Z-2026-10-31T04:07:22Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: nG3jfPQHU2ZQhPERkTZD8YPSAsrrWiePPDcm9jxpump
- PumpSwap pool: FEJsEq9mo3myRyU6D3LHz3TXwoE8GrYhEkzkoqyGsKLP (https://dexscreener.com/solana/FEJsEq9mo3myRyU6D3LHz3TXwoE8GrYhEkzkoqyGsKLP)
- DexScreener ~04:05Z: liquidity 25196 USD, 1h volume 23661.59 USD
- Created: 2026-10-30T22:05:17Z, slot 463446789, tx 44DzDRDPLt67vR8uYFAudfTz2YbKLVPCcVDoE9fxjKkeum6rCMrhYDAhkeuHRpBWbmVSdCiW7zpf6iesauu3eGcT; curve 6mAfrvtqTr8eLHEUfcJstQdPYLwysEj5LgcSA7igE9Wy; creator 3j5NrcnM9ZgLf7z9LaBiywUYpfEezqXTGHySx9yENw9W
- Rule 1: creation slot 4 buying wallets (creator counted, migration tx and pool excluded), 63.3 % of tradable supply, wallets to reach 30 %: 2; slots 0-2: 4 wallets, 63.3 %. **HIT**
- Rule 2: migration 5GrHfAjgFGAuTjpNVKjZTAbxs79rr3JupmfQ3dMnqSobr91fkUvfSzN56raV74pgiCu6xQLDgmFWZQUhmpQ73iBm, not same slot, creator not co-signer. Not hit.
- Rule 11: migration slot 463446800 (+11 slots), window +0..+2: 11 buyers, 2.32 % of tradable supply, wallets to reach 80 %: None. Not hit.
- Rule hit: **Rule 1**
- Raw: research/raw-20261031/c104/bundle_ARNOLD-nG3j.json, rule11_ARNOLD-nG3j.json, log_ARNOLD-nG3j.txt, r11log_ARNOLD-nG3j.txt
- Discovery note: DexScreener search 04:04Z showed liquidity 25,196 USD; direct pair re-check 04:05Z showed 24,767 USD (below the 25k floor) - fails discovery liquidity too. Pre-check run anyway for the record. Migration tx 5GrHfA... (Migrate + CreatePool) at slot +11, signers 9ns7.../TRAX..., creator not co-signer (chkmig_c104.txt).
