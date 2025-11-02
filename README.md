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

**Key Visuals:** <br />

**📊 KPI Cards:**

  - Total Market Cap

  - Average Daily Volume

  - Overall Gain/Loss %

**📈 Line Chart:** Daily closing prices of major indices (S&P 500, NASDAQ, Dow Jones).

**💹 Treemap:** Sector performance (Technology, Healthcare, Finance, etc.).

**🧭 Heatmap:** Daily or hourly stock performance changes by sector.
**Business Questions:**
- Which sectors outperform the market?
- What’s the portfolio return rate today?
- How do market indices trend weekly/monthly?

**Example DAX:**
```DAX
Total Gain/Loss % =
DIVIDE(SUM('StockData'[Close]) - SUM('StockData'[Open]), SUM('StockData'[Open])) * 100

Average Volume =
AVERAGE('StockData'[Volume])

```

---
### 🔮 2. Predictive Analytics
**Objective:** Forecast stock prices, index values, or portfolio returns.

**Key Visuals:**

- **🔁 Forecast Line Chart:** Actual vs. Predicted Closing Price over time.

- **📊 Confidence Interval Ribbon:** Prophet or ARIMA forecast with upper/lower bounds.

- **🧩 Dynamic Filter:** Choose specific tickers or forecast periods (1 day, 7 days, 30 days).

- **📋 Table View:** Displays predicted values alongside actuals and errors (RMSE, MAPE).

**Metrics Displayed:**

- Predicted Close Price

- Forecast Error (RMSE)

- Next-Day Change %

- Confidence Interval (±%)

**Business Questions Answered:**

- What is the expected price movement tomorrow or next week?

- How accurate is the prediction model?

- Which stocks show stable vs volatile forecasts?

**Example DAX Measures:**
```DAX
Prediction Error (RMSE) =
SQRT(AVERAGEX('ModelResults',
    POWER('ModelResults'[Actual] - 'ModelResults'[Predicted], 2)
))

Forecast Accuracy (%) =
100 - (AVERAGE('ModelResults'[MAPE]) * 100)

```

---
### ⚠️ 3. Risk & Volatility
**Objective:** Assess portfolio risk via volatility and dispersion.

**Key Visuals:**
- **📉 Line Chart:** Rolling standard deviation of closing prices.

- **📊 Bar Chart:** Comparison of volatility across stocks/sectors.

- **💡 Variance Gauge:** Measures deviation from mean performance.

- **🧾 Scatter Plot:** Risk vs. Return relationship (Sharpe ratio analysis).

**Metrics Displayed:**

- Rolling 30-day Volatility

- Standard Deviation

- Beta Coefficient (vs Market Index)

- Sharpe Ratio

**Business Questions Answered:**

- Which stocks carry the highest volatility risk?

- How does my portfolio’s risk compare to the benchmark index?

- What are the potential downside and drawdown scenarios?

**Example DAX Measures:**
```DAX
Volatility (Std Dev) =
STDEVX.P('StockData', 'StockData'[Close])

Sharpe Ratio =
DIVIDE(
    (AVERAGE('StockData'[Return]) - [Risk-Free Rate]),
    STDEVX.P('StockData', 'StockData'[Return])
)

```

---
### 🚨 4. Anomaly Detection
**Objective:** Identify outlier price movements and abnormal deviations.

**Key Visuals:**
- **📊 Scatter Plot:** Predicted vs. Actual price — highlighting anomalies.

- **🧠 Conditional Formatting Table:** Flags records where deviation > defined threshold.

- **⚡ KPI Alerts:** Auto-alert on large deviations (e.g., 5%+ price change).

- **📈 Bar Chart:** Day-over-day difference highlighting spikes or dips.

**Metrics Displayed:**

- Outlier Count (Daily)

- % Change from Expected Price

- Alert Frequency

- Anomaly Score (Z-score)

**Business Questions Answered:**

- Which stocks deviated most from forecasted prices?

- Are there abnormal trading volume patterns?

- When did unusual market movements occur?

**Example DAX Measures:**
```DAX
Anomaly Score (Z-Score) =
DIVIDE(
    'StockData'[Close] - AVERAGE('StockData'[Close]),
    STDEV.P('StockData'[Close])
)

Outlier Flag =
IF(ABS([Anomaly Score (Z-Score)]) > 2, "⚠️ Outlier", "Normal")

```

---
### 🧭 Interactivity & Alerts
- **Slicers:** Date range, stock ticker, sector, volatility range
- **Drillthrough Pages:** From Market Overview → Risk View → Predictive Analytics
- **Tooltips:** Hover to view additional details (predicted change %, confidence range)
- **Auto Refresh:** Dashboard refreshes hourly via Power BI Service + SQL Agent job
---
🔔 Alerts & Notifications

- Power BI data alerts trigger emails when:

  - Price deviation > ±3%

  - Volatility exceeds threshold

  - Forecast accuracy drops below 90%


### 📊 Insights Delivered

- Detects short-term opportunities based on AI-driven forecasts.

- Highlights underperforming sectors or high-risk assets in real time.

- Supports proactive decision-making with predictive and anomaly-based intelligence.


## 💡 Key Insight Example

“The Prophet model predicted a 2.4% increase in S&P 500 weekly closing prices with a confidence interval of ±1.1%, correlating strongly (r=0.89) with recent tech sector gains.”

## 👥 Contributors

- Data Engineering & Modeling — Data Science Team

- Dashboard Development — BI Analyst Team

- Deployment — DevOps Engineer

## 📜 License

This project is licensed under the **MIT License**.
## 🏁 How to Run Locally
```bash
# Clone repository
git clone https://github.com/your-username/real-time-financial-dashboard.git
cd real-time-financial-dashboard

# Install dependencies
pip install -r requirements.txt

# Run scripts
python scripts/load_data.py
python scripts/train_model.py
streamlit run scripts/app.py
```
