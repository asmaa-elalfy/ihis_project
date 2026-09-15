_phq9_questions = [
    "Little interest or pleasure in doing things",
    "Feeling down, depressed, or hopeless",
    "Trouble falling/staying asleep, or sleeping too much",
    "Feeling tired or having little energy",
    "Poor appetite or overeating",
    "Feeling bad about yourself or that you are a failure",
    "Trouble concentrating on things",
    "Moving or speaking slowly, or being fidgety/restless",
    "Thoughts that you would be better off dead or of hurting yourself"
]

_gad7_questions = [
    "Feeling nervous, anxious, or on edge",
    "Not being able to stop or control worrying",
    "Worrying too much about different things",
    "Trouble relaxing",
    "Being so restless that it is hard to sit still",
    "Becoming easily annoyed or irritable",
    "Feeling afraid as if something awful might happen"
]


def score_depression(answers):
    """answers: list of 9 ints (0-3) matching PHQ-9 questions."""
    total = sum(answers)

    if total <= 4:
        severity = "Minimal"
    elif total <= 9:
        severity = "Mild"
    elif total <= 14:
        severity = "Moderate"
    elif total <= 19:
        severity = "Moderately Severe"
    else:
        severity = "Severe"

    self_harm_flag = answers[8] > 0  # question 9 is about self-harm thoughts

    return {"total": total, "severity": severity, "self_harm_flag": self_harm_flag}


def score_anxiety(answers):
    """answers: list of 7 ints (0-3) matching GAD-7 questions."""
    total = sum(answers)

    if total <= 4:
        severity = "Minimal"
    elif total <= 9:
        severity = "Mild"
    elif total <= 14:
        severity = "Moderate"
    else:
        severity = "Severe"

    return {"total": total, "severity": severity}


def get_recommendations(depression_result, anxiety_result):
    recs = []

    if depression_result["self_harm_flag"]:
        recs.append("Please reach out to a mental health professional or crisis line immediately.")

    if depression_result["severity"] in ["Moderate", "Moderately Severe", "Severe"]:
        recs.append("Recommend follow-up with a psychiatrist or psychologist.")
    elif depression_result["severity"] == "Mild":
        recs.append("Consider counseling or lifestyle changes; monitor symptoms.")

    if anxiety_result["severity"] in ["Moderate", "Severe"]:
        recs.append("Recommend anxiety management support (therapy, relaxation techniques).")

    if not recs:
        recs.append("No significant concerns detected. Continue routine wellbeing checks.")

    return recs