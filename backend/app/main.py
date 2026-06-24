from fastapi import FastAPI, APIRouter, HTTPException
from app.routers import analyzer
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Career Copilot AI",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173",
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)

app.include_router(analyzer.router)


@app.get('/')
def root():
    return {
        "message": "Career Copilot AI Backend Running"
    }
    