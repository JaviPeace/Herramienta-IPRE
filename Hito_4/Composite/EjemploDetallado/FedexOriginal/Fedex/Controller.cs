namespace Fedex;

public static class Controller
{
    public static Component CreateOrder()
    {
        Hammer hammer = new Hammer();
        Phone phone = new Phone();
        Headphones headphones = new Headphones();
        Charger charger = new Charger();
        Receipt receipt = new Receipt();
        
        Box box1 = new Box();
        Box box2 = new Box();
        Box box3 = new Box();
        Box box4 = new Box();
        Box completeOrder = new Box();
        
        box1.Add(hammer);
        box3.Add(phone);
        box3.Add(headphones);
        box4.Add(charger);
        box2.Add(box3);
        box2.Add(box4);
        
        completeOrder.Add(box1);
        completeOrder.Add(box2);
        completeOrder.Add(receipt);
        
        return completeOrder;
        
    }
    
    public static List<int> GetPriceListUsing(Iterator iterator)
    {
        List<int> listOfPrices = new List<int>();
        while (iterator.HasMore())
            listOfPrices.Add(iterator.GetNext().GetTotalPrice());
        return listOfPrices;
    }

    public static Iterator CreateIteratorThatIgnoresBoxes(Component order)
    {
        BFSIteratorWithoutBoxes iteratorWithoutBoxes = new BFSIteratorWithoutBoxes(order);
        return iteratorWithoutBoxes;
    }

    public static List<string> GetOrderInformationInEnglish(Iterator iterator)
    {
        ExportVisitInEnglish exportVisitInEnglish = new ExportVisitInEnglish();
        while (iterator.HasMore())
        {
            Component component = iterator.GetNext();
            component.AcceptVisitor(exportVisitInEnglish);
        }
        return exportVisitInEnglish.GetOrderInformation();
    }
    
    public static List<string> GetOrderInformationInSpanish(Iterator iterator)
    {
        ExportVisitInSpanish exportVisitInSpanish = new ExportVisitInSpanish();
        while (iterator.HasMore())
        {
            Component component = iterator.GetNext();
            component.AcceptVisitor(exportVisitInSpanish);
        }
        return exportVisitInSpanish.GetOrderInformation();
    }

}