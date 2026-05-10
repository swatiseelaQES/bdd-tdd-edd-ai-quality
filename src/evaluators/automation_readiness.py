def score_automation_readiness(feature_text: str) -> float:
    """Scores whether generated scenarios contain enough structure to automate.

    This intentionally stays simple for the demo:
    - Scenario exists
    - Given/When/Then exists
    - Endpoint reference exists
    """
    scenario_count = feature_text.count("Scenario:")
    if scenario_count == 0:
        return 0.0

    score = 0
    score += 0.35 if "Given " in feature_text else 0
    score += 0.35 if "When " in feature_text else 0
    score += 0.20 if "Then " in feature_text else 0
    score += 0.10 if "/booking" in feature_text else 0

    return round(score, 2)
