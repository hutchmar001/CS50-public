import sys
from pyfiglet import Figlet

figlet = Figlet()
n = len(sys.argv)
fontlist = figlet.getFonts()

def checkusage():
    if(sys.argv[1] != "-f" and sys.argv[1] != "--font"):
        {
            print("Invalid usage"),
            sys.exit(0)
        }
    for i in fontlist:
        if(sys.argv[2] == i):
            return
    print("Invalid usage")
    sys.exit(0)

def checkargcount():
    if(n == 1):
        {
            print("random")
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

checkargcount()
checkusage()




