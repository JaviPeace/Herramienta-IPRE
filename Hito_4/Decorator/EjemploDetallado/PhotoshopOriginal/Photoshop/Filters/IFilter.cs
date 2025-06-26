using SixLabors.ImageSharp;
using SixLabors.ImageSharp.PixelFormats;

namespace Photoshop.Filters;

public interface IFilter
{
    Image<Rgb24> Apply(Image<Rgb24> image);
}