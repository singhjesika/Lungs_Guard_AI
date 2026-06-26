"""Audio preprocessing — MFCC extraction for cough analysis."""
import numpy as np


def extract_mfcc(audio_path: str, n_mfcc: int = 40, max_len: int = 130) -> np.ndarray:
    try:
        import librosa
        y, sr = librosa.load(audio_path, sr=22050)
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc)
        if mfcc.shape[1] < max_len:
            mfcc = np.pad(mfcc, ((0, 0), (0, max_len - mfcc.shape[1])))
        else:
            mfcc = mfcc[:, :max_len]
        return mfcc[np.newaxis, ..., np.newaxis]  # (1, n_mfcc, max_len, 1)
    except ImportError:
        raise ImportError("librosa is required: pip install librosa")
