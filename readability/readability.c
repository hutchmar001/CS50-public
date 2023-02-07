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
        int result = strcmp(&txt[0], ' ');
        if (result != 32) {
            count++;
            printf("%d\n", count);
        }
                }
    return count;
}

int main(void)
{
    string txt = get_string("Text: ");
    printf("%s\n", txt);
    count_letters(txt);
}