# Simplified simulation of treatment plan comparison (RL-inspired scoring)
_treatment_plans = {
    "Hypertension": [
        {"name": "Lifestyle changes only", "effectiveness": 0.4, "risk": 0.1, "cost": 0.1},
        {"name": "ACE Inhibitor + lifestyle", "effectiveness": 0.8, "risk": 0.3, "cost": 0.4},
        {"name": "Combination therapy (2 drugs)", "effectiveness": 0.9, "risk": 0.5, "cost": 0.6},
    ],
    "Diabetes": [
        {"name": "Diet and exercise only", "effectiveness": 0.5, "risk": 0.1, "cost": 0.1},
        {"name": "Metformin + lifestyle", "effectiveness": 0.85, "risk": 0.2, "cost": 0.3},
        {"name": "Insulin therapy", "effectiveness": 0.95, "risk": 0.6, "cost": 0.7},
    ],
    "Flu": [
        {"name": "Rest and fluids", "effectiveness": 0.6, "risk": 0.05, "cost": 0.05},
        {"name": "Antiviral medication", "effectiveness": 0.85, "risk": 0.2, "cost": 0.4},
    ],
}


def _reward(plan):
    """
    Simple reward function simulating an RL-style trade-off:
    reward = effectiveness - (risk + cost) penalty
    """
    return round(plan["effectiveness"] - (0.5 * plan["risk"] + 0.3 * plan["cost"]), 3)


def optimize_treatment(condition):
    """
    Compares alternative treatment plans for a condition and
    recommends the one with the highest simulated reward score.
    """
    plans = _treatment_plans.get(condition, [])
    if not plans:
        return None

    scored = []
    for plan in plans:
        reward = _reward(plan)
        scored.append({**plan, "reward_score": reward})

    scored.sort(key=lambda p: p["reward_score"], reverse=True)

    return {
        "condition": condition,
        "ranked_plans": scored,
        "recommended": scored[0]["name"]
    }