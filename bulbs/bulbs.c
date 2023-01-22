#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    int i;
    int j;
    int k = 0;
    int l = 0;
    int m;
    int revarray[8];
    int num;
    int binary[100];
    string word = get_string("Player 1: ");
    int array[strlen(word)];

    for (i = 0; i < (strlen(word)); i++)
    {
        char str[] = {word[i]}; // Makes character into string
        num = strtol(str, NULL, 36) + 55; //Converts letter to number using base 10
        array[0] = num;
        printf("%d\n", *array);
    } //Makes array of ASCII numbers

    for (j = 0; j < 8; j++) {
        if (array[k] % 2 == 0 && (array[k] != 1))
            {
                binary[j] = 0;
                array[k] /= 2;
                printf("%d\n", binary[j]);
            } else {
                binary[j] = 1;
                array[k] /= 2;
                printf("%d\n", binary[j]);
            }
    } //Turns ASCII into binary (backwards)

    for (m = 8; m > 0; m--) {
        revarray[l] = binary[m];
        l++;
        printf("%d\n", revarray[l]);
    } //Flips binary to forwards

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
