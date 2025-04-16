from fastapi import APIRouter
from pydantic import BaseModel
from app.routes.scrape import scrape_brand

router = APIRouter()

# This is no longer needed if you're passing the parameter directly in the query string
# class BrandRequest(BaseModel):
#     brand_name: str

@router.get("/score")
def score_brand(brand_name: str):
    result = scrape_brand(brand_name)
    
    if result:
        return result
    else:
        return {
            "brand": brand_name,
            "score": None,
            "summary": "Brand not found."
        }
