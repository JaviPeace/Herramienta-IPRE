import BaseHandler
from ..models.VehicleRoutingProblem import VehicleRoutingProblem

class NoLocationIsVisitedTwiceHandler(BaseHandler):
    DESCRIPTION = "Some locations are visited multiple times."
    DEPOT = VehicleRoutingProblem.DEPOT

    def __init__(self):
        super().__init__()
        self._solution = []

    def is_solution_valid(self, solution: list[int]) -> bool:
        self._solution = solution
        if self._is_every_location_visited_at_most_once():
            return super().is_solution_valid(solution)
        self.update_subscribers(self.DESCRIPTION)
        return False

    def _is_every_location_visited_at_most_once(self) -> bool:
        for i in range(len(self._solution)):
            if self._is_not_depot(i) and self._is_location_visited_twice(i):
                return False
        return True

    def _is_location_visited_twice(self, id_location: int) -> bool:
        for j in range(id_location + 1, len(self._solution)):
            if self._solution[id_location] == self._solution[j]:
                return True
        return False

    def _is_not_depot(self, id_location: int) -> bool:
        return self._solution[id_location] != self.DEPOT
