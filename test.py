class Critter(object):
    total = 0
    
    def  __init__(self, name):
        print("a critter has been born")
        self.name = name
        Critter.total += 1

    def __str__(self):
        rep = self.name
        return rep

    @staticmethod
    def status():
        print("\nThe total number of critters is", Critter.total)

    def talk(self):
        print("hi im an instance of class critter. my name is "+self.name)

crit = Critter("bob")
crit2 = Critter("frank")
crit3 = Critter("jo")
obj = crit.__str__()
if obj == "bob":
    print("yes")
print(crit)
crit.talk()
print(crit2)
crit2.talk()
Critter.status()

