import pandas as pd

from src.analytics.cashflow_kpis import (
    cfo_quality,
    capex_intensity,
    distress_signal,
    deleveraging
)

data = {

    "company_id": [1, 2],

    "sector": ["IT", "Auto"],

    "CFO": [1200, -300],

    "PAT": [1000, 500],

    "Sales": [10000, 8000],

    "Investing": [-200, -1200],

    "CFF": [-400, 600],

    "Borrowings_Old": [1000, 2000],

    "Borrowings_New": [900, 2500]

}

df = pd.DataFrame(data)

results = []

alerts = []

for _, row in df.iterrows():

    score, quality = cfo_quality(row["CFO"], row["PAT"])

    capex, capex_label = capex_intensity(
        row["Investing"],
        row["Sales"]
    )

    distress = distress_signal(
        row["CFO"],
        row["CFF"]
    )

    deleverage = deleveraging(
        row["CFF"],
        row["Borrowings_Old"],
        row["Borrowings_New"]
    )

    results.append({

        "company_id": row["company_id"],

        "sector": row["sector"],

        "cfo_quality_score": score,

        "cfo_quality_label": quality,

        "capex_intensity_pct": capex,

        "capex_label": capex_label,

        "distress_flag": distress,

        "deleveraging_flag": deleverage,
        
        "capital_allocation_label": "Reinvestor"

    })

    if distress:

        alerts.append({

            "company_id": row["company_id"],

            "CFO": row["CFO"],

            "CFF": row["CFF"],

            "PAT": row["PAT"]

        })

cashflow = pd.DataFrame(results)

alerts = pd.DataFrame(alerts)

cashflow.to_excel(
    "output/cashflow_intelligence.xlsx",
    index=False
)

alerts.to_csv(
    "output/distress_alerts.csv",
    index=False
)

print(cashflow)

print(alerts)