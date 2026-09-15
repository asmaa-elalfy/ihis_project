import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load the dataset once when the app starts
_data = pd.read_csv("disease_data.csv")

_features = ["fever", "cough", "fatigue", "age"]
_X = _data[_features]
_y = _data["diagnosis"]

# Train a simple Decision Tree model
_model = DecisionTreeClassifier(random_state=42)
_model.fit(_X, _y)


def predict_disease(fever, cough, fatigue, age):
    """
    Takes basic symptom inputs and returns a predicted diagnosis.
    """
    input_data = pd.DataFrame(
        [[fever, cough, fatigue, age]],
        columns=_features
    )
    prediction = _model.predict(input_data)[0]
    return prediction


def assess_risk(diagnosis, age):
    """
    Simple rule-based risk assessment based on diagnosis and age.
    """
    if diagnosis == "Flu":
        risk_level = "High" if age >= 60 else "Moderate"
        recommendations = ["Rest and fluids", "Monitor temperature", "Antiviral consultation if symptoms worsen"]

    elif diagnosis == "Diabetes":
        risk_level = "High"
        recommendations = ["Fasting blood glucose test", "HbA1c test", "Dietician referral"]

    elif diagnosis == "Common Cold":
        risk_level = "Low"
        recommendations = ["Rest and fluids", "Over-the-counter symptom relief"]

    else:  # Healthy
        risk_level = "Low"
        recommendations = ["Routine annual checkup"]

    return {
        "risk_level": risk_level,
        "recommendations": recommendations
    }