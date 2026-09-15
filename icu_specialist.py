def assess_vitals(heart_rate, systolic_bp, spo2, temperature, respiratory_rate):
    """
    Monitors vital signs and flags abnormal findings.
    Returns a status, a list of alerts, and recommended interventions.
    """
    alerts = []

    if heart_rate > 120:
        alerts.append("Severe tachycardia (heart rate too high)")
    elif heart_rate < 50:
        alerts.append("Severe bradycardia (heart rate too low)")

    if systolic_bp < 90:
        alerts.append("Hypotension (low blood pressure)")
    elif systolic_bp > 180:
        alerts.append("Hypertensive crisis (very high blood pressure)")

    if spo2 < 90:
        alerts.append("Severe hypoxia (low oxygen saturation)")

    if temperature >= 39:
        alerts.append("High fever")
    elif temperature < 35:
        alerts.append("Hypothermia")

    if respiratory_rate > 30:
        alerts.append("Severe tachypnea (breathing too fast)")
    elif respiratory_rate < 8:
        alerts.append("Severe bradypnea (breathing too slow)")

    if len(alerts) >= 2:
        status = "CRITICAL"
        interventions = [
            "Immediate physician notification",
            "Continuous vital sign monitoring",
            "Prepare for possible emergency intervention"
        ]
    elif len(alerts) == 1:
        status = "WARNING"
        interventions = [
            "Notify nursing staff",
            "Recheck vitals within 15 minutes"
        ]
    else:
        status = "STABLE"
        interventions = ["Continue routine monitoring"]

    return {
        "status": status,
        "alerts": alerts,
        "interventions": interventions
    }