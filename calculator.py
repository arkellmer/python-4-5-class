#andrew kellmer, parker gowans, nicholaus whites 10/3/18

#calculator program


def main():

    
    num1, num2, operation = inputs()
    det_op()
    check()
    print_ans()
    restart_fn()


def restart_fn():
    restart = input("would you like to start another operation? y/n: ")
    
    if restart == "y":
        main()

    elif restart == "n":
        print ("thank you for using the calculator")

    else:
        print("the value you entered was incorrect")
        restart_fn()
    
def inputs():
        num1 = int(input("enter a number"))
        operation = input("enter +,-,*,/, or %")
        num2 = int(input("enter a number"))
        if operation == "+" or operation == "-" or operation == "*" or operation == "/" or operation == "%":
            return num1, num2, operation
        else:
            print("your operation does not work or is not a symbol")
            inputs()

def det_op(operation):
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
    answer = num1-num2
    return answer               

def multiply(num1,num2):
    answer = num1*num2
    return answer               

def divide(num1,num2):
    if num2 == 0:
        print("cannot divide by 0")
    else:
        answer = num1/num2
        return answer
                   
def modulus(num1,num2):
    if num2 == 0:
        print("cannot divide by 0")
    else:
        answer = num1%num2
        return answer

def check(num1,num2,operation, answer):
                   
    if operation == "+":
        answer2 = add()
    elif operation == "-":
        answer2 = subtract()
    elif operation == "*":
        answer2 = multiply()
    elif operation == "/":
        answer2 =  divide()
    elif operation == "%":
        answer2 = modulus()
    if answer2 == answer:
        check1 = True
    elif answer2 != answer:
        check1 = False
    
    



def print_ans():
    

main()


