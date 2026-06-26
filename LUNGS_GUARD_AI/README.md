# 🫁 LungsGuard AI

Multi-modal lung cancer risk detection system using symptom analysis, cough audio, and chest X-rays.

## Project Structure

```
LUNGS_GUARD_AI/
├── app/
│   ├── main.py              FastAPI app factory
│   ├── config.py            Settings (reads .env)
│   ├── api/
│   │   ├── routes.py        Router aggregator
│   │   └── predict_api.py   /api/predict/* endpoints
│   ├── ui/
│   │   ├── dashboard.py     Streamlit main page
│   │   ├── upload_page.py   Symptom form + prediction UI
│   │   └── report_page.py   PDF report viewer
│   ├── services/
│   │   ├── symptom_service.py   ML training + inference (6 classifiers)
│   │   ├── cough_service.py     Audio CNN inference
│   │   ├── xray_service.py      Image CNN inference
│   │   └── risk_engine.py       Weighted risk fusion (brain)
│   ├── realtime/
│   │   ├── oxygen_monitor.py    Async SpO2 monitor
│   │   ├── alert_system.py      Critical alert dispatcher
│   │   └── sensor_stream.py     Live / mock sensor stream
│   └── utils/
│       ├── preprocess.py        Shared data cleaning
│       ├── audio_utils.py       MFCC extraction
│       ├── image_utils.py       X-ray tensor prep
│       ├── explainability.py    SHAP feature importance
│       └── logger.py            Centralised logging
├── models/                  Trained model artifacts (.pkl / .h5)
├── data/raw/                Original CSV + Lungs_original.py
├── notebooks/               Jupyter training notebooks
├── reports/                 Patient logs, PDFs, visualizations
├── tests/                   pytest suite
├── requirements.txt
├── .env
└── run.py
```

## Quick Start

```bash
pip install -r requirements.txt

# 1. Train symptom model
jupyter notebook notebooks/symptom_training.ipynb
# or: python -c "from app.services.symptom_service import train_all_models; train_all_models('data/raw/survey_lung_cancer.csv')"

# 2. Start API
python run.py api          # http://localhost:8000/docs

# 3. Start UI
python run.py ui           # http://localhost:8501

# 4. Both together
python run.py both

# 5. Run tests
pytest tests/
```

## Bug Fixes from Original Lungs.py

| # | Original Bug | Fixed In |
|---|---|---|
| 1 | `kNeighborsClassifier` (wrong case) | `symptom_service.py` |
| 2 | `OneVSRestClassifier` (wrong case) | `symptom_service.py` |
| 3 | `svc(c=10, ...)` (wrong case) | `symptom_service.py` |
| 4 | `x_tran` (typo for `x_train`) | `symptom_service.py` |
| 5 | `GaussiansNB` (wrong class name) | `symptom_service.py` |
| 6 | `accuracy = precision_score(...)` (wrong metric) | `symptom_service.py` |
| 7 | `corelation` typo in heatmap | `symptom_service.py` |
| 8 | `plt.xtricks` / `plt.his` typos | Fixed in notebooks |
| 9 | `'orage'` color string (should be `'orange'`) | Fixed in notebooks |

## Models

| Modality | File | Notes |
|---|---|---|
| Symptom (Random Forest) | `models/symptom_model.pkl` | Auto-saved on training |
| Scaler | `models/scaler.pkl` | StandardScaler for symptom features |
| Cough CNN | `models/cough_model.h5` | Train via `notebooks/cough_training.ipynb` |
| X-Ray CNN | `models/xray_model.h5` | Train via `notebooks/xray_training.ipynb` |
