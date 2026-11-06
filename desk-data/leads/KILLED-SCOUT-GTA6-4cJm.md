# KILLED-SCOUT GTA6 (4cJmQze3dDHU7cd9o5ZZNMwuYquo6r7RYTP8Eit6pump)
Cycle 264 (00:0x Stockholm, 2026-11-07), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11), measured 2026-11-06T23:07:33Z-2026-11-06T23:08:15Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: 4cJmQze3dDHU7cd9o5ZZNMwuYquo6r7RYTP8Eit6pump
- PumpSwap pool: J3SMcXevTVmD4zVytbLFWY3B27H8JExXZnyPhXeE1bAK (https://dexscreener.com/solana/J3SMcXevTVmD4zVytbLFWY3B27H8JExXZnyPhXeE1bAK)
- DexScreener/GT ~23:07Z: GTA VI / GTA6, found via gtslow.py: DS liq ~45,450, 1h vol ~37,173, age ~117 min.
- Created: 2026-11-06T21:10:49Z, slot 466255456, tx 4ebbMjJqshvEsVQMs1og6UsNdci9d57koMFPg4etczNx9wTwNVjqK9KfTdkUBT5odoSP53GgmGr15oUiPRfsqkMM; curve 3rxBKbmV9PhjcBjBWVHKstyFu4cSrrWzEP6DmV1n2ncA; creator 5atKvsrkQiG2Ugip8VwXjuqLciTKinbqtGzvmaWGpmzy
- Rule 1: creation slot 7 buying wallets (creator counted, r1 after excl mig), 100 % of tradable supply, wallets to reach 30 %: 2; slots 0-2: 7 wallets, 100 %. Raw w_slot0 8 wallets 126.09 %, k30=2. Multi-wallet txs in slot0: two 3-signer buys. **HIT**
- Rule 2: migration yAVgXeJetteeCMqv9wQFTWcwGeK7EsuYNKNPm4P57iVLkJpDSc1G7d7jxpfe858q3doyj7NdGZxxq5bf2y5Auu9 (rule11 authoritative MigrateV2+CreatePool), same slot as create (dslot 0), creator 5atK… co-signed. Coordinated buy volume in creation slot. **HIT** (bundle.py later no-op MigrateV2 at +2 slots by 9C4n… is the known quirk; rule11 migration is authoritative)
- Rule 11: migration window +0..+2: 12 buyers, 110.73 % of tradable, k80=5. **HIT** (mechanical k80<=5 + >80 %).
- Rule hit: **Rules 1+2+11**
- Raw: research/raw-20261107/c264/bundle_GTA6.json, rule11_GTA6.json, bun_GTA6.log, r11_GTA6.log
