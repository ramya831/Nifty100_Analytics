import sqlite3


conn = sqlite3.connect("db/nifty100.db")

queries = [
    "SELECT * FROM companies LIMIT 5",
    "SELECT COUNT(*) FROM profitandloss",
    "SELECT COUNT(*) FROM balancesheet",
    "SELECT COUNT(*) FROM cashflow"
]


for q in queries:
    print("\nResult:")
    print(conn.execute(q).fetchall())


conn.close()