# TODO
import cs50

height = int(input("Please enter an integer.\n"))

def main():
    while height not in range(1, 9):
        input("Please enter an integer.\n")
    for h in range (1, height):
        for j in range (1, height):
            print(" ")
        for k in range (0, h):
            print("#")
        print("\n")


main()

