using SixLabors.ImageSharp.PixelFormats;

namespace Photoshop.Filters;

public class NoGreenFilter: Filter
{
    public NoGreenFilter(IFilter wrapper) : base(wrapper)
    { }
    protected override Rgb24 ApplyPixelFilter(Rgb24 pixel)
    {
        int r = pixel.R;
        int b = pixel.B;
        return new Rgb24((byte)r, 0, (byte)b);
    }
    
}