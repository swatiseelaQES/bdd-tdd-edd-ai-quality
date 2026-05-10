def score_hallucination_risk(feature_text: str, unsupported_terms: list[str]) -> float:
    text = feature_text.lower()
    unsupported_hits = sum(1 for term in unsupported_terms if term.lower() in text)

    scenario_count = max(feature_text.count("Scenario:"), 1)
    risk = unsupported_hits / scenario_count

    return round(min(risk, 1.0), 2)
