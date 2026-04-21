# Rule-based validation engine (extensible)

RULES = {
    "routes": "CRITICAL",
    "interfaces": "HIGH",
    "vlans": "MEDIUM"
}

def evaluate(validation):
    findings = []
    for k, v in validation.items():
        if not v:
            findings.append({
                "control": k,
                "severity": RULES[k]
            })
    return findings