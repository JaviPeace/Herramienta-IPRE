import BaseHandler
from ..models.VehicleRoutingProblem import VehicleRoutingProblem

class DepotIsNotVisitedTwiceInARowHandler(BaseHandler):
    DESCRIPTION = "Depot is visited twice in a row."
    DEPOT = VehicleRoutingProblem.DEPOT

    def __init__(self):
        super().__init__()

    def is_solution_valid(self, solution: list[int]) -> bool:
        if self._is_depot_not_visited_twice_in_a_row(solution):
            return super().is_solution_valid(solution)
        self.update_subscribers(self.DESCRIPTION)
        return False

    def _is_depot_not_visited_twice_in_a_row(self, solution: list[int]) -> bool:
        for i in range(1, len(solution)):
            if solution[i - 1] == self.DEPOT and solution[i] == self.DEPOT:
                return False
        return True
