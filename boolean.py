#andrew kellmer 9/27/18

#name = input("whats your name")
#age = input("how old are you")

#if name.isalpha() and age.isdigit() and name.istitle() and age<"20" and age>"15" or name == "Eric":
#    print("you're in")

#else:
#    print("you're not in")


age = int(input("how old are you"))

if age>=16 and age<=70:
    print("you are old enough to drive")

elif age>70:
    print("you are too old to drive")

elif age<15:
    print("you are too young to drive")
    
