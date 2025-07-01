from ..models import VehicleRoutingProblem
import BaseHandler


class AllLocationsAreVisitedHandler(BaseHandler):
    DESCRIPTION = "Some locations are not visited."
    DEPOT = VehicleRoutingProblem.DEPOT  # Asegúrate de que esto exista como atributo de clase

    def __init__(self, number_of_locations: int):
        super().__init__()
        self._number_of_locations = number_of_locations

    def is_solution_valid(self, solution: list[int]) -> bool:
        if self._are_all_locations_visited(solution):
            return super().is_solution_valid(solution)
        self.update_subscribers(self.DESCRIPTION)
        return False

    def _are_all_locations_visited(self, solution: list[int]) -> bool:
        for location in range(self._number_of_locations + 1):
            if location != self.DEPOT and location not in solution:
                return False
        return True
