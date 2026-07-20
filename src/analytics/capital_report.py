import pandas as pd


def pattern_summary(df):

    return df["capital_allocation"].value_counts().reset_index().rename(
        columns={
            "index": "Pattern",
            "capital_allocation": "Companies"
        }
    )


def pattern_changes(df):

    changes = []

    for _, row in df.iterrows():

        if row["previous_pattern"] != row["current_pattern"]:

            changes.append({

                "company_id": row["company_id"],

                "previous_pattern": row["previous_pattern"],

                "current_pattern": row["current_pattern"]

            })

    return pd.DataFrame(changes)