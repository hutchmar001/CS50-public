#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>
int main()
{

    int getHeight(void)
{
    int height = 0;
    printf("Please enter an integer.\n");
    scanf("%d", &height);
    while (height < 1 || height > 8) {
        printf("Please enter an integer.\n");
        scanf("%d", &height);
    } printf("The height is %d.\n", height);
    for (int h = 1; h <= height; h++) {
        for (int j = 0; j <= height - h; j++) {
            printf(" ");
        } for (int k = 0; k <= h - 1; k++) {
                printf("#");
            }
            printf("\n");
    }

    return 0;
}

    return 0;
}