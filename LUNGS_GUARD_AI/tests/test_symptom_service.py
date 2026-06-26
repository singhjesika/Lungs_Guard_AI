"""
Basic tests for symptom service.
Run: pytest tests/
"""
import pytest

SAMPLE = {
    "gender": 1, "age": 55, "smoking": 2, "yellow_fingers": 1,
    "anxiety": 1, "peer_pressure": 1, "chronic_disease": 1,
    "fatigue": 2, "allergy": 1, "wheezing": 2, "alcohol_consuming": 1,
    "coughing": 2, "shortness_of_breath": 2,
    "swallowing_difficulty": 1, "chest_pain": 2,
}


def test_risk_engine_structure():
    from app.services.risk_engine import RiskEngine
    engine = RiskEngine()
    fused = engine.fuse(symptom_prob=0.8)
    assert "fused_risk_score" in fused
    assert fused["risk_level"] in ("LOW", "MODERATE", "HIGH", "CRITICAL")


def test_score_to_level():
    from app.services.risk_engine import RiskEngine
    engine = RiskEngine()
    assert engine._score_to_level(0.9)[0] == "CRITICAL"
    assert engine._score_to_level(0.6)[0] == "HIGH"
    assert engine._score_to_level(0.3)[0] == "MODERATE"
    assert engine._score_to_level(0.1)[0] == "LOW"
