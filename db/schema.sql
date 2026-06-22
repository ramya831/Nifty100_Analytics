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