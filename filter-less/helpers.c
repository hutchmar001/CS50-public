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
    int oppwidth = width - 1;
    for (int h = 0; h < height; h++)
        for (int w = 0; w < (width - w - 1); w++)
            {
                int tmp = image[h][w].rgbtRed;
                int tmp2 = image[h][w].rgbtGreen;
                int tmp3 = image[h][w].rgbtBlue;
                int filteredRed = image[h][oppwidth - w].rgbtRed;
                int filteredGreen = image[h][oppwidth - w].rgbtGreen;
                int filteredBlue = image[h][oppwidth - w].rgbtBlue;
                image[h][oppwidth - w].rgbtRed = tmp;
                image[h][oppwidth - w].rgbtGreen = tmp2;
                image[h][oppwidth - w].rgbtBlue = tmp3;
                image[h][w].rgbtRed = filteredRed;
                image[h][w].rgbtGreen = filteredGreen;
                image[h][w].rgbtBlue = filteredBlue;
            }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE copy[height][width];
    for (int h = 0; h < height; h++)
        for (int w = 0; w < width; w++)
        {
            if (h == 0 && w == 0)
            {
                copy[h][w].rgbtRed = round(image[h][w].rgbtRed + image[h][w + 1].rgbtRed
                                           + image[h + 1][w + 1].rgbtRed + image[h + 1][w].rgbtRed) / 4;
                copy[h][w].rgbtGreen = round(image[h][w].rgbtGreen + image[h][w + 1].rgbtGreen
                                             + image[h + 1][w + 1].rgbtGreen + image[h + 1][w].rgbtGreen) / 4;
                copy[h][w].rgbtBlue = round(image[h][w].rgbtBlue + image[h][w + 1].rgbtBlue
                                            + image[h + 1][w + 1].rgbtBlue + image[h + 1][w].rgbtBlue) / 4;
            }
            else if (h == 0 && w == width - 1)
            {
                copy[h][w].rgbtRed = round(image[h][w].rgbtRed + image[h + 1][w].rgbtRed
                                           + image[h + 1][w - 1].rgbtRed + image[h][w - 1].rgbtRed) / 4;
                copy[h][w].rgbtGreen = round(image[h][w].rgbtGreen + image[h + 1][w].rgbtGreen
                                             + image[h + 1][w - 1].rgbtGreen + image[h][w - 1].rgbtGreen) / 4;
                copy[h][w].rgbtBlue = round(image[h][w].rgbtBlue + image[h + 1][w].rgbtBlue
                                            + image[h + 1][w - 1].rgbtBlue + image[h][w - 1].rgbtBlue) / 4;
            }
            else if (h == height - 1 && w == 0)
            {
                copy[h][w].rgbtRed = round(image[h][w].rgbtRed + image[h - 1][w].rgbtRed
                                           + image[h - 1][w + 1].rgbtRed + image[h][w + 1].rgbtRed) / 4;
                copy[h][w].rgbtGreen = round(image[h][w].rgbtGreen + image[h - 1][w].rgbtGreen
                                             + image[h - 1][w + 1].rgbtGreen + image[h][w + 1].rgbtGreen) / 4;
                copy[h][w].rgbtBlue = round(image[h][w].rgbtBlue + image[h - 1][w].rgbtBlue
                                            + image[h - 1][w + 1].rgbtBlue + image[h][w + 1].rgbtBlue) / 4;
            }
            else if (h == height - 1 && w == width - 1)
            {
                copy[h][w].rgbtRed = round(image[h][w].rgbtRed + image[h - 1][w].rgbtRed
                                           + image[h][w - 1].rgbtRed + image[h - 1][w - 1].rgbtRed) / 4;
                copy[h][w].rgbtGreen = round(image[h][w].rgbtGreen + image[h - 1][w].rgbtGreen
                                             + image[h][w - 1].rgbtGreen + image[h - 1][w - 1].rgbtGreen) / 4;
                copy[h][w].rgbtBlue = round(image[h][w].rgbtBlue + image[h - 1][w].rgbtBlue
                                            + image[h][w - 1].rgbtBlue + image[h - 1][w - 1].rgbtBlue) / 4;
            }
            else if (h == 0 && 0 < w && w < (width - 1))
            {
                copy[h][w].rgbtRed = (round((image[h][w].rgbtRed + image[h + 1][w].rgbtRed
                                           + image[h + 1][w + 1].rgbtRed + image[h][w + 1].rgbtRed
                                           + image[h][w - 1].rgbtRed + image[h + 1][w - 1].rgbtRed)) / 6);
                copy[h][w].rgbtGreen = (round((image[h][w].rgbtGreen + image[h + 1][w].rgbtGreen
                                             + image[h + 1][w + 1].rgbtGreen + image[h][w + 1].rgbtGreen
                                             + image[h][w - 1].rgbtGreen + image[h + 1][w - 1].rgbtGreen)) / 6);
                copy[h][w].rgbtBlue = (round((image[h][w].rgbtBlue + image[h + 1][w].rgbtBlue
                                            + image[h + 1][w + 1].rgbtBlue + image[h][w + 1].rgbtBlue
                                            + image[h][w - 1].rgbtBlue + image[h + 1][w - 1].rgbtBlue)) / 6);
            }
            else if (0 < h && h < (height - 1) && w == width - 1)
            {
                copy[h][w].rgbtRed = (round((image[h][w].rgbtRed + image[h + 1][w].rgbtRed
                                           + image[h - 1][w].rgbtRed + image[h - 1][w - 1].rgbtRed
                                           + image[h][w - 1].rgbtRed + image[h + 1][w - 1].rgbtRed)) / 6);
                copy[h][w].rgbtGreen = (round((image[h][w].rgbtGreen + image[h + 1][w].rgbtGreen
                                             + image[h - 1][w].rgbtGreen + image[h - 1][w - 1].rgbtGreen
                                             + image[h][w - 1].rgbtGreen + image[h + 1][w - 1].rgbtGreen)) / 6);
                copy[h][w].rgbtBlue = (round((image[h][w].rgbtBlue + image[h + 1][w].rgbtBlue
                                            + image[h - 1][w].rgbtBlue + image[h - 1][w - 1].rgbtBlue
                                            + image[h][w - 1].rgbtBlue + image[h + 1][w - 1].rgbtBlue)) / 6);
            }
            else if (h == height - 1 && 0 < w && w < (width - 1))
            {
                copy[h][w].rgbtRed = (round((image[h][w].rgbtRed + image[h][w + 1].rgbtRed
                                           + image[h - 1][w + 1].rgbtRed + image[h - 1][w].rgbtRed
                                           + image[h - 1][w - 1].rgbtRed + image[h][w - 1].rgbtRed)) / 6);
                copy[h][w].rgbtGreen = (round((image[h][w].rgbtGreen + image[h][w + 1].rgbtGreen
                                             + image[h - 1][w + 1].rgbtGreen + image[h - 1][w].rgbtGreen
                                             + image[h - 1][w - 1].rgbtGreen + image[h][w - 1].rgbtGreen)) / 6);
                copy[h][w].rgbtBlue = (round((image[h][w].rgbtBlue + image[h][w + 1].rgbtBlue
                                            + image[h - 1][w + 1].rgbtBlue + image[h - 1][w].rgbtBlue
                                            + image[h - 1][w - 1].rgbtBlue + image[h][w - 1].rgbtBlue)) / 6);
            }
            else if (0 < h && h < (height - 1) && w == 0)
            {
                copy[h][w].rgbtRed = (round((image[h][w].rgbtRed + image[h + 1][w].rgbtRed
                                           + image[h + 1][w + 1].rgbtRed + image[h][w + 1].rgbtRed
                                           + image[h - 1][w + 1].rgbtRed + image[h - 1][w].rgbtRed)) / 6);
                copy[h][w].rgbtGreen = (round((image[h][w].rgbtGreen + image[h + 1][w].rgbtGreen
                                             + image[h + 1][w + 1].rgbtGreen + image[h][w + 1].rgbtGreen
                                             + image[h - 1][w + 1].rgbtGreen + image[h - 1][w].rgbtGreen)) / 6);
                copy[h][w].rgbtBlue = (round((image[h][w].rgbtBlue + image[h + 1][w].rgbtBlue
                                            + image[h + 1][w + 1].rgbtBlue + image[h][w + 1].rgbtBlue
                                            + image[h - 1][w + 1].rgbtBlue + image[h - 1][w].rgbtBlue)) / 6);
            }
            else
            {
                copy[h][w].rgbtRed = (round((float(image[h][w].rgbtRed + image[h - 1][w].rgbtRed + image[h - 1][w + 1].rgbtRed
                                           + image[h][w + 1].rgbtRed + image[h + 1][w + 1].rgbtRed + image[h + 1][w].rgbtRed
                                           + image[h + 1][w - 1].rgbtRed + image[h][w - 1].rgbtRed + image[h - 1][w - 1].rgbtRed))) / 9);
                copy[h][w].rgbtGreen = (round((float(image[h][w].rgbtGreen + image[h - 1][w].rgbtGreen + image[h - 1][w + 1].rgbtGreen
                                           + image[h][w + 1].rgbtGreen + image[h + 1][w + 1].rgbtGreen + image[h + 1][w].rgbtGreen
                                           + image[h + 1][w - 1].rgbtGreen + image[h][w - 1].rgbtGreen + image[h - 1][w - 1].rgbtGreen))) / 9);
                copy[h][w].rgbtBlue = (round((float(image[h][w].rgbtBlue + image[h - 1][w].rgbtBlue + image[h - 1][w + 1].rgbtBlue
                                           + image[h][w + 1].rgbtBlue + image[h + 1][w + 1].rgbtBlue + image[h + 1][w].rgbtBlue
                                           + image[h + 1][w - 1].rgbtBlue + image[h][w - 1].rgbtBlue + image[h - 1][w - 1].rgbtBlue))) / 9);
            }
        image[h][w].rgbtRed = copy[h][w].rgbtRed;
        image[h][w].rgbtGreen = copy[h][w].rgbtGreen;
        image[h][w].rgbtBlue = copy[h][w].rgbtBlue;
        printf("%i\n", copy[h][w].rgbtRed);
        printf("%i\n", copy[h][w].rgbtGreen);
        printf("%i\n", copy[h][w].rgbtBlue);
        printf("%i\n", image[h][w].rgbtRed);
        printf("%i\n", image[h][w].rgbtGreen);
        printf("%i\n", image[h][w].rgbtBlue);
        }
    return;
}
