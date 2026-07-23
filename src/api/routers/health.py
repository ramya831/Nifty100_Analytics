from fastapi import APIRouter
import sqlite3
import time

router = APIRouter(
    tags=["Health"]
)

START_TIME = time.time()

DATABASE = "db/nifty100.db"


@router.get("/")
def health_check():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    tables = [
        "companies",
        "financial_ratios",
        "profit_loss",
        "balance_sheet",
        "cash_flow"
    ]

    counts = {}

    for table in tables:
        try:
            cursor.execute(f"SELECT COUNT(*) FROM {table}")
            counts[table] = cursor.fetchone()[0]
        except:
            counts[table] = 0

    conn.close()

    return {
        "status": "ok",
        "version": "1.0.0",
        "uptime_seconds": int(time.time() - START_TIME),
        "db_row_counts": counts
    }