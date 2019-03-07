#andrew kellmer 3/19 gofish
#2-4 players play against each other

#imports
import cards, games

#classes
class GF_Deck(cards.Deck):
    """sets up the deck and allows it to populate, and shuffle"""

    def populate(self):
        for suit in cards.Card.SUITS:
            for rank in cards.Card.RANKS:
                self.cards.append(cards.Card(rank, suit))

class GF_Hand(cards.Hand):
    """sets up the hands and names them. also allows printing the cards in your hand"""

    def __init__(self, name):
        self.name = name

#*****************make deal and check if this works (display)***************
    def __str__(self):
        for i in len(self):
            rep = rep + GF_Hand[i] + " "
        return rep

#destroys a pair of cards
    def discard(self):
        pass

    @property
    def pair(self):
        for card in self.cards:
            for i in self.cards:
                pass
                #checks all other cards in your hand if it is matching.

        return points >= 5

class GF_Player(GF_Hand):
    """sets up a player and allows them to hold cards"""
    pass

class GF_Field(object):
    """ allows us to play the game and let the player to try and take a persons card or go fish"""

    def __init__(self, names):
        self.players = []

        for name in names:
            player = GF_Player(name)
            self.players.append(player)

        self.deck = GF_Deck()
        self.deck.populate()
        self.deck.shuffle()

    def play(self):
        #aka steal or take a card from a player
        pass

    def turn(self):
        pass

    def draw(self):
        pass

    def win(self):
        pass

#main which runs the program
def main():

    print("Welcome to Go Fish!")
    names = []
    number = games.ask_num("How many players? (2-4) ", low=2, high=5)

    for i in range(number):
        name = input("Enter a name: ")
        names.append(name)










deck = GF_Deck()
deck.populate()
print(deck)
hand = GF_Hand
print(hand.__str__(GF_Hand))