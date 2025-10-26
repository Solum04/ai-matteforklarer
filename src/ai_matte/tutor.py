from dataclasses import dataclass
from typing import List

@dataclass
class Step:
    description: str

@dataclass
class Solution:
    steps: List[Step]
    final_answer: str

    def as_text(self) -> str:
        lines = [f"Steg {i+1}: {s.description}" for i, s in enumerate(self.steps)]
        lines.append(f"Svar: {self.final_answer}")
        return "\n".join(lines)

class MathTutor:
    """En enkel tutor som senere skal bruke ulike 'løsere' (lokal/LLM)."""
    def explain(selfself, problem: str) -> str:
        #Foreløpig: vi later som vi forklarer noe, for å teste rørledningen.
        steps = [
            Step(f"Les oppgaven: {problem}"),
            Step("Identifiser type (foreløpig: ukjent – demo)"),
            Step("Vis hvordan vi ville tenkt steg-for-steg (kommer snart)")
        ]
        sol = Solution(steps=steps, final_answer="(demo) Kommer med ekte løsning senere")
        return sol.as_text()
