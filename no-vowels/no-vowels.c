// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <stdio.h>
#include <string.h>

string replace(string);
char new_string[1000];
char c1, c2, c3, c4, c5, c6, c7, c8;

int main(int argc, string argv[])
{
    strcpy(new_string, argv[1]);
    c1 = 'a';
    c2 = '6';
    c3 = 'e';
    c4 = '3';
    c5 = 'i';
    c6 = '1';
    c7 = 'o';
    c8 = '0';
    if (argc != 2)
    {
        printf("Error! Input one word.\n");
        return 1;
    }
    else
    {
        printf("%s\n", replace(new_string));
    }
}

string replace(string string)
{
    for (int i = 0; i < strlen(string); i++)
    {
        switch (string[i])
        {
            case c1:
                string[i] = c2;
                break;
            case c1:
                string[i] = c2;
                break;
        }
        else if (string[i] == c3)
        {
            (string[i] = c4);
        }
        else if (string[i] == c5)
        {
            (string[i] = c6);
        }
        else if (string[i] == c7)
        {
            (string[i] = c8);
        }
        else
        {
            continue;
        }
    }
    return string;
}
