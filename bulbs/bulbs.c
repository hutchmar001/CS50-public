#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);


int main(void)
{
    string word1 = get_string("Player 1: ");
    int* array[strlen(word)];
    int* cvrted2num = convert2_num(word1);
    printf("%p\n", cvrted2num);
        };

int* convert2_num(string word)
{
    int i;
    int num;

    for (i = 0; i < (strlen(word)); i++)
    {
        char str[] = {word[i]}; // Makes character into string
        num = strtol(str, NULL, 36) + 55; //Converts letter to number using base 10
        *array[i] = num;
    };
    return *array;
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
