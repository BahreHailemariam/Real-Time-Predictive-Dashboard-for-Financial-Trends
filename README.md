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
