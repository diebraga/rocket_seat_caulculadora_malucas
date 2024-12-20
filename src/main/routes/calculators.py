from fastapi import APIRouter

router = APIRouter()

@router.get("/calculators")
def get_calculators():
    return {"message": "Hello, World!"}