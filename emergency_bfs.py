# Simple diagnostic tree for BFS-based emergency triage
_diagnostic_tree = {
    "start": ["chest pain", "difficulty breathing", "severe bleeding", "abdominal pain", "head injury"],
    "chest pain": ["Heart Attack", "Angina", "Muscle Strain"],
    "difficulty breathing": ["Asthma Attack", "Pneumonia", "Pulmonary Embolism"],
    "severe bleeding": ["Trauma - Immediate Surgery", "Laceration - Suturing"],
    "abdominal pain": ["Appendicitis", "Gallstones", "Gastroenteritis"],
    "head injury": ["Concussion", "Skull Fracture", "Intracranial Bleeding"],
}

_urgency_map = {
    "Heart Attack": "CRITICAL", "Intracranial Bleeding": "CRITICAL",
    "Trauma - Immediate Surgery": "CRITICAL", "Pulmonary Embolism": "CRITICAL",
    "Asthma Attack": "URGENT", "Appendicitis": "URGENT", "Skull Fracture": "URGENT",
    "Pneumonia": "URGENT", "Angina": "URGENT",
    "Gallstones": "MODERATE", "Gastroenteritis": "MODERATE", "Concussion": "MODERATE",
    "Muscle Strain": "LOW", "Laceration - Suturing": "LOW",
}


def bfs_triage(chief_complaint):
    """
    Explores the diagnostic tree breadth-first starting from the complaint,
    returning all possible conditions found, ranked by urgency.
    """
    complaint = chief_complaint.strip().lower()
    queue = [complaint]
    visited = set()
    possibilities = []

    while queue:
        node = queue.pop(0)
        if node in visited:
            continue
        visited.add(node)

        if node in _diagnostic_tree:
            for child in _diagnostic_tree[node]:
                queue.append(child)
        elif node in _urgency_map:
            possibilities.append({"condition": node, "urgency": _urgency_map[node]})

    urgency_order = {"CRITICAL": 0, "URGENT": 1, "MODERATE": 2, "LOW": 3}
    possibilities.sort(key=lambda x: urgency_order.get(x["urgency"], 4))

    return possibilities