#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE pixel = image[0][0];
    pixel.rgbtBlue = 50;
    pixel.rgbtGreen = 50;
    pixel.rgbtRed = 50;
    for (int h = 0; h < 20; h++)
        for (int w = 0; w < 20; w++)
            image[h][w] = image[0][0];
    // Change all black pixels to a color of your choosing
}
