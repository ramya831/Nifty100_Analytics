# 📊 Nifty100 Analytics Project

A comprehensive financial analytics platform for **NIFTY 100 companies** built using **Python, FastAPI, SQLite, Pandas, Plotly, and Streamlit**.

The project provides an end-to-end analytics solution including ETL processing, financial ratio calculations, valuation analysis, stock screening, peer comparison, portfolio analytics, REST APIs, automated testing, and an interactive dashboard.

---

# 🚀 Features

- ETL Pipeline
- Data Validation & Quality Checks
- SQLite Database
- Financial Ratio Analysis
- Profitability Analysis
- Liquidity Analysis
- Leverage Analysis
- Efficiency Analysis
- Growth Analysis
- CAGR Analysis
- Cash Flow Analytics
- Valuation Module
- Company Screener
- Peer Comparison Engine
- Portfolio Analytics
- Trend Analysis
- Sector Analysis
- Capital Allocation Map
- Annual Reports Viewer
- CSV & Excel Export
- Interactive Streamlit Dashboard
- FastAPI REST APIs
- Swagger & ReDoc API Documentation
- Automated Testing
- Performance Benchmarking
- Code Coverage Analysis

---

# 🧪 Testing & Quality Assurance

- Unit Testing
- API Integration Testing
- ETL Testing
- KPI Testing
- Data Quality Testing
- Performance Benchmarking
- Code Coverage Analysis
- HTML Test Reports

---

# 🛠 Technologies Used

### Programming

- Python

### Backend

- FastAPI
- Uvicorn

### Database

- SQLite

### Data Processing

- Pandas
- NumPy

### Visualization

- Plotly
- Streamlit

### Testing

- Pytest
- Pytest-Cov
- Requests

### Version Control

- Git
- GitHub

---
# 📂 Project Structure

```text
Nifty100_Analytics/
│
├── config/
├── data/
│   ├── raw/
│   └── processed/
│
├── db/
│
├── notebooks/
│
├── output/
│   ├── valuation_summary.xlsx
│   ├── valuation_flags.csv
│   ├── perf_notes.md
│   └── reports/
│
├── reports/
│
├── src/
│   ├── analytics/
│   ├── api/
│   ├── dashboard/
│   ├── dq/
│   ├── etl/
│   └── screener/
│
├── tests/
│
├── performance_test.py
├── create_tables.py
├── requirements.txt
└── README.md
```

---

# 📅 Sprint Progress

## ✅ Sprint 1

- Environment Setup
- Project Structure
- Data Collection
- ETL Pipeline
- Data Cleaning

---

## ✅ Sprint 2

- SQLite Database
- Financial Ratio Analysis
- KPI Calculations
- SQL Queries
- Reports Generation

---

## ✅ Sprint 3

- Company Screener
- Peer Comparison Engine
- Sector Analytics
- Portfolio Analytics

---

## ✅ Sprint 4

- Streamlit Dashboard
- Company Profile
- Screener Dashboard
- Peer Comparison Dashboard
- Trend Analysis
- Sector Analysis
- Capital Allocation
- Annual Reports Viewer
- Valuation Module

---

## ✅ Sprint 5

- FastAPI REST APIs
- Health API
- Companies API
- Sectors API
- Screener API
- Portfolio API
- Documents API
- Peer Comparison API
- Valuation API
- Swagger Documentation
- API Integration Testing

---

## ✅ Sprint 6

- Unit Testing
- API Testing
- ETL Testing
- KPI Testing
- Screener Testing
- Data Quality Testing
- Performance Benchmarking
- Code Coverage Analysis
- Project Documentation

---
# 🌐 REST APIs

The project exposes REST APIs using **FastAPI** for accessing financial analytics, screening companies, portfolio insights, and other project modules.

## Available APIs

- Health API
- Companies API
- Sectors API
- Screener API
- Portfolio API
- Documents API
- Peer Comparison API
- Valuation API

---

## API Documentation

### Swagger UI

```
http://127.0.0.1:8000/docs
```

### ReDoc

```
http://127.0.0.1:8000/redoc
```

---

# 📊 Dashboard Modules

## 🏠 Home Dashboard

- KPI Summary Cards
- Sector Distribution
- Top Companies Table
- Year Selection
- Overall Market Overview

---

## 🏢 Company Profile

- Company Details
- Financial KPI Cards
- Revenue Trend
- ROE Trend
- Pros & Cons
- Company Overview

---

## 🔍 Company Screener

- Financial Metric Filters
- Preset Filters
- Composite Score
- Live Results
- CSV Export

---

## 👥 Peer Comparison

- Peer Group Selection
- Radar Chart
- KPI Comparison Table
- Financial Benchmarking

---

## 📈 Trend Analysis

- Multi-Year Financial Trends
- Revenue Growth
- Profit Growth
- Company Search
- Historical Performance

---

## 🏭 Sector Analysis

- Sector KPI Summary
- Bubble Chart
- Revenue vs ROE Analysis
- Sector Performance Comparison

---

## 🌳 Capital Allocation

- Treemap Visualization
- Capital Allocation Breakdown
- Investment Distribution

---

## 📄 Annual Reports

- Company Search
- Available Annual Reports
- Report Links
- Report Downloads

---

# 📈 Financial Analytics

The project calculates:

- Return on Equity (ROE)
- Return on Capital Employed (ROCE)
- Earnings Per Share (EPS)
- Debt-to-Equity Ratio
- Current Ratio
- Quick Ratio
- Net Profit Margin
- Operating Margin
- CAGR
- Cash Flow KPIs
- Financial Health Score

---

# 📊 Valuation Module

The valuation engine performs:

- Price-to-Earnings (P/E) Analysis
- Price-to-Book (P/B) Analysis
- EV/EBITDA Analysis
- Free Cash Flow (FCF) Yield
- Sector Median Comparison
- Valuation Flags

### Generated Outputs

- valuation_summary.xlsx
- valuation_flags.csv

---
# ▶️ Running the Project

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/ramya831/Nifty100_Analytics.git

cd Nifty100_Analytics
```

---

## 2️⃣ Create a Virtual Environment

```bash
python -m venv .venv
```

### Activate Environment

**Windows (Command Prompt)**

```bash
.venv\Scripts\activate
```

**Git Bash**

```bash
source .venv/Scripts/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Create the Database

```bash
python create_tables.py
```

---

## 5️⃣ Run the ETL Pipeline

```bash
python src/etl/loader.py
```

---

## 6️⃣ Start the FastAPI Server

```bash
uvicorn src.api.main:app --reload
```

After starting the server, open:

**Swagger UI**

```
http://127.0.0.1:8000/docs
```

**ReDoc**

```
http://127.0.0.1:8000/redoc
```

---

## 7️⃣ Run the Streamlit Dashboard

```bash
streamlit run src/dashboard/app.py
```

---

# 🧪 Running Tests

## Run All Tests

```bash
pytest
```

---

## Run Tests with Code Coverage

```bash
pytest --cov=. tests
```

---

## Generate HTML Coverage Report

```bash
pytest --cov=. --cov-report=html tests
```

The coverage report will be generated in:

```
htmlcov/index.html
```

Open `htmlcov/index.html` in your browser to view the report.

---

## Run Performance Benchmark

```bash
python performance_test.py
```

Example Output:

```text
========================================
Concurrent Requests: 10
Total Time: 0.15 seconds
Average Response: 0.095 seconds
========================================
```

---
# 📦 Project Deliverables

The project successfully delivers:

- ETL Data Pipeline
- SQLite Database
- Financial Ratio Analysis
- CAGR & Cash Flow Analytics
- Company Screener
- Peer Comparison Engine
- Portfolio Analytics
- Sector Analysis
- Valuation Module
- Interactive Streamlit Dashboard
- FastAPI REST APIs
- Swagger & ReDoc API Documentation
- CSV & Excel Export
- Automated Testing Suite
- Performance Benchmarking
- Code Coverage Report
- Project Documentation

---

# 📈 Performance & Quality

### Testing Summary

- ✅ 72 Automated Tests Passed
- ✅ API Integration Testing Completed
- ✅ ETL Validation Completed
- ✅ KPI Validation Completed
- ✅ Screener Logic Verified
- ✅ Data Quality Rules Validated

### Performance Benchmark

- Concurrent API Performance Testing
- Average API Response Time Measured
- Performance Notes Generated

### Code Quality

- Pytest Test Suite
- Code Coverage Analysis
- HTML Coverage Report
- Modular Project Structure

---

# 📝 Sprint 6 Retrospective

## Key Achievements

- Successfully completed all planned Sprint 6 tasks.
- Developed and validated REST APIs using FastAPI.
- Implemented automated unit and integration tests.
- Measured API performance through benchmarking.
- Generated code coverage reports for quality assurance.
- Improved project documentation and maintainability.

## Performance Improvements

- Optimized API response times.
- Improved project modularity.
- Added automated testing for reliable deployments.
- Enhanced overall project stability.

## Lessons Learned

- Importance of modular architecture.
- Benefits of automated testing.
- API documentation using Swagger and ReDoc.
- Performance monitoring and benchmarking.
- Version control using Git and GitHub.

---

# 👩‍💻 Author

**Ungarala Ramya**

B.Tech – Computer Science Engineering

GitHub:
https://github.com/ramya831

---

# ⭐ Project Status

✅ Sprint 1 Completed

✅ Sprint 2 Completed

✅ Sprint 3 Completed

✅ Sprint 4 Completed

✅ Sprint 5 Completed

✅ Sprint 6 Completed

✅ ETL Pipeline Completed

✅ Financial Analytics Completed

✅ Streamlit Dashboard Completed

✅ FastAPI REST APIs Completed

✅ Automated Testing Completed

✅ Performance Benchmarking Completed

✅ Code Coverage Analysis Completed

✅ Project Documentation Completed

🎉 **Nifty100 Analytics Platform Successfully Developed.**
