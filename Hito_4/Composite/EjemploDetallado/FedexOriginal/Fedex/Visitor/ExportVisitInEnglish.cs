namespace Fedex;

public class ExportVisitInEnglish : Visitor
{
    private List<string> orderInformation = new List<string>();
    public List<string> GetOrderInformation()
    {
        return orderInformation;
    }
    public override void VisitCharger(Charger charger)
    {
        orderInformation.Add($"I am a charger. My price is ${charger.GetTotalPrice()} USD.");
    }

    public override void VisitHammer(Hammer hammer)
    {
        orderInformation.Add($"I am a hammer. My price is ${hammer.GetTotalPrice()} USD.");
    }

    public override void VisitHeadphones(Headphones headphones)
    {
        orderInformation.Add($"I am a headphones. My price is ${headphones.GetTotalPrice()} USD.");
    }

    public override void VisitPhone(Phone phone)
    {
        orderInformation.Add($"I am a phone. My price is ${phone.GetTotalPrice()} USD.");
    }

    public override void VisitReceipt(Receipt receipt)
    {
        orderInformation.Add($"I am a receipt. My price is ${receipt.GetTotalPrice()} USD.");
    }

    public override void VisitBox(Box box)
    {
        orderInformation.Add($"I am a box. My price is ${box.GetTotalPrice()} USD.");
    }
}