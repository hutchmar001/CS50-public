#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int count_letters(string text){
    int count = 0;
    int i;
    for (i = 0; i < strlen(text); i++) {
        char txt[1];
        txt[0] = text[i];
        char blank[1];
        blank[0] = ' ';
        int result = strcmp(txt, blank);
        if (result >= 0) {
            count++; //Counting amount of letters w/o spaces, space returns neg.
        }
                }
    return count;
}

int count_words(string text){
    int count2 = 1;
    int j;
    for (j = 0; j < strlen(text); j++) {
        char txt[1];
        txt[0] = text[j];
        char blank[1];
        blank[0] = ' ';
        int result = strcmp(txt, blank);
        if (result <= 0) {
            count2++; //Counting amount of spaces w/ 1 added, space returns neg.
        }
                }
    return count2;
}

int count_sentences(string text){
    int count3 = 0;
    int k;
    for (k = 0; k < strlen(text); k++) {
        char txt[1];
        txt[0] = text[k];
        char blank[1];
        blank[0] = '.';
        char expoint[1];
        expoint[0] = '!';
        char questionmark[1];
        questionmark[0] = '?';
        int result1 = memcmp(txt, blank, 1);
        int result2 = memcmp(txt, expoint, 1);
        int result3 = memcmp(txt, questionmark, 1); //Switch to memcmp to compare strings
        printf("%d\n", result1);
        if (result1 == 0 ) {
            count3++;
        }
                }
    printf("%d\n", count3);
    return count3;
}

int main(void)
{
    string txt = get_string("Text: ");
    printf("%s\n", txt);
    count_letters(txt);
    count_words(txt);
    count_sentences(txt);
}