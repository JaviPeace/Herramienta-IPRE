using VehicleRoutingValidator.VehicleRouting;

namespace VehicleRoutingValidator.Handlers;

public class DepotIsNotVisitedTwiceInARowHandler : BaseHandler
{
    private const string Description = "Depot is visited twice in a row.";
    private const int Depot = VehicleRoutingProblem.Depot;

    public override bool IsSolutionValid(int[] solution)
    {
        if(IsDepotNotVisitedTwiceInARow(solution))
            return base.IsSolutionValid(solution);
        UpdateSubscribers(Description);
        return false;
    }

    private bool IsDepotNotVisitedTwiceInARow(int[] solution)
    {
        for(int i = 1; i < solution.Length; i++)
            if (solution[i - 1] == Depot && solution[i] == Depot)
                return false;

        return true;
    }
}