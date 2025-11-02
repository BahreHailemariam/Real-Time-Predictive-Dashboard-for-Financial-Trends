"""
load_data.py
-------------
Loads raw financial/stock data from a CSV file or an API endpoint.
"""

import pandas as pd
import yfinance as yf

def load_from_csv(path: str) -> pd.DataFrame:
    """Load stock data from a local CSV file."""
    try:
        df = pd.read_csv(path, parse_dates=["Date"])
        print(f"✅ Loaded data from {path} — {df.shape[0]} rows.")
        return df
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return pd.DataFrame()

def load_from_yahoo(ticker: str, period="1y") -> pd.DataFrame:
    """Load stock data directly from Yahoo Finance."""
    df = yf.download(ticker, period=period)
    df.reset_index(inplace=True)
    print(f"📥 Downloaded {ticker} data — {df.shape[0]} rows.")
    return df

if __name__ == "__main__":
    data = load_from_yahoo("AAPL", "6mo")
    data.to_csv("../data/raw/apple_stock.csv", index=False)
