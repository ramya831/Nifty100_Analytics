from fastapi import APIRouter
from src.api.database import get_connection

router = APIRouter(
    prefix="/screener",
    tags=["Screener"]
)

@router.get("/")
def get_screener():
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
        LIMIT 20
    """)

    data = [dict(row) for row in cursor.fetchall()]
    conn.close()

    return data