from fastapi import APIRouter
from app.api.predict_api import router as predict_router

router = APIRouter()
router.include_router(predict_router, prefix="/predict", tags=["Prediction"])

@router.get("/health")
def health_check():
    return {"status": "ok"}
