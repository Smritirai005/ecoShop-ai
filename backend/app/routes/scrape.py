from fastapi import APIRouter, Query
from bs4 import BeautifulSoup
import requests

# ✅ This is the function you can import in brand.py
def scrape_brand(brand_name: str):
    try:
        url = f"https://directory.goodonyou.eco/?s={brand_name}"
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        # Check if this selector actually works on the page
        brand_info = soup.select_one(".search-results .score")

        if brand_info:
            score = brand_info.text.strip()
            return {
                "brand": brand_name,
                "score": score,
                "summary": f"{brand_name} sustainability info fetched successfully."
            }
        else:
            return None  # Let the caller handle this

    except Exception as e:
        print(f"Scraping failed: {e}")
        return None