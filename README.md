# BDD, TDD, and EDD: Three Layers of Modern AI Quality Engineering

A practical example of how BDD, TDD, and Evaluation-Driven Development (EDD) can work together in an AI-assisted testing workflow.

```text
BDD defines intended behavior.
TDD verifies implemented behavior.
EDD evaluates generated behavior quality.
```

This repo demonstrates:

* executable BDD scenarios using Behave
* deterministic REST API testing using pytest
* AI-generated BDD scenario creation using OpenAI
* evaluation-driven quality scoring for generated outputs
* CI/CD-style quality gates for AI-assisted testing workflows

---

# Architecture

```text
BDD Feature Files
        ↓
Behave Step Definitions
        ↓
REST API Calls + Deterministic Assertions
        ↓
AI-Generated BDD Scenarios
        ↓
EDD Evaluation Scores
        ↓
Quality Gates / CI Checks
```

---

# What Each Layer Does

| Layer | Purpose                                | Implementation                     |
| ----- | -------------------------------------- | ---------------------------------- |
| BDD   | Define expected behavior               | Gherkin feature files + Behave     |
| TDD   | Verify deterministic implementation    | Pytest + REST API assertions       |
| EDD   | Evaluate AI-generated behavior quality | Evaluation scoring + quality gates |

---

# Tech Stack

| Area          | Technology            |
| ------------- | --------------------- |
| BDD           | Behave                |
| API Testing   | pytest + requests     |
| AI Generation | OpenAI API            |
| Evaluation    | Custom EDD evaluators |
| CI/CD         | GitHub Actions        |
| Demo API      | Restful Booker        |

---

# Project Structure

```text
features/
  booking_validation.feature
  environment.py
  steps/
    booking_steps.py

tests/
  test_booking_api.py
  test_edd_quality_gate.py

src/
  booking_client.py
  generate_bdd_scenarios.py
  evaluate_bdd_output.py
  evaluators/

data/
  api_context.md
  generated_scenarios.feature
  expected_coverage.json

reports/
  evaluation_report.md
```

---

# Setup

## Clone Repo

```bash
git clone <repo-url>
cd bdd-tdd-edd-ai-quality
```

---

## Create Virtual Environment

### macOS/Linux

```bash
python -m venv .venv
source .venv/bin/activate
```

### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# OpenAI Setup

This repo uses OpenAI to generate AI-assisted BDD scenarios.

## Set API Key

### macOS/Linux

```bash
export OPENAI_API_KEY=your_key_here
```

### Windows PowerShell

```powershell
$env:OPENAI_API_KEY="your_key_here"
```

---

# SSL Verification

By default, SSL verification is enabled.

To disable SSL verification for local/dev environments:

### macOS/Linux

```bash
export VERIFY_SSL=false
```

### Windows PowerShell

```powershell
$env:VERIFY_SSL="false"
```

This passes:

```python
verify=False
```

for outbound REST API calls.

---

# Running the BDD Layer

The BDD layer is implemented using Behave.

## Execute Feature Files

```bash
behave
```

Example feature:

```gherkin
Scenario: Create booking with missing firstname
  Given I have a valid booking request
  When I remove the firstname field
  And I send a POST request to /booking
  Then the API should reject the request
```

Step definitions are implemented in:

```text
features/steps/booking_steps.py
```

This layer defines and executes expected behavior.

---

# Running the TDD Layer

The TDD layer uses pytest for deterministic API validation.

## Execute Deterministic Tests

```bash
pytest tests/test_booking_api.py
```

Example:

assert response.status_code == 200

This layer verifies deterministic implementation behavior.

---

# Running the AI Generation Layer

AI-generated BDD scenarios are created using OpenAI.

## Generate BDD Scenarios

```bash
python src/generate_bdd_scenarios.py
```

This:

* loads API context
* sends prompt to OpenAI
* generates Gherkin scenarios
* saves output to:

```text
data/generated_scenarios.feature
```

Example generated output:

```gherkin
Scenario: Create booking with invalid totalprice
Scenario: Create booking with checkout before checkin
```

---

# Running the EDD Layer

EDD evaluates the quality of AI-generated BDD scenarios.

## Run Evaluation

```bash
python src/evaluate_bdd_output.py
```

Example console output:

```text
EDD Evaluation Scores for AI-Generated BDD Scenarios
----------------------------------------------------------
Groundedness              0.80
Coverage                  0.60
Hallucination Risk        0.25
BDD Syntax Validity       1.00
Automation Readiness      1.00
```

This layer evaluates:

* groundedness
* coverage
* hallucination risk
* BDD syntax quality
* automation readiness

---

# Running the EDD Quality Gate

The quality gate enforces evaluation thresholds.

## Execute Quality Gate

```bash
pytest tests/test_edd_quality_gate.py
```

Example thresholds:

```json
{
  "groundedness": 0.80,
  "coverage": 0.60,
  "hallucination_risk": 0.25
}
```

If evaluation scores degrade below acceptable thresholds, the pipeline fails.

---

# GitHub Actions Workflow

The repo includes a GitHub Actions pipeline that:

* runs Behave scenarios
* executes pytest API tests
* runs EDD quality gates
* generates evaluation reports

Workflow file:

```text
.github/workflows/quality.yml
```

This demonstrates how evaluation-driven quality checks can become operational CI/CD gates.

---

# Important Note About Restful Booker

This repo uses the public Restful Booker API as a lightweight demo target.

Public demo APIs may not strictly enforce all validations. Some negative tests intentionally allow:

```python
[400, 422, 500]
```

to keep the repo runnable while still demonstrating deterministic testing patterns.

In a real production API:

* validation behavior should be stricter
* assertions should target exact contracts
* negative test expectations should be deterministic

---

# Why This Repo Exists

Traditional testing was designed for systems that execute logic.

AI systems increasingly generate behavior.

That changes how quality itself needs to be evaluated.

This repo explores one possible quality stack for AI-assisted testing systems where:

* BDD defines behavior
* TDD verifies implementation
* EDD evaluates generated behavior quality

---

# Future Ideas

Potential future extensions:

* LLM-as-judge evaluators
* vector database retrieval evaluation
* drift detection
* prompt regression tracking
* retrieval groundedness scoring
* multi-model comparisons
* semantic diff reporting
* AI-generated step definition generation

---

# License

MIT License
