from pathlib import Path
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from evaluators.bdd_syntax import score_bdd_syntax
from evaluators.coverage import score_coverage
from evaluators.groundedness import score_groundedness
from evaluators.hallucination import score_hallucination_risk
from evaluators.automation_readiness import score_automation_readiness


def evaluate(feature_text: str, config: dict) -> dict:
    return {
        "groundedness": score_groundedness(
            feature_text,
            config["known_supported_terms"],
            config["unsupported_terms"]
        ),
        "coverage": score_coverage(
            feature_text,
            config["required_negative_scenarios"]
        ),
        "hallucination_risk": score_hallucination_risk(
            feature_text,
            config["unsupported_terms"]
        ),
        "bdd_syntax_validity": score_bdd_syntax(feature_text),
        "automation_readiness": score_automation_readiness(feature_text)
    }


def write_report(scores: dict) -> None:
    report_path = ROOT / "reports" / "evaluation_report.md"

    lines = [
        "# EDD Evaluation Report",
        "",
        "Evaluation scores for AI-generated BDD scenarios.",
        "",
        "| Metric | Score |",
        "|---|---:|",
    ]

    for metric, score in scores.items():
        lines.append(f"| {metric} | {score:.2f} |")

    report_path.write_text("\n".join(lines), encoding="utf-8")


def print_report(scores: dict) -> None:
    print("EDD Evaluation Scores for AI-Generated BDD Scenarios")
    print("-" * 58)
    for metric, score in scores.items():
        print(f"{metric.replace('_', ' ').title():<28} {score:.2f}")


def main() -> dict:
    feature_text = (ROOT / "data" / "generated_scenarios.feature").read_text(encoding="utf-8")
    config = json.loads((ROOT / "data" / "expected_coverage.json").read_text(encoding="utf-8"))

    scores = evaluate(feature_text, config)
    write_report(scores)
    print_report(scores)

    return scores


if __name__ == "__main__":
    main()
