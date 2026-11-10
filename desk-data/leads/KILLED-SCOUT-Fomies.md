# KILLED-SCOUT Fomies (HipJR79p21LdH1WNAxKfNXiGULdA1QWUaG7uLwonpump)
Cycle 23, bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 with fixed c6 locator), measured 2026-10-27T17:08:37Z-2026-10-27T17:08:53Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: HipJR79p21LdH1WNAxKfNXiGULdA1QWUaG7uLwonpump
- PumpSwap pool: 3gEmeWRbHcuhoUKtnvURAgrF7sJNCiVVfQRvw8eU7EAx (https://dexscreener.com/solana/3gEmeWRbHcuhoUKtnvURAgrF7sJNCiVVfQRvw8eU7EAx)
- DexScreener ~17:18Z: liquidity 238950 USD, 1h volume 3709.71 USD
- Created: 2026-10-27T00:50:00Z, slot 461873430, tx 2KaiUrKTL2wywDA8qt97NpftzwvPw1BEgTEAZ1jCTdm3C926V8EbCJg66pJqGKWryse4rmswZmfYH37Hka1ybsih; curve CTANUCYEGaQWpqNR1n7siMymd4uFVd7Eu8jZKvv4UEHz; creator 4gp94Z8b4BgBQgqpeWsgyFck1pUXrj6Nwv6PtvRcGFMF
- Rule 1: creation slot 2 buying wallets (creator counted, migration tx and pool excluded), 24.98 % of tradable supply, wallets to reach 30 %: None; slots 0-2: 3 wallets, 26.44 %. Not hit.
- Rule 2: migration 445CqyGgUKUAHaooMAitR4oV3LyALKgwxWUYXLcBaP3tYUGSqbEG3pbDV3xpSvzG9NjENQKHQEnqwbYrDZfqyrfA, not same slot, creator not co-signer. Not hit.
- Rule 11: migration slot 461882241 (+8811 slots), window +0..+2: 11 buyers, 100.08 % of tradable supply, wallets to reach 80 %: 3. **HIT**
- Rule hit: **Rule 11**
- Raw: research/raw-20261027/c23/bundle_Fomies.json, rule11_Fomies.json, log_Fomies.txt, r11log_Fomies.txt
- Rule 11 detail: graduation slot 461882241 (~1 h after creation): multi-signer buy txs cjE8T4.../AQ3J7m... (~461M tokens) and 76uAcv.../5zpRFM... (~146M tokens; 5zpRFM... also signed the MigrateV2 in the same slot) bought ~77 % of the tradable curve from the bonding curve, plus DCWFme... ~187M from the new pool in the same slot. 3 wallets reach > 80 % of tradable supply -> immediate KILL. (Creation slot: 2 wallets 24.98 %, would have been soft flag "Misstänkt bundling"; moot.) Early Signals ranking irrelevant (KILL rules override).
