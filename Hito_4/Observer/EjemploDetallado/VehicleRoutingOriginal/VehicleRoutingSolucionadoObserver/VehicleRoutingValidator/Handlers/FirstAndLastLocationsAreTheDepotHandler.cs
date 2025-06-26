using VehicleRoutingValidator.VehicleRouting;

namespace VehicleRoutingValidator.Handlers;

public class FirstAndLastLocationsAreTheDepotHandler: BaseHandler
{
    private const string Description = "Solution does not start or end at depot.";
    private const int Depot = VehicleRoutingProblem.Depot;
    
    public override bool IsSolutionValid(int[] solution)
    {
        if(DoesSolutionStartAndEndAtDepot(solution))
            return base.IsSolutionValid(solution);
        UpdateSubscribers(Description);
        return false;
    }

    private bool DoesSolutionStartAndEndAtDepot(int[] solution)
        => DoesSolutionStartAtDepot(solution) && DoesSolutionEndAtDepot(solution);

    private bool DoesSolutionStartAtDepot(int[] solution)
        => solution[0] == Depot;

    private bool DoesSolutionEndAtDepot(int[] solution)
        => solution[^1] == Depot;

}