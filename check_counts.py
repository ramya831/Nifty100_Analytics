import sqlite3


conn = sqlite3.connect("db/nifty100.db")

tables = [
"companies",
"profitandloss",
"balancesheet",
"cashflow",
"stock_prices"
]


for table in tables:

    result = conn.execute(
        f"SELECT COUNT(*) FROM {table}"
    ).fetchone()

    print(table, result[0])


conn.close()