from fastapi import APIRouter
from src.api.database import get_connection

router = APIRouter(
    prefix="/peers",
    tags=["Peers"]
)

@router.get("/")
def get_peers():
    conn = get_connection()

    cursor = conn.execute("""
        SELECT *
        FROM peer_groups
        LIMIT 20
    """)

    data = [dict(row) for row in cursor.fetchall()]
    conn.close()

    return data