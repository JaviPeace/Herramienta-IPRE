namespace Fedex;

public class Headphones : Item
{
    private const int Price = 30;
    
    public Headphones() : base(Price)
    {
    }
    
    public override void AcceptVisitor(Visitor visitor)
        => visitor.VisitHeadphones(this);
}