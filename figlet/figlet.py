import sys
from pyfiglet import Figlet

figlet = Figlet()
n = len(sys.argv)
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
        print("Invalid usage")
        sys.exit()
    }

