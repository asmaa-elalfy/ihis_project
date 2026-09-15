# DFS-based diagnostic pathway for oncology-related symptoms
_oncology_tree = {
    "unexplained weight loss": {
        "children": ["persistent cough", "abdominal mass", "night sweats"],
        "leaf": False
    },
    "persistent cough": {
        "children": ["Possible Lung Cancer - Stage Workup Needed"],
        "leaf": False
    },
    "abdominal mass": {
        "children": ["Possible GI Cancer - Imaging & Biopsy Needed"],
        "leaf": False
    },
    "night sweats": {
        "children": ["Possible Lymphoma - Blood Work & Biopsy Needed"],
        "leaf": False
    },
    "Possible Lung Cancer - Stage Workup Needed": {"children": [], "leaf": True},
    "Possible GI Cancer - Imaging & Biopsy Needed": {"children": [], "leaf": True},
    "Possible Lymphoma - Blood Work & Biopsy Needed": {"children": [], "leaf": True},
}

_investigations = {
    "Possible Lung Cancer - Stage Workup Needed": ["Chest CT scan", "Biopsy", "PET scan for staging"],
    "Possible GI Cancer - Imaging & Biopsy Needed": ["Abdominal CT/MRI", "Endoscopy", "Tumor markers"],
    "Possible Lymphoma - Blood Work & Biopsy Needed": ["Complete blood count", "Lymph node biopsy", "PET-CT scan"],
}


def dfs_oncology_pathway(starting_symptom):
    """
    Explores the diagnostic pathway depth-first, following one branch
    fully before backtracking, returning the path taken and final findings.
    """
    symptom = starting_symptom.strip().lower()
    path = []
    findings = []

    def dfs(node):
        path.append(node)
        node_data = _oncology_tree.get(node)

        if not node_data:
            return

        if node_data["leaf"]:
            findings.append({
                "diagnosis": node,
                "recommended_investigations": _investigations.get(node, [])
            })
            return

        for child in node_data["children"]:
            dfs(child)

    dfs(symptom)
    return {"path": path, "findings": findings}