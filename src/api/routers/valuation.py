from fastapi import APIRouter

router = APIRouter(
    prefix="/valuation",
    tags=["Valuation"]
)

@router.get("/")
def get_valuation():
    return {
        "message": "Valuation endpoint"
    }