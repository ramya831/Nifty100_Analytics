from fastapi import APIRouter, Query
from src.api.database import get_connection

router = APIRouter(
    prefix="/screener",
    tags=["Screener"]
)


@router.get("/")
def get_screener(
    search: str = "",
    min_roe: float = 0
):
    conn = get_connection()

    query = """
    SELECT
        id,
        company_name,
        roe_percentage,
        roce_percentage,
        face_value,
        book_value
    FROM companies
    WHERE company_name LIKE ?
    """

    cursor = conn.execute(
        query,
        (f"%{search}%",)
    )

    rows = cursor.fetchall()

    result = []

    for row in rows:

        try:
            roe = float(row["roe_percentage"])
        except:
            roe = 0

        if roe >= min_roe:
            result.append(dict(row))

    conn.close()

    return result