from .solver import Solver, LocalLinearSolver, Step, Solution
from .ai_solver import AISolver

class MathTutor:
    def __init__(self, engine: str = "local"):
        if engine == "ai":
            self.Solver: Solver = AISolver()
        else:
            self.Solver: Solver = LocalLinearSolver()


    def explain(self, problem: str) -> str:
        solution: Solution = self.Solver.solve(problem)
        lines = [f"Steg {i+1}: {s.description}" for i, s in enumerate(solution.steps)]
        lines.append(f"Svar: {solution.final_answer}")
        return "\n".join(lines)


