# KILLED-SCOUT wen-GGLZ (GGLZzgVssSaW7zKrtNveFYyp2zrkfVTce1TjgPfNpump)
Cycle 160 (13:06 Stockholm, 2026-11-02), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 with fixed c6 locator), measured 2026-11-02T12:08:33Z-2026-11-02T12:08:46Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: GGLZzgVssSaW7zKrtNveFYyp2zrkfVTce1TjgPfNpump
- PumpSwap pool: 12SzKCF7zECUeM9z87DijGLuppPrtTErKN82w7YuP3KD (https://dexscreener.com/solana/12SzKCF7zECUeM9z87DijGLuppPrtTErKN82w7YuP3KD)
- DexScreener/GT ~12:07Z: Symbol wen. DS candidate (scan2.py): pumpswap pool liquidity ~27.6k USD, 1h volume ~305k USD, h1 +184 %, FDV ~112k USD, pair ~35 min old; DS h1 4144 buys / 2298 sells; DS socials: one X post link. Creation slot 464479901: 11 wallets bought 100 % of the tradable curve (k30 = 3; two 5-signer/5-recipient multiwallet buy txs). MigrateV2 KjC9gXu1... in the creation slot, signed by FMDpFm... (a creation-slot fee payer/buyer, not curve creator CMmxVk...; strict Rule 2 needs creator co-sign, so not hit). bundle.py locator picked later MigrateV2 51qA4prq... +2 slots by 9C4nRv... (known quirk; rule11.py authoritative). Rule 11 window: 17 buyers 108.25 %, k80 = 8 (not hit)
- Created: 2026-11-02T11:33:07Z, slot 464479901, tx 5vgxctJj22p2fT9DRMjG6ySqWuqvLjbaTP4KcmiGtQmcNx79Rujbp46D8zCLkZsBUx3LGKnvbp5heWCj5iyHVumS; curve C7cLmNUpQLajifvdzCSsjaNiBbJNqnFvKMoyTbXjX2wp; creator CMmxVkuBmdZvE4LLq8vdN5ve9Q5hsxCZZCpvPKvthtCa
- Rule 1: creation slot 11 buying wallets (creator counted, migration tx and pool excluded), 100.0 % of tradable supply, wallets to reach 30 %: 3; slots 0-2: 11 wallets, 100.0 %. **HIT**
- Rule 2: migration KjC9gXu16fE1iZmGc5zh8CbHc6EnZ4JxQptDmZCoqRt6dVjvYapjT63fRUwJzkZq9RVTXH5e6wkT33fxhDaAfdC, same slot as creation, creator not co-signer. Not hit.
- Rule 11: migration slot 464479901 (+0 slots), window +0..+2: 17 buyers, 108.25 % of tradable supply, wallets to reach 80 %: 8. Not hit.
- Rule hit: **Rule 1**
- Raw: research/raw-20261102/c160/bundle_wen-GGLZ.json, rule11_wen-GGLZ.json, log_wen-GGLZ.txt, r11log_wen-GGLZ.txt
