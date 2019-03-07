#andrew kellmer 3/19 gofish
#2-4 players play against each other

#imports
import cards, games

#classes
class GF_Deck(cards.Deck):

    def populate(self):
        for suit in cards.Card.SUITS:
            for rank in cards.Card.RANKS:
                self.cards.append(cards.Card(rank, suit))

class GF_Hand(cards.Hand):

    def __init__(self, name):
        self.name = name

#make deal and check if this works
    def __str__(self):
        for i in len(self):
            rep = rep + GF_Hand[i] + " "
        return rep

    @property
    def pair(self):
        for card in self.cards:
            for i in self.cards:
                #checks all other cards in your hand if it is matching.




deck = GF_Deck()
deck.populate()
print(deck)
hand = GF_Hand
print(hand.__str__(GF_Hand))