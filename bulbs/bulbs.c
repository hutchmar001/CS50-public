#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

struct MyStruct {
    int dec[100];
    };

struct convert2_num (word);
{
    int i;
    int num;
    struct myStructure s1;
    for (i = 0; i < (strlen(word)); i++)
    {
        char str[] = {word[i]}; // Makes character into string
        num = strtol(str, NULL, 36) + 55; //Converts letter to number using base 10
    s1.dec[i] = num;
    };
    return MyStruct;
}

int main(void)
{
    string word1 = get_string("Player 1: ");
    int cvrted2num = convert2_num(word1);
    printf("%i\n", cvrted2num);
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
