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

    quarters = calculate_quarters(cents)
    cents = cents - quarters * 25

    dimes = calculate_dimes(cents)
    cents = cents - dimes * 10

    nickels = calculate_nickels(cents)
    cents = cents - nickels * 5

    pennies = calculate_pennies(cents)
    cents = cents - pennies

    coins = q + d + n + p
    print(coins)


def calculate_quarters(cents):
    q = int(math.floor(cents / 25.00))
    return q


def calculate_dimes(cents):
    d = int(math.floor(cents / 10.00))
    return d


def calculate_nickels(cents):
    n = int(math.floor(cents / 5.00))
    return n


def calculate_pennies(cents):
    p = int(math.floor(cents))
    return p


main()
