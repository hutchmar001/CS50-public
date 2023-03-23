#include "helpers.h"
#include <math.h>

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
                image[h][w].rgbtRed = round(.393 * image[h][w].rgbtRed + .769 * image[h][w].rgbtGreen + .189 * image[h][w].rgbtBlue);
                printf("%i\n", image[h][w].rgbtRed)
                image[h][w].rgbtGreen = round(.349 * image[h][w].rgbtRed + .686 * image[h][w].rgbtGreen + .168 * image[h][w].rgbtBlue);
                image[h][w].rgbtBlue = round(.272 * image[h][w].rgbtRed + .534 * image[h][w].rgbtGreen + .131 * image[h][w].rgbtBlue);
                if (image[h][w].rgbtRed > 255)
                    {
                        image[h][w].rgbtRed = 255;
                    }
                if (image[h][w].rgbtGreen > 255)
                    {
                        image[h][w].rgbtGreen = 255;
                    }
                if (image[h][w].rgbtBlue > 255)
                    {
                        image[h][w].rgbtBlue = 255;
                    }
            }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int h = 0; h < height; h++)
        for (int w = 0; w < width; w++)
            {
                int oppwidth = width;
                int tmp = w;
                image[h][w] = image[h][oppwidth];
                image[h][oppwidth] = image[h][tmp];
                oppwidth --;
            }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
