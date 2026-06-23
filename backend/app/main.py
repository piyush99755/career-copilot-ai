from fastapi import FastAPI, APIRouter, HTTPException
from app.routers import analyzer

app = FastAPI(
    title="Career Copilot AI",
    version="1.0.0"
)

app.include_router(analyzer.router)


@app.get('/')
def root():
    return {
        "message": "Career Copilot AI Backend Running"
    }
    