#Nicholaus Whites
#9/13
import math

#Get a users name
def get_name(name):
    input_name = name
    input_name=input_name.lower()
    input_name=input_name.title()

    print("You entered",name)
#step 3 verify name
    input("is this correct yes or no ")


print("This is our function")
#step one ask user for name
name=input("Enter your name: ")
#step two display name
get_name(name)









#calculate the area of a circle
#radius*radius*pi
def areaOfCircle():
    pi=3.141592653
#1 get a radius
    radius=input("Enter The Radius: ")
#2 calculate area
    radius = float(radius)
    area=radius*radius*pi
#3 display the area
    print("This is the area: ",area)

##areaOfCircle()

def build_sandich():
    x=input("Enter a thing to put on sandich: ")
    y=input("Enter second thing: ")
    print("You made a",x,"and",y,"sandich")
##build_sandich()

def pythagoras_theorem(ap=5,bp=5):
    a=float(ap)
    b=float(bp)
    c=a*a+b*b
    c=math.sqrt(c)

    print("The third side is",c)


#ai=input("Enter First Side of Triangle: ")
#bi=input("Enter Second Side of Triangle: ")
#pythagoras_theorem(3,4)


def add_nums(x,y):
    num1=x
    print("num1=x",num1)
    num2=y
    print("num2=y",num2)
    num3=int(num1)+int(num2)
    return num3

x=1   #input("Enter a number: ")
y=-9   #input("enter a num: ")
#num4 = add_nums(y,x)
print(num4)


































