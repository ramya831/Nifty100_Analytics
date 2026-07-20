import pandas as pd


def generate_pros_cons(df):

    results = []

    for _, row in df.iterrows():

        company = row["company_id"]

        # ---------- PROS ----------

        if row["ROE"] > 20:

            results.append({

                "company_id": company,

                "type": "Pro",

                "rule_id": "P1",

                "text": "Consistently high return on equity above 20% demonstrates exceptional capital efficiency.",

                "confidence_pct": 95

            })

        if row["FCF"] > 0:

            results.append({

                "company_id": company,

                "type": "Pro",

                "rule_id": "P2",

                "text": "Strong free cash flow generation indicates healthy business fundamentals.",

                "confidence_pct": 90

            })

        if row["Revenue_CAGR"] > 15:

            results.append({

                "company_id": company,

                "type": "Pro",

                "rule_id": "P3",

                "text": "Revenue growing above 15% CAGR reflects strong business momentum.",

                "confidence_pct": 88

            })

        # ---------- CONS ----------

        if row["Debt_Equity"] > 2:

            results.append({

                "company_id": company,

                "type": "Con",

                "rule_id": "C1",

                "text": "Debt-to-equity ratio is elevated and warrants monitoring.",

                "confidence_pct": 90

            })

        if row["ROCE"] < 10:

            results.append({

                "company_id": company,

                "type": "Con",

                "rule_id": "C2",

                "text": "Return on capital employed below 10% suggests weak capital efficiency.",

                "confidence_pct": 85

            })

        if row["Revenue_CAGR"] < 5:

            results.append({

                "company_id": company,

                "type": "Con",

                "rule_id": "C3",

                "text": "Revenue growth below 5% indicates limited business momentum.",

                "confidence_pct": 80

            })

    return pd.DataFrame(results)