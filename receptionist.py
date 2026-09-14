def triage_patient(chief_complaint):
    text = chief_complaint.lower()

    if "chest pain" in text or "difficulty breathing" in text:
        return "Emergency Department"

    if "tooth" in text or "teeth" in text:
        return "Dental Clinic"

    if "fever" in text or "cough" in text or "cold" in text:
        return "Internal Medicine"

    if "child" in text or "baby" in text:
        return "Pediatrics"

    return "General Consultation"