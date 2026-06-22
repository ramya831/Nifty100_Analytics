PRAGMA foreign_keys = ON;


CREATE TABLE companies (
    company_id INTEGER PRIMARY KEY,
    company_name TEXT NOT NULL,
    sector TEXT
);


CREATE TABLE profitandloss (
    id INTEGER PRIMARY KEY,
    company_id INTEGER,
    year INTEGER,
    revenue REAL,
    profit REAL,

    FOREIGN KEY(company_id)
    REFERENCES companies(company_id)
);


CREATE TABLE balancesheet (
    id INTEGER PRIMARY KEY,
    company_id INTEGER,
    year INTEGER,

    FOREIGN KEY(company_id)
    REFERENCES companies(company_id)
);


CREATE TABLE cashflow (
    id INTEGER PRIMARY KEY,
    company_id INTEGER,
    year INTEGER,

    FOREIGN KEY(company_id)
    REFERENCES companies(company_id)
);
CREATE TABLE analysis (
    id INTEGER PRIMARY KEY,
    company_id INTEGER,
    FOREIGN KEY(company_id) REFERENCES companies(company_id)
);


CREATE TABLE documents (
    id INTEGER PRIMARY KEY,
    company_id INTEGER,
    FOREIGN KEY(company_id) REFERENCES companies(company_id)
);


CREATE TABLE prosandcons (
    id INTEGER PRIMARY KEY,
    company_id INTEGER,
    FOREIGN KEY(company_id) REFERENCES companies(company_id)
);


CREATE TABLE sectors (
    sector_id INTEGER PRIMARY KEY,
    sector_name TEXT
);


CREATE TABLE stock_prices (
    id INTEGER PRIMARY KEY,
    company_id INTEGER,
    price REAL,
    FOREIGN KEY(company_id) REFERENCES companies(company_id)
);


CREATE TABLE financial_ratios (
    id INTEGER PRIMARY KEY,
    company_id INTEGER,
    ratio REAL,
    FOREIGN KEY(company_id) REFERENCES companies(company_id)
);


CREATE TABLE peer_groups (
    id INTEGER PRIMARY KEY,
    company_id INTEGER,
    FOREIGN KEY(company_id) REFERENCES companies(company_id)
);