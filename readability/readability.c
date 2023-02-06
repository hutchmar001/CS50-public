#include <cs50.h>
#include <stdio.h>
#include <ctype.h>

int main(void)
{
    int count_letters(string text);
    string txt = get_string("Text: ");
    printf("%s\n", txt);
    count_letters(txt);
}
