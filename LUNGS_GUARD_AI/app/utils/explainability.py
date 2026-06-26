"""
SHAP-based explainability for symptom model predictions.
"""
from app.utils.logger import get_logger
logger = get_logger(__name__)


def explain_prediction(model, X, feature_names: list) -> dict:
    try:
        import shap
        explainer = shap.TreeExplainer(model)
        shap_values = explainer.shap_values(X)
        values = shap_values[1][0] if isinstance(shap_values, list) else shap_values[0]
        return dict(zip(feature_names, [round(float(v), 4) for v in values]))
    except ImportError:
        logger.warning("shap not installed; skipping explainability")
        return {}
