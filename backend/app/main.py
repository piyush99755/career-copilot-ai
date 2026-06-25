from fastapi import FastAPI, APIRouter, HTTPException
from app.routers import analyzer, resume
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine
from app.models import Base


Base.metadata.create_all(
    bind=engine
)

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
app.include_router(resume.router)


@app.get('/')
def root():
    return {
        "message": "Career Copilot AI Backend Running"
    }
    