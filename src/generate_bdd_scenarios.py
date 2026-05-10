from pathlib import Path
import os

import httpx
from openai import OpenAI

ROOT = Path(__file__).resolve().parents[1]

http_client = httpx.Client(
    verify=False,
    timeout=httpx.Timeout(20.0, connect=10.0),
)


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"), http_client=http_client,)


def load_api_context() -> str:
    context_file = ROOT / "data" / "api_context.md"
    return context_file.read_text(encoding="utf-8")


def generate_bdd_scenarios(api_context: str) -> str:
    prompt = f"""
You are a senior QA engineer.

Using the API documentation/context below, generate concise Gherkin BDD scenarios
for negative API validation testing.

Requirements:
- Generate only valid Gherkin
- Focus on realistic negative validation scenarios
- Do not hallucinate unsupported fields or API behaviors
- Keep the output concise and automation-friendly
- Use Given/When/Then format

API Context:
{api_context}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        temperature=0.2,
        messages=[
            {
                "role": "system",
                "content": "You generate high-quality BDD scenarios for API testing."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content.strip()


def save_generated_scenarios(output: str) -> Path:
    target = ROOT / "data" / "generated_scenarios.feature"
    target.write_text(output, encoding="utf-8")
    return target


def main() -> None:
    api_context = load_api_context()

    generated_output = generate_bdd_scenarios(api_context)

    output_path = save_generated_scenarios(generated_output)

    print("Generated AI BDD scenarios successfully")
    print(f"Saved scenarios to: {output_path}")


if __name__ == "__main__":
    main()
