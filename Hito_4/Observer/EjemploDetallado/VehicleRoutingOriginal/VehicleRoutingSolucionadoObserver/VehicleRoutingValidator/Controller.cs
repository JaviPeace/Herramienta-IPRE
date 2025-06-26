using System.Diagnostics;
using VehicleRoutingValidator.Handlers;
using VehicleRoutingValidator.VehicleRouting;

namespace VehicleRoutingValidator;

public static class Controller
{
    public static IHandler BuildHandler(VehicleRoutingProblem problem)
    {
        IHandler nextHandler = new BaseHandler();
        foreach (var constrain in problem.Constraints.Reverse())
        {
            var handler = BuildHandler(constrain, problem);
            handler.SetNext(nextHandler);
            nextHandler = handler;
        }

        return nextHandler;
    }

    private static IHandler BuildHandler(Constraint constrain, VehicleRoutingProblem problem)
    {
        return constrain switch
        {
            Constraint.AllLocationsAreVisited => new AllLocationsAreVisitedHandler(problem.NumberOfLocations),
            Constraint.DepotIsNotVisitedTwiceInARow => new DepotIsNotVisitedTwiceInARowHandler(),
            Constraint.NoLocationIsVisitedTwice => new NoLocationIsVisitedTwiceHandler(),
            Constraint.NumberOfToursIsValid => new NumOfToursIsValidHandler(problem.MaxNumberOfTours),
            Constraint.FirstAndLastLocationsAreTheDepot => new FirstAndLastLocationsAreTheDepotHandler(),
            Constraint.Precedence => new PrecedenceHandler(problem.Precedences),
            _ => throw new ArgumentOutOfRangeException(nameof(constrain), constrain, null)
        };
    }

    public static void AddSubscriber(IHandler handler, Subscriber subscriber)
    {
        handler.AddSubscriber(subscriber);
    }
}