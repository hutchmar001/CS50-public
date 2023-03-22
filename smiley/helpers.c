#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE pixel = image[0][0];
    pixel.rgbtBlue = 25;
    pixel.rgbtGreen = 0;
    pixel.rgbtRed = 250;
    for (int h = 0; h < height; h++)
        for (int w = 0; w < width; w++)
            if (image[h][w].rgbtBlue == 0 && image[h][w].rgbtGreen == 0 && image[h][w].rgbtRed == 0)
            {
                image[h][w].rgbtBlue = pixel.rgbtBlue;
                image[h][w].rgbtGreen = pixel.rgbtGreen;
                image[h][w].rgbtRed = pixel.rgbtRed;
            }
    // Change all black pixels to a color of your choosing
}
