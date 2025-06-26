namespace VehicleRoutingValidator.Handlers;

public class BaseHandler : IHandler
{
    private IHandler? _nextHandler;
    private readonly List<Subscriber> _subscribers = new();
    
    public void SetNext(IHandler nextHandler)
        => _nextHandler = nextHandler;

    public virtual bool IsSolutionValid(int[] solution)
    {
        if(_nextHandler != null)
            return _nextHandler.IsSolutionValid(solution);
        UpdateSubscribers("All good.");
        return true;
    }

    public void AddSubscriber(Subscriber subscriber)
    {
        if (_nextHandler != null) 
            _nextHandler.AddSubscriber(subscriber);
        _subscribers.Add(subscriber);
    }

    protected void UpdateSubscribers(string description)
    {
        foreach (var subscriber in _subscribers)
        {
            subscriber.Update(description);
        }
    }
    
}