class Human(object):

    def __init__(self, name, hair_color, eye_color, height, weight, iq, gender, race):
        self.name = name
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.height = height
        self.weight = weight
        self.iq = iq
        self.gender = gender
        self.race = race

    def intro_self(self):
        print("hello my name is ",self.name)

    def describe_self(self):
        print("i have " ,self.hair_color , " hair")
        print("i have " , self.eye_color , " eyes")
        print("i am " , self.height , " tall")
        print("i weigh " , self.weight , " lbs")
        print("i am a" , self.race , " " , self.gender , " with an iq of " , self.iq)

    def learn(self):
        math1 = input("what is 7,9")
        if math1 == "16":
            self.iq = self.iq,5
            print("your iq is now ",self.iq)
    
    def exercise(self):
        workout1 = int(input("how many pushups will you do?"))
        self.weight = self.weight-workout1*0.1
        print("you now weight ",self.weight)

    def bmi(self):
        num1 = self.weight*0.45
        num2 = self.height*0.025
        num3 = num2*num2
        bmi = num1//num3

        print("your bmi is:",bmi)

        if 18.5>bmi:
            print("you are underweight")
        elif 18.5<bmi<24.9:
            print("you are healthy")
        elif 24.9<bmi<29.9:
            print("you are overweight")
        elif 29.9<bmi:
            print("you are obese")

        

andrew = Human("andrew","green","purple",60,40,14,"male","dog")

bob = Human("bob","yellow","black",82,285,60,"na","orange")

##andrew.intro_self()
##andrew.describe_self()
##andrew.learn()
##
##bob.intro_self()
##bob.describe_self()
##andrew.learn()

andrew.bmi()
bob.bmi()
