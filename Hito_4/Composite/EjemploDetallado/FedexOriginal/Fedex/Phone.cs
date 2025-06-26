namespace Fedex;

public class Phone:Item
{
    private const int Price = 829;
    
    public Phone() : base(Price)
    {
    }
    public override void AcceptVisitor(Visitor visitor)
        => visitor.VisitPhone(this);
}