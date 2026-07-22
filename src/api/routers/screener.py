from fastapi import APIRouter

router = APIRouter(
    prefix="/screener",
    tags=["Screener"]
)

@router.get("/")
def get_screener():
    return {
        "message": "Screener endpoint"
    }