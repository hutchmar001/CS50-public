#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE pixel = image[0][0];
    pixel.rgbtBlue = 250;
    pixel.rgbtGreen = 250;
    pixel.rgbtRed = 50;
    for (int h = 0; h < 5; h++)
        for (int w = 0; w < 5; w++)
            if (image[h][w].rgbtBlue == 0 && image[h][w].rgbtGreen == 0 && image[h][w].rgbtRed == 0)
            {
                image[h][w].rgbtBlue = pixel.rgbtBlue;
                image[h][w].rgbtGreen = pixel.rgbtGreen;
                image[h][w].rgbtRed = pixel.rgbtRed;
            }
        // Change all black pixels to a color of your choosing
}
