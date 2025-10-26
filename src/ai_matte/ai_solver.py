import os
from dataclasses import dataclass
from typing import List
from dotenv import load_dotenv
from .solver import Solver, Step, Solution

@dataclass
class AISolver(Solver):
    """Skall for LLM-basert forklaring. Kaller ikke API ennå."""
    model: str = "gpt-4o-mini"

    def __post_init__(self):
        load_dotenv()
        self.api_key = os.getenv("OPENAI_API_KEY")

    def solve(self, problem: str) -> Solution:
        # Foreløpig: bare validerer at vi har nøkkel. Ingen ekte API-kall ennå.
        if not self.api_key:
            return Solution(
                steps=[
                    Step("Fant ingen API-nøkkel (OPENAI_API_KEY)."),
                    Step("Legg den i .env for å aktivere AI-motoren."),
                    Step(f"Forberedt modell: {self.model}")
                ],
                final_answer="(AI ikke aktivert enda)"
            )

        # Placeholder: her vil vi senere kalle API og bygge trinnvis løsning.
        return Solution(
            steps=[
                Step("AI-motoren er klar (nøkkel funnet)."),
                Step("Ekte forklaring kommer i neste steg.")
            ],
            final_answer="(placeholder fra AI)"
        )


