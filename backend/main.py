from fastapi import FastAPI
from routes.hazards import router as hazards_router

app = FastAPI(
    title="Disaster Dashboard API",
    description="Backend API for Nepal Disaster Risk Intelligence Dashboard",
    version="1.0.0"
)

app.include_router(hazards_router, prefix="/api", tags=["Hazards"])

@app.get("/")
def home():
    return {
        "message": "Disaster Dashboard Backend is running successfully"
    }

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "backend"
    }