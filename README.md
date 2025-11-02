# 📈 Real-Time Predictive Dashboard for Financial Trends

This project builds an **interactive, real-time predictive dashboard** that analyzes and forecasts financial and stock market trends using **machine learning**, **streaming data**, and **Power BI** visualizations.  
It enables decision-makers to monitor market indicators, detect anomalies, and project future movements dynamically.

---

## 🚀 Project Overview

The Real-Time Predictive Dashboard integrates **data ingestion**, **machine learning forecasting**, and **visual analytics** into a seamless system that updates automatically.  
It helps financial analysts, traders, and business leaders identify patterns and make data-driven decisions.

**Key Features:**
- Real-time data pipeline with live updates.
- Predictive modeling using regression and time-series algorithms.
- Interactive Power BI dashboard with KPIs and trend visuals.
- Automated daily or hourly refresh with alerts.

---

## 🧩 Business Problem

Financial data is highly volatile, and static dashboards cannot capture rapid market movements.  
Organizations need **automated, predictive, and self-refreshing dashboards** that show:
- Stock price forecasts  
- Portfolio risk levels  
- Trading volume anomalies  
- Sector-wise market performance

This project solves that need with a modular and automated analytics system.

---

## 🧠 Project Architecture

Data Source → Data Ingestion (API/Streaming) → Data Cleaning (Python) <br />
↓<br />
Feature Engineering → Model Training (ML/Forecasting) → Predictions<br />
↓<br />
Power BI Dashboard → Real-Time KPIs & Forecast Visuals → Alerts & Notifications


---

## ⚙️ Tech Stack

| Layer | Tools / Technologies |
|-------|----------------------|
| **Data Ingestion** | Python, yfinance, Alpha Vantage API, Kafka (optional) |
| **Processing & Modeling** | pandas, scikit-learn, statsmodels, Prophet |
| **Database** | SQL Server / PostgreSQL |
| **Visualization** | Power BI (Live Connection / DirectQuery) |
| **Automation** | SQL Server Agent / Airflow for scheduled refresh |
| **Deployment** | Streamlit / Power BI Service |

---

## 📊 Workflow

### 1. Data Extraction
- Pull financial data from APIs (e.g., Yahoo Finance, Alpha Vantage).
- Stream live updates using WebSocket or Kafka.

### 2. Data Cleaning
- Handle missing prices, adjust stock splits, and convert timestamps.
- Apply data normalization for volatility indicators.

### 3. Feature Engineering
- Compute technical indicators: RSI, EMA, MACD, Bollinger Bands.
- Generate rolling averages and lag features for time-series models.

### 4. Predictive Modeling
- Apply regression or Prophet models to forecast short-term trends.
- Evaluate with RMSE, MAPE, and visualize model accuracy.

### 5. Visualization
- Build Power BI dashboards with dynamic KPIs:
  - **Stock Performance Overview**
  - **Price Forecast vs Actual**
  - **Market Sector Heatmap**
  - **Volatility and Anomaly Detection**

### 6. Automation
- Schedule refreshes with SQL Server Agent or Airflow.
- Send email/SMS alerts for significant market movements.

---

## 🧮 Example KPIs & Metrics
- **Predicted Closing Price**
- **Volatility Index (VIX)**
- **Daily Gain/Loss %**
- **Prediction Error (RMSE)**
- **Moving Average Crossover Alerts**

---

## 📁 Project Structure
```
Real-Time-Financial-Dashboard/
│
├── data/
│ ├── raw/
│ └── processed/
│
├── scripts/
│ ├── load_data.py
│ ├── clean_data.py
│ ├── feature_engineering.py
│ ├── train_model.py
│ └── app.py
│
├── dashboard/
│ └── PowerBI_Report_Spec.md
│
├── docs/
│ └── Workflow_Spec.md
│
├── requirements.txt
└── README.md
```


---

## 🧠 Example DAX Measures (Power BI)
```DAX
Total Gain/Loss % = 
DIVIDE(SUM('StockData'[Close]) - SUM('StockData'[Open]), SUM('StockData'[Open])) * 100

Predicted Error (RMSE) = 
SQRT(AVERAGEX('ModelResults', POWER('ModelResults'[Actual] - 'ModelResults'[Predicted], 2)))

```

## 📅 Automation Example (SQL Server Agent)
```sql
-- Run daily Power BI data refresh
EXEC msdb.dbo.sp_start_job N'Refresh_Financial_Predictions_Job';
```

## 🧠 Future Enhancements

- Integrate sentiment analysis from financial news.

- Add anomaly detection using LSTM models.

- Deploy as a Streamlit or Flask web app.

- Enable push notifications for key price events.

  
## 🧰 Dependencies
```
pandas
numpy
yfinance
scikit-learn
prophet
statsmodels
matplotlib
sqlalchemy
streamlit
plotly
requests
```

📈 Power BI Dashboard Preview
### 🏦 1. Market Overview
**Objective:** Provide a snapshot of key market indicators, stock performance, and financial health.

**Key Visuals:**
- KPI Cards (Market Cap, Daily Volume, Gain/Loss %)
- Line Chart for closing prices (S&P 500, NASDAQ, Dow Jones)
- Treemap for sector performance
- Heatmap for daily/hourly stock changes

**Business Questions:**
- Which sectors outperform the market?
- What’s the portfolio return rate today?
- How do market indices trend weekly/monthly?

**Example DAX:**
```DAX
Total Gain/Loss % =
DIVIDE(SUM('StockData'[Close]) - SUM('StockData'[Open]), SUM('StockData'[Open])) * 100
```

---
### 🔮 2. Predictive Analytics
**Objective:** Forecast stock prices, index values, or portfolio returns.

**Key Visuals:**
- Forecast Line Chart (Actual vs Predicted)
- Confidence Interval Ribbon (Prophet/ARIMA output)
- Filter by Ticker or Forecast Period
- Table with Predicted vs Actuals (RMSE, MAPE)

**Metrics:**
- Predicted Close Price
- Forecast Error (RMSE)
- Confidence Interval ±%

**Example DAX:**
```DAX
Forecast Accuracy (%) =
100 - (AVERAGE('ModelResults'[MAPE]) * 100)
```

---
### ⚠️ 3. Risk & Volatility
**Objective:** Assess portfolio risk via volatility and dispersion.

**Key Visuals:**
- Line Chart for rolling standard deviation
- Bar Chart comparing sector volatility
- Variance Gauge and Scatter (Sharpe ratio)

**Example DAX:**
```DAX
Volatility (Std Dev) =
STDEVX.P('StockData', 'StockData'[Close])
```

---
### 🚨 4. Anomaly Detection
**Objective:** Identify outlier price movements and abnormal deviations.

**Key Visuals:**
- Scatter Plot (Predicted vs Actual)
- Conditional Table with deviation threshold
- KPI Alerts and Bar Charts for spikes/dips

**Example DAX:**
```DAX
Anomaly Score (Z-Score) =
DIVIDE(
    'StockData'[Close] - AVERAGE('StockData'[Close]),
    STDEV.P('StockData'[Close])
)
```

---
