from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.risk_engine import RiskEngine

router = APIRouter()
engine = RiskEngine()

class SymptomInput(BaseModel):
    gender: int           
    age: int
    smoking: int
    yellow_fingers: int
    anxiety: int
    peer_pressure: int
    chronic_disease: int
    fatigue: int
    allergy: int
    wheezing: int
    alcohol_consuming: int
    coughing: int
    shortness_of_breath: int
    swallowing_difficulty: int
    chest_pain: int

@router.post("/symptoms")
def predict_from_symptoms(data: SymptomInput):
    try:
        result = engine.predict_from_symptoms(data.dict())
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/xray")
def predict_from_xray():
    # Placeholder — see xray_service.py
    return {"message": "X-ray prediction endpoint (connect via xray_service)"}
