import pickle
import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
)
from sklearn.preprocessing import StandardScaler
from app.utils.logger import get_logger

logger = get_logger(__name__)
MODEL_PATH = Path("models/symptom_model.pkl")
SCALER_PATH = Path("models/scaler.pkl")


def load_and_preprocess(csv_path: str) -> tuple:
    df = pd.read_csv(csv_path)
    df["GENDER"] = df["GENDER"].map({"M": 0, "F": 1})
    df["LUNG_CANCER"] = df["LUNG_CANCER"].map({"YES": 1, "NO": 0})

    X = df.iloc[:, :-1]
    y = df["LUNG_CANCER"].values.ravel()

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=1/3, random_state=0
    )
    return X_train, X_test, y_train, y_test, scaler, X.columns.tolist()


def train_all_models(csv_path: str) -> dict:
    X_train, X_test, y_train, y_test, scaler, feature_names = load_and_preprocess(csv_path)

    models = {
        "Logistic Regression": LogisticRegression(max_iter=200),
        "KNN": KNeighborsClassifier(n_neighbors=3, metric="minkowski", p=2),
        "Decision Tree": DecisionTreeClassifier(random_state=0, criterion="entropy"),
        "SVM": OneVsRestClassifier(
            BaggingClassifier(SVC(C=10, kernel="rbf", random_state=9, probability=True), n_jobs=-1)
        ),
        "Naive Bayes": GaussianNB(),
        "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
    }

    results = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        metrics = {
            "accuracy":  accuracy_score(y_test, y_pred),
            "precision": precision_score(y_test, y_pred, zero_division=0),
            "recall":    recall_score(y_test, y_pred, zero_division=0),
            "f1":        f1_score(y_test, y_pred, zero_division=0),
            "confusion_matrix": confusion_matrix(y_test, y_pred).tolist(),
        }
        results[name] = {"model": model, "metrics": metrics}
        logger.info(f"{name} accuracy: {metrics['accuracy']:.4f}")

    best = results["Random Forest"]["model"]
    MODEL_PATH.parent.mkdir(exist_ok=True)
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(best, f)
    with open(SCALER_PATH, "wb") as f:
        pickle.dump(scaler, f)

    return results


def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError("symptom_model.pkl not found. Run training first.")
    with open(MODEL_PATH, "rb") as f:
        return pickle.load(f)


def load_scaler():
    if not SCALER_PATH.exists():
        raise FileNotFoundError("scaler.pkl not found. Run training first.")
    with open(SCALER_PATH, "rb") as f:
        return pickle.load(f)


def get_feature_importance(features: dict) -> dict:
    model = load_model()
    if not hasattr(model, "feature_importances_"):
        return {}
    names = list(features.keys())
    importances = model.feature_importances_
    impacts = {}
    for name, imp in zip(names, importances):
        val = features[name]
        if name == "age":
            direction = 1 if val >= 55 else -1
        elif name == "gender":
            direction = 1
        else:
            direction = 1 if val == 2 else -1
        impacts[name] = round(float(imp) * direction, 4)
    return impacts


def predict_single(features: dict) -> dict:
    model = load_model()
    scaler = load_scaler()
    X = np.array(list(features.values())).reshape(1, -1)
    X_scaled = scaler.transform(X)
    prob = model.predict_proba(X_scaled)[0][1] if hasattr(model, "predict_proba") else None
    pred = model.predict(X_scaled)[0]
    return {
        "prediction": int(pred),
        "label": "HIGH RISK" if pred == 1 else "LOW RISK",
        "probability": round(float(prob), 4) if prob is not None else None,
    }