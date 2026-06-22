import sqlite3

conn = sqlite3.connect("db/nifty100.db")

result = conn.execute("PRAGMA foreign_key_check")

rows = result.fetchall()

if len(rows) == 0:
    print("Foreign key check passed - 0 errors")
else:
    print(rows)

conn.close()