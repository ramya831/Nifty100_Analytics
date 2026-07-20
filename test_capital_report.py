import pandas as pd

from src.analytics.capital_report import (
    pattern_summary,
    pattern_changes
)

data = {

    "company_id": [1,2,3,4],

    "capital_allocation":[

        "Reinvestor",

        "Dividend",

        "Distress",

        "Reinvestor"

    ],

    "previous_pattern":[

        "Dividend",

        "Dividend",

        "Reinvestor",

        "Reinvestor"

    ],

    "current_pattern":[

        "Reinvestor",

        "Dividend",

        "Distress",

        "Reinvestor"

    ]

}

df = pd.DataFrame(data)

summary = pattern_summary(df)

changes = pattern_changes(df)

print(summary)

print(changes)

summary.to_csv(
    "output/capital_distribution.csv",
    index=False
)

changes.to_csv(
    "output/pattern_changes.csv",
    index=False
)