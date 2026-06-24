import sqlite3
import pandas as pd
import os


DB_PATH = "db/nifty100.db"
DATA_PATH = "data/raw"


def load_excel():

    conn = sqlite3.connect(DB_PATH)

    conn.execute("PRAGMA foreign_keys = ON")


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


    for file, table in files.items():

        path = os.path.join(DATA_PATH, file)


        if os.path.exists(path):

            print("Loading:", file)


            df = pd.read_excel(path)


            # remove empty columns
            df = df.dropna(axis=1, how="all")


            # remove duplicate columns
            df = df.loc[:, ~df.columns.duplicated()]


            df.to_sql(
                table,
                conn,
                if_exists="replace",
                index=False
            )


            print(table, "loaded")


        else:
            print(file, "missing")


    conn.close()

    print("All files loaded")


if __name__ == "__main__":
    load_excel()