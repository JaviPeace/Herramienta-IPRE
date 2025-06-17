import BaseHandler
from ..models.VehicleRoutingProblem import VehicleRoutingProblem

class NumOfToursIsValidHandler(BaseHandler):
    DESCRIPTION = "There are too many tours."
    DEPOT = VehicleRoutingProblem.DEPOT

    def __init__(self, max_num_of_tours: int):
        super().__init__()
        self._max_num_of_tours = max_num_of_tours

    def is_solution_valid(self, solution: list[int]) -> bool:
        if self._is_number_of_tours_valid(solution):
            return super().is_solution_valid(solution)
        self.update_subscribers(self.DESCRIPTION)
        return False

    def _is_number_of_tours_valid(self, solution: list[int]) -> bool:
        number_of_tours = self._compute_number_of_tours(solution)
        return number_of_tours <= self._max_num_of_tours

    def _compute_number_of_tours(self, solution: list[int]) -> int:
        return sum(1 for i in range(1, len(solution)) if solution[i] == self.DEPOT)
