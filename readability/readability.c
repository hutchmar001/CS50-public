#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int count_letters(string text)
{
    int count = 0;
    int i;
    for (i = 0; i < strlen(text); i++)
    {
        char txt[1];
        txt[0] = text[i];
        char blank[1];
        blank[0] = ' ';
        char period[1];
        period[0] = '.';
        char expoint[1];
        expoint[0] = '!';
        char questionmark[1];
        questionmark[0] = '?';
        char apostrophe[1];
        apostrophe[0] = '\'';
        char doublequotes[1];
        doublequotes[0] = '\"';
        int result1 = memcmp(txt, blank, 1);
        int result2 = memcmp(txt, period, 1);
        int result3 = memcmp(txt, expoint, 1);
        int result4 = memcmp(txt, questionmark, 1);
        int result5 = memcmp(txt, apostrophe, 1);
        int result6 = memcmp(txt, doublequotes, 1);
        if (result1 != 0 && result2 != 0 && result3 != 0 && result4 != 0 && result5 != 0 && result6 != 0)
        {
            count++;    //if a letter is not blank, ., !, ?, ', or ", add to letter count
        }
    }
    return count;
}

int count_words(string text)
{
    int count2 = 1;
    int j;
    for (j = 0; j < strlen(text); j++)
    {
        char txt[1];
        txt[0] = text[j];
        char blank[1];
        blank[0] = ' ';
        int result = memcmp(txt, blank, 1);
        if (result == 0)
        {
            count2++;   //if a letter is a blank, add to word count
        }
    }
    return count2;
}

int count_sentences(string text)
{
    int count3 = 0;
    int k;
    for (k = 0; k < strlen(text); k++)
    {
        char txt[1];
        txt[0] = text[k];
        char period[1];
        period[0] = '.';
        char expoint[1];
        expoint[0] = '!';
        char questionmark[1];
        questionmark[0] = '?';
        int result1 = memcmp(txt, period, 1);
        int result2 = memcmp(txt, expoint, 1);
        int result3 = memcmp(txt, questionmark, 1);
        if (result1 == 0 || result2 == 0 || result3 == 0)
        {
            count3++;   //if a letter is ., !, or ?, add to sentence count
        }
    }
    return count3;
}

int main(void)
{
    string txt = get_string("Text: ");
    double letters = count_letters(txt);
    double words = count_words(txt);
    double sentences = count_sentences(txt);
    double L = letters / words * 100;   //average letters per 100 words
    double S = sentences / words * 100;     //average sentences per 100 words
    double index = 0.058 * L - 0.296 * S - 15.8;    // Coleman-Liau index formula
    index = round(index);   //index rounded to nearest whole number
    int idx = index;    //index changed to int
    if (idx < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (idx > 15)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("%s%d\n", "Grade ", idx);
    }
    return 0;
}