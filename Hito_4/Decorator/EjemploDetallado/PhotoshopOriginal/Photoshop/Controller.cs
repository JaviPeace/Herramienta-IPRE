using Photoshop.Filters;

namespace Photoshop;

public static class Controller
{
    public static IFilter BuildFilter(FilterType[] filters)
    {
        IFilter finalFilter = new NoFilter();

        foreach (var filterType in filters)
        {
            if (filterType == FilterType.Negative)
            {
                finalFilter = new NegativeFilter(finalFilter);
            }
            if (filterType == FilterType.NoGreen)
            {
                finalFilter = new NoGreenFilter(finalFilter);
            }
            if (filterType == FilterType.BlackAndWhite)
            {
                finalFilter = new BlackAndWhiteFilter(finalFilter);
            }
        }

        return finalFilter;
    }
    
    public static IFilter BuildMyFilter()
    {
        return new BlueFilter(new NoFilter());
    }

}   