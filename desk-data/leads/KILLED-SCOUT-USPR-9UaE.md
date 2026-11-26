# KILLED-SCOUT USPR (9UaEUzhQZ9MJtdUpQdzSE5v3uDVyMrJaxHs3xmwpump)
Cycle 193 (22:08 Stockholm, 2026-11-03), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11), measured 2026-11-03T21:09:55Z-2026-11-03T21:10:23Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: 9UaEUzhQZ9MJtdUpQdzSE5v3uDVyMrJaxHs3xmwpump
- PumpSwap pool: DxrA9BF8Y8XZeY9Wu9QCwf7W8ef6xnVNUHb6atDW9rZ7 (https://dexscreener.com/solana/DxrA9BF8Y8XZeY9Wu9QCwf7W8ef6xnVNUHb6atDW9rZ7)
- GeckoTerminal ~21:09Z: reserve 147,091 USD, 1h volume ~6.9k USD, h24 ~173k USD; h1 txns 3,292 buys vs 105 sells, 5 sellers (found by gtslow.py only; DS search did not list it as a candidate)
- Created: 2026-11-03T03:31:33Z, slot 464748224, tx 32dwD3kTM3HPfTzZLz8SCW3iUWPkv1V7nJbtSNgC9BHpYkQYDoro49ezRfB5L7jGN35Fne18FVJFxt7vQ9xZQP7Q; curve 5mvCJe8ezqN9snGTjyfUXpimw5HfGhQLTw13fkmkvnZK; creator AU5Gsg9hVzktFeg6HEZZJvJKYDHiVGWobuT9MeoTnyLZ (create co-signer CHLdFXwJ...)
- Rule 1: the creator alone bought 793.1M tokens = 100 % of tradable supply in the create tx (k30 = 1). **HIT**
- Rule 2: MigrateV2+CreatePool FnmDCKgu... in the creation slot 464748224, signed by creator AU5Gsg... + CHLdFXwJ...; CHLdFXwJ... also bought 180.5M (~22.8 % of tradable) from the new pool in the same slot -> coordinated. **HIT**
- Rule 11: migration slot +0..+2: 5 buyers 122.76 % of tradable, k80 = 1 (whole curve by the creator). **HIT**
- bundle.py located the later no-op MigrateV2 (3QxwMC..., +2 slots, 9C4nRv...) = known quirk; rule11.py authoritative.
- Rule hit: **Rules 1 + 2 + 11**
- Raw: research/raw-20261103/c193/bundle_USPR.json, rule11_USPR.json, b_USPR.log, r11log_USPR.txt
