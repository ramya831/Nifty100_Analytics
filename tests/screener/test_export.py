import pandas as pd

from src.screener.export import calculate_composite_score


def test_composite_score():

    df = pd.DataFrame({
        "roe": [10, 20],
        "fcf": [50, 100],
        "revenue_cagr_5yr": [15, 25],
        "de": [2, 1]
    })

    result = calculate_composite_score(df)

    assert "composite_quality_score" in result.columns
    assert len(result) == 2
from src.screener.export import export_to_excel
import os


def test_export_to_excel():

    df = pd.DataFrame({
        "company_name": ["ABC", "XYZ"],
        "composite_quality_score": [90, 80]
    })

    filename = "output/test_screener.xlsx"

    export_to_excel(df, filename)

    assert os.path.exists(filename)