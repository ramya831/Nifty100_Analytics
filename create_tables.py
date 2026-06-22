import sqlite3

connection = sqlite3.connect("db/nifty100.db")

connection.execute("PRAGMA foreign_keys = ON")

with open("db/schema.sql", "r") as file:
    sql_script = file.read()

connection.executescript(sql_script)

connection.commit()

connection.close()

print("Tables created successfully")