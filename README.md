# 📊 Nifty100 Analytics Project

## 📌 Project Overview

Nifty100 Analytics is a data analytics project that processes and analyzes Nifty100 company financial data.

The project uses Python, Pandas, SQLite, and SQL to build an ETL pipeline that loads, validates, stores, and analyzes financial datasets.

---

## 🎯 Project Objectives

- Collect Nifty100 company financial datasets
- Clean and validate raw data
- Create structured database tables
- Load data using ETL pipeline
- Perform SQL-based analysis
- Generate quality reports

---

## 🛠️ Technologies Used

- Python
- Pandas
- SQLite
- SQL
- Git & GitHub
- Excel Dataset Processing

---

## 📂 Project Structure

```
Nifty100_Analytics
│
├── data/
│   └── raw/
│       └── Financial datasets (.xlsx)
│
├── db/
│   └── SQLite database
│
├── notebooks/
│   └── SQL analysis queries
│
├── output/
│   └── Validation reports
│
├── src/
│   └── etl/
│       ├── loader.py
│       └── normalizer.py
│
├── tests/
│   └── etl/
│       └── Data validation tests
│
├── create_tables.py
├── review_data.py
└── README.md
```

---

## 📅 Project Progress

### Day 1: Environment Setup
- Created project structure
- Setup Python environment

### Day 3: Data Validation
- Implemented schema validation
- Added 16 Data Quality rules

### Day 4: Database Creation
- Created SQLite database
- Added primary key and foreign key constraints

### Day 5: Data Loading
- Loaded 12 Nifty100 datasets
- Completed ETL data loading process

### Day 6: Data Quality Review
- Verified database tables
- Checked loaded records
- Performed manual data quality review

### Day 7: Analysis & Review
- Created SQL exploratory queries
- Reviewed complete project workflow

---

## 📊 Datasets Used

- Companies
- Stock Prices
- Market Capitalization
- Financial Ratios
- Balance Sheet
- Profit & Loss
- Cash Flow
- Sectors
- Peer Groups
- Documents
- Pros & Cons
- Analysis Data

---

## 🚀 How to Run Project

Clone repository:

```bash
git clone <your-github-link>
```

Install requirements:

```bash
pip install pandas openpyxl
```

Create database:

```bash
python create_tables.py
```

Load data:

```bash
python src/etl/loader.py
```

Review data:

```bash
python review_data.py
```

---

## 👩‍💻 Author

**Ungarala Ramya**

B.Tech Computer Science Engineering

---

## ⭐ Project Status

Completed ✅