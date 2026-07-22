from fastapi import APIRouter

router = APIRouter(
    prefix="/peers",
    tags=["Peers"]
)

@router.get("/")
def get_peers():
    return {
        "message": "Peers endpoint"
    }