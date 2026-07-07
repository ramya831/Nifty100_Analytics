import pandas as pd

from src.screener.export import (
    calculate_composite_score,
    export_to_excel
)

data = {
    "company_name": ["TCS", "Infosys", "Wipro"],
    "roe": [28, 24, 18],
    "fcf": [15000, 12000, 8000],
    "revenue_cagr_5yr": [15, 12, 8],
    "de": [0.1, 0.2, 0.5]
}

df = pd.DataFrame(data)

df = calculate_composite_score(df)

file = export_to_excel(df)

print("Excel created:", file)