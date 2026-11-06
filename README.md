# 🦁 Lejon Terminal – PAPER MODE

Mobil-först, **endast läsande** instrumentpanel för PumpGrok-paperdesken.
Inga riktiga pengar, ingen plånbok, inga privata nycklar, inga order.

**Huvudfil för Streamlit Community Cloud:** `app.py` (repo-root).

## Streamlit Community Cloud

1. New app → repo `Hevjaza/lejon-terminal` → Branch `main` → Main file path: `app.py`
2. Under **Advanced settings → Secrets** lägg in (välj ett):

```toml
SPIDER_PASSWORD = "välj-ett-starkt-lösen"
```

eller

```toml
LEJON_PASSWORD = "välj-ett-starkt-lösen"
```

3. Deploy. Appen vägrar visa data utan lösenord i Secrets.
4. Logga in med samma lösenord i webbläsaren.

Data läses från `desk-data/` i repot (ögonblicksbild). Uppdatera den lokalt med
`/workspace/trading-desk/sync-lejon.sh` (eller kopiera manuellt) och pusha.

## Lokalt

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
# Lokalt kan du också använda miljövariabel eller .spider_password —
# på Cloud ska lösenordet endast ligga i st.secrets.
export SPIDER_PASSWORD='välj-ett-starkt-lösen'
streamlit run app.py
```

Öppna http://localhost:8501

## Säkerhet

- Committa **aldrig** `.env`, `.spider_password`, `.lejon_password`, RPC-URL:er, API-nycklar eller plånboksnycklar.
- Appen är strikt read-only mot desk-filer. PAPER MODE only.
