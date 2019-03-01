class Critter(object):
    """a virtual pet"""
    def __init__(self, name, hunger, boredom):
        print("A new critter has been born!")
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self,add):
        self.hunger += 1+add
        self.boredom += 1+add

    def talk(self):
        print("\nHi, I'm,", self.__name,".")
        print("My mood is", self.mood)
        self.__pass_time(1)

    def play(self):
        print("You play with your pet.")
        fun = int(input("how long will you play with your pet?"))
        boredom = self.boredom - fun
        if boredom <= 0:
            self.boredom = 0
        add = fun
        self.__pass_time(add)

    def eat(self):
        print("You feed your pet.")
        food = int(input("How much will you feed your pet?"))
        hunger = self.hunger - food
        if hunger <= 0:
            self.hunger = 0
        add = food
        self.__pass_time(add)

    @property
    def mood(self):
        unhappiness = self.boredom+self.hunger
        if unhappiness <5:
            mood = "Happy"
        elif 5<=unhappiness<=10:
            mood = "Okay"
        elif 11<=unhappiness<=15:
            mood = "Frustrated"
        else:
            mood = "Angry"
        return mood

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("A critter's name can't be the empty string.")
        else:
            self.__name = new_name
            print("Name change successful.")

def main():
    name = input("Enter a name for your critter:")
    hunger = 0
    boredom = 0
    crit = Critter(name, hunger, boredom)
    choice = None
    while choice != "0":
        print("\nChoose:\n0 to exit\n1 to talk\n2 to eat\n3 to play")
        choice = input()
        if choice == "0":
            print("goodbye")
            break
        elif choice == "1":
            crit.talk()
        elif choice == "2":
            crit.eat()
        elif choice == "3":
            crit.play()
        else:
            print("That was not a valid input.")

main()



#crit = Critter("Poochie")
#mood = crit.mood()
#crit.talk(mood)


#print("\nMy critter's name is:", end= " ")
#print(crit.name)

#print("\nAttempting to change my critter's name to Randolph...")
#crit.name = "Randolph"