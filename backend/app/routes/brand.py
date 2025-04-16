from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class BrandRequest(BaseModel):
    brand_name: str

@router.post("/score")
def score_brand(data: BrandRequest):
    brand = data.brand_name
    return {
        "brand": brand,
        "score": 72,
        "summary": f"{brand} has a moderate reputation for ethical practices."
    }
