namespace Fedex;

public abstract class Visitor
{
    protected List<string> orderInformation = new List<string>();
    
    public List<string> GetOrderInformation()
    {
        return orderInformation;
    }
    public abstract void VisitCharger(Charger charger);
    public abstract void VisitHammer(Hammer hammer);
    public abstract void VisitHeadphones(Headphones headphones);
    public abstract void VisitPhone(Phone phone);
    public abstract void VisitReceipt(Receipt receipt);
    public abstract void VisitBox(Box box);
}