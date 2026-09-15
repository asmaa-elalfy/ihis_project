from receptionist import triage_patient
from disease_predictor import predict_disease, assess_risk
from clinical_reasoning import generate_differential


def generate_integrated_report(full_name, age, chief_complaint, symptoms_text, fever, cough, fatigue):
    """
    Orchestrates multiple AI specialists together and produces
    one combined clinical report for a patient.
    """
    # Agent 1: Receptionist AI - routing
    department = triage_patient(chief_complaint)

    # Agent 2: General Practitioner AI - disease prediction + risk
    prediction = predict_disease(fever, cough, fatigue, age)
    risk_info = assess_risk(prediction, age)

    # Agent 3: Clinical Reasoning AI - differential diagnosis
    symptoms_list = [s.strip() for s in symptoms_text.split(",") if s.strip()]
    differential = generate_differential(symptoms_list)

    return {
        "patient_name": full_name,
        "age": age,
        "chief_complaint": chief_complaint,
        "routed_department": department,
        "gp_prediction": prediction,
        "risk_level": risk_info["risk_level"],
        "recommendations": risk_info["recommendations"],
        "differential_diagnoses": differential,
    }