import sys
from pyfiglet import Figlet

figlet = Figlet()
n = len(sys.argv)

def checkusage():
    if(n == 1):
        {
            print("random")
        }
    elif(n == 3):
        {
            print("specific")
        }
    elif(argv[0] != "-f" or argv[0] != "--font")
    else:
        {
            print("Invalid usage"),
            sys.exit(0)
        }


checkusage()



