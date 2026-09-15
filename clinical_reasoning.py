_disease_symptom_map = {
    "Influenza": {"fever", "cough", "fatigue", "body ache", "headache"},
    "Common Cold": {"cough", "sore throat", "runny nose", "sneezing"},
    "Pneumonia": {"fever", "cough", "shortness of breath", "chest pain"},
    "Migraine": {"headache", "nausea", "sensitivity to light"},
    "Gastroenteritis": {"nausea", "vomiting", "diarrhea", "abdominal pain"},
    "Urinary Tract Infection": {"burning urination", "frequent urination", "abdominal pain", "fever"},
    "Diabetes": {"frequent urination", "increased thirst", "fatigue", "blurred vision"},
    "Hypertension": {"headache", "dizziness", "blurred vision"},
}


def generate_differential(patient_symptoms):
    """
    patient_symptoms: list of symptom strings (lowercase, matching keywords above)
    Returns a ranked list of possible diagnoses with match scores and reasoning.
    """
    patient_set = set(s.strip().lower() for s in patient_symptoms)
    results = []

    for disease, disease_symptoms in _disease_symptom_map.items():
        matched = patient_set & disease_symptoms
        if matched:
            score = len(matched) / len(disease_symptoms)
            results.append({
                "disease": disease,
                "match_percentage": round(score * 100, 1),
                "matched_symptoms": sorted(matched),
                "reasoning": (
                    f"{len(matched)} out of {len(disease_symptoms)} typical symptoms "
                    f"of {disease} were reported: {', '.join(sorted(matched))}."
                )
            })

    results.sort(key=lambda r: r["match_percentage"], reverse=True)
    return results