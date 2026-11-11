from fastapi import FastAPI

from app.core.config import settings
from app.api.v1.router import api_router

app = FastAPI(
    title=settings.APP_NAME,
    description="AI-powered stock market assistant backend",
    version="1.0.0"
)


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/")
def root():
    return {"message": "Welcome to Financial Harness API"}


app.include_router(
    api_router,
    prefix=settings.API_V1_PREFIX
)