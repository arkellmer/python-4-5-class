#andrew kellmer 10/10/18
#adventure quest with 20 choices

room = "room1"
big_map = False
lamp = False
matches = False
small_key = False
medium_key = False
large_key = False
chest = False
basement = False
lit_lamp = False


##################################################################################################################################
    
def action():
    action1 = input("Enter an action: ").lower()

    if action1 == "grab":
        grab(room, big_map, lamp, matches, small_key, medium_key, large_key)
        
    elif action1 == "move":
        move(basement, lit_lamp)

    elif action1 == "look":
        look(room)
        
    elif action1 == "inv" or action1 == "inventory":
        inv(big_map, lamp, matches, small_key, medium_key, large_key)
        
    elif action1 == "map":
        map1(big_map)
        
    elif action1 == "use":
        use(lamp, matches, small_key, medium_key, large_key, lit_lamp, room, basement, chest)

    elif action1 == "escape":
        escape(room, large_key)

    elif action1 == "restart":
        restart()

    elif action1 == "help":
        help1()

    else:
        print("The value you entered was not recognized. type 'help' for the help page.")
        action()

#################################################################################################################################

def grab(room, big_map, lamp, matches, small_key, medium_key, large_key):
    item = input("enter the item you wish to grab: ").lower()
    
    if item == "big map" or item == "map":
        
        if room == "room3":
            
            if big_map == False:
                print("you picked up the big map")
                big_map = True
                action()
                
            elif big_map == True:
                print("you already have that")
                action()
                
        else:
            print("you are not in the correct room")
            action()
            
    if item == "lamp":
        
        if room == "room1":
                
            if lamp == False:
                print("you picked up the lamp")
                lamp1 = True
                return lamp1
                action()
                
            elif lamp == True:
                print("you already have that")
                action()
                
        else:
            print("you are not in the correct room")
            action()
            
    if item == "matches":
        
        if room == "room2":
                
            if matches == False:
                print("you picked up the matches")
                matches = True
                action()
                
            elif matches == True:
                print("you already have that")
                action()
                
        else:
            print("you are not in the correct room")
            action()
            
    if item == "small key":
        
        if room == "attic2":
                
            if small_key == False:
                print("you picked up the small key")
                small_key = True
                action()
                
            elif small_key == True:
                print("you already have that")
                action()
                
        else:
            print("you are not in the correct room")
            action()
            
    if item == "medium key":
        
        if room == "room3":
                
            if medium_key == False:
                print("you picked up the medium key")
                medium_key = True
                action()
                
            elif medium_key == True:
                print("you already have that")
                action()
                
        else:
            print("you are not in the correct room")
            action()
                
            
    if item == "relic":
        if room == "basement":
            print("you picked up the relic")
            print("you feel an ominous presence")
            print("you have died.")
            restart()
                
        else:
            print("you are not in the correct room")
            action()
            
##################################################################################################################################
            
def move(basement, lit_lamp):
    rc = input("which room do you want to move to? ").lower()

    if rc == "basement":
    
        if basement == True:
            room = "basement"
            look(room)
            action()

        elif basement == False:
            print("the basement is not unlocked. you need a medium key")
            action()

    elif rc == "room1" or rc == "room 1":
        room = "room1"
        look(room)
        action()

    elif rc == "room2" or rc == "room 2":
        room = "room2"
        look(room)
        action()

    elif rc == "room3" or rc == "room 3":
        room = "room3"
        look(room)
        action()

    elif rc == "room4" or rc == "room 4":
        room = "room4"
        look(room)
        action()

    elif rc == "attic1" or rc == "attic 1":

        if lit_lamp == True:
            room = "attic1"
            look(room)
            action()

        elif lit_lamp == False:
            print("the attic is too dark to enter. you need a lamp.")
            action()

    elif rc == "attic2" or rc == "attic 2":
        
        if lit_lamp == True:
            room = "attic2"
            look(room)
            action()

        elif lit_lamp == False:
            print("the attic is too dark to enter. you need a lamp.")
            action()
        
##################################################################################################################################

def look(room):

    if room == "room1":
        print("You are in room 1. There is an unlit lamp in the corner.")
        action()
        
    elif room == "room2":
        print("You are in room 2. There are some matches on a table.")
        action()
        
    elif room == "room3":
        print("You are in room 3. There is a large map here.")
        action()
        
    elif room == "room4":
        print("You are in room 4. There is a chest in here.")
        action()
        
    elif room == "attic1":
        print("You are in attic 1. There is a large locked window.")
        action()
        
    elif room == "attic2":
        print("You are in attic 2. There is a small key on the floor.")
        action()
        
    elif room == "basement1":
        print("you are in the basement. You feel an ominous precence. There is a large relic in the middle of the room.")
        action()
        
##################################################################################################################################

def inv(big_map, lamp, matches, small_key, medium_key, large_key):

    if big_map == True:
        print("You have the big map.")

    if lamp == True:
        print("You have the lamp.")

    if matches == True:
        print("You have the matches.")

    if small_key == True:
        print("You have the small key.")

    if medium_key == True:
        print("You have the medium key.")

    if large_key == True:
        print("You have the large key.")

    else:
        print("You have no items.")

    action()

##################################################################################################################################
    
def map1(big_map):
    if big_map == False:
        print("""
 _____________     _____________
|             |   |             |
|   room 1    |---|   room 2    |
|                               |
|             |---|             |
|_____    ____|   |_____    ____| 
      |  |              |  |
      |  |              |  |
 _____|  |____     _____|  |____
|             |   |             |
|   room 3    |---|   room 4    |
|                               |
|             |---|             |
|_____________|   |_____________|
""")
        action()
        
    elif big_map == True:
        print("""
                 _____________     _____________     _____________
                |             |   |             |   |             |
                |   room 1    |---|   room 2    |---|  attic 1    |
                |                                ->               |
                |             |---|             |---|             |
                |_____    ____|   |_____    ____|   |_____    ____|
                      |  |              |  |              |  |
                      |  |              |  |              |  |
 ___________     _____|  |____     _____|  |____     _____|  |____
|           |   |             |   |             |   |             |
|  basement |---|   room 3    |---|   room 4    |---|  attic 2    |
|             <-                                 ->               |
|           |---|             |---|             |---|             |
|___________|   |_____________|   |_____________|   |_____________|
""")
        action()

##################################################################################################################################
    
def use(lamp, matches, small_key, medium_key, large_key, lit_lamp, room, basement, chest):
    useans = input("what would you like to use? ").lower()

    if useans == "lamp" or useans == "matches":
        if lamp == True and matches == True:
            lit_lamp = True
            print("you lit your lamp.")
            action()
        elif lamp == False or matches == False:
            print("you do not have the lamp OR matches.")
            action()

    if useans == "small key":
        if small_key == True and room == "room4" and chest == False:
            print("you open the chest. inside is a large key. you take it.")
            large_key = True
            chest = True
            action()
        elif small_key == False or room != "room4" or chest == True:
            print("you are not in the correct room or do not have the small key or have already unlocked the chest.")
            action()

    if useans == "medium key":
        if medium_key == True and room == "room3":
            print("you open the door to the basement.")
            basement = True
            action()
        elif medium_key == False or room != "room3":
            print("you are not in the correct room or do not have the medium key.")
            action()
        


##################################################################################################################################
    
def escape(room, large_key):
    if room == "attic1":

        if large_key == True:
            print("you use the large key to unlock the window. you climb out the window and escape.")
            print("you win!!")
            restart()
            
        elif large_key == False:
            print("the window is locked. you need a large key to unlock it")
            action()            

    elif room != "attic1":
        print("you are not in the correct room.")
        action()
        
##################################################################################################################################

def restart():
    ryn = input("would you like to restart or quit? y/n or quit: ").lower()
    if ryn == "y" or ryn == "yes":
        main()
    elif ryn == "n" or run == "no":
        action()
    elif ryn == "quit":
        print("you have quit the game.")
    else:
        print("The value you entered was not recognized.")
        action()
    
##################################################################################################################################
        
def help1():
    print("actions that are acceptable are 'grab', 'move', 'look', 'inv', 'inventory', 'map', 'use', 'escape', 'restart', and 'help'")
    action()

##################################################################################################################################
def main():
    print("you are in a room by yourself.")
    help1()
    room = "room1"
    big_map = False
    lamp = False
    matches = False
    small_key = False
    medium_key = False
    large_key = False
    chest = False
    basement = False
    lit_lamp = False
    action()
    
main()

##functions that return values
##use
##grab
##move
    


    
