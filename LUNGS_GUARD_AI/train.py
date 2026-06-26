from app.services.symptom_service import train_all_models

if __name__ == "__main__":
    results = train_all_models("data/raw/survey_lung_cancer.csv")
    for name, r in results.items():
        print(name, r["metrics"]["accuracy"])