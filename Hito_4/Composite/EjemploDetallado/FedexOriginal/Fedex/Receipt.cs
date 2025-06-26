namespace Fedex;

public class Receipt:Item
{
    private const int Price = 1;
    
    public Receipt() : base(Price)
    {
    }
    
    public override void AcceptVisitor(Visitor visitor)
        => visitor.VisitReceipt(this);
}