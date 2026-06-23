import sqlite3
import os


DB_PATH = "db/nifty100.db"


def load_data():

    conn = sqlite3.connect(DB_PATH)

    conn.execute("PRAGMA foreign_keys = ON")

    cursor = conn.cursor()

    print("Database connected")

    tables = cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table'"
    ).fetchall()

    print("Tables:")

    for table in tables:
        print(table[0])


    conn.close()


if __name__ == "__main__":
    load_data()