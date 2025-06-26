namespace VehicleRoutingValidator;

public class Subscriber
{
    private List<string> _status = new List<string>();

    public List<string> GetStatus()
        => _status;

    public void Update(string newStatus)
        => _status.Add(newStatus);
}