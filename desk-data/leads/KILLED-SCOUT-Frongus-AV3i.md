# KILLED-SCOUT Frongus-AV3i (AV3iJmpLP8AzKBCREoiaPYDsSn5y9GDeemS1AnQJpump)
Cycle 47, bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 with fixed c6 locator), measured 2026-10-28T17:19:30Z-2026-10-28T17:19:41Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: AV3iJmpLP8AzKBCREoiaPYDsSn5y9GDeemS1AnQJpump
- PumpSwap pool: GzppARUujh44x9Tz7LU5ni7B5qXyfaYprshnoMdk1ug8 (https://dexscreener.com/solana/GzppARUujh44x9Tz7LU5ni7B5qXyfaYprshnoMdk1ug8)
- DexScreener ~17:14-17:17Z: liquidity 214821 USD, 1h volume 2244.19 USD
- Created: 2026-10-27T21:49:49Z, slot 462228724, tx V8i8Fgo8jQLo3Wzvc5eBTtPRDbH5FbyCH7WSpt52Y41xrtLYXaeGWZkkbEVEeZteZVjb98T7tjUpkaWs3zo5Bgo; curve J7jY5wQZvoFvBUfLuAX28fcmbKnMk5uszk5NbC5wjHr3; creator 5zpRFMhPMjWGjZ77NhceguPHoWqhgyWSJrtd8aDEcpbV
- Rule 1: creation slot 1 buying wallets (creator counted, migration tx and pool excluded), 21.6 % of tradable supply, wallets to reach 30 %: None; slots 0-2: 3 wallets, 22.23 %. Not hit.
- Rule 2: migration ToHJ9eFe2cUmWTMyzVYDufzaNYtqAeXnVRAmJrks3UB3WaFterWvm1u2UNwy2WaXxcSQWZ67kNiNZhDXLTYSmXz, not same slot, creator co-signed. Not hit.
- Rule 11: migration slot 462392101 (+163377 slots), window +0..+2: 12 buyers, 123.56 % of tradable supply, wallets to reach 80 %: 3. **HIT**
- Rule hit: **Rule 11**
- Raw: research/raw-20261028/c47/bundle_Frongus-AV3i.json, rule11_Frongus-AV3i.json, log_Frongus-AV3i.txt, r11log_Frongus-AV3i.txt
- Data note: migration window total exceeds 100 % (123.56 %) because the +0..+2 window includes pool churn right after the creator-co-signed migration; top wallet cjE8T4... alone 56.1 %, 3 wallets reach 80 %. Hit per the standing Rule 11 formula (k80 <= 5). Creation slot dev buy 21.6 % by 1 wallet (soft-flag range), moot.
