#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int l;
    int endl;
    int y = 0;
    do
    {
        l = get_int("How many llamas do we start with?\n");
    }
    while (l < 9);
    // TODO: Prompt for end size
    do
    {
        endl = get_int("How many llamas do we finish with?\n");
    }
    while (endl < l);
    // TODO: Calculate number of years until we reach threshold
    while (l < endl)
    {
        l += (l / 3) - (l / 4);
        y++;
    }
    // TODO: Print number of years
    printf("Years: %i", y);
}