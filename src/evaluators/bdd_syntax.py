def score_bdd_syntax(feature_text: str) -> float:
    """Simple syntax heuristic for demo purposes.

    A production version could use a stricter Gherkin parser.
    """
    scenario_count = feature_text.count("Scenario:")
    given_count = feature_text.count("Given ")
    when_count = feature_text.count("When ")
    then_count = feature_text.count("Then ")

    if scenario_count == 0:
        return 0.0

    complete = min(given_count, when_count, then_count)
    return round(complete / scenario_count, 2)
