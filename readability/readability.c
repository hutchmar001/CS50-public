#include <cs50.h>
#include <stdio.h>
#include <ctype.h>

int count_letters(string text){
    int count = 0;
    int i;
    for (i = 0; i < len(text); i++) {
        if(text[i] != " ")
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