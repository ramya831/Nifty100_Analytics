# -----------------------------
# Sprint 2 - Day 08
# Profitability Ratios
# -----------------------------

def net_profit_margin(net_profit, sales):
    if sales == 0:
        return None
    return (net_profit / sales) * 100


def operating_profit_margin(operating_profit, sales):
    if sales == 0:
        return None
    return (operating_profit / sales) * 100


def return_on_equity(net_profit, equity_capital, reserves):
    equity = equity_capital + reserves
    if equity <= 0:
        return None
    return (net_profit / equity) * 100


def return_on_capital_employed(ebit, equity_capital, reserves, borrowings):
    capital = equity_capital + reserves + borrowings
    if capital <= 0:
        return None
    return (ebit / capital) * 100


def return_on_assets(net_profit, total_assets):
    if total_assets == 0:
        return None
    return (net_profit / total_assets) * 100


# -----------------------------
# Sprint 2 - Day 09
# Leverage & Efficiency Ratios
# -----------------------------

def debt_to_equity(borrowings, equity_capital, reserves):
    equity = equity_capital + reserves

    if borrowings == 0:
        return 0

    if equity <= 0:
        return None

    return borrowings / equity


def high_leverage_flag(de_ratio, sector):
    if sector == "Financials":
        return False
    return de_ratio > 5


def interest_coverage(operating_profit, other_income, interest):
    if interest == 0:
        return None

    return (operating_profit + other_income) / interest


def interest_coverage_label(icr):
    if icr is None:
        return "Debt Free"
    return "Normal"


def interest_warning_flag(icr):
    if icr is None:
        return False

    return icr < 1.5


def net_debt(borrowings, investments):
    return borrowings - investments


def asset_turnover(sales, total_assets):
    if total_assets == 0:
        return None

    return sales / total_assets 

import sqlite3

def save_financial_ratio(db_path, company_id, year, ratio_name, ratio_value):
    """
    Save a financial ratio into the financial_ratios table.
    """

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS financial_ratios (
            company_id INTEGER,
            year INTEGER,
            ratio_name TEXT,
            ratio_value REAL
        )
    """)

    cursor.execute("""
        INSERT INTO financial_ratios
        (company_id, year, ratio_name, ratio_value)
        VALUES (?, ?, ?, ?)
    """, (company_id, year, ratio_name, ratio_value))

    conn.commit()
    conn.close()                                                                                                                                                 
