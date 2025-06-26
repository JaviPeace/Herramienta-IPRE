from handlers import (
    BaseHandler,
    AllLocationsAreVisitedHandler,
    DepotIsNotVisitedTwiceInARowHandler,
    NoLocationIsVisitedTwiceHandler,
    NumOfToursIsValidHandler,
    FirstAndLastLocationsAreTheDepotHandler,
    PrecedenceHandler
)
from models import Constraint, VehicleRoutingProblem


class Controller:
    @staticmethod
    def build_handler(problem: VehicleRoutingProblem):
        next_handler = BaseHandler()
        for constraint in reversed(problem.constraints):
            handler = Controller._build_handler(constraint, problem)
            handler.set_next(next_handler)
            next_handler = handler
        return next_handler

    @staticmethod
    def _build_handler(constraint: Constraint, problem: VehicleRoutingProblem):
        if constraint == Constraint.ALL_LOCATIONS_ARE_VISITED:
            return AllLocationsAreVisitedHandler(problem.number_of_locations)
        elif constraint == Constraint.DEPOT_IS_NOT_VISITED_TWICE_IN_A_ROW:
            return DepotIsNotVisitedTwiceInARowHandler()
        elif constraint == Constraint.NO_LOCATION_IS_VISITED_TWICE:
            return NoLocationIsVisitedTwiceHandler()
        elif constraint == Constraint.NUMBER_OF_TOURS_IS_VALID:
            return NumOfToursIsValidHandler(problem.max_number_of_tours)
        elif constraint == Constraint.FIRST_AND_LAST_LOCATIONS_ARE_THE_DEPOT:
            return FirstAndLastLocationsAreTheDepotHandler()
        elif constraint == Constraint.PRECEDENCE:
            return PrecedenceHandler(problem.precedences)
        else:
            raise ValueError(f"Unknown constraint: {constraint}")

    @staticmethod
    def add_subscriber(handler, subscriber):
        handler.add_subscriber(subscriber)
