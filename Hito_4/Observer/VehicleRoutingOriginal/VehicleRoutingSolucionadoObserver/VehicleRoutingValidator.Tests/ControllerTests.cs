using System.Collections.Generic;
using VehicleRoutingValidator.Handlers;
using VehicleRoutingValidator.VehicleRouting;
using Xunit;

namespace VehicleRoutingValidator.Tests;

public class ControllerTests
{
    [Theory]
    [InlineData(new[] { 0, 2, 3, 4, 0, 1, 5, 0 }, false)]
    [InlineData(new[] { 0, 2, 3, 0, 0, 1, 5, 6, 0 }, false)]
    [InlineData(new[] { 0, 3, 2, 2, 0, 1, 5, 6, 0, 4 }, true)]
    [InlineData(new[] { 1, 2, 3, 4, 5, 6 }, true)]
    public void PartA_BuildHandler_ShouldValidateThatAllLocationsAreVisited(int[] solution, bool expected)
    {
        Constraint[] constraints = { Constraint.AllLocationsAreVisited };
        VehicleRoutingProblem problem = new() { NumberOfLocations = 6, Constraints = constraints };
        Validate(problem, solution, expected);
    }

    private void Validate(VehicleRoutingProblem problem, int[] solution, bool expected)
    {
        IHandler handler = Controller.BuildHandler(problem);
        bool isValid = handler.IsSolutionValid(solution);
        Assert.Equal(expected, isValid);
    }

    [Theory]
    [InlineData(new[] { 0, 2, 3, 4, 0, 1, 5, 0 }, true)]
    [InlineData(new[] { 0, 2, 3, 0, 2, 0, 1, 5, 6, 0 }, true)]
    [InlineData(new[] { 0, 3, 2, 2, 0, 1, 0, 5, 6, 0, 4, 0, 0 }, false)]
    [InlineData(new[] { 0, 1, 0, 0, 2, 0, 3, 4, 0, 5, 6, 0, 1, 0 }, false)]
    public void PartA_BuildHandler_ShouldValidateThatTheDepotIsNotVisitedTwiceInARow(int[] solution, bool expected)
    {
        Constraint[] constraints = { Constraint.DepotIsNotVisitedTwiceInARow };
        VehicleRoutingProblem problem = new() { Constraints = constraints };
        Validate(problem, solution, expected);
    }

    [Theory]
    [InlineData(new[] { 0, 2, 3, 4, 0, 1, 5, 0 }, true)]
    [InlineData(new[] { 0, 2, 3, 0, 0, 1, 5, 6, 0 }, true)]
    [InlineData(new[] { 0, 3, 2, 2, 0, 1, 5, 6, 0, 4 }, false)]
    [InlineData(new[] { 0, 1, 2, 3, 4, 5, 6, 0, 1 }, false)]
    public void PartA_BuildHandler_ShouldValidateThatNoLocationIsVisitedTwice(int[] solution, bool expected)
    {
        Constraint[] constraints = { Constraint.NoLocationIsVisitedTwice };
        VehicleRoutingProblem problem = new() { Constraints = constraints };
        Validate(problem, solution, expected);
    }

    [Theory]
    [InlineData(new[] { 0, 2, 3, 4, 0, 1, 5, 0 }, true)]
    [InlineData(new[] { 0, 2, 3, 0, 2, 0, 1, 5, 6, 0 }, true)]
    [InlineData(new[] { 0, 3, 2, 2, 0, 1, 0, 5, 6, 0, 4, 0 }, false)]
    [InlineData(new[] { 0, 1, 0, 2, 0, 3, 4, 0, 5, 6, 0, 1, 0 }, false)]
    public void PartA_BuildHandler_ShouldValidateThatThereAreNoMoreToursThanTheLimit(int[] solution, bool expected)
    {
        Constraint[] constraints = { Constraint.NumberOfToursIsValid };
        VehicleRoutingProblem problem = new() { MaxNumberOfTours = 3, Constraints = constraints };
        Validate(problem, solution, expected);
    }

    [Theory]
    [InlineData(new[] { 0, 2, 3, 4, 0, 1, 5, 0 }, true)]
    [InlineData(new[] { 0, 2, 3, 0, 2, 0, 1, 5, 6, 0 }, true)]
    [InlineData(new[] { 0, 3, 2, 2, 0, 1, 0, 5, 6, 0, 4, 0, 2 }, false)]
    [InlineData(new[] { 0, 1, 0, 2, 0, 3, 4, 0, 5, 6, 0, 1, 0, 1 }, false)]
    public void PartA_BuildHandler_ShouldValidateThatTheFirstAndLastLocationsAreTheDepot(int[] solution, bool expected)
    {
        Constraint[] constraints = { Constraint.FirstAndLastLocationsAreTheDepot };
        VehicleRoutingProblem problem = new() { Constraints = constraints };
        Validate(problem, solution, expected);
    }

    [Theory]
    [InlineData(new[] { 0, 1, 6, 5, 0, 2, 3, 4, 0 }, true)]
    [InlineData(new[] { 0, 1, 2, 6, 3, 5, 4, 0 }, true)]
    [InlineData(new[] { 0, 2, 6, 3, 1, 4, 5, 0 }, true)]
    [InlineData(new[] { 0, 6, 0, 2, 3, 4, 0, 1, 5, 0 }, true)]
    [InlineData(new[] { 0, 1, 2, 0, 5, 6, 0, 3, 4, 0 }, true)]
    [InlineData(new[] { 0, 1, 2, 3, 4, 0, 5, 6, 0 }, true)]
    [InlineData(new[] { 0, 1, 2, 3, 0, 4, 5, 6, 0 }, true)]
    [InlineData(new[] { 0, 2, 3, 0, 4, 0, 1, 5, 6, 0 }, true)]
    [InlineData(new[] { 0, 2, 3, 4, 0, 1, 5, 0 }, false)]
    [InlineData(new[] { 0, 2, 3, 0, 2, 4, 0, 1, 5, 6, 0 }, false)]
    [InlineData(new[] { 1, 2, 3, 4, 5, 6, 0 }, false)]
    [InlineData(new[] { 0, 3, 2, 4, 0, 0, 1, 5, 6, 0 }, false)]
    [InlineData(new[] { 0, 1, 0, 2, 0, 3, 4, 0, 5, 6, 0 }, false)]
    public void PartA_BuildHandler_ShouldValidateAllConstraintsWithoutPrecedences(int[] solution, bool expected)
    {
        VehicleRoutingProblem problem = TestProblems.CreateProblemWithoutPrecedences();
        Validate(problem, solution, expected);
    }
    
    [Theory]
    [InlineData(new[] { 0, 2, 3, 4, 0, 1, 5, 6, 0 }, true)]
    [InlineData(new[] { 0, 2, 3, 0, 4, 0, 1, 5, 6, 0 }, false)]
    [InlineData(new[] { 0, 3, 2, 0, 0, 1, 5, 6, 0 }, false)]
    [InlineData(new[] { 0, 1, 2, 3, 4, 5, 6, 0 }, true)]
    public void PartB_BuildHandler_ShouldValidatePrecedenceOnly(int[] solution, bool expected)
    {
        Constraint[] constraints = { Constraint.Precedence };
        VehicleRoutingProblem problem = new() { Precedences = TestProblems.GetSimplePrecedences(), Constraints = constraints };
        Validate(problem, solution, expected);
    }

    [Theory]
    [InlineData(new[] { 0, 1, 6, 5, 0, 2, 3, 4, 0 }, true)]
    [InlineData(new[] { 0, 1, 2, 6, 3, 5, 4, 0 }, true)]
    [InlineData(new[] { 0, 2, 6, 3, 1, 4, 5, 0 }, true)]
    [InlineData(new[] { 0, 6, 0, 2, 3, 4, 0, 1, 5, 0 }, true)]
    [InlineData(new[] { 0, 1, 2, 0, 5, 6, 0, 3, 4, 0 }, false)]
    [InlineData(new[] { 0, 1, 2, 3, 4, 0, 5, 6, 0 }, false)]
    [InlineData(new[] { 0, 1, 2, 3, 0, 4, 5, 6, 0 }, false)]
    [InlineData(new[] { 0, 2, 3, 0, 4, 0, 1, 5, 6, 0 }, false)]
    [InlineData(new[] { 0, 2, 3, 4, 0, 1, 5, 0 }, false)]
    [InlineData(new[] { 0, 2, 3, 0, 2, 4, 0, 1, 5, 6, 0 }, false)]
    [InlineData(new[] { 1, 2, 3, 4, 5, 6, 0 }, false)]
    [InlineData(new[] { 0, 3, 2, 4, 0, 0, 1, 5, 6, 0 }, false)]
    [InlineData(new[] { 0, 1, 0, 2, 0, 3, 4, 0, 5, 6, 0 }, false)]
    public void PartB_BuildHandler_ShouldValidateAllConstraints(int[] solution, bool expected)
    {
        VehicleRoutingProblem problem = TestProblems.CreateProblemWithPrecedences();
        Validate(problem, solution, expected);
    }

    [Theory]
    [InlineData( new []{0, 1, 6, 5, 0, 2, 3, 4, 0}, "All good.")]
    [InlineData( new []{0, 1, 2, 6, 3, 5, 4, 0}, "All good.")]
    [InlineData( new []{0, 2, 6, 3, 1, 4, 5, 0}, "All good.")]
    [InlineData( new []{0, 6, 0, 2, 3, 4, 0, 1, 5, 0}, "All good.")]
    [InlineData( new []{0, 1, 2, 0, 5, 6, 0, 3, 4, 0}, "Some deliveries were unsuccessful.")]
    [InlineData( new []{0, 1, 2, 3, 4, 0, 5, 6, 0}, "Some deliveries were unsuccessful.")]
    [InlineData( new []{0, 1, 2, 3, 0, 4, 5, 6, 0}, "Some deliveries were unsuccessful.")]
    [InlineData( new []{0, 2, 3, 0, 4, 0, 1, 5, 6, 0}, "Some deliveries were unsuccessful.")]
    [InlineData( new []{0, 2, 3, 4, 0, 1, 5, 0}, "Some locations are not visited.")]
    [InlineData( new []{0, 2, 3, 0, 2, 4, 0, 1, 5, 6, 0}, "Some locations are visited multiple times.")]
    [InlineData( new []{1, 2, 3, 4, 5, 6, 0}, "Solution does not start or end at depot.")]
    [InlineData( new []{0, 3, 2, 4, 0, 0, 1, 5, 6, 0}, "Depot is visited twice in a row.")]
    [InlineData( new []{0, 1, 0, 2, 0, 3, 4, 0, 5, 6, 0}, "There are too many tours.")]
    public void PartC_AddSubscriber_SubscribersShouldReceiveTheRightUpdate(int[] solution, string expected)
    {
        Subscriber[] subscribers = { new Subscriber(), new Subscriber() };
        VehicleRoutingProblem problem = TestProblems.CreateProblemWithPrecedences();
        IHandler handler = Controller.BuildHandler(problem);

        AddSubscribers(handler, subscribers);
        handler.IsSolutionValid(solution);

        ValidateThatSubscribersReceivedTheRightUpdate(subscribers, expected);
    }

    private void AddSubscribers(IHandler handler, Subscriber[] subscribers)
    {
        foreach (Subscriber subscriber in subscribers)
            Controller.AddSubscriber(handler, subscriber);
    }

    private void ValidateThatSubscribersReceivedTheRightUpdate(Subscriber[] subscribers, string expected)
    {
        foreach (Subscriber subscriber in subscribers)
        {
            List<string> updates = subscriber.GetStatus();
            Assert.Single(updates);
            Assert.Equal(expected, updates[0]);
        }
    }
}