import sys
from pyfiglet import Figlet

figlet = Figlet()
n = len(sys.argv)
fontlist = figlet.getFonts()

def checkfont():
    for i in fontlist:
        if(sys.argv[2] == i):
            print("valid")
    print("Invalid usage")
    sys.exit(0)

def checkusage():
    if(n == 1):
        {
            print("random")
        }
    elif(sys.argv[1] != "-f" and sys.argv[1] != "--font"):
        {
            print("Invalid usage"),
            sys.exit(0)
        }
    elif(n == 3):
        {
            print("specific")
        }
    else:
        {
            print("Invalid usage"),
            sys.exit(0)
        }

checkfont()
checkusage()




