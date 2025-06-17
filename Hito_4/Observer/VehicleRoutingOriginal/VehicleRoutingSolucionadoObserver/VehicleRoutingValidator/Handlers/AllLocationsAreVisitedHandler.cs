using VehicleRoutingValidator.VehicleRouting;

namespace VehicleRoutingValidator.Handlers;

public class AllLocationsAreVisitedHandler : BaseHandler
{
    private const string Description = "Some locations are not visited.";
    private const int Depot = VehicleRoutingProblem.Depot;
    private readonly int _numberOfLocations;

    public AllLocationsAreVisitedHandler(int numberOfLocations)
        => _numberOfLocations = numberOfLocations;

    public override bool IsSolutionValid(int[] solution)
    {
        if(AreAllLocationsVisited(solution))
            return base.IsSolutionValid(solution);
        UpdateSubscribers(Description);
        return false;
    }

    private bool AreAllLocationsVisited(int[] solution)
    {
        for(int location = 0; location <= _numberOfLocations; location++)
            if (location != Depot && !solution.Contains(location))
                return false;
        return true;
    }
}