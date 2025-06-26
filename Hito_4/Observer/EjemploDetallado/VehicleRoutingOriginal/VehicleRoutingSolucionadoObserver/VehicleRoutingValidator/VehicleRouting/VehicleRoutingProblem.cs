namespace VehicleRoutingValidator.VehicleRouting;

public class VehicleRoutingProblem
{
    public const int Depot = 0;
    public int NumberOfLocations { get; set; }
    public int MaxNumberOfTours { get; set; }
    public Precedence[] Precedences { get; set; }
    public Constraint[] Constraints { get; set; }
}