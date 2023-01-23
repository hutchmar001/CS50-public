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
    int revarray[8];
    int num;
    int binary[8];
    string word = get_string("Player 1: ");
    int array[strlen(word)];

for (j = 0; j < sizeof(array)/sizeof(array[0]); j++) {
    for (i = 0; i < (strlen(word)); i++)
    {
        char str[] = {word[i]}; // Makes character into string
        num = strtol(str, NULL, 36) + 55; //Converts letter to number using base 10
        array[i] = num;
    } //Makes array of ASCII numbers
}

    for (i = 0; i < 3; i++) {
        printf("%d\n", array[i]);
    }

for (k = 0; k < 3; k++){
    for (i = 0; i < 8; i++) {
        if (array[k] % 2 == 0 && (array[k] != 1))
            {
                binary[i] = 0;
                array[k] /= 2;

            } else {
                binary[i] = 1;
                array[k] /= 2;
            }
        } //Turns ASCII into binary (backwards)

    for (i = 7; i >= 0; i--) {
        revarray[l] = binary[i];
        print_bulb(revarray[l]);
        l++;
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