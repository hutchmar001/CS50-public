#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

int count_letters(string text){
    int count = 0;
    int i;
    for (i = 0; i < strlen(text); i++) {
        if(text[i] != (" "))
            {
                count += 1;
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