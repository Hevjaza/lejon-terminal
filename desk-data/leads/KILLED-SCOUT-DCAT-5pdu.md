# KILLED-SCOUT DCAT (5pdu9jrUf9ryLzCsv3S92ikoBiK3n2zA9tMN9Rr7pump)
Cycle 265 (02:0x Stockholm, 2026-11-07), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 with fixed c6 locator), measured 2026-11-07T01:12:04Z-2026-11-07T01:13:26Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: 5pdu9jrUf9ryLzCsv3S92ikoBiK3n2zA9tMN9Rr7pump
- PumpSwap pool: GbCzV3VF1LPzoqyPoaLNvfzHBAK3ZQc3AJCA9G79VHgn (https://dexscreener.com/solana/GbCzV3VF1LPzoqyPoaLNvfzHBAK3ZQc3AJCA9G79VHgn)
- DexScreener/GT ~01:1xZ: DCAT, pool GbCzV3VF..., age ~141 min at scan (curve created 2026-11-06 22:50:01Z, creation slot 466283194, creator ATQTfQ...; migrated in the SAME slot), found via dsretry+scan2+gtslow: DS liq ~46k, 1h vol ~146k, h1 +42 %, FDV ~339k. Creation slot: CreateV2 + multiwallet Buys (6-signer + two 7-signer Buy txs) -> r1 (ex-pool) 19 wallets 100 % of tradable, k30 = 3 -> Rule 1 HIT. Authoritative MigrateV2/CreatePool Kkh2eh... same slot, co-signed by the creator ATQTfQ... (+GTwe6f...) -> Rule 2 HIT. Rule 11: window 26 buyers 111.66 %, k80 = 8 (mechanical cap 5 not hit); same-slot multiwallet BuyV3 pattern (6+7+7 signers) with top10 90.55 % of tradable in migration window -> Rule 11 judgment HIT (hard KILL per t39u). bundle.py locator picked a later no-op Migrate by 9C4nRv... (+3 slots, known quirk); rule11.py authoritative.
- Created: 2026-11-06T22:50:01Z, slot 466283194, tx 5AHRC88pHZchb6heWjpzVR4ELgibJPkkQ9WhaBK5HHwpCzJM6ppRyrVsvLdEAhHm5aWC1MyH2jW8ZDzLx7Z8LH2b; curve BFjhqDfkpe4thq5arMMd2LvzTT1xoyaE8evPA7xkj5Fz; creator ATQTfQ3rWpc2bpRvVSjamX94CTW39dVsWMzLuRbyVwgB
- Rule 1: creation slot 19 buying wallets (creator counted, migration tx and pool excluded), 100.0 % of tradable supply, wallets to reach 30 %: 3; slots 0-2: 19 wallets, 100.0 %. **HIT**
- Rule 2: migration Kkh2eh7M5DsazgbPV1wnXrnb6J8Wq8cLDQ6LeXYYsFY3AwZAP5Eq3c6q3ttiT3Moyu8zPZ8weEEupwGAv7RqagN, same slot as creation, creator co-signed. **HIT**
- Rule 11: migration slot 466283194 (+0 slots), window +0..+2: 26 buyers, 111.66 % of tradable supply, wallets to reach 80 %: 8. Not hit mechanically (k80>5).
- Rule hit: **Rule 1, Rule 2, Rule 11 (judgment: same-slot 6+7+7-signer BuyV3 multiwallet = top10 90.55 % in migration window)**
- Raw: research/raw-20261107/c265/bundle_DCAT.json, rule11_DCAT.json, bun_DCAT.log, r11_DCAT.log
