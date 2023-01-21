#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    int i;
    int num;
    string word = get_string("Player 1: ");
    for (i = 0; i < (strlen(word)); i++)
    {
        int array[strlen(word)];
        char str[] = {word[i]}; // Makes character into string
        num = strtol(str, NULL, 36) + 55; //Converts letter to number using base 10
        array[0] = num;
        int binary[3];
        int j = 0;
        int k = 0;
        while (array[j] % 2 == 0 || (array[j] > 0))
            {
                binary[k] = 0;
                printf("%d\n", *binary);
                array[j] /= 2;
            }
        binary[j] = 1;
        printf("%d\n", *binary);
    }
};

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
