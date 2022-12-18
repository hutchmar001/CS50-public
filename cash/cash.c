#include <stdio.h>
#include <math.h>
#include <cs50.h>

int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{
    // Ask how many cents the customer is owed
    int cents = get_cents();

    // Calculate the number of quarters to give the customer
    int quarters = calculate_quarters(cents);
    cents = cents - quarters * 25;

    // Calculate the number of dimes to give the customer
    int dimes = calculate_dimes(cents);
    cents = cents - dimes * 10;

    // Calculate the number of nickels to give the customer
    int nickels = calculate_nickels(cents);
    cents = cents - nickels * 5;

    // Calculate the number of pennies to give the customer
    int pennies = calculate_pennies(cents);
    cents = cents - pennies * 1;

    // Sum coins
    int coins = quarters + dimes + nickels + pennies;

    // Print total number of coins to give the customer
    printf("%i\n", coins);
}

int get_cents(void){
    printf("Please enter the amount of cents. ");
    int cents;
    scanf("%d", &cents);

    while (cents <= 0 || scanf("%d", &cents) !=1)
    {
        printf("Please enter the amount of cents. ");
        int c;
        while((c=getchar())!='\n' && c!=EOF);
        scanf("%d", &cents);
    }
    return cents;
}


int calculate_quarters(int cents)
{
    int q = (int)floor(cents/25);
    printf("%d\n", q);
    return q;
}

int calculate_dimes(int cents)
{
    int d = (int)floor(cents/10);
    printf("%d\n", d);
    return d;
}

int calculate_nickels(int cents)
{
    int n = (int)floor(cents/5);
    printf("%d\n", n);
    return n;
}

int calculate_pennies(int cents)
{
    int p = (int)floor(cents);
    printf("%d\n", p);
    return p;
}
