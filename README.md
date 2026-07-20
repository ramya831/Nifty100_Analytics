# 📊 Nifty100 Analytics Project

A comprehensive financial analytics platform for Nifty100 companies built using **Python**, **Pandas**, **SQLite**, **Plotly**, and **Streamlit**.

The project performs ETL processing, financial ratio analysis, valuation analysis, and provides an interactive dashboard for exploring company performance.

---

# 🚀 Features

- ETL Pipeline
- Data Validation
- SQLite Database
- Financial Ratio Analysis
- Profitability Analysis
- Liquidity Analysis
- Leverage Analysis
- Efficiency Analysis
- Growth Analysis
- Valuation Module
- Interactive Streamlit Dashboard
- Company Screener
- Peer Comparison
- Trend Analysis
- Sector Analysis
- Capital Allocation Map
- Annual Reports Viewer
- CSV Export

---

# 🛠 Technologies Used

- Python
- Pandas
- SQLite
- SQL
- Streamlit
- Plotly
- OpenPyXL
- Git
- GitHub

---

# 📂 Project Structure

```
Nifty100_Analytics/
│
├── config/
├── data/
│   └── raw/
├── db/
├── notebooks/
├── output/
│   ├── valuation_summary.xlsx
│   └── valuation_flags.csv
├── reports/
├── src/
│   ├── analytics/
│   │   └── valuation.py
│   ├── dashboard/
│   │   ├── app.py
│   │   ├── pages/
│   │   │   ├── 01_home.py
│   │   │   ├── 02_profile.py
│   │   │   ├── 03_screener.py
│   │   │   ├── 04_peers.py
│   │   │   ├── 05_trends.py
│   │   │   ├── 06_sectors.py
│   │   │   ├── 07_capital.py
│   │   │   └── 08_reports.py
│   │   └── utils/
│   │       └── db.py
│   └── etl/
├── tests/
├── README.md
└── requirements.txt
```

---

# 📅 Sprint Progress

## Sprint 1

- Environment Setup
- Project Structure
- Data Collection
- ETL Pipeline

## Sprint 2

- SQLite Database
- Financial Ratios
- SQL Analysis
- Reports
- Testing

## Sprint 3

- Screener Logic
- Peer Comparison Engine
- Financial Metrics
- Composite Score

## Sprint 4

- Streamlit Dashboard
- Company Profile
- Screener
- Peer Comparison
- Trend Analysis
- Sector Analysis
- Capital Allocation
- Annual Reports
- Valuation Module
- Dashboard Integration
- Documentation

---

# 📊 Dashboard Screens

## 🏠 Home

- Summary KPI Cards
- Sector Distribution
- Top Companies Table
- Year Selector

---

## 🏢 Company Profile

- Company Details
- Financial KPI Cards
- Revenue Chart
- ROE Trend
- Pros & Cons

---

## 🔍 Screener

- Financial Metric Filters
- Preset Filters
- Live Results
- CSV Download

---

## 👥 Peer Comparison

- Peer Group Selection
- Radar Chart
- KPI Comparison Table

---

## 📈 Trend Analysis

- Multi-Metric Trends
- Company Search
- 10-Year Analysis

---

## 🏭 Sector Analysis

- Bubble Chart
- Sector KPIs
- Revenue vs ROE Analysis

---

## 🌳 Capital Allocation

- Treemap Visualization
- Capital Allocation Patterns

---

## 📄 Annual Reports

- Company Search
- Available Reports
- Report Links

---

# 📈 Valuation Module

The valuation module calculates:

- FCF Yield
- P/E Analysis
- P/B Analysis
- EV/EBITDA
- Sector Median P/E
- Valuation Flags

Outputs generated:

- valuation_summary.xlsx
- valuation_flags.csv

---

# ▶️ Running the Project

## Clone Repository

```bash
git clone https://github.com/ramya831/Nifty100_Analytics.git
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Create Database

```bash
python create_tables.py
```

---

## Run ETL

```bash
python src/etl/loader.py
```

---

## Run Dashboard

```bash
streamlit run src/dashboard/app.py
```

---

# 📊 Deliverables

- ETL Pipeline
- SQLite Database
- Financial Analytics
- Dashboard
- Valuation Module
- CSV Export
- Reports
- Documentation

---

# 📝 Sprint 4 Retrospective

## UX Decisions

- Sidebar navigation for all screens
- KPI cards for quick insights
- Interactive Plotly charts
- Responsive dashboard layout

### Data Edge Cases

- Missing values displayed as **N/A**
- Invalid ticker handled gracefully
- Empty datasets handled without crashes

### Performance

- Cached database queries
- Optimized chart rendering
- Dashboard pages load quickly

---

# 👩‍💻 Author

**Ungarala Ramya**

B.Tech – Computer Science Engineering

---

# ⭐ Project Status

✅ Sprint 1 Completed

✅ Sprint 2 Completed

✅ Sprint 3 Completed

✅ Sprint 4 Completed

🎉 Nifty100 Analytics Dashboard Successfully Developed.