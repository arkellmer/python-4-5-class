import cards
def ask_num(question,low,high):
    """ask for a number within a range
    ask_num("how are you",1,2)
    """
    while True:
        try:
            response = int(input(question))
            if response in range(low, high):
                return response
            else:
                print("out of range")
        except:
            print("must be a number")

def ask_yes_no(question):
    """ask a yes or no question
    ask_yes_no("how are you")
    """
    response = None
    while response not in ("y","n"):
        response = input(question).lower()
    return response

def switch_turn(num_players,turn):
    """switches the player turns
    switch_turn(4,3)
    """
    turn += 1
    if turn == num_players:
        turn = 0

    return turn

def winner_grats(winner):
    """congrats the winner on winning
    winner_grats("billy")
    """
    if winner != None:
        print("CONGRATULATIONS!", winner,"WON THE GAME!")

    else:
        pass

def roll(die_low, die_high, die_count = 1):
    """rolls a die or 2 for movement or such
    roll(1,6,3)
    """
    roll = 0
    for i in range(die_count):
        roll += random.randrange(die_low,die_high+1)
        print("you rolled a:",roll)
    return roll

class Player(object):
    """a player for a game"""
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __str__(self):
        rep = self.name
        rep = rep + " "+str(self.score)
        return rep

if __name__ == "__main__":
    print("Your ran this module directly and didnt import it")
    input("\n\nPress enter to exit")