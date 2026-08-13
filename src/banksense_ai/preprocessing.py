import pandas as pd


MODEL_FEATURES = [
    "age",
    "annual_income",
    "customer_tenure_years",
    "gender",
    "country",
    "occupation",
    "employment_status",
    "tenure_group",
]

CATEGORICAL_FEATURES = [
    "gender",
    "country",
    "occupation",
    "employment_status",
    "tenure_group",
]

TENURE_BINS = [-1, 2, 5, 8, 11]

TENURE_LABELS = [
    "0-2 Years",
    "3-5 Years",
    "6-8 Years",
    "9-11 Years",
]


def prepare_features(customer_data: pd.DataFrame) -> pd.DataFrame:
    """Prepare customer data using the same transformations as the notebook."""

    data = customer_data.copy()

    # Create the same tenure groups used during model training
    data["tenure_group"] = pd.cut(
        data["customer_tenure_years"],
        bins=TENURE_BINS,
        labels=TENURE_LABELS,
    )

    # Keep the exact modelling features
    data = data[MODEL_FEATURES]

    # Apply the same one-hot encoding used during training
    encoded = pd.get_dummies(
        data,
        columns=CATEGORICAL_FEATURES,
        drop_first=True,
    )

    # Convert boolean columns to integers
    bool_cols = encoded.select_dtypes(include="bool").columns
    encoded[bool_cols] = encoded[bool_cols].astype(int)

    return encoded