from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# This is no longer needed if you're passing the parameter directly in the query string
# class BrandRequest(BaseModel):
#     brand_name: str

@router.get("/score")
def score_brand(brand_name: str):
    brand = brand_name
    if brand.lower() == "nike":  # Example check
        return {
            "brand": "Nike",
            "score": 72,
            "summary": "Nike has a moderate reputation for ethical practices."
        }
    else:
        return {
            "brand": brand,
            "score": None,
            "summary": "Brand not found."
        }
