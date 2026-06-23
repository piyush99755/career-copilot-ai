from fastapi import FastAPI

app = FastAPI(
    title="Career Copilot AI",
    version="1.0.0"
)

@app.get('/')
def root():
    return {
        "message": "Career Copilot AI Backend Running"
    }
    