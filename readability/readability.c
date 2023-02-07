#include <cs50.h>
#include <stdio.h>
#include <ctype.h>

int count_letters(string text){
    printf("no\n");
    return 4;
}

int main(void)
{
    string txt = get_string("Text: ");
    printf("%s\n", txt);
    count_letters(txt);
}