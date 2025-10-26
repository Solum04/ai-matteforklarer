import os
from dataclasses import dataclass
from typing import List, TypedDict
from dotenv import load_dotenv
from openai import OpenAI, APIError, RateLimitError, APITimeoutError
import json
from .solver import Solver, Step, Solution


# Vi definerer forventet struktur fra modellen
class StepDict(TypedDict):
    description: str

class SolutionDict(TypedDict):
    steps: List[StepDict]
    final_answer: str

SYSTEM_PROMPT = (
    "Du er en norsk mattelærer. Forklar steg-for-steg veldig tydelig.\n"
    "Returner KUN JSON med feltene: steps (liste av objekter med 'description'), "
    "og final_answer (streng). Ikke noe annet."
)

USER_PROMPT_TEMPLATE = (
    "Forklar og løs denne oppgaven for en elev på videregående:\n"
    "{problem}\n"
    "Krav:\n"
    "- Bruk korte, konkrete steg (maks 1–2 setninger per steg).\n"
    "- Skriv norsk.\n"
    "- Ikke bruk spesialtegn som '→'. Bruk '->'.\n"
    "- Ikke ta med LaTeX, bare ren tekst.\n"
)

@dataclass
class AISolver(Solver):
    """LLM-basert oppgave forklaring. Kaller openai API."""
    model: str = "gpt-4o-mini"

    def __post_init__(self):
        load_dotenv()
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=self.api_key) if self.api_key else None

    def solve(self, problem: str) -> Solution:
        if not self.api_key:
            if not self.client:
                return Solution(
                    steps=[
                        Step("Fant ingen API-nøkkel (OPENAI_API_KEY)."),
                        Step("Legg nøkkelen i .env for å aktivere AI-motoren.")
                    ],
                    final_answer="(AI ikke aktivert enda)"
                )

        try:
            resp = self.client.responses.create(
                model=self.model,
                input=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": USER_PROMPT_TEMPLATE.format(problem=problem)},
                ],
            )

            text = getattr(resp, "output_text", None)

            if not text:
                try:
                    text = resp.output[0].content[0].text
                except Exception:
                    text = ""

            try:
                parsed = json.loads(text)  # forventer {"steps":[{"description":...}], "final_answer":"..."}
                steps = [Step(s["description"]) for s in parsed.get("steps", [])]
                final = parsed.get("final_answer", "").strip() or "(mangler svar)"
                return Solution(steps=steps, final_answer=final)
            except Exception:
                if not text.strip():
                    return Solution([Step("AI svarte uten innhold.")], "(tomt svar)")
                # Faller tilbake til å vise hele AI-svaret som ett steg
                return Solution([Step(text.strip())], "(se tekst over)")

        except (RateLimitError, APITimeoutError) as e:
            return Solution(
                steps=[Step("Tidsavbrudd eller for mange forespørsler. Prøv igjen snart.")],
                final_answer=str(e),
            )
        except APIError as e:
            return Solution(
                steps=[Step("API-feil oppstod. Sjekk modellnavn og saldo.")],
                final_answer=str(e),
            )
        except Exception as e:
            return Solution(
                steps=[Step("Uventet feil under AI-kall.")],
                final_answer=str(e),
            )








