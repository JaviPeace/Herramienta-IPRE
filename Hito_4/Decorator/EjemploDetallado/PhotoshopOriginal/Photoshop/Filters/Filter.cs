using SixLabors.ImageSharp;
using SixLabors.ImageSharp.PixelFormats;

namespace Photoshop.Filters;

public abstract class Filter : Decorator
{
    protected Filter(IFilter wrapper) : base(wrapper)
    {
    }
    
    public override Image<Rgb24> Apply(Image<Rgb24> image)
    {
        image = base.Apply(image);
        return ApplyFilter(image);
    }

    private Image<Rgb24> ApplyFilter(Image<Rgb24> image)
    {
        int width = image.Width;
        int height = image.Height;
        Image<Rgb24> filteredImage = new Image<Rgb24>(width, height); 
        for (int x = 0; x < width; x++)
        {
            for (int y = 0; y < height; y++)
            {
                filteredImage[x, y] = ApplyPixelFilter(image[x, y]);
            }   
        }
        return filteredImage;
    }
    
    protected abstract Rgb24 ApplyPixelFilter(Rgb24 pixel);
    
}