import BaseHandler
from ..models.Precedence import Precedence


class PrecedenceHandler(BaseHandler):
    def __init__(self, precedences: list[Precedence]):
        super().__init__()
        self._precedences = precedences

    def is_solution_valid(self, solution: list[int]) -> bool:
        if self._are_precedences_valid(solution):
            return super().is_solution_valid(solution)
        self.update_subscribers("Some deliveries were unsuccessful.")
        return False

    def _are_precedences_valid(self, solution: list[int]) -> bool:
        return all(self._is_precedence_valid(precedence, solution) for precedence in self._precedences)

    @staticmethod
    def _is_precedence_valid(precedence: Precedence, solution: list[int]) -> bool:
        visited_pickup_location = False
        visited_delivery_location = False

        for loc_id in solution:
            if loc_id == precedence.pick_up_location:
                visited_pickup_location = True
            if loc_id == precedence.delivery_location:
                visited_delivery_location = True

            if loc_id != 0:
                continue

            if visited_pickup_location:
                return visited_delivery_location
            if visited_delivery_location:
                return False

        return True
