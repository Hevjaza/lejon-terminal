# KILLED-SCOUT FOMO-GAcg (GAcgjHjsj9pUWtcRAjCNS56EP1X4eD4DNYbyJQnBpump)
Cycle 177 (06:08 Stockholm, 2026-11-03), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11), measured 2026-11-03T05:09:37Z-2026-11-03T05:10:45Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: GAcgjHjsj9pUWtcRAjCNS56EP1X4eD4DNYbyJQnBpump
- PumpSwap pool: 2HjRvzBqgfkuGL11juruUDgyqzA3sQjLqyCFpngHVauj (https://dexscreener.com/solana/2HjRvzBqgfkuGL11juruUDgyqzA3sQjLqyCFpngHVauj)
- Market data: fomo, age ~105 min, GT reserve ~62.9k, 1h vol ~94.0k, h24 vol ~155.8k, FDV ~625k (GeckoTerminal ~05:09Z)
- Created: 2026-11-03T03:24:12Z, slot 464746147, tx 2ZVoE5dZ84gHVA3EFfwDYjmMpiEDMSaZ7dXyqbMnK2uPqVTv1mwt9USTgxzGnuabzKbgvS18aNmQmvGav8mo2y2d; curve 37FttjUUW82FqfAD4PY5WM8ugFNUHpm96tyqtgwgC6Hd; curve creator 65gZZEK9XerM8xFHPYX1acwu3gpdzJtC1swtAEYFwbXE; create signers ['65gZZEK9XerM8xFHPYX1acwu3gpdzJtC1swtAEYFwbXE', 'GAcgjHjsj9pUWtcRAjCNS56EP1X4eD4DNYbyJQnBpump']
- Rule 1: creation slot 7 buying wallets (creator counted, migration tx and pool excluded), 100.0 % of tradable supply (top-15 100.0 %), wallets to reach 30 %: 2; slots 0-2: 7 wallets, 100.0 %. **HIT**
- Rule 2: migration MigrateV2+CreatePool 5SKfi5rJ... in the creation slot (+0 slots) signed by the creator 65gZZE... (creator_cosigned true); 6 near-equal ~13-14 % buys in the creation slot = coordinated -> **HIT**
- Rule 11: window +0..+2: 21 buyers, 110.06 % of tradable, wallets to reach 80 %: 5 -> **HIT** (k80 = 5 precedent: fomo-EUhv, FOMO-GDea, fomo-BU4S)
- bundle.py's migration locator picked the later no-op MigrateV2 (+2 slots, migration authority 9C4nRv...) where applicable = known quirk; rule11.py authoritative; verdict unaffected.
- Rule hit: **Rule 1, Rule 2, Rule 11**
- Raw: research/raw-20261103/c177/bundle_FOMO.json, rule11_FOMO.json, b_FOMO.log, r11log_FOMO.txt
