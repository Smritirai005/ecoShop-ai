from fastapi import FastAPI
from app.routes.brand import router as brand_router

app = FastAPI()
app.include_router(brand_router)
