# TODO
import cs50
import math

def get_cents():
    try:
        cents = float(input("Please enter a postive amount.\n"))
    except ValueError:
        get_cents()
    if cents < 0:
        get_cents()
    return cents


def main():
    global cents
    cents = get_cents()

    calculate_quarters(cents)
    cents = cents - q * 25

    calculate_dimes(cents)
    cents = cents - d * 10

    calculate_nickels(cents)
    cents = cents - n * 5

    calculate_pennies(cents)
    cents = cents - p

    coins = q + d + n + p
    print(coins)


def calculate_quarters(cents):
    global q
    q = int(cents / 25.00)


def calculate_dimes(cents):
    global d
    d = int(cents / 10.00)


def calculate_nickels(cents):
    global n
    n = int(cents / 5.00)


def calculate_pennies(cents):
    global p
    p = int(cents)


main()
