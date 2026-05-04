import json
from pathlib import Path
from fastapi import APIRouter

router = APIRouter()

DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "hazards.json"

@router.get("/hazards")
def get_hazards():
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        hazards = json.load(file)

    return {
        "count": len(hazards),
        "hazards": hazards
    }