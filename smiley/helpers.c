#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE pixel = image[0][0];
    pixel.rgbtBlue = 50;
    pixel.rgbtGreen = 50;
    pixel.rgbtRed = 50;
    // Change all black pixels to a color of your choosing
}
