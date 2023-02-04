#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    int i;
    int j;
    int k = 0;
    int l = 0;
    int revarray[8];
    int num;
    int num2;
    int binary[8];
    string word = get_string("Player 1: ");
    int array[strlen(word)];

    for (i = 0; i < (strlen(word)); i++)
        {
            array[i] = (int)word[i];
        } //Makes array of ASCII numbers

for (k = 0; k < sizeof(array)/sizeof(array[0]); k++){
    for (i = 0; i < 8; i++) {
        if (array[k] % 2 == 0 && (array[k] != 1))
            {
                binary[i] = 0;
            } else {
                binary[i] = 1;
}
            array[k] /= 2;

        } //Turns ASCII into binary (backwards)
for (i = 7; i >= 0; i--) {
        print_bulb(binary[i]);
    }  //Flips binary to forwards

    printf("\n");

}

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