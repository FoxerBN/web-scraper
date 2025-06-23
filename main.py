from fastapi import FastAPI
from app.api.v1 import house_routes

app = FastAPI()

@app.get("/")
async def read_root():
    return {"Hello": "World"}

app.include_router(house_routes.router, prefix="/api/v1")