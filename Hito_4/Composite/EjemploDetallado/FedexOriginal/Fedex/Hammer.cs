namespace Fedex;

public class Hammer:Item
{
    private const int Price = 9;
    
    public Hammer() : base(Price)
    {
    }
    
    public override void AcceptVisitor(Visitor visitor)
        => visitor.VisitHammer(this);
}