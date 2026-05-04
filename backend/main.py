from fastapi import FastAPI

app = FastAPI(
    title="Disaster Dashboard API",
    description="Backend API for Nepal Disaster Risk Intelligence Dashboard",
    version="1.0.0"
)

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

@app.get("/api/hazards")
def get_hazards():
    return {
        "hazards": [
            "Flood",
            "Landslide",
            "Rainfall",
            "Settlement Exposure"
        ]
    }