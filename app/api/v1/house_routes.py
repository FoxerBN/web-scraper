from fastapi import APIRouter


router = APIRouter()

@router.get("/houses")
def get_houses():
    return {"message": "List of houses"}