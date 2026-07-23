import sqlite3
import pandas as pd
import os

DB_PATH = "db/nifty100.db"
DATA_PATH = "data/raw"


def make_unique(columns):
    """Make duplicate column names unique."""
    seen = {}
    new_cols = []

    for col in columns:
        col = str(col).strip()

        if col in seen:
            seen[col] += 1
            new_cols.append(f"{col}_{seen[col]}")
        else:
            seen[col] = 0
            new_cols.append(col)

    return new_cols


def load_excel():

    conn = sqlite3.connect(DB_PATH)

    files = {
        "companies.xlsx": "companies",
        "profitandloss.xlsx": "profitandloss",
        "balancesheet.xlsx": "balancesheet",
        "cashflow.xlsx": "cashflow",
        "analysis.xlsx": "analysis",
        "documents.xlsx": "documents",
        "prosandcons.xlsx": "prosandcons",
        "sectors.xlsx": "sectors",
        "stock_prices.xlsx": "stock_prices",
        "financial_ratios.xlsx": "financial_ratios",
        "peer_groups.xlsx": "peer_groups",
        "market_cap.xlsx": "market_cap"
    }

    # Files having a title row before the real header
    special_files = {
        "companies.xlsx",
        "analysis.xlsx"
    }

    for file, table in files.items():

        path = os.path.join(DATA_PATH, file)

        if not os.path.exists(path):
            print(f"{file} not found")
            continue

        print(f"\nLoading {file}...")

        try:

            if file in special_files:
                # Read without header
                df = pd.read_excel(path, header=None)

                # Remove title row
                df = df.iloc[1:].reset_index(drop=True)

                # First row becomes header
                headers = df.iloc[0].astype(str)

                # Remaining rows are data
                df = df.iloc[1:].reset_index(drop=True)

                headers = make_unique(headers)
                df.columns = headers

            else:
                # Normal Excel files
                df = pd.read_excel(path)

                df.columns = make_unique(df.columns)

            # Remove empty columns
            df = df.dropna(axis=1, how="all")

            # Remove empty rows
            df = df.dropna(how="all")

            df.to_sql(
                table,
                conn,
                if_exists="replace",
                index=False
            )

            print(f"✓ {table} loaded successfully ({len(df)} rows)")

        except Exception as e:
            print(f"✗ Error loading {file}")
            print(e)

    conn.close()

    print("\nAll files loaded successfully.")


if __name__ == "__main__":
    load_excel()