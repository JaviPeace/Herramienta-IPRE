namespace VehicleRoutingValidator.VehicleRouting;

public enum Constraint
{
    AllLocationsAreVisited, 
    DepotIsNotVisitedTwiceInARow, 
    NoLocationIsVisitedTwice, 
    NumberOfToursIsValid, 
    Precedence,
    FirstAndLastLocationsAreTheDepot
}