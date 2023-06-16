# TODO
import cs50

try:
    height = int(input("Please enter an integer.\n"))
except ValueError or :
    print("Please enter a valid integer.")

def main():
    while height not in range(1, 9):
        input("Please enter an integer.\n")
    for h in range (0, height):
        for j in range (1, height - h):
            print(" ", end='')
        for k in range (0, h + 1):
            print("#", end='')
        print("\n")


main()

