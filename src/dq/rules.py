import pandas as pd


def validate(df):
    issues = []

    if "sales" in df.columns:
        if (df["sales"] < 0).any():
            issues.append("NEGATIVE_SALES")

    if "profit" in df.columns:
        if (df["profit"] < 0).any():
            issues.append("NEGATIVE_PROFIT")

    if "equity" in df.columns:
        if (df["equity"] <= 0).any():
            issues.append("INVALID_EQUITY")

    if "debt" in df.columns:
        if (df["debt"] < 0).any():
            issues.append("NEGATIVE_DEBT")

    if "roe" in df.columns:
        if (df["roe"] > 100).any():
            issues.append("ROE_TOO_HIGH")

    if "pe" in df.columns:
        if (df["pe"] < 0).any():
            issues.append("NEGATIVE_PE")

    if "market_cap" in df.columns:
        if (df["market_cap"] <= 0).any():
            issues.append("INVALID_MARKET_CAP")

    if "company_name" in df.columns:
        if df["company_name"].isnull().any():
            issues.append("MISSING_COMPANY")

    if "ticker" in df.columns:
        if df["ticker"].duplicated().any():
            issues.append("DUPLICATE_TICKER")

    if "sector" in df.columns:
        if df["sector"].isnull().any():
            issues.append("MISSING_SECTOR")

    if "year" in df.columns:
        if df["year"].isnull().any():
            issues.append("MISSING_YEAR")

    if "cashflow" in df.columns:
        if df["cashflow"].isnull().any():
            issues.append("MISSING_CASHFLOW")

    if "revenue" in df.columns:
        if (df["revenue"] == 0).any():
            issues.append("ZERO_REVENUE")

    if "shares" in df.columns:
        if (df["shares"] <= 0).any():
            issues.append("INVALID_SHARES")

    return issues