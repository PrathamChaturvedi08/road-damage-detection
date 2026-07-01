from fastapi import FastAPI

from app.api.routes import router as base_router

from app.api.predict import router as predict_router

from fastapi.staticfiles import StaticFiles


app = FastAPI(
    title="RoadVision API",
    description="Backend API for AI-based Road Damage Detection",
    version="1.0.0",
)

app.mount(
    "/outputs",
    StaticFiles(directory="outputs"),
    name="outputs"
)

app.include_router(base_router)

app.include_router(predict_router)