from fastapi import APIRouter
from src.api.database import get_connection

router = APIRouter(
    prefix="/valuation",
    tags=["Valuation"]
)

@router.get("/")
def get_valuation():
    conn = get_connection()

    cursor = conn.execute("""
        SELECT *
        FROM financial_ratios
        LIMIT 20
    """)

    data = [dict(row) for row in cursor.fetchall()]
    conn.close()

    return data