from fastapi import APIRouter

router = APIRouter(
    prefix="/sectors",
    tags=["Sectors"]
)

@router.get("/")
def get_sectors():
    return {
        "message": "Sectors endpoint"
    }