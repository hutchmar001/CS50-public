# TODO
import cs50

def get_cents():
    global cents
    try:
        cents = int(input("Please enter a postive amount.\n"))
    except ValueError:
        get_cents()
    if height < 0:
        get_cents()


def calculate_quarters(cents):
    global q
    q = int(floor(cents / 25))


def calculate_dimes(cents):
    global d
    d = int(floor(cents / 10))


def calculate_nickels(cents):
    global n
    n = int(floor(cents / 5))


def calculate_pennies(cents):
    global p
    p = int(floor(cents))


def main():
    
