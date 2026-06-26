"""
Risk Engine — brain of the system.
Fuses predictions from symptom, cough, and x-ray services
into a unified risk score with SHAP-style explanation.
"""
from app.services.symptom_service import predict_single
from app.utils.logger import get_logger

logger = get_logger(__name__)

RISK_WEIGHTS = {
    "symptom": 0.50,
    "cough":   0.20,
    "xray":    0.30,
}

RISK_LEVELS = [
    (0.75, "CRITICAL", "🔴"),
    (0.50, "HIGH",     "🟠"),
    (0.25, "MODERATE", "🟡"),
    (0.00, "LOW",      "🟢"),
]


class RiskEngine:
    def predict_from_symptoms(self, features: dict) -> dict:
        result = predict_single(features)
        score = result["probability"] or (1.0 if result["prediction"] else 0.0)
        level, icon = self._score_to_level(score)
        return {
            **result,
            "risk_score": round(score, 4),
            "risk_level": level,
            "icon": icon,
            "source": "symptom",
        }

    def fuse(self, symptom_prob=None, cough_prob=None, xray_prob=None) -> dict:
        """Weighted fusion of all modalities."""
        total_weight = 0
        fused = 0.0
        for prob, key in [(symptom_prob, "symptom"), (cough_prob, "cough"), (xray_prob, "xray")]:
            if prob is not None:
                fused += prob * RISK_WEIGHTS[key]
                total_weight += RISK_WEIGHTS[key]
        if total_weight == 0:
            return {"error": "No modality provided"}
        fused /= total_weight
        level, icon = self._score_to_level(fused)
        return {
            "fused_risk_score": round(fused, 4),
            "risk_level": level,
            "icon": icon,
            "components": {
                "symptom": symptom_prob,
                "cough": cough_prob,
                "xray": xray_prob,
            },
        }

    @staticmethod
    def _score_to_level(score: float):
        for threshold, level, icon in RISK_LEVELS:
            if score >= threshold:
                return level, icon
        return "LOW", "🟢"
