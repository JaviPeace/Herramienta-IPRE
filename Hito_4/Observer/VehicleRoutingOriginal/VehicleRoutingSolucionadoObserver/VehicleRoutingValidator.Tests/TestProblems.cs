using VehicleRoutingValidator.VehicleRouting;

namespace VehicleRoutingValidator.Tests;

public static class TestProblems
{
    public static VehicleRoutingProblem CreateProblemWithoutPrecedences()
        => new()
        {
            NumberOfLocations = 6,
            MaxNumberOfTours = 3,
            Constraints = GetAllTheConstraintsWithoutPrecedences()
        }; 

    private static Constraint[] GetAllTheConstraintsWithoutPrecedences()
        => new[]
        {
            Constraint.FirstAndLastLocationsAreTheDepot,
            Constraint.AllLocationsAreVisited,
            Constraint.DepotIsNotVisitedTwiceInARow,
            Constraint.NoLocationIsVisitedTwice,
            Constraint.NumberOfToursIsValid
        };
    
    public static VehicleRoutingProblem CreateProblemWithPrecedences()
        => new()
        {
            NumberOfLocations = 6,
            MaxNumberOfTours = 3,
            Constraints = GetAllTheConstraints(),
            Precedences = GetSimplePrecedences()
        }; 

    private static Constraint[] GetAllTheConstraints()
        => new[]
        {
            Constraint.FirstAndLastLocationsAreTheDepot,
            Constraint.AllLocationsAreVisited,
            Constraint.DepotIsNotVisitedTwiceInARow,
            Constraint.NoLocationIsVisitedTwice,
            Constraint.NumberOfToursIsValid,
            Constraint.Precedence
        };
    
    public static Precedence[] GetSimplePrecedences()
        => new[]
        {
            new Precedence() { PickUpLocation = 1, DeliveryLocation = 5 },
            new Precedence() { PickUpLocation = 2, DeliveryLocation = 3 },
            new Precedence() { PickUpLocation = 3, DeliveryLocation = 4 }
        };

}