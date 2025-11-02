"""
feature_engineering.py
----------------------
Creates new financial features (technical indicators).
"""

import pandas as pd

def add_technical_indicators(df: pd.DataFrame) -> pd.DataFrame:
    """Add moving averages, volatility, and RSI."""
    print("⚙️ Generating features...")

    df["MA_7"] = df["Close"].rolling(window=7).mean()
    df["MA_21"] = df["Close"].rolling(window=21).mean()
    df["Volatility"] = df["Close"].pct_change().rolling(window=7).std()
    df["Returns"] = df["Close"].pct_change()
    df["Lag_1"] = df["Close"].shift(1)
    df["Lag_2"] = df["Close"].shift(2)

    print(f"✅ Added technical indicators — {df.shape[1]} columns total.")
    return df

if __name__ == "__main__":
    df = pd.read_csv("../data/processed/apple_stock_cleaned.csv")
    df = add_technical_indicators(df)
    df.to_csv("../data/processed/apple_stock_features.csv", index=False)
