import pandas as pd

from src.screener.engine import run_preset


def sample_data():
    return pd.DataFrame({
        "company_name": ["AAA", "BBB", "CCC"],

        "roe": [18, 10, 25],
        "de": [0.5, 2.5, 0],
        "fcf": [100, -20, 300],

        "revenue_cagr_5yr": [15, 5, 25],
        "pat_cagr_5yr": [22, 8, 30],

        "pe": [18, 40, 12],
        "pb": [2, 5, 1],

        "dividend_yield": [2.5, 0.5, 3],

        "dividend_payout": [60, 90, 50],

        "sales": [7000, 2000, 10000]
    })


def test_quality_compounder():
    df = sample_data()
    result = run_preset(df, "Quality Compounder")
    assert len(result) >= 1


def test_value_pick():
    df = sample_data()
    result = run_preset(df, "Value Pick")
    assert len(result) >= 1


def test_growth_accelerator():
    df = sample_data()
    result = run_preset(df, "Growth Accelerator")
    assert len(result) >= 1


def test_dividend_champion():
    df = sample_data()
    result = run_preset(df, "Dividend Champion")
    assert len(result) >= 1


def test_debt_free_bluechip():
    df = sample_data()
    result = run_preset(df, "Debt-Free Blue Chip")
    assert len(result) >= 1


def test_turnaround_watch():
    df = sample_data()
    result = run_preset(df, "Turnaround Watch")
    assert len(result) >= 1