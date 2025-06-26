using SixLabors.ImageSharp.PixelFormats;

namespace Photoshop.Filters;

public class NegativeFilter: Filter 
{
    public NegativeFilter(IFilter wrapper) : base(wrapper)
    {
    }
    protected override Rgb24 ApplyPixelFilter(Rgb24 pixel)
    {
        int r = 255 - pixel.R;
        int g = 255 - pixel.G;
        int b = 255 - pixel.B;
        return new Rgb24((byte)r, (byte)g, (byte)b);
    }

}