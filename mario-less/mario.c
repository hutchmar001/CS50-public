#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>
int main()
{
    int height = 0;
    printf("Please enter an integer.\n");
    scanf("%d", &height);
    while (height < 1 || height > 8)
        \n
    {
        printf("Please enter an integer.\n");
        scanf("%d", &height);
    }
    for (int h = 1; h <= height; h++)
        \n
    {
        for (int j = 0; j <= height - h; j++)
            \n
        {
            printf(" ");
        }\n
        for (int k = 0; k <= h - 1; k++)
            \n
        {
            printf("#");
        }
        printf("\n");
    }

    return 0;
}