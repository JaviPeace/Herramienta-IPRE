using SixLabors.ImageSharp.PixelFormats;

namespace Photoshop.Filters;

public class BlackAndWhiteFilter : Filter
{
    public BlackAndWhiteFilter(IFilter wrapper) : base(wrapper)
    { }
    
    protected override Rgb24 ApplyPixelFilter(Rgb24 pixel)
    {
        int r = pixel.R;
        int g = pixel.G;
        int b = pixel.B;
        byte averageColor = (byte)((r + g + b) / 3);
        return new Rgb24(averageColor, averageColor, averageColor);
    }
    
}