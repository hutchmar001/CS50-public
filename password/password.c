// Check that a password has at least one lowercase letter, uppercase letter, number and symbol
// Practice iterating through a string
// Practice using the ctype library

#include <cs50.h>
#include <stdio.h>
#include <string.h>

bool valid(string password);

int main(void)
{
    string password = get_string("Enter your password: ");
    if (valid(password))
    {
        printf("Your password is valid!\n");
    }
    else
    {
        printf("Your password needs at least one uppercase letter, lowercase letter, number and symbol\n");
    }
}

// TODO: Complete the Boolean function below
bool valid(string password)
{
    int array[strlen(password)];
    bool upper = false;
    bool lower = false;
    bool num = false;
    bool sym = false;
    for (int i = 0; i < (strlen(password)); i++)
    {
        array[i] = (int)password[i];
    }
    for (int i = 0; i < (strlen(password)); i++)
    {
        if (65 < array[i] && array[i] < 91)
        {
            upper = true;
        }
        if (96 < array[i] && array[i] < 123)
        {
            lower = true;
        }
        if (47 < array[i] && array[i] < 58)
        {
            num = true;
        }
        if (32 < array[i] && array[i] < 48)
        {
            sym = true;
        }
    }
    if (upper == true && lower == true && num == true && sym == true)
    {
        return true;
    }
    else
    {
        return false;
    }
}
