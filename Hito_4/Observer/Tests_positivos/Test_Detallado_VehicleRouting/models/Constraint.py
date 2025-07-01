from enum import Enum, auto

class Constraint(Enum):
    ALL_LOCATIONS_ARE_VISITED = auto()
    DEPOT_IS_NOT_VISITED_TWICE_IN_A_ROW = auto()
    NO_LOCATION_IS_VISITED_TWICE = auto()
    NUMBER_OF_TOURS_IS_VALID = auto()
    PRECEDENCE = auto()
    FIRST_AND_LAST_LOCATIONS_ARE_THE_DEPOT = auto()
