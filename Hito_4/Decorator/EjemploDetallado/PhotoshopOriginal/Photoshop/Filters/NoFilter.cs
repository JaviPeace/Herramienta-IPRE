using SixLabors.ImageSharp;
using SixLabors.ImageSharp.PixelFormats;

namespace Photoshop.Filters;

public class NoFilter : IFilter
{
    public Image<Rgb24> Apply(Image<Rgb24> image)
        => image;
}