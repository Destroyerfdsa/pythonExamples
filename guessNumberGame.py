#requirements
#game choose random number 1-100
#5 attempts
#win/lose condition
#menu play,credits,quit
#advanced option - option menu

#output - menu, explaining what the game is, telling you to guess, or to use advanced options, or credits.
#input - numbers guessed, if put a non-number.





global attempts
global maxTries
global intRange
attempts = 0
maxTries = 5
intRange = "1-100"


def menu():
    while True:
        print("This is a number guessing game.")
        start = input("Would you like to play? [play, credits, or quit]")
        if start.lower() == "play":
            custom = input("Do you want to create your own parameters for the game? y/n")
            if custom.lower() == "y":
                return options()
            if custom.lower == "n":
                return play()
        if start.lower() == "credits":
                return credits()
        if start.lower() == "quit":
            input("Press enter to quit")
            exit()
        else:
            print("Invalid Option")
            
def options():
    print("Max Tries is",maxTries+".")
    print("Range is",intRange+".")
    yn = input("Do you want to change max tries? [y/n]: ")
    if yn.lower() == "y":
        maxTries = input("Enter new Max tries: ")
    elif yn.lower() == "n":

        yn = input("Do you want to change range? [y/n]: ")
        if yn.lower() == "y":
            tempRange = input("'1-100' or ‘1-200' or ‘1-300'")
            if tempRange == "1-100":
                intRange = "1-100"
                print("range changed to 1-100")
            
            elif tempRange == "1-200":
                intRange = "1-200"
                print("range changed to 1-200")
            
            elif tempRange == "1-300":
                intRange = "1-300"
                print("range changed to 1-300")
            
            else:
                print("I don't know what you mean")
        else:
            print("i dont know what that means")
menu()
