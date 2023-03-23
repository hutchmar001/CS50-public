#include "helpers.h"
#include <math.h>
#include <stdio.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int h = 0; h < height; h++)
        for (int w = 0; w < width; w++)
            {
                int greyscale = round((image[h][w].rgbtBlue + image[h][w].rgbtGreen + image[h][w].rgbtRed) / 3.0);
                image[h][w].rgbtBlue = greyscale;
                image[h][w].rgbtGreen = greyscale;
                image[h][w].rgbtRed = greyscale;
            }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int h = 0; h < height; h++)
        for (int w = 0; w < width; w++)
            {
                int sepiaRed = round(.393 * image[h][w].rgbtRed + .769 * image[h][w].rgbtGreen + .189 * image[h][w].rgbtBlue);
                int sepiaGreen = round(.349 * image[h][w].rgbtRed + .686 * image[h][w].rgbtGreen + .168 * image[h][w].rgbtBlue);
                int sepiaBlue = round(.272 * image[h][w].rgbtRed + .534 * image[h][w].rgbtGreen + .131 * image[h][w].rgbtBlue);
                image[h][w].rgbtRed = sepiaRed;
                image[h][w].rgbtGreen = sepiaGreen;
                image[h][w].rgbtBlue = sepiaBlue;
                if (sepiaRed > 255)
                    {
                        image[h][w].rgbtRed = 255;
                    }
                if (sepiaGreen > 255)
                    {
                        image[h][w].rgbtGreen = 255;
                    }
                if (sepiaBlue > 255)
                    {
                        image[h][w].rgbtBlue = 255;
                    }
            }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    int oppwidth = width;
    for (int h = 0; h < height; h++)
        for (int w = 0; w < width; w++)
            {
                int tmp = image[h][w].rgbtRed;
                image[h][w].rgbtRed = image[h][oppwidth].rgbtRed;
                image[h][oppwidth].rgbtRed = tmp;
                int tmp2 = image[h][w].rgbtGreen;
                image[h][w].rgbtGreen = image[h][oppwidth].rgbtGreen;
                image[h][oppwidth].rgbtGreen = tmp2;
                int tmp3 = image[h][w].rgbtBlue;
                image[h][w].rgbtBlue = image[h][oppwidth].rgbtBlue;
                image[h][oppwidth].rgbtBlue = tmp3;
                oppwidth --;
            }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
