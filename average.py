#Average of Test scores
#9/17/2018=

def average_scores(num1, num2, num3, num4, num5, num6, num7, num8, num9, num10):

    num1=float(num1)
    num2=float(num2)
    num3=float(num3)
    num4=float(num4)
    num5=float(num5)
    num6=float(num6)
    num7=float(num7)
    num8=float(num8)
    num9=float(num9)
    num10=float(num10)
    average=num1+num2+num3+num4+num5+num6+num7+num8+num9+num10
    average=average/10
    print("The average is: ",average)

num1=input("Enter score: ")
num2=input("Enter score: ")
num3=input("Enter score: ")
num4=input("Enter score: ")
num5=input("Enter score: ")
num6=input("Enter score: ")
num7=input("Enter score: ")
num8=input("Enter score: ")
num9=input("Enter score: ")
num10=input("Enter score: ")


average_scores(num1, num2, num3, num4, num5, num6, num7, num8, num9, num10)
