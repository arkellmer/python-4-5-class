##andrew kellmer 9/27/18
##
##psuedocode
##
##num1: input from the user;
##num2: input from the user;
##
##check numbers if num1 and num2 are all digits
##if both are digits tell the user
##if one or the other is a digit tell user
##if neither are digits tell the user



num1 = (input("enter a number"))
num2 = (input("enter a number"))

if num1.isdigit() and num2.isdigit():
    print("they are both digits")

elif num1.isdigit() or num2.isdigit():
    print("one is a digit")

else:
    print("they are not digits")



    
    
