namespace Fedex;

public class Box : Component
{
    private List<Component> components = new List<Component>();

    public void Add(Component component)
        => components.Add(component);

    public int GetTotalPrice()
    {
        int total = 0;
        foreach (var component in components)
            total += component.GetTotalPrice();
        return total;
    }

    public Component[] GetChildren()
        => components.ToArray();

    public bool IsBox() => true;    
    
    public void AcceptVisitor(Visitor visitor)
        => visitor.VisitBox(this);
}