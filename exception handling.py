#Nicholaus
#exception handling





##try:
##    num = float(input("Enter a number: "))
##except:
##    print("Only Numbers")
##try:
##    print(num)
##except:
##    print("Nothing to print")



##while True:
##    try:
##        num = float(input("Enter a number: "))
##        break
##    except:
##        print("Numbers Only!")




##try:
##    num = float(input("Enter a number: "))
##except ValueError:
##    print("Numbers Only!")
##except NameError:
##    print("name error")

##for value in (None,"Hi!"):
##    try:
##        print("Attempting to convert",value,"-->",end=" ")
##        print(float(value))
##    except (TypeError):
##        print("Something went wrong! type error")
##    except (ValueError):
##        print("Something went wrong! value error")


##try:
##    num = float(input("\nEnter a number: "))
##except ValueError as e:
##    print("That was not a number! Or as Python would say: ")
##    print(e)



try:
    num = float(input("\nEnter a number: "))
except ValueError:
    print("That was not a number!")
else:
    print("you entered the number",num)
