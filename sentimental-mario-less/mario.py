# TODO
import cs50


def get_input():
    global height
    try:
        height = int(input("Please enter an integer betwen 1 and 8.\n"))
    except ValueError:
        get_input()
    if height not in range(1, 9):
        get_input()

def main():
    for h in range (0, height):
        for j in range (1, height - h):
            print(" ", end='')
        for k in range (0, h + 1):
            print("#", end='')
        print("\n")

get_input()
main()

