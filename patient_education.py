_knowledge_base = [
    {"keywords": ["diabetes", "sugar"], "answer": "Diabetes is a condition where blood sugar levels are too high. Managing diet, exercise, and medication as prescribed is essential."},
    {"keywords": ["flu", "influenza"], "answer": "The flu is a viral infection causing fever, cough, and fatigue. Rest, fluids, and antiviral medication if prescribed can help recovery."},
    {"keywords": ["hypertension", "blood pressure"], "answer": "Hypertension means high blood pressure. It's managed through diet, exercise, reducing salt intake, and prescribed medication."},
    {"keywords": ["paracetamol", "acetaminophen"], "answer": "Paracetamol is used to relieve mild to moderate pain and reduce fever. Always follow the prescribed dosage."},
    {"keywords": ["antibiotic", "antibiotics"], "answer": "Antibiotics treat bacterial infections. Always complete the full course as prescribed, even if you feel better."},
    {"keywords": ["pneumonia"], "answer": "Pneumonia is an infection that inflames the air sacs in the lungs. Symptoms include cough, fever, and difficulty breathing. Treatment depends on severity."},
    {"keywords": ["fracture", "broken bone"], "answer": "A fracture is a broken bone. Treatment may include immobilization with a cast, and in some cases, surgery."},
]

_default_answer = "I don't have specific information on that yet. Please consult your doctor for personalized medical advice."


def get_answer(question):
    text = question.lower()

    for entry in _knowledge_base:
        for keyword in entry["keywords"]:
            if keyword in text:
                return entry["answer"]

    return _default_answer