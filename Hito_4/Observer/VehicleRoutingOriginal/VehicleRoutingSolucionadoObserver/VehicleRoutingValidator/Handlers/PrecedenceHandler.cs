using VehicleRoutingValidator.VehicleRouting;

namespace VehicleRoutingValidator.Handlers;

public class PrecedenceHandler : BaseHandler
{
    private readonly Precedence[] _precedences;

    public PrecedenceHandler(Precedence[] precedences)
    {
        _precedences = precedences;
    }

    public override bool IsSolutionValid(int[] solution)
    {
        if(ArePrecedencesValid(solution))
            return base.IsSolutionValid(solution);
        UpdateSubscribers("Some deliveries were unsuccessful.");
        return false;
    }

    private bool ArePrecedencesValid(int[] solution)
    {
        return _precedences.All(precedence => IsPrecedenceValid(precedence, solution));
    }

    private static bool IsPrecedenceValid(Precedence precedence, IEnumerable<int> solution)
    {
        var visitedPickupLocation = false;
        var visitedDeliveryLocation = false;
        foreach (var id in solution)
        {
            if (id == precedence.PickUpLocation) 
                visitedPickupLocation = true;
            if (id == precedence.DeliveryLocation) 
                visitedDeliveryLocation = true;
            if (id != 0) 
                continue;
            if (visitedPickupLocation)
                return visitedDeliveryLocation;
            if (visitedDeliveryLocation) 
                return false;
        }
        return true;
    }
}