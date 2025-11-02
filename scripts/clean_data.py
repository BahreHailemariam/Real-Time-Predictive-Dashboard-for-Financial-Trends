"""
clean_data.py
-------------
Cleans raw financial data and prepares it for analysis.
"""

import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Perform standard cleaning operations on financial data."""
    print("🧹 Cleaning data...")

    df = df.drop_duplicates()
    df = df.dropna(subset=["Close"])

    # Ensure chronological order
    df = df.sort_values("Date")

    # Convert data types
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    print(f"✅ Cleaned data — {df.shape[0]} rows remaining.")
    return df

if __name__ == "__main__":
    df = pd.read_csv("../data/raw/apple_stock.csv")
    df = clean_data(df)
    df.to_csv("../data/processed/apple_stock_cleaned.csv", index=False)
