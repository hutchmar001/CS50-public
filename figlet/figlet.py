import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
n = len(sys.argv)
fontlist = figlet.getFonts()

def checkargcount():
    if(n == 1):
        {
            getinput(),
            randomfont()
        }
    elif(n == 3):
        {
            checkusage(),
            getinput(),
            specfont()
        }
    else:
        {
            print("Invalid usage"),
            sys.exit(1)
        }

def checkusage():
    if(sys.argv[1] != "-f" and sys.argv[1] != "--font"):
        {
            print("Invalid usage"),
            sys.exit(1)
        }
    for i in fontlist:
        if(sys.argv[2] == i):
            return
    print("Invalid usage")
    sys.exit(1)

def randomfont():
    figlet.setFont(font=random.choice(fontlist))

def specfont():
    figlet.setFont(font=sys.argv[2])

def getinput():
    global x
    x = input("Input: ")

checkargcount()
print(figlet.renderText(x))




