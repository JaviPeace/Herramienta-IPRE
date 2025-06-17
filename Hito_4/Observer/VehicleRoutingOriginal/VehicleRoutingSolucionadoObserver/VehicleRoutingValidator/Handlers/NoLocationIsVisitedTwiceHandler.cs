using VehicleRoutingValidator.VehicleRouting;

namespace VehicleRoutingValidator.Handlers;

public class NoLocationIsVisitedTwiceHandler : BaseHandler
{
    private const string Description = "Some locations are visited multiple times.";
    private const int Depot = VehicleRoutingProblem.Depot;
    private int[] _solution;

    public override bool IsSolutionValid(int[] solution)
    {
        _solution = solution;
        if(IsEveryLocationVisitedAtMostOneTime())
            return base.IsSolutionValid(_solution);
        UpdateSubscribers(Description);
        return false;
    }

    private bool IsEveryLocationVisitedAtMostOneTime()
    {
        for (int i = 0; i < _solution.Length; i++)
            if(IsNotDepot(i) && IsThisLocationVisitedTwice(i))
                return false;
        return true;
    }

    private bool IsThisLocationVisitedTwice(int idLocation)
    {
        for (int j = idLocation + 1; j < _solution.Length; j++)
            if (_solution[idLocation] == _solution[j])
                return true;
        return false;
    }

    private bool IsNotDepot(int idLocation)
        => _solution[idLocation] != Depot;
}