def score_groundedness(feature_text: str, supported_terms: list[str], unsupported_terms: list[str]) -> float:
    text = feature_text.lower()

    supported_hits = sum(1 for term in supported_terms if term.lower() in text)
    unsupported_hits = sum(1 for term in unsupported_terms if term.lower() in text)

    if supported_hits + unsupported_hits == 0:
        return 0.0

    score = supported_hits / (supported_hits + unsupported_hits)
    return round(score, 2)
