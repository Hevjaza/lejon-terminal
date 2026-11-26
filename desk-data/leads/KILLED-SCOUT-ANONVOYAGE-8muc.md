# KILLED-SCOUT ANONVOYAGE-8muc (8muc9DdhqWfAPcvmEebNQCG89bLiwi12T2KtBtzVpump)
Cycle 186 (15:12 Stockholm, 2026-11-03), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11), measured 2026-11-03T14:13:30Z-14:16:20Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: 8muc9DdhqWfAPcvmEebNQCG89bLiwi12T2KtBtzVpump
- PumpSwap pool: 2Yx74Z677vrMWJn4QNm9AQThbxQi1DSXRYSiFk4RSMmA (https://dexscreener.com/solana/2Yx74Z677vrMWJn4QNm9AQThbxQi1DSXRYSiFk4RSMmA)
- Market data (DexScreener ~14:13Z): age ~32 min, liq ~64.5k USD, 1h vol ~622k USD, h1 +960 %, FDV ~640k.
- Created: 2026-11-03T13:41:39Z, slot 464919411; curve 2XEniTwP...; curve creator = create signer 5ixmtzSCp5LvwihvEaeMW34WMCp95Ev1FN5BHzqx5m4s; only 32 curve sigs.
- Rule 1: creation slot 7 buying wallets (creator counted; dev buy 0.44 %) bought 100 % of tradable supply; wallets to reach 30 %: 2 (DCcAt7... 22.3 %, LyCwG1... 22.2 %, 8AUvjA... 19.2 %, CzmdNX... 17.9 %, 8u49tb... 13.6 %); two 3-signer multi-wallet buy txs. **HIT**
- Rule 2: MigrateV2+CreatePool 5DZiP9fo... in the creation slot (+0) signed by the creator 5ixmtz...; coordinated multi-wallet buys in the same slot -> **HIT**
- Rule 11: window +0..+2: 12 buyers, 116.58 % of tradable, top 5 95.27 %, wallets to reach 80 %: 4 -> **HIT** (whole curve bought by a small cluster before/at migration; hard per t39u)
- bundle.py's migration locator picked the later no-op MigrateV2 (+1 slot, 9C4nRv...) = known quirk; rule11.py authoritative; verdict unaffected.
- Rule hit: **Rule 1, Rule 2, Rule 11**
- Raw: research/raw-20261103/c186/bundle_ANONVOYAGE.json, rule11_ANONVOYAGE.json, b_ANONVOYAGE.log, r11log_ANONVOYAGE.txt
