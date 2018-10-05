#andrew kellmer, parker gowans, nicholaus whites 10/3/18

#calculator program


def main():

    
    num1, num2, operation = inputs()
    answer = det_op(num1,num2,operation)
    check1 = check(num1,num2,operation,answer)
    if check1 == True:
        print("the work is checked")
    else:
        print("the work failed the check")
    print_ans(num1,num2,operation,answer)
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

def det_op(num1,num2,operation):
    if operation == "+":
        answer = add(num1,num2)
        print(answer)
    elif operation == "-":
        answer = subtract(num1,num2)
        print(answer)
    elif operation == "*":
        answer = multiply(num1,num2)
        print(answer)
    elif operation == "/":
        answer = divide(num1,num2)
        print(answer)
    elif operation == "%":
        answer = modulus(num1,num2)
        print(answer)
    return answer
                   
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
        answer2 = add(num1,num2)
    elif operation == "-":
        answer2 = subtract(num1,num2)
    elif operation == "*":
        answer2 = multiply(num1,num2)
    elif operation == "/":
        answer2 =  divide(num1,num2)
    elif operation == "%":
        answer2 = modulus(num1,num2)
    if answer2 == answer:
        check1 = True
    elif answer2 != answer:
        check1 = False
    return check1



def print_ans(num1,num2,operation,answer):
    print (num1,operation,num2,"=", answer)
    
    

main()


