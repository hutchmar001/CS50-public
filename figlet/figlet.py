import sys
from pyfiglet import Figlet

figlet = Figlet()
n = len(sys.argv)
if(n == 1):
    {
        print("random")
    }
if(n == 3):
    {
        print("specific")
    }
