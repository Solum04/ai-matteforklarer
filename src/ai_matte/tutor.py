from dataclasses import dataclass
from typing import List
from .solver import Solver, LocalLinearSolver, Step, Solution


class MathTutor:
    def __init__(self, solver: Solver | None = None):
        self.solver = solver or LocalLinearSolver()

    def explain(self, problem: str) -> str:
        solution: Solution = self.solver.solve(problem)
        lines = [f"Steg {i+1}: {s.description}" for i, s in enumerate(solution.steps)]
        lines.append(f"Svar: {solution.final_answer}")
        return "\n".join(lines)


