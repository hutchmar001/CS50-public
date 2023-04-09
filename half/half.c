// Calculate your half of a restaurant bill
// Data types, operations, type casting, return value

#include <cs50.h>
#include <stdio.h>

float half(float bill, float tax, int tip);

int main(void)
{
    float bill_amount = get_float("Bill before tax and tip: ");
    float tax_percent = get_float("Sale Tax Percent: ");
    int tip_percent = get_int("Tip percent: ");

    printf("You will owe $%.2f each!\n", half(bill_amount, tax_percent, tip_percent));
}

// TODO: Complete the function
float half(float bill, float tax, int tip)
{
    float tax_float = tax * .01;
    float tip_float = (float)tip * .01;
    float tax_total = tax_float * bill;
    float subtotal = (bill + tax_total);
    float tip_total = tip_float * subtotal;
    float total = (subtotal + tip_total) / 2;
    return total;
}
