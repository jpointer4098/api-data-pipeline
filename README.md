# API Data Pipeline

Python script that fetches top cryptocurrencies from CoinGecko, formats the data, and stores it in CSV + SQLite.

### Features
- Real-time crypto prices
- Saves data to:
  - `data/crypto_data.csv`
  - `database/crypto.db`

### Run it:
```bash
pip install -r requirements.txt
python main.py
