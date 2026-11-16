# KILLED-SCOUT PUMP-Hxqh (Hxqh7Fxsz11pyqDRdEkBgP8vP44BPLPnQDrxzPYZpump)
Cycle 187 (16:11 Stockholm, 2026-11-03), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11), measured 2026-11-03T15:12:50Z-15:14:57Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: Hxqh7Fxsz11pyqDRdEkBgP8vP44BPLPnQDrxzPYZpump
- PumpSwap pool: 5hR1QiEzvxPnLHipFLV1WFZXFA39ZDZTABHYLZVtnuNv (https://dexscreener.com/solana/5hR1QiEzvxPnLHipFLV1WFZXFA39ZDZTABHYLZVtnuNv)
- Market data (DexScreener ~15:11Z): age ~201 min, liq ~476-500k USD, 1h vol ~27-29k USD, h24 ~865k USD, FDV ~991k.
- Created: 2026-11-03T11:49:57Z, slot 464888135; curve BEYjsCt7...; curve creator = create signer 4PtNudn5F2KtaHXh15wuv5qWGLHRadXJyhKeWMYNRxuk (dev buy 1.26 %).
- Rule 1: creation slot 3 buying wallets (creator counted) bought 57.8 % of tradable; DGxaMZUoCQeQq7FuewJMaas7vKebYKsU5UsEgXxoZkZA alone 370M = 46.65 %, dKMjeG... 9.9 %; wallets to reach 30 %: 1; slots 0-2 identical. **HIT**
- Rule 2: migration (rule11.py) 5PcoqSuW... slot 464888248 (+113 slots, 11:50:21Z), signer AwfBEu..., creator not co-signer -> not hit.
- Rule 11: window +0..+2: 14 buyers 1.91 % -> not hit.
- bundle.py's migration locator returned "NOT FOUND in newest 25 successful curve txs" (locator limitation, same family as the known quirk); rule11.py located the migration and is authoritative; verdict unaffected.
- Rule hit: **Rule 1**
- Raw: research/raw-20261103/c187/bundle_PUMP.json, rule11_PUMP.json, b_PUMP.log, r11log_PUMP.txt
