# KILLED-SCOUT MUTTAPE-2Squ (2SquPKDVfGw9rBFBBZjJ2QPzSaDYjfwBY72FGBHZpump)
Cycle 269 (06:0x Stockholm, 2026-11-07), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11), measured 2026-11-07T05:06:12Z-05:06:29Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: 2SquPKDVfGw9rBFBBZjJ2QPzSaDYjfwBY72FGBHZpump
- PumpSwap pool: 4Srofe2xgVd7ji81kwnR8ESvXVWXUpPipo9vTQuxFT4Q (https://dexscreener.com/solana/4Srofe2xgVd7ji81kwnR8ESvXVWXUpPipo9vTQuxFT4Q)
- DexScreener ~05:05Z (scan2.py): MUTTAPE, age ~92 min, liq ~55.5k USD, 1h vol ~289k, h1 +44 %, FDV ~479k. (Different mint from the c154 MUTTAPE rcyt kill.)
- Created: 2026-11-07T03:33:47Z, slot 466362592, tx QFMxPR84...; curve HZ46wgNw...; curve creator 6RCjnv6v58yqGoyGuUdWxR6sYHjzvYmDCLrTDdBsHdGH
- Rule 1: creation slot 2 buying wallets (creator 6RCjnv... counted + HCsfJh2q... 789,568,652 tokens), 100 % of tradable supply, wallets to reach 30 %: 1 (HCsfJh2q... alone ~99.6 %). Slots 0-2 identical. **HIT**
- Rule 2: authoritative MigrateV2 wqKHit4H... in the SAME slot as creation (dslot 0), signer DCLc9vFd... (fee payer of a creation-slot tx), creator not co-signer. Not hit (formal co-sign condition not met).
- Rule 11: migration slot 466362592 (+0 slots), window +0..+2: 6 buyers, 104.91 % of tradable, wallets to reach 80 %: 1. **HIT** (one wallet took the whole curve in the creation/migration slot; t39u hard).
- Rule hit: **Rule 1, Rule 11**
- Raw: research/raw-20261107/c269/bundle_MUTTAPE.json, rule11_MUTTAPE.json, sigs_MUTTAPE.json, bun_MUTTAPE.log, r11_MUTTAPE.log
