"""Data preprocessing utilities shared across services."""
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


def encode_lung_csv(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["GENDER"] = df["GENDER"].map({"M": 0, "F": 1})
    df["LUNG_CANCER"] = df["LUNG_CANCER"].map({"YES": 1, "NO": 0})
    return df


def scale_features(X_train, X_test):
    scaler = StandardScaler()
    return scaler.fit_transform(X_train), scaler.transform(X_test), scaler
