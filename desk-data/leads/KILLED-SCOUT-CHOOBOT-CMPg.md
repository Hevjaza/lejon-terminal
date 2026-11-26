# KILLED-SCOUT CHOOBOT-CMPg (CMPgvtyfyQwXGeT8hDFGqegm5ehvJnmti7LMadjvpump)
Cycle 192 (21:01 Stockholm, 2026-11-03), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11), measured 2026-11-03T20:03Z-20:04Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: CMPgvtyfyQwXGeT8hDFGqegm5ehvJnmti7LMadjvpump
- PumpSwap pool: E5X7xf7ro9CUkkFwetyJBU47gLBQVaUH3HM8Pcb5Cu7k (https://dexscreener.com/solana/E5X7xf7ro9CUkkFwetyJBU47gLBQVaUH3HM8Pcb5Cu7k)
- Market data (DexScreener ~20:02Z: age ~63 min, liq ~27.5k USD, 1h vol ~152k USD, FDV ~125k, h1 -1.4 %.)
- Created: 2026-11-03T18:59:02Z, slot 465008093; curve 3rhd3Pbw...; curve creator HpqiWyYrGFJ6SU2J9T2UrXBB1GXYW63rWmpscUeZCaJ4 (dev buy 1.31 %); create tx signers 2; 39 curve sigs.
- Rule 1: creation slot 18 buying wallets (creator counted) bought 100 % of tradable supply; top 15 = 96.84 %; wallets to reach 30 %: 4; two multi-wallet buy txs with 10 and 7 signers (bSZbcMVR..., 6DyhmMwP...). **HIT**
- Rule 2: MigrateV2 1ySr5PXW... in the creation slot (+0) signed by the creator HpqiWy...; coordinated 10-/7-signer buys in the same slot -> **HIT**
- Rule 11: window +0..+2: 26 buyers, 112.72 % of tradable, wallets to reach 80 %: 10 (not counted strictly as a small cluster).
- bundle.py's migration locator picked the later no-op MigrateV2 (+2 slots, 9C4nRv...) = known quirk; rule11.py authoritative; verdict unaffected.
- Rule hit: **Rule 1, Rule 2**
- Raw: research/raw-20261103/c192/bundle_CHOO.json, rule11_CHOO.json, b_CHOO.log, r11log_CHOO.txt
