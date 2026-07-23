from fastapi import APIRouter
from src.api.database import get_connection

router = APIRouter(
    prefix="/companies",
    tags=["Companies"]
)

@router.get("/")
def get_companies():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM companies LIMIT 20")

    rows = cursor.fetchall()

    conn.close()

    companies = [dict(row) for row in rows]

    return companies