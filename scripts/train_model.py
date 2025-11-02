"""
train_model.py
---------------
Trains a machine learning model to predict stock closing prices.
"""

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error

def train_model(df: pd.DataFrame):
    """Train and evaluate a regression model."""
    print("🤖 Training model...")

    df = df.dropna()
    X = df[["MA_7", "MA_21", "Volatility", "Lag_1", "Lag_2"]]
    y = df["Close"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
    model = LinearRegression()
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)
    mse = mean_squared_error(y_test, preds)

    print(f"✅ Model trained — MAE: {mae:.4f}, RMSE: {mse**0.5:.4f}")
    return model

if __name__ == "__main__":
    df = pd.read_csv("../data/processed/apple_stock_features.csv")
    train_model(df)
