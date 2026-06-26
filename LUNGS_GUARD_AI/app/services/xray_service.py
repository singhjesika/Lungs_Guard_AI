"""
Chest X-ray analysis service.
Loads xray_model.h5 and predicts from preprocessed image tensors.
"""
from pathlib import Path
from app.utils.image_utils import preprocess_xray
from app.utils.logger import get_logger

logger = get_logger(__name__)
MODEL_PATH = Path("models/xray_model.h5")


def predict_from_image(image_path: str) -> dict:
    """Preprocess X-ray and run CNN inference."""
    if not MODEL_PATH.exists():
        return {"error": "xray_model.h5 not found. Train or provide the model."}
    try:
        import tensorflow as tf
        model = tf.keras.models.load_model(str(MODEL_PATH))
        tensor = preprocess_xray(image_path)
        prob = float(model.predict(tensor)[0][0])
        return {"probability": round(prob, 4), "label": "ABNORMAL" if prob > 0.5 else "NORMAL"}
    except Exception as e:
        logger.error(f"X-ray prediction failed: {e}")
        return {"error": str(e)}
