using System.IO;
using Photoshop.Filters;
using SixLabors.ImageSharp;
using SixLabors.ImageSharp.PixelFormats;
using Xunit;

namespace Photoshop.Tests;

public class ControllerTests
{
    [Theory]
    [InlineData("Lenna.png", "Lenna.png", new FilterType[] { })]
    [InlineData("Lenna.png", "blackAndWhite.png", new [] { FilterType.BlackAndWhite })]
    [InlineData("Lenna.png", "noGreen.png", new [] { FilterType.NoGreen })]
    [InlineData("Lenna.png", "negative.png", new [] { FilterType.Negative })]
    [InlineData("Lenna.png", "blackAndWhite_noGreen.png",
        new [] { FilterType.BlackAndWhite, FilterType.NoGreen })]
    [InlineData("Lenna.png", "noGreen_blackAndWhite.png",
        new [] { FilterType.NoGreen, FilterType.BlackAndWhite })]
    [InlineData("Lenna.png", "noGreen_blackAndWhite_negative.png",
        new [] { FilterType.NoGreen, FilterType.BlackAndWhite, FilterType.Negative })]
    public void BuildFilter_FilterShouldGenerateTheRightImage(string imageFile, string expectedImageFile,
        FilterType[] filters)
    {
        Image<Rgb24> expectedImage = Image.Load<Rgb24>(GetPath(expectedImageFile));
        Image<Rgb24> image = Image.Load<Rgb24>(GetPath(imageFile));

        IFilter filter = Controller.BuildFilter(filters);
        image = filter.Apply(image);
        
        VerifyTheseImagesAreIdentical(expectedImage, image);
    }

    [Fact]
    public void BuildMyFilter_MyFilterShouldGenerateTheRightImage()
    {
        Image<Rgb24> expectedImage = Image.Load<Rgb24>(GetPath("myFilter.png"));
        Image<Rgb24> image = Image.Load<Rgb24>(GetPath("Lenna.png"));

        IFilter filter = Controller.BuildMyFilter();
        image = filter.Apply(image);
        
        VerifyTheseImagesAreIdentical(expectedImage, image);
    }

    private string GetPath(string fileName)
        => Path.Combine("imgs", fileName);

    private void VerifyTheseImagesAreIdentical(Image<Rgb24> expected, Image<Rgb24> actual)
    {
        VerifyTheseImagesHaveTheSameDimensions(expected, actual);
        VerifyThatThePixelsAreIdentical(expected, actual);
    }

    private void VerifyTheseImagesHaveTheSameDimensions(Image<Rgb24> expected, Image<Rgb24> actual)
    {
        Assert.Equal(expected.Width, actual.Width);
        Assert.Equal(expected.Height, actual.Height);
    }

    private void VerifyThatThePixelsAreIdentical(Image<Rgb24> expected, Image<Rgb24> actual)
    {
        for (int x = 0; x < expected.Width; x++)
        for (int y = 0; y < expected.Height; y++)
            Assert.Equal(expected[x, y], actual[x, y]);
    }
}