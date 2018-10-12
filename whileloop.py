#andrew kellmer 10/12/18
#while loop

##loops = 1
##while True:
##    print("i have looped", loops,"times")
##    loops+=1
##
##count = 0
##while True:
##    count+=1
##    if count > 100:
##        break
##    if count == 5 or count == 25 or count == 50 or count == 75:
##        continue
##    print(count)
##        

print("your lone hero is surrounded by a massive army of trolls.")
print("their decaying green bodies stretch out, melting into the horizon.")
print("your hero unsheathes his sword for the last fight of his life.\n")

health = 10
trolls = 0
damage = 3

while health > 0:
    trolls += 1
    health -= damage
    print("your hero swings and defeats a troll,"\
          "but takes", damage, "damage points.\n")

print("your hero fought valiantly and defeated", trolls, "trolls.")
print("but alas, your hero is no more.")
