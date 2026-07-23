from fastapi import APIRouter
from src.api.database import get_connection

router = APIRouter(
    prefix="/portfolio",
    tags=["Portfolio"]
)

@router.get("/")
def get_portfolio():
    conn = get_connection()

    cursor = conn.execute("""
        SELECT
            id,
            company_name,
            face_value,
            book_value,
            roe_percentage,
            roce_percentage
        FROM companies
        ORDER BY company_name
        LIMIT 20
    """)

    data = [dict(row) for row in cursor.fetchall()]
    conn.close()

    return data