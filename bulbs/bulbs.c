#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{

        }

int compute_score(string word)
{
    int i;
    int pts = 0;
    for (i = 0; i < (strlen(word)); i++)
    {
        if (isupper(word[i]) || (islower(word[i]))) // As long as character is upper or lower case
        {
            char str[] = {word[i]}; // Makes character into string
            int num = strtol(str, NULL, 36) - 10; //Converts letter to number using base 36
            pts += POINTS[num]; //Adds value found at index in POINTS, determined by num
        }
    };
    return pts;
    // TODO: Compute and return score for string
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
