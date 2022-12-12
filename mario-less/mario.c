#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int height;
    int i;
    printf("Please enter an integer.");

    while (getchar() < 1 && getchar() > 8) {
        continue;
    }
    height = getchar();
    printf("%d", height);
}
