def score_coverage(feature_text: str, required_scenarios: list[str]) -> float:
    text = feature_text.lower()
    matched = [item for item in required_scenarios if item.lower() in text]

    if not required_scenarios:
        return 1.0

    return round(len(matched) / len(required_scenarios), 2)
