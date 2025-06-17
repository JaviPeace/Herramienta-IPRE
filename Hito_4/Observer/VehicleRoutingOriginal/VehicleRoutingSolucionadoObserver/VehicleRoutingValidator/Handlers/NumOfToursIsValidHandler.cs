using VehicleRoutingValidator.VehicleRouting;

namespace VehicleRoutingValidator.Handlers;

public class NumOfToursIsValidHandler : BaseHandler
{
    private const string Description = "There are too many tours.";
    private const int Depot = VehicleRoutingProblem.Depot;
    private readonly int _maxNumOfTours;

    public NumOfToursIsValidHandler(int maxNumOfTours)
        => _maxNumOfTours = maxNumOfTours;

    public override bool IsSolutionValid(int[] solution)
    {
        if(IsTheNumberOfToursValid(solution))
            return base.IsSolutionValid(solution);
        UpdateSubscribers(Description);
        return false;
    }

    private bool IsTheNumberOfToursValid(int[] solution)
    {
        int numberOfTours = ComputeNumberOfToursAssumingSolutionStartsAndEndsAtDepot(solution);
        if (numberOfTours > _maxNumOfTours)
            return false;

        return true;
    }

    private int ComputeNumberOfToursAssumingSolutionStartsAndEndsAtDepot(int[] solution)
    {
        int numberOfTours = 0;
        for (int i = 1; i < solution.Length; i++)
            if (solution[i] == Depot)
                numberOfTours++;
        return numberOfTours;
    }
}