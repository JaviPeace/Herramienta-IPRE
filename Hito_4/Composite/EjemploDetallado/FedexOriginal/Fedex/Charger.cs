namespace Fedex;

public class Charger:Item
{
    private const int Price = 14;
    
    public Charger() : base(Price)
    {
    }
    public override void AcceptVisitor(Visitor visitor)
        => visitor.VisitCharger(this);
}