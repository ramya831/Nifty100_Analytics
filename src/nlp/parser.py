import re
import pandas as pd

pattern = r"(\d+)\s*Years?:?\s*([\d.]+)%"


def parse_metric(text, metric_type="Unknown", company_id=1):

    match = re.search(pattern, str(text))

    if match:

        return {
            "company_id": company_id,
            "metric_type": metric_type,
            "period_years": int(match.group(1)),
            "value_pct": float(match.group(2))
        }

    return None


def parse_dataframe(df):

    parsed = []
    failed = []

    columns = [
        "compounded_sales_growth",
        "compounded_profit_growth",
        "stock_price_cagr",
        "roe"
    ]

    for index, row in df.iterrows():

        company_id = row.get("company_id", index + 1)

        for col in columns:

            result = parse_metric(
                row.get(col, ""),
                col,
                company_id
            )

            if result:
                parsed.append(result)

            else:

                failed.append({
                    "company_id": company_id,
                    "metric": col,
                    "text": row.get(col, "")
                })

    return (
        pd.DataFrame(parsed),
        pd.DataFrame(failed)
    )
def compare_values(parsed_value, calculated_value):
    difference = abs(parsed_value - calculated_value)

    if difference > 5:
        return "Manual Review"

    return "OK"