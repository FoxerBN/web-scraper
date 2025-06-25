
# 🏠 Bazos.sk House Scraper

This is a **FastAPI-based web scraper** that fetches house listings from [bazos.sk](https://reality.bazos.sk/predam/dom) and displays them in a simple HTML view.

> 🚀 Live Demo: [web-scraper-production-f717.up.railway.app](https://web-scraper-production-f717.up.railway.app/)

---

## 📌 Features

* Web scraping using `requests` + `BeautifulSoup`
* Clean FastAPI backend
* Server-side rendering with `Jinja2`
* Paginated house listings
* Shows title, price, image, location, description, and views

---

## 🧪 Why This Project?

This was a **test project** to explore:

* Basic web scraping with Python
* Displaying scraped data using FastAPI and HTML templates
* Deploying on [Railway](https://railway.app/)

There is **no frontend filtering yet** (e.g. by location or price). Data is hardcoded to filter houses in and around **Žilina (01001)** with a max price of **120,000€**.

---

## 🧰 Tech Stack

* 🐍 Python 3.11+
* ⚡ FastAPI
* 🎨 Jinja2 Templates
* 🧹 BeautifulSoup (for scraping)
* 🚀 Uvicorn
* ☁️ Deployed via Railway

---

## 🚀 Getting Started

### 1. Clone and install dependencies:

```bash
git clone https://github.com/yourusername/house-scraper.git
cd house-scraper
pip install -r requirements.txt
```

### 2. Run the app:

```bash
uvicorn main:app --reload
```

Visit: `http://localhost:8000`

---

## 📂 Project Structure

```
.
├── app/
│   ├── models/
│   │   └── house_model.py   # Pydantic model for house listing
│   └── service/
│       └── house_scraper.py # Scraper logic
├── templates/
│   └── houses.html          # HTML view for listings
├── main.py                  # FastAPI app entrypoint
```

---
