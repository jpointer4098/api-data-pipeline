# API Data Pipeline

A fast Python pipeline that pulls real-time crypto market data from the CoinGecko API, cleans it with pandas, and stores it in both CSV and SQLite formats.

### 🧠 What It Does
- Extracts top 10 coins by market cap
- Formats fields like name, price, market cap, and timestamp
- Saves clean data to:
  - `data/crypto_data.csv`
  - `database/crypto.db` (table: `crypto_prices`)

### 🚀 Tech Stack
- Python 3
- requests
- pandas
- sqlite3

### ▶️ How to Run

```bash
pip install -r requirements.txt
python main.py

