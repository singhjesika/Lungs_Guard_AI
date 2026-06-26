"""Image preprocessing for X-ray CNN inference."""
import numpy as np


def preprocess_xray(image_path: str, target_size: tuple = (224, 224)) -> np.ndarray:
    try:
        from PIL import Image
        img = Image.open(image_path).convert("RGB").resize(target_size)
        arr = np.array(img, dtype=np.float32) / 255.0
        return arr[np.newaxis]  # (1, H, W, 3)
    except ImportError:
        raise ImportError("Pillow is required: pip install Pillow")
