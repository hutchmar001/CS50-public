# TODO
import cs50
import math

def get_cents():
    try:
        cents = int(input("Please enter a postive amount.\n"))
    except ValueError:
        get_cents()
    if cents < 0:
        get_cents()


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


def calculate_quarters(c):
    global q
    q = int(math.floor(cents / 25))


def calculate_dimes(c):
    global d
    d = int(math.floor(cents / 10))


def calculate_nickels(c):
    global n
    n = int(math.floor(cents / 5))


def calculate_pennies(c):
    global p
    p = int(math.floor(cents))


main()
