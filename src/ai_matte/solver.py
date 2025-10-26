import re
from dataclasses import dataclass
from typing import List, Protocol

@dataclass
class Step:
    description: str

@dataclass
class Solution:
    steps: List[Step]
    final_answer: str

class Solver(Protocol):
    def solve(self, problem: str) -> Solution:
        ...

class LocalLinearSolver:
    """
    Løser veldig enkle ligninger av typen: ax + b = c (heltall).
    Eksempel: 3x + 5 = 11  ->  x = 2
    """
    _PATTERN = re.compile(r"^\s*([+-]?\d+)\s*x\s*([+-]\s*\d+)?\s*=\s*([+-]?\d+)\s*$", re.IGNORECASE)

    def solve(self, problem: str) -> Solution:
        m = self._PATTERN.match(problem.replace(" ", ""))
        if not m:
            return Solution(
                steps=[Step("Ukjent format. Støtter bare ax + b = c med heltall foreløpig.")],
                final_answer="(ingen løsning)",
            )

        a = int(m.group(1))
        b = int(m.group(2).replace(" ", "")) if m.group(2) else 0
        c = int(m.group(3))

        steps: List[Step] = []
        # steg 1: flytt konstanten
        rhs = c - b
        if b != 0:
            steps.append(Step(f"Trekk {abs(b)} fra begge sider -> {a}x = {rhs}"))
        else:
            steps.append(Step(f"Ingen konstant å flytte: {a}x = {c}"))

        # steg 2: del på koeffisienten til x
        if a == 0:
            steps.append(Step("Kan ikke dele på 0 – ugyldig ligning."))
            return Solution(steps, final_answer="(ingen løsning)")

        x_value = rhs / a
        steps.append(Step(f"Del på {a} for å isolere x: x = {rhs}/{a} = {x_value:g}"))
        return Solution(steps, final_answer=f"x = {x_value:g}")


