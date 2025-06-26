namespace Fedex.Tests;

public class ControllerTests
{
    [Fact]
    public void CreateOrder_DefaultOrderShouldContainTheRightObjects()
    {
        Component order = Controller.CreateOrder();
        Component box1 = order.GetChildren()[0];
        Component box2 = order.GetChildren()[1];
        Component receipt = order.GetChildren()[2];
        Component hammer = box1.GetChildren()[0];
        Component box3 = box2.GetChildren()[0];
        Component box4 = box2.GetChildren()[1];
        Component phone = box3.GetChildren()[0];
        Component headphones = box3.GetChildren()[1];
        Component charger = box4.GetChildren()[0];

        Assert.IsType<Box>(order);
        Assert.IsType<Box>(box1);
        Assert.IsType<Box>(box2);
        Assert.IsType<Box>(box3);
        Assert.IsType<Box>(box4);
        Assert.IsType<Receipt>(receipt);
        Assert.IsType<Hammer>(hammer);
        Assert.IsType<Phone>(phone);
        Assert.IsType<Headphones>(headphones);
        Assert.IsType<Charger>(charger);
    }

    [Fact]
    public void GetPriceListUsing_PricesShouldAppearInTheOrderGivenByTheBFSIterator()
    {
        List<int> expected = new List<int>() { 883, 9, 873, 1, 9, 859, 14, 829, 30, 14 };
        Component order = Controller.CreateOrder();
        Iterator bfsIterator = new BFSIterator(order);

        List<int> prices = Controller.GetPriceListUsing(bfsIterator);
        
        for(int i = 0; i < expected.Count; i++)
            Assert.Equal(expected[i], prices[i]);
    }

    [Fact]
    public void CreateIteratorThatIgnoresBoxes_IteratorShouldOnlyShowThePricesOfItems()
    {
        List<int> expected = new List<int>() { 1, 9, 829, 30, 14 };
        Component order = Controller.CreateOrder();
        Iterator iterator = Controller.CreateIteratorThatIgnoresBoxes(order);
        
        List<int> prices = Controller.GetPriceListUsing(iterator);

        for(int i = 0; i < expected.Count; i++)
            Assert.Equal(expected[i], prices[i]);
    }

    [Fact]
    public void GetOrderInformationInEnglish_InformationShouldAppearInEnglish()
    {
        List<string> expected = new List<string>()
        {
            "I am a box. My price is $883 USD.",
            "I am a box. My price is $9 USD.",
            "I am a box. My price is $873 USD.",
            "I am a receipt. My price is $1 USD.",
            "I am a hammer. My price is $9 USD.",
            "I am a box. My price is $859 USD.",
            "I am a box. My price is $14 USD.",
            "I am a phone. My price is $829 USD.",
            "I am a headphones. My price is $30 USD.",
            "I am a charger. My price is $14 USD.",
        };
        Component order = Controller.CreateOrder();
        Iterator bfsIterator = new BFSIterator(order);

        List<string> info = Controller.GetOrderInformationInEnglish(bfsIterator);
        
        for(int i = 0; i < expected.Count; i++)
            Assert.Equal(expected[i], info[i]);
    }
    
    [Fact]
    public void GetOrderInformationInSpanish_InformationShouldAppearInSpanish()
    {
        List<string> expected = new List<string>()
        {
            "Soy un(a) caja. Mi precio es $883 USD.",
            "Soy un(a) caja. Mi precio es $9 USD.",
            "Soy un(a) caja. Mi precio es $873 USD.",
            "Soy un(a) recibo. Mi precio es $1 USD.",
            "Soy un(a) martillo. Mi precio es $9 USD.",
            "Soy un(a) caja. Mi precio es $859 USD.",
            "Soy un(a) caja. Mi precio es $14 USD.",
            "Soy un(a) teléfono. Mi precio es $829 USD.",
            "Soy un(a) audífono. Mi precio es $30 USD.",
            "Soy un(a) cargador. Mi precio es $14 USD.",
        };
        Component order = Controller.CreateOrder();
        Iterator bfsIterator = new BFSIterator(order);

        List<string> info = Controller.GetOrderInformationInSpanish(bfsIterator);
        
        for(int i = 0; i < expected.Count; i++)
            Assert.Equal(expected[i], info[i]);
    }
}