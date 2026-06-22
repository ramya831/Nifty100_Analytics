import pandas as pd
import os


class DataValidator:

    def __init__(self):
        self.failures = []


    def add_failure(self, rule, message):
        self.failures.append({
            "rule": rule,
            "message": message
        })


    # DQ-01 Primary Key uniqueness
    def check_primary_key(self, df, column):

        if df[column].duplicated().any():
            self.add_failure(
                "DQ-01",
                f"Duplicate primary key found in {column}"
            )


    # DQ-02 Null value check
    def check_nulls(self, df):

        if df.isnull().sum().sum() > 0:
            self.add_failure(
                "DQ-02",
                "Null values found"
            )


    # DQ-03 Foreign Key integrity
    def check_foreign_key(self, child, parent, column):

        invalid = child[
            ~child[column].isin(parent[column])
        ]

        if len(invalid) > 0:
            self.add_failure(
                "DQ-03",
                "Foreign key mismatch"
            )


    # DQ-06 Positive sales check
    def check_positive_sales(self, df):

        if (df["sales"] <= 0).any():
            self.add_failure(
                "DQ-06",
                "Sales value should be positive"
            )


    # Save validation report
    def save_report(self):

        os.makedirs("output", exist_ok=True)

        df = pd.DataFrame(self.failures)

        df.to_csv(
            "output/validation_failures.csv",
            index=False
        )



# -------------------------
# Standalone DQ Functions
# (For Unit Tests)
# -------------------------


def check_positive_sales(df):

    failures = []

    if (df["sales"] <= 0).any():

        failures.append({
            "rule": "DQ-06",
            "message": "Sales value should be positive"
        })

    return failures



def check_pk_unique(df, column):

    failures = []

    if df[column].duplicated().any():

        failures.append({
            "rule": "DQ-01",
            "message": "Duplicate primary key found"
        })

    return failures



def check_null_values(df):

    failures = []

    if df.isnull().sum().sum() > 0:

        failures.append({
            "rule": "DQ-02",
            "message": "Null values found"
        })

    return failures



# Run directly
if __name__ == "__main__":

    validator = DataValidator()

    print("Validator ready")