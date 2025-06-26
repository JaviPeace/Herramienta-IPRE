from typing import List
from Constraint import Constraint
from Precedence import Precedence


class VehicleRoutingProblem:
    DEPOT: int = 0 

    def __init__(
        self,
        number_of_locations: int,
        max_number_of_tours: int,
        precedences: List[Precedence],
        constraints: List[Constraint]
    ):
        self.number_of_locations = number_of_locations
        self.max_number_of_tours = max_number_of_tours
        self.precedences = precedences
        self.constraints = constraints
