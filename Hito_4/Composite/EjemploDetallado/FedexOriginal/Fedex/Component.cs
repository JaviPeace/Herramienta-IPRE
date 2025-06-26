namespace Fedex;

public interface Component
{
    int GetTotalPrice();
    Component[] GetChildren();
    bool IsBox();
    public abstract void AcceptVisitor(Visitor visitor);
    

}