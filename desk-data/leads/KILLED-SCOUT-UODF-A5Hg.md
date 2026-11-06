# KILLED-SCOUT UODF-A5Hg (A5HgibiDoeGHrJeeBPGJHDFsBkM2uwodQAG1TJ2spump)
Cycle 224 (05:05 Stockholm, 2026-11-05), bundler pre-check (rule 1 cap 15 wallets, creator buy counted, rule 2, Rule 11 with fixed c6 locator), measured 2026-11-05T04:03:47Z-2026-11-05T04:04:26Z (UTC; Stockholm = UTC+1). Engagement: paper. No lead ID, no ticket.

- Mint: A5HgibiDoeGHrJeeBPGJHDFsBkM2uwodQAG1TJ2spump
- PumpSwap pool: HwRotpaf2JLhbPGaSz8uEytToZkwZrxxZBLfv3ZkREJu (https://dexscreener.com/solana/HwRotpaf2JLhbPGaSz8uEytToZkwZrxxZBLfv3ZkREJu)
- DexScreener/GT ~04:03Z: UODF, pool HwRotp..., age ~777 min (curve created 2026-11-04 15:05:55Z, slot 465346017, creator H4FxiW...), found via GT (gtslow): GT reserve ~3.13M USD, FDV ~1.44B, 1h vol ~56.4k, h1 3,493 buys / 270 sells by 20 buyers / 13 sellers (bot-like). Creator bought 100 % of tradable in the create tx (k30 = 1); authoritative MigrateV2+CreatePool 31MBG6... in the creation slot signed by the creator -> rule 2 HIT; Rule 11 window 2 buyers 125.94 %, k80 = 1 -> HIT. Same single-creator template as USOE/USPR/SARP. bundle.py locator picked a later no-op MigrateV2 2RBXTn... by 9C4nRv... (+3 slots, known quirk); rule11.py authoritative.
- Created: 2026-11-04T15:05:55Z, slot 465346017, tx 2XR1D3tPa8ZUpdRFcHkQ9PLpjLovrYgpqbNo3pgMqi9j4uwPeZdtUxSwyB5KDasVz5zmDDE7S62P8hNQyxxoh4Qk; curve 9BkXxvKP4cpptSYo73SsX5KuNZyM3E99gduKF95WwhG8; creator H4FxiWQymjxU2MowG2LBrogTdjsHLMhodyfdXMJYBTAG
- Rule 1: creation slot 1 buying wallets (creator counted, migration tx and pool excluded), 100.0 % of tradable supply, wallets to reach 30 %: 1; slots 0-2: 1 wallets, 100.0 %. **HIT**
- Rule 2: migration 31MBG61MGEfgpGNMypHSCpcXLa9FW6taTGfmjDKjv2VEC3kG3mAx6AM4FQKynVEZJAU2ruMXjndFA9VuZeozizqn, same slot as creation, creator co-signed. **HIT**
- Rule 11: migration slot 465346017 (+0 slots), window +0..+2: 2 buyers, 125.94 % of tradable supply, wallets to reach 80 %: 1. **HIT**
- Rule hit: **Rule 1, Rule 2, Rule 11**
- Raw: research/raw-20261105/c224/bundle_UODF-A5Hg.json, rule11_UODF-A5Hg.json, b_*.log, r11log_UODF-A5Hg.txt
