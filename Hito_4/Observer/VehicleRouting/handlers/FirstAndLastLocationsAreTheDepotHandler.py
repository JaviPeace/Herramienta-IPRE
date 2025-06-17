import BaseHandler
from ..models.VehicleRoutingProblem import VehicleRoutingProblem

class FirstAndLastLocationsAreTheDepotHandler(BaseHandler):
    DESCRIPTION = "Solution does not start or end at depot."
    DEPOT = VehicleRoutingProblem.DEPOT

    def __init__(self):
        super().__init__()

    def is_solution_valid(self, solution: list[int]) -> bool:
        if self._does_solution_start_and_end_at_depot(solution):
            return super().is_solution_valid(solution)
        self.update_subscribers(self.DESCRIPTION)
        return False

    def _does_solution_start_and_end_at_depot(self, solution: list[int]) -> bool:
        return self._does_solution_start_at_depot(solution) and self._does_solution_end_at_depot(solution)

    def _does_solution_start_at_depot(self, solution: list[int]) -> bool:
        return solution[0] == self.DEPOT

    def _does_solution_end_at_depot(self, solution: list[int]) -> bool:
        return solution[-1] == self.DEPOT
