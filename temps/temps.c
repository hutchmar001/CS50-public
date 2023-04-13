// Practice working with structs
// Practice applying sorting algorithms

#include <cs50.h>
#include <stdio.h>

#define NUM_CITIES 11

typedef struct
{
    string city;
    int temp;
    bool elim;
}
avg_temp;

avg_temp temps[NUM_CITIES];
avg_temp temporary[1];

void sort_cities(void);

int main(void)
{
    temps[0].city = "Austin";
    temps[0].temp = 97;

    temps[1].city = "Boston";
    temps[1].temp = 82;

    temps[2].city = "Chicago";
    temps[2].temp = 85;

    temps[3].city = "Denver";
    temps[3].temp = 90;

    temps[4].city = "Las Vegas";
    temps[4].temp = 105;

    temps[5].city = "Los Angeles";
    temps[5].temp = 82;

    temps[6].city = "Miami";
    temps[6].temp = 97;

    temps[7].city = "New York";
    temps[7].temp = 85;

    temps[8].city = "Phoenix";
    temps[8].temp = 107;

    temps[9].city = "San Francisco";
    temps[9].temp = 66;

    temporary[0].city = "0";
    temporary[0].temp = 0;

    sort_cities();

    printf("\nAverage July Temperatures by City\n\n");

    for (int i = 0; i < NUM_CITIES; i++)
    {
        printf("%s: %i\n", temps[i].city, temps[i].temp);
    }
}

// TODO: Sort cities by temperature in descending order
void sort_cities(void)
{
        // Bubble sort for sorting list of ints
        for (int j = 0; j < NUM_CITIES; j++)
    {
        for (int k = 0; k < NUM_CITIES; k++)
        {
        if (temps[k].temp < temps[k + 1].temp)
            {
                temporary[0] = temps[k];
                temps[k] = temps[k + 1];
                temps[k + 1] = temporary[0];
            }
    }
}
}
