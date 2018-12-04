#<Nicholaus Whites>
#<10/3/2018>
#<Calculator>



def main():
    oper()
    again()




def oper():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    operator = input("Enter an operator(*,/,+,-): ")
    if operator == "*":
        print("Multiplication")
        out=num1*num2
        print(out)
    elif operator == "/":
        print("Division")
        if num1 or num2 == 0:
            print("Cant divide by zero")
            oper()
        out=num1/num2
        print(out)
    elif operator == "+":
        print("Addition")
        out=num1+num2
        print(out)
    elif operator == "-":
        print("Subtraction")
        out=num1-num2
        print(out)
    else:
        print("Invalid option")
        oper()
    
def again():
    retry = input("again? yes/no: ")
    if retry == "yes":
        oper()
    else:
        exit()
    


main()
