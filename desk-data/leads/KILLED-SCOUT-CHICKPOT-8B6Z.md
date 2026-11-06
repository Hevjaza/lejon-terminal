# KILLED-SCOUT CHICKPOT-8B6Z (8B6ZZAC2FQ7AJrZPz7veXJrod5t2MG1C5MZBLNbUpump)
Cycle 202 (07:10 Stockholm, 2026-11-04), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 with fixed c6 locator), measured 2026-11-04T06:11:58Z-2026-11-04T06:12:15Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: 8B6ZZAC2FQ7AJrZPz7veXJrod5t2MG1C5MZBLNbUpump
- PumpSwap pool: 4jAPU7rXQ26g4A56uQY73n3FAef5UZYpV7nx28HWuCkv (https://dexscreener.com/solana/4jAPU7rXQ26g4A56uQY73n3FAef5UZYpV7nx28HWuCkv)
- DexScreener/GT ~06:11Z: ChickPot (CHICKPOT), pool 4jAPU7..., age ~111 min (pool created 2026-11-04 04:20:15Z = creation slot), DS liq ~75.8k (399.3 SOL quote side), FDV ~850k, 1h vol ~219k, DS h1 1334 buys / 992 sells, h1 +5 %; DS profile present. Found via DS scan2. Pattern: whole bonding curve emptied in the creation slot 465165259: creator 9VXc9N... dev buy 0.45 %, then HCsfJh... bought 99.55 % of tradable in one tx (k30 = 1, k80 = 1); MigrateV2+CreatePool 5kVwPY... in the creation slot signed by DCLc9v... (slot-0 fee payer, not the curve creator) -> rule 2 not hit strictly. bundle.py located the later no-op MigrateV2 by 9C4nRv... (+1 slot) = known quirk; rule11.py authoritative. Rule 11 window 9 buyers 107.08 %, k80 = 1 -> HIT (one wallet bought the whole curve in the migration slot).
- Created: 2026-11-04T04:20:15Z, slot 465165259, tx 3siEfx4Z63NrTqab5ojkgNcp64dUgnpB5hEa5bbnqxEgKfxaNjrix3nY9boR4VjZ9VFBdeRSSi5u32dr38bnaTBa; curve J4faYqdRT8S2MngM5zzmBtG5KEffLwbX7VN3YsRANvQP; creator 9VXc9N5gG3KjpXypR5svC64rtMBxBT2a7vWNfQRX9FCM
- Rule 1: creation slot 2 buying wallets (creator counted, migration tx and pool excluded), 100.0 % of tradable supply, wallets to reach 30 %: 1; slots 0-2: 2 wallets, 100.0 %. **HIT**
- Rule 2: migration 5kVwPYpEtd9zZ4KY6x3vFgs1JEWuCWkzFFsprMNeV6pe6T7puysAxmLRdafs7X7MSEqUPzCExtx9gGEwpcq5Kdag, same slot as creation, creator not co-signer. Not hit.
- Rule 11: migration slot 465165259 (+0 slots), window +0..+2: 9 buyers, 107.08 % of tradable supply, wallets to reach 80 %: 1. **HIT**
- Rule hit: **Rule 1, Rule 11**
- Raw: research/raw-20261104/c202/bundle_CHICKPOT-8B6Z.json, rule11_CHICKPOT-8B6Z.json, b_*.log, r11log_CHICKPOT-8B6Z.txt
