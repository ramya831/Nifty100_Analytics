import pandas as pd
from src.dq.rules import validate


def test_negative_sales():
    assert "NEGATIVE_SALES" in validate(pd.DataFrame({"sales":[-1]}))

def test_negative_profit():
    assert "NEGATIVE_PROFIT" in validate(pd.DataFrame({"profit":[-1]}))

def test_invalid_equity():
    assert "INVALID_EQUITY" in validate(pd.DataFrame({"equity":[0]}))

def test_negative_debt():
    assert "NEGATIVE_DEBT" in validate(pd.DataFrame({"debt":[-1]}))

def test_high_roe():
    assert "ROE_TOO_HIGH" in validate(pd.DataFrame({"roe":[150]}))

def test_negative_pe():
    assert "NEGATIVE_PE" in validate(pd.DataFrame({"pe":[-10]}))

def test_market_cap():
    assert "INVALID_MARKET_CAP" in validate(pd.DataFrame({"market_cap":[0]}))

def test_missing_company():
    assert "MISSING_COMPANY" in validate(pd.DataFrame({"company_name":[None]}))

def test_duplicate_ticker():
    assert "DUPLICATE_TICKER" in validate(pd.DataFrame({"ticker":["ABC","ABC"]}))

def test_missing_sector():
    assert "MISSING_SECTOR" in validate(pd.DataFrame({"sector":[None]}))

def test_missing_year():
    assert "MISSING_YEAR" in validate(pd.DataFrame({"year":[None]}))

def test_missing_cashflow():
    assert "MISSING_CASHFLOW" in validate(pd.DataFrame({"cashflow":[None]}))

def test_zero_revenue():
    assert "ZERO_REVENUE" in validate(pd.DataFrame({"revenue":[0]}))

def test_invalid_shares():
    assert "INVALID_SHARES" in validate(pd.DataFrame({"shares":[0]}))