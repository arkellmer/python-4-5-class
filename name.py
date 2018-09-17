
#andrew kellmer 9/13/18

#get a users name

def get_name():
    
#step one ask user for name

    name = input("whats your name")    

#step two display name back

    print("the name you entered was",name)

#step three verify the name is correct

    input("is this the correct name y/n")

#call the function

get_name()










#calculate the area of a circle
#radius*radius*pi

def areaOfCircle():
    pi = 3.14159

#step one ask for radius

    radius = input("what is the radius ")

#convert the string to an int

    radius = int(radius)

#step two calculate the area

    area = radius*radius*pi
    
#display the area

    print ("the area is",area)

#call the function

areaOfCircle()
