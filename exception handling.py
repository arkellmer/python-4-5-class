##
##while True:
##    try:
##        num = float(input("enter a number:"))
##        break
##    except:
##        print("something went wrong!")
##
##try:
##    num = float(input("\nenter a number:"))
##except ValueError:
##    print("that was not a number")
##except NameError:
##    print("that was a name")
##
##for value in (None, "Hi!"):
##    try:
##        print("Attempting to convert", value, "-->", end = " ")
##        print(float(value))
##    except (TypeError):
##        print("type error")
##    except (ValueError):
##        print("value error")


##try:
##    num = float(input("enter a number"))
##except ValueError as e:
##    print("not a number")
##    print(e)

try:
    num = float(input("enter a number"))
except ValueError:
    print("not a number")
else:
    print("you entered a number")
    
