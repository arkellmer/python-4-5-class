#andrew kellmer 10/10/18
#adventure quest with 20 choices


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
    relic = False
    chest = False
    basement = False
    
    action()

def action():
    action1 = input("Enter an action: ").lower()

    if action1 == "grab":
        grab(room, big_map, lamp, matches, small_key, medium_key, large_key, relic, chest)
    elif action1 == "unlock":

    elif action1 == "move":

    elif action1 == "look":

    elif action1 == "inv" or action1 == "inventory":

    elif action1 == "map":

    elif action1 == "use":

    elif action1 == "escape":

    elif action1 == "restart":
        restart()

    elif action1 == "help":
        help1()

    else:
        print("The value you entered was not recognized. type 'help' for the help page.")
        action()
        
def grab(room, big_map, lamp, matches, small_key, medium_key, large_key, relic, chest):
    item = input("enter the item you wish to grab: ").lower()
    
    if item == "big map" or item == "map":
        if room == "room3":
            if big_map == False:
                

            elif big_map == True:
        else:
            print("you are not in the correct room")
            
    if item == "lamp":
        if room == "room1":
        else:
            print("you are not in the correct room")
            break
            
    if item == "matches":
        if room == "room2":
        else:
            print("you are not in the correct room")
            break
            
    if item == "small key":
        if room == "attic2":
        else:
            print("you are not in the correct room")
            break
            
    if item == "medium key":
        if room == "room3":
        else:
            print("you are not in the correct room")
            break
            
    if item == "large key":
        if room == "room4":
        else:
            print("you are not in the correct room")
            break
            
    if item == "relic":
        if room == "basement":
        else:
            print("you are not in the correct room")
            break
            
    
def unlock():

def move():

def look():

def inv():

def map():

def use():

def escape():

def restart():
    ryn = input("would you like to restart? y/n: ").lower()
    if ryn == "y" or ryn == "yes":
        main()
    elif ryn == "n" or run == "no":
        action()
    else:
        print("The value you entered was not recognized. type 'help' for the help page.")
        action()
    
def help():
    print("actions that are acceptable are 'grab', 'unlock', 'move', 'look', 'inv', 'inventory', 'map', 'use', 'escape', 'restart', and 'help'")
    action()
    


    
