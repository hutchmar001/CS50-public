x = input("Enter a greeting.\n")
greeting = x.lower()


def check(grtg):
    if (greeting == "hello"):
        {
            print("$0")
        }
    if (greeting == " hello "):
        {
            print("$0")
        }
    elif (greeting[:5] == "hello" and len(greeting) > 5):
        {
            print("$0")
        }
    elif (greeting[0] == "h" and greeting[1] != "e"):
        {
            print("$20")
        }
    else:
        {
            print("$100")
        }


check(greeting)