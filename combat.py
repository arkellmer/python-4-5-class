#andrew kellmer 10/12/18
#combat system

import random

win = 0
p_health = 100
m_health = 100

print("your lone hero is surrounded by a massive army of trolls.")
print("their decaying green bodies stretch out, melting into the horizon.")
print("your hero unsheathes his sword for the last fight of his life.\n")

choice = input ("fight or run")

while choice == "fight":
    if p_health > 0:
        p_damage = random.randrange(0,31)
        print("you attack the troll for", p_damage,"damage")
        m_health -= p_damage
    
    if  m_health > 0:
        m_damage = random.randrange(0,51)
        print ("the troll attacks you for", m_damage,"damage")
        p_health -= m_damage

    if p_health <= 0:
        print("you have died")
        win = 0
        break
    
    elif m_health <= 0 :
        print("you killed the troll")
        win = 1
        break
    
    elif p_health > 0 and m_health > 0:
        print("you have", p_health, "health")
        print("the trolls have", m_health, "health")
        
        choice = input("fight or run")
        if choice == "fight":
            print("you attack again")

        elif choice == "run":
            break


if choice == "run":
    print("you are a coward")

if win == 1:
    print("you won")

elif win == 0:
    print("you lost")



        
