import requests
from bs4 import BeautifulSoup
from app.models.house_model import House

BASE_URL = "https://reality.bazos.sk/predam/dom"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "sk-SK,sk;q=0.9,en;q=0.8"
}

def fetch_house_data(page: int = 1) -> list[House]:
    offset = "" if page == 1 else f"/{(page-1)*20}"
    url = (
        f"{BASE_URL}{offset}/?hledat=&hlokalita=01001&humkreis=30&cenaod=&cenado=120000&order="
    )
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        house_data = []

        for ad in soup.select(".inzeraty.inzeratyflex"):
            title_tag = ad.select_one("h2.nadpis a")
            if not title_tag:
                continue

            title = title_tag.get_text(strip=True)
            link = "https://reality.bazos.sk" + title_tag['href']
            price = ad.select_one(".inzeratycena b").get_text(strip=True)
            location = ad.select_one(".inzeratylok").get_text(separator=" ", strip=True)
            description = ad.select_one(".popis")
            description = description.get_text(strip=True) if description else ""
            img_tag = ad.select_one("img.obrazek")
            image_url = img_tag["src"] if img_tag else None
            views = ad.select_one(".inzeratyview")
            views = views.get_text(strip=True) if views else None

            house_data.append(House(
                title=title,
                price=price,
                link=link,
                location=location,
                description=description,
                image=image_url,
                views=views
            ))

        return house_data

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return []