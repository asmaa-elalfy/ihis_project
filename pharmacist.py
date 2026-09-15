_interactions = {
    frozenset(["warfarin", "aspirin"]): "High risk of bleeding when combined.",
    frozenset(["warfarin", "ibuprofen"]): "Increased bleeding risk; avoid combination.",
    frozenset(["metformin", "alcohol"]): "Increased risk of lactic acidosis.",
    frozenset(["ace inhibitor", "potassium"]): "Risk of dangerously high potassium levels.",
    frozenset(["ssri", "maoi"]): "Risk of serotonin syndrome; contraindicated combination.",
}

_contraindications = {
    "ibuprofen": ["kidney disease", "peptic ulcer"],
    "metformin": ["kidney disease"],
    "aspirin": ["peptic ulcer", "bleeding disorder"],
    "ace inhibitor": ["pregnancy"],
}

_recommendations = {
    "fever": ["Paracetamol"],
    "pain": ["Paracetamol", "Ibuprofen"],
    "hypertension": ["ACE Inhibitor", "Amlodipine"],
    "diabetes": ["Metformin"],
    "infection": ["Antibiotic (as prescribed)"],
}


def check_interactions(drug_list):
    drugs = [d.strip().lower() for d in drug_list]
    alerts = []
    for i in range(len(drugs)):
        for j in range(i + 1, len(drugs)):
            pair = frozenset([drugs[i], drugs[j]])
            if pair in _interactions:
                alerts.append(f"{drugs[i]} + {drugs[j]}: {_interactions[pair]}")
    return alerts


def check_contraindications(drug_list, conditions):
    drugs = [d.strip().lower() for d in drug_list]
    conds = [c.strip().lower() for c in conditions]
    flags = []
    for drug in drugs:
        if drug in _contraindications:
            for cond in conds:
                if cond in _contraindications[drug]:
                    flags.append(f"{drug} is contraindicated with {cond}")
    return flags


def suggest_medications(symptom):
    symptom = symptom.strip().lower()
    return _recommendations.get(symptom, ["No specific recommendation available. Consult a physician."])