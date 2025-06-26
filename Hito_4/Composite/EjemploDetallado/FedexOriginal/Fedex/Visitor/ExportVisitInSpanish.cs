namespace Fedex;

public class ExportVisitInSpanish : Visitor
{
    public override void VisitCharger(Charger charger)
    {
        orderInformation.Add($"Soy un(a) cargador. Mi precio es ${charger.GetTotalPrice()} USD.");
    }

    public override void VisitHammer(Hammer hammer)
    {
        orderInformation.Add($"Soy un(a) martillo. Mi precio es ${hammer.GetTotalPrice()} USD.");
    }

    public override void VisitHeadphones(Headphones headphones)
    {
        orderInformation.Add($"Soy un(a) audífono. Mi precio es ${headphones.GetTotalPrice()} USD.");
    }

    public override void VisitPhone(Phone phone)
    {
        orderInformation.Add($"Soy un(a) teléfono. Mi precio es ${phone.GetTotalPrice()} USD.");
    }

    public override void VisitReceipt(Receipt receipt)
    {
        orderInformation.Add($"Soy un(a) recibo. Mi precio es ${receipt.GetTotalPrice()} USD.");
    }

    public override void VisitBox(Box box)
    {
        orderInformation.Add($"Soy un(a) caja. Mi precio es ${box.GetTotalPrice()} USD.");
    }
}