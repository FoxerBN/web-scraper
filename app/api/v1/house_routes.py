from fastapi import APIRouter, Query
from typing import List
from app.service.house_scraper import fetch_house_data
from app.models.house_model import House

router = APIRouter()

@router.get("/houses", response_model=List[House])
def get_houses(page: int = Query(1, ge=1)):
    return fetch_house_data(page=page)