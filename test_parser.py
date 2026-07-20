import pandas as pd

from src.nlp.parser import parse_dataframe, compare_values

data = {

    "company_id": [1],

    "compounded_sales_growth": ["10 Years: 21%"],

    "compounded_profit_growth": ["5 Years: 18%"],

    "stock_price_cagr": ["10 Years: 30%"],

    "roe": ["5 Years: 24%"]

}

df = pd.DataFrame(data)

parsed, failed = parse_dataframe(df)

print("Parsed Data:")
print(parsed)

print("\nFailed Data:")
print(failed)

parsed.to_csv(
    "output/analysis_parsed.csv",
    index=False
)

failed.to_csv(
    "output/parse_failures.csv",
    index=False
)

print("\nCross Validation:")
print(compare_values(20, 22))
print(compare_values(20, 30))