from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.api.v1 import house_routes
from app.service.house_scraper import fetch_house_data
<<<<<<< HEAD
import os
import uvicorn
=======
>>>>>>> 65fe6a5d7e4705bc85dbdb377717a69025312e83

app = FastAPI()

templates = Jinja2Templates(directory="templates")
<<<<<<< HEAD
=======

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request, page: int = 1):
    houses = fetch_house_data(page)
    return templates.TemplateResponse(
        "houses.html",
        {"request": request, "houses": houses, "page": page}
    )
>>>>>>> 65fe6a5d7e4705bc85dbdb377717a69025312e83

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request, page: int = 1):
    houses = fetch_house_data(page)
    return templates.TemplateResponse(
        "houses.html",
        {"request": request, "houses": houses, "page": page}
    )

app.include_router(house_routes.router, prefix="/api/v1")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)