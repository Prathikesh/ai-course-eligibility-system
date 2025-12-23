import joblib
import pandas as pd

dt_model = joblib.load("app/ml/decision_tree.pkl")
lr_model = joblib.load("app/ml/logistic_regression.pkl")

def predict_eligibility(input_data: dict):
    df = pd.DataFrame([input_data])

    eligibility = dt_model.predict(df)[0]
    probability = lr_model.predict_proba(df)[0][1]

    return {
        "eligible": bool(eligibility),
        "eligibility_score": round(probability * 100, 2)
    }
