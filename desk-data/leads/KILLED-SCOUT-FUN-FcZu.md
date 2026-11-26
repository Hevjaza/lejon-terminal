# KILLED-SCOUT FUN-FcZu (FcZuu76twm89BKVN6WoWhFwfCmAVFPx24NkT8hKvpump)
Cycle 111 (12:12 Stockholm), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 with fixed c6 locator), measured 2026-10-31T11:09:19Z-2026-10-31T11:09:48Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: FcZuu76twm89BKVN6WoWhFwfCmAVFPx24NkT8hKvpump
- PumpSwap pool: BLmGxiCQiRjFedQ3hFwNXbeRbuPRnUZ6qa8itXrXonzm (https://dexscreener.com/solana/BLmGxiCQiRjFedQ3hFwNXbeRbuPRnUZ6qa8itXrXonzm)
- DexScreener ~11:10Z: liquidity 33541 USD, 1h volume 538243.31 USD
- Created: 2026-10-31T10:10:41Z, slot 463649929, tx 4amsPi5ufRRZgkCoLMrQJLZk2PoSpKtN8KttE9SY65L56kmwQdEDHPy94DML9H5hx3FDgdj2N3ACrsB7deCZKYCz; curve 7N3yESeq2AStRab9sS84s6dY373QB3Hrr8u6g3Z3oRC7; creator 4Wdttec7Ev1TsiX69zbAVWgHm7ZHW1VdcqZ4kGRZ2THG
- Rule 1: creation slot 11 buying wallets (creator counted, migration tx and pool excluded), 100.0 % of tradable supply, wallets to reach 30 %: 2; slots 0-2: 11 wallets, 100.0 %. **HIT**
- Rule 2: migration 5YtdyHaptrBHyJoYtCrijTuaXiWGYxe54FJUnBa6Jui3j8r6etkmS7x8QkvdKKNN8RWkvg8xXYtcsY78EBVkySaK, same slot as creation, creator not co-signer. Not hit.
- Rule 11: migration slot 463649929 (+0 slots), window +0..+2: 16 buyers, 109.8 % of tradable supply, wallets to reach 80 %: 7. Not hit.
- Rule hit: **Rule 1**
- Raw: research/raw-20261031/c111/bundle_FUN-FcZu.json, rule11_FUN-FcZu.json, log_FUN-FcZu.txt, r11log_FUN-FcZu.txt
- Note (c111): the real migration tx 5Ytdy... (MigrateV2 + CreatePool) is in the creation slot and signed by DhyuvG49..., a creation-slot buy fee payer (not the creator), so Rule 2 is not hit formally. bundle.py's first locator picked a later MigrateV2-only tx (44Rt8U..., slot +4); chkmig.py confirms the rule11.py locator. Two 5-signer multi-wallet buy txs in the creation slot.
