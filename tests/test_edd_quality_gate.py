import json
from pathlib import Path

from src.evaluate_bdd_output import evaluate

ROOT = Path(__file__).resolve().parents[1]


def test_ai_generated_bdd_scenarios_meet_quality_gate():
    feature_text = (ROOT / "data" / "generated_scenarios.feature").read_text(encoding="utf-8")
    config = json.loads((ROOT / "data" / "expected_coverage.json").read_text(encoding="utf-8"))

    scores = evaluate(feature_text, config)
    thresholds = config["quality_thresholds"]

    assert scores["groundedness"] >= thresholds["groundedness"]
    assert scores["coverage"] >= thresholds["coverage"]
    assert scores["hallucination_risk"] <= thresholds["hallucination_risk"]
    assert scores["bdd_syntax_validity"] >= thresholds["bdd_syntax_validity"]
    assert scores["automation_readiness"] >= thresholds["automation_readiness"]
