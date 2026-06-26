"""
Cough audio analysis service.
Loads a trained cough model (cough_model.h5) and predicts from audio features.
"""
from pathlib import Path
from app.utils.audio_utils import extract_mfcc
from app.utils.logger import get_logger

logger = get_logger(__name__)
MODEL_PATH = Path("models/cough_model.h5")


def predict_from_audio(audio_path: str) -> dict:
    """Extract MFCC features and run inference."""
    if not MODEL_PATH.exists():
        return {"error": "cough_model.h5 not found. Train or provide the model."}
    try:
        import tensorflow as tf
        model = tf.keras.models.load_model(str(MODEL_PATH))
        features = extract_mfcc(audio_path)
        prob = float(model.predict(features)[0][0])
        return {"probability": round(prob, 4), "label": "ABNORMAL" if prob > 0.5 else "NORMAL"}
    except Exception as e:
        logger.error(f"Cough prediction failed: {e}")
        return {"error": str(e)}
