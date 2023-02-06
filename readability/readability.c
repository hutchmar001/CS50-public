#include <cs50.h>
#include <stdio.h>
#include <lcs50.h>
int count_letters(string text);
int main(void)
{
    string txt = get_string("Text: ");
    printf("%s\n", txt);
    count_letters(txt);
}
