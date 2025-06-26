namespace VehicleRoutingValidator.Handlers;

public interface IHandler
{
    void SetNext(IHandler nextHandler);
    bool IsSolutionValid(int[] solution);

    void AddSubscriber(Subscriber subscriber);
}