from fastapi import APIRouter
from src.api.database import get_connection

router = APIRouter(
    prefix="/documents",
    tags=["Documents"]
)

@router.get("/")
def get_documents():
    conn = get_connection()

    cursor = conn.execute("""
        SELECT *
        FROM documents
        LIMIT 20
    """)

    data = [dict(row) for row in cursor.fetchall()]
    conn.close()

    return data