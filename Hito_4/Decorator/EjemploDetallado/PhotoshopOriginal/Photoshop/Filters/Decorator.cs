using SixLabors.ImageSharp;
using SixLabors.ImageSharp.PixelFormats;

namespace Photoshop.Filters;

public abstract class Decorator : IFilter
{
    private IFilter _wrapper;

    protected Decorator(IFilter wrapper)
        => _wrapper = wrapper;

    public virtual Image<Rgb24> Apply(Image<Rgb24> image)
        => _wrapper.Apply(image);

}