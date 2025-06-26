namespace Fedex;

public abstract class Item : Component
{
    private int price;

    protected Item(int price)
        => this.price = price;
  
    public int GetTotalPrice() 
        => price;

    public Component[] GetChildren()
        => Array.Empty<Component>();
    
    public bool IsBox() => false;
    
    public virtual void AcceptVisitor(Visitor visitor)
    {
        throw new NotImplementedException();
    }
}