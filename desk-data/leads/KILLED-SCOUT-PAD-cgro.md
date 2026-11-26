# KILLED-SCOUT PAD-cgro (cgroWcQiEf73UsPPhvBsf81Kcn88EKrfFUSfE7Jpump)
Cycle 241 (22:10 Stockholm, 2026-11-05), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 with fixed c6 locator), measured 2026-11-05T21:11:48Z-2026-11-05T21:12:36Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: cgroWcQiEf73UsPPhvBsf81Kcn88EKrfFUSfE7Jpump
- PumpSwap pool: 5ymgZfTy1BRkyr39i3PDxBpCR14cGyg1edoLy8JjTZ7Z (https://dexscreener.com/solana/5ymgZfTy1BRkyr39i3PDxBpCR14cGyg1edoLy8JjTZ7Z)
- DexScreener/GT ~21:10Z: PAD (different mint from c233 PAD 94M7), pool 5ymgZfTy..., age ~1144 min at scan (curve created 2026-11-05 02:07:24Z, creation slot 465530755, creator B1iHXP...; migrated in the SAME slot), found via gtslow.py: GT reserve ~1.12M, FDV ~200M, 1h vol ~6.7k (2,295 buys / 69 sells by 1,773 buyers / 3 sellers), 24h vol ~638k. Creator bought 100 % of tradable in the create tx, k30 = 1 -> Rule 1 HIT. MigrateV2 3v5DzV... same slot, signed by the creator -> Rule 2 HIT. Rule 11: window 4 buyers 125.65 %, k80 = 1 -> HIT. Same single-creator template as AODT c236 / USRP c239 / PAD c233 / NADF c230. bundle.py locator picked a later no-op MigrateV2 by 9C4nRv... (+3 slots, known quirk); rule11.py authoritative.
- Created: 2026-11-05T02:07:24Z, slot 465530755, tx 4jTCjmjnHb4dyCaAUpo5oN7QwKQbNy2t989ASrJ3Se2XdvNfmcmVqTQe1a4Gt1D5xLmiUxDzjH41iTP3PSbYNDMQ; curve AbUtk6utoZv3HZSSedA9usFqJwJL6XkVpp9gnX9V6C5i; creator B1iHXPsV9PV1aUaP5FM9DuojbtAVAyArUoN618fDKeye
- Rule 1: creation slot 1 buying wallets (creator counted, migration tx and pool excluded), 100.0 % of tradable supply, wallets to reach 30 %: 1; slots 0-2: 1 wallets, 100.0 %. **HIT**
- Rule 2: migration 3v5DzVr3bLAWW7vY9fjdHvwXcH5KzenCvscnQ2eWmGnEXZx7kNcS13fgUSqzW35UiaiHxcNKtPA8DLKiSnoSxSkY, same slot as creation, creator co-signed. **HIT**
- Rule 11: migration slot 465530755 (+0 slots), window +0..+2: 4 buyers, 125.65 % of tradable supply, wallets to reach 80 %: 1. **HIT**
- Rule hit: **Rule 1, Rule 2, Rule 11**
- Raw: research/raw-20261105/c241/bundle_PAD-cgro.json, rule11_PAD-cgro.json, b_*.log, r11log_PAD-cgro.txt
