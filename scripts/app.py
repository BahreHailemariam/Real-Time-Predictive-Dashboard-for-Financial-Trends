"""
app.py
------
Flask web application to display financial predictions.
"""

from flask import Flask, jsonify
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

@app.route("/")
def home():
    return "💹 Real-Time Financial Dashboard API is running."

@app.route("/predict")
def predict():
    """Dummy prediction endpoint."""
    data = {"Next_Day_Prediction": 189.75, "Symbol": "AAPL"}
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
