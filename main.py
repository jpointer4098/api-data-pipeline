import os
import requests
import pandas as pd
import sqlite3
from datetime import datetime, timezone

CSV_PATH = "data/crypto_data.csv"
DB_PATH = "database/crypto.db"
API_URL = "https://api.coingecko.com/api/v3/coins/markets"

def setup_folders():
    os.makedirs("data", exist_ok=True)
    os.makedirs("database", exist_ok=True)

def fetch_data(vs_currency="usd", limit=10):
    params = {
        "vs_currency": vs_currency,
        "order": "market_cap_desc",
        "per_page": limit,
        "page": 1,
        "sparkline": False
    }
    try:
        res = requests.get(API_URL, params=params, timeout=10)
        res.raise_for_status()
        return res.json()
    except requests.RequestException as e:
        print(f"[!!] Couldn’t fetch data: {e}")
        return []

def format_data(raw):
    if not raw:
        return pd.DataFrame()
    return pd.DataFrame([{
        "id": coin.get("id"),
        "symbol": coin.get("symbol"),
        "name": coin.get("name"),
        "current_price": coin.get("current_price"),
        "market_cap": coin.get("market_cap"),
        "last_updated": coin.get("last_updated")
    } for coin in raw])

def dump_csv(df, path=CSV_PATH):
    df.to_csv(path, index=False)
    print(f"[+] Saved CSV → {path}")

def dump_sqlite(df, db_path=DB_PATH):
    try:
        conn = sqlite3.connect(db_path)
        df.to_sql("crypto_prices", conn, if_exists="replace", index=False)
        conn.close()
        print(f"[+] Data stored in → {db_path}")
    except sqlite3.Error as e:
        print(f"[!!] DB error: {e}")

def main():
    setup_folders()
    print("[*] Pulling crypto stats...")
    raw = fetch_data()
    df = format_data(raw)
    if df.empty:
        print("[x] Nothing pulled.")
        return
    print(f"[✓] Data pulled @ {datetime.now(timezone.utc).isoformat()}")
    dump_csv(df)
    dump_sqlite(df)
    print("[✓] Done.")

if __name__ == "__main__":
    main()
