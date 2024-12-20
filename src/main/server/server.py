from fastapi import FastAPI
from src.main.routes.calculators import router as calculators_router

app = FastAPI()

app.include_router(calculators_router, prefix="/api", tags=["calculators"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}