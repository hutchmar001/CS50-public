import sys

menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
t = 0.00

class Counter(dict):
    def __missing__(self, key):
        return 0
c = Counter(menu)


while True:
    try:
        item = input("Please enter a food.\n")
        i = item.title()
        if i in c:
            t += c[i]
            print("Total: $", total)
    except EOFError:
        sys.exit(0)