from pathlib import Path

import joblib
import pandas as pd

from banksense_ai.preprocessing import prepare_features


MODEL_PATH = (
    Path(__file__).resolve().parents[2]
    / "models"
    / "banksense_rf_tuned.joblib"
)


def load_model():
    """Load the saved BankSense AI model artifact."""
    artifact = joblib.load(MODEL_PATH)
    return artifact["model"], artifact["feature_columns"]


def predict_risk(customer_data: pd.DataFrame) -> pd.DataFrame:
    """Predict high-risk status for one or more customers."""

    model, feature_columns = load_model()

    features = prepare_features(customer_data)

    # Ensure prediction data has exactly the same columns as training data
    features = features.reindex(columns=feature_columns, fill_value=0)

    predictions = model.predict(features)
    probabilities = model.predict_proba(features)[:, 1]

    results = customer_data.copy()
    results["high_risk_prediction"] = predictions
    results["high_risk_probability"] = probabilities

    return results