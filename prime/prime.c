#include <cs50.h>
#include <stdio.h>

bool prime(int number);

int main(void)
{
    int min;
    do
    {
        min = get_int("Minimum: ");
    }
    while (min < 1);

    int max;
    do
    {
        max = get_int("Maximum: ");
    }
    while (min >= max);

    for (int i = min; i <= max; i++)
    {
        if (prime(i))
        {
            printf("%i\n", i);
        }
    }
}

bool prime(int number)
{
    // TODO
    if ((number % 2 != 0) && (number % 3 != 0) && (number % 5 != 0) && (number != 1))
        // If the num is not evenly divisible by these 3, and if the num is not one, is prime...
    {
        return true;
    }
    else if (number == 2 || number == 3 || number == 5)
        //  Except if the num actually is 2, 3, or 5, is also prime.
    {
        return true;
    }
    else
    {
        return false;
    }
}
