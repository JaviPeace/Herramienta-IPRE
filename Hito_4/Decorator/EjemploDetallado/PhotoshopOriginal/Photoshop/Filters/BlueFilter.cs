using SixLabors.ImageSharp.PixelFormats;

namespace Photoshop.Filters;

public class BlueFilter : Filter
{
    public BlueFilter(IFilter wrapper) : base(wrapper)
    {
    }
    protected override Rgb24 ApplyPixelFilter(Rgb24 pixel)
    {
        int r = pixel.R;
        int g = pixel.G;
        int b = 255 - pixel.B;
        return new Rgb24((byte)r, (byte)g, (byte)b);
        
    }
}