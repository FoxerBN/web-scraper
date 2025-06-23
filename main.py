import os
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.service.house_scraper import fetch_house_data

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request, page: int = 1):
    houses = fetch_house_data(page)
    return templates.TemplateResponse(
        "houses.html",
        {"request": request, "houses": houses, "page": page}
    )

@app.get("/ping")
async def ping():
    return {"message": "pong"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port)
