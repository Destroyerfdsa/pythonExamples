def main():

    inputs(operation)
    det_op()
    check()
    print_ans()
    restart_fn()

def restart_fn():
    restart = input("restart?y/n: ")

    if restart == "y":
        main()
    elif restart == "n":
        print("thx bye")
    else:
        print("INVALID")
        restart_fn()

def inputs(operation):
    num1 = int(input("enter num1"))
    operation = input("enter +,-,*,/, or %")
    num2 = int(input("enter a number"))

def det_op():
    if operation == "+":
        add()
    elif operation == "-":
        subtract()
    elif operation == "*":
        multiply()
    elif operation == "/":
        divide()
    elif operation == "%":
        modulus()

def add(num1,num2):
    answer = num1+num2
    return answer

def subtract(num1,num2):
    answer = num1+num2
    return answer


def multiply(num1,num2):
    answer = num1+num2
    return answer


def divide(num1,num2):
    if num1 or num2:
        print("cannot divide by 0")
    else:
        answer = num1+num2
        return answer


def modulus(num1,num2):
    answer = num1+num2
    return answer


def check(num1,num2,operation,answer):
    if operation == "+":
        answer2 = add()
    elif operation == "-":
        answer2 = subtract()
    elif operation == "*":
        answer2 = multiply()
    elif operation == "/":
        answer2 = divide()
    elif operation == "%":
        answer2 = modulus()
    if answer2 == answer:
        check1 = True
    elif answer2 != answer:
        check1 = False


main()
