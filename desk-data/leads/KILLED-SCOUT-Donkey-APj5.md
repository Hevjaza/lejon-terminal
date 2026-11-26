# KILLED-SCOUT Donkey-APj5 (APj59xtb4dRp49bXwKSq5E1XWKLrFbtaYfoQZ9Arpump)
Cycle 212 (17:12 Stockholm, 2026-11-04), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 with fixed c6 locator), measured 2026-11-04T16:13:51Z-2026-11-04T16:14:10Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: APj59xtb4dRp49bXwKSq5E1XWKLrFbtaYfoQZ9Arpump
- PumpSwap pool: 5yabcmxNn5Gsmj6NPZ5wgVSScC1iMd5tN5F9DetR1GJb (https://dexscreener.com/solana/5yabcmxNn5Gsmj6NPZ5wgVSScC1iMd5tN5F9DetR1GJb)
- DexScreener/GT ~16:12Z: Donkey, pool 5yabcm..., age ~49 min (curve created 2026-11-04 15:23:45Z, MigrateV2+CreatePool 4zDdhR... in the same slot 465351009, signed by Yyz7zN..., not the creator), found via DS (scan2.py) only: DS liq ~26.6k USD, FDV ~107k, 1h vol ~423k, h1 +165 %. Pattern: whole bonding curve emptied in the creation slot: creator D2AjvH... (dev 6.12 %) + two 5-signer multi-wallet buy txs, 11 buying wallets 100 % of tradable, k30 = 3 -> rule 1 HIT; migration in the creation slot but not creator-signed -> rule 2 not hit strictly. Rule 11 window 16 buyers 108.27 %, k80 = 8 -> mechanical not hit, noted as concern. (bundle.py picked the later MigrateV2 by 9C4nRv... at +1 slot, known quirk; rule11.py authoritative.)
- Created: 2026-11-04T15:23:45Z, slot 465351009, tx 32sXGxjytv1o4vq8RC6u1ANJtBkfSVyZJVKvxy4MsHHnon696KePtQ8g4RaAKyfF95c7mF67jdhtnRKJVsHuCnUS; curve E3AcUN3S9cJc3gjjtrvNSBFFoLHFruqJFSUZFVFjXDvh; creator D2AjvHhxtRJkrL38cPtfAT2hTv9vkfDpVhabackE9TpN
- Rule 1: creation slot 11 buying wallets (creator counted, migration tx and pool excluded), 100.0 % of tradable supply, wallets to reach 30 %: 3; slots 0-2: 11 wallets, 100.0 %. **HIT**
- Rule 2: migration 4zDdhRiqRZiYPkF5cqfVGjRcj6Z5HhWB6YB4P2wMbUxRhCPCXsqscMsnTFP7FL7qb3dRYS4aDtwEJkQNXbssdxSg, same slot as creation, creator not co-signer. Not hit.
- Rule 11: migration slot 465351009 (+0 slots), window +0..+2: 16 buyers, 108.27 % of tradable supply, wallets to reach 80 %: 8. Not hit.
- Rule hit: **Rule 1**
- Raw: research/raw-20261104/c212/bundle_Donkey-APj5.json, rule11_Donkey-APj5.json, b_*.log, r11log_Donkey-APj5.txt
