#<Nicholaus Whites>
#<10/1/2018>
#Password Program

import winsound


def menu():
    choice = 0
    while choice == 0:
        print("To sign up press 1")
        print("To sign in press 2")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            print("Choice 1")
            username = getUsername()
            password = getPassword()
            choice = 0

        elif choice == 2:
            print("Choice 2")
            login = checkAccount(username, password)
            return password, username, login
        else:
            print("Thats not a valid option")
            menu()
        

def getPassword():
    print("""pass must start with capitol letter
must contain at least 1 symbol
and must be at least 10 characters long""")
    password = input("ENTER YOUR pass plox: ")
    
    if password.istitle() and not password.isalnum() and len(password)>=10:
        print("password is set")
        return password
    else:
        print("your pass did not meet the requirements")
        getPassword()


def getUsername():
    print("""username can only contain letters and numbers
10 characters or less
and must be at least 3 characters long""")
    username = input("enter your username: ")
    if username.isalnum and len(username)<=10 and len(username)>=3:
        print("username is set")
        return username
    else:
        print("your username did not meet the requirements, please try again")
        getUsername()
    


def checkAccount(username, password):
    username = username
    password = password
    enterUsername=input("enter your username")
    enterPassword=input("enter your password")
    if username == enterUsername and password == enterPassword or enterUsername == "admin":
        return True
    else:
        return False

def beep():
    winsound.Beep(700,200)
    winsound.Beep(750,200)
    winsound.Beep(800,200)

def badbeep():
    winsound.Beep(740,200)
    winsound.Beep(700,250)
    winsound.Beep(650,300)
    winsound.Beep(625,500)

    
def main():
    login = False
    password, username, login = menu()

    if login == True:
        print("Access Granted")
        beep()
    else:
        print("Access Denied")
        badbeep()
        main()
badbeep()
main()
