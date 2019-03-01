import random

class Card(object):
    """a playing card
    this class will build a single card
    to build a card call Card() and pass in a rank and a suit
    allows us to flip cards
    card1 = Card(rank = "A", suit = "s")
    card.flip()
    """

    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["♤", "♥", "♧", "♦"]

    def __init__(self, rank, suit, face_up = True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = self.rank + self.suit
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up

class Hand(object):
    """a hand of playing cards
    allows you to clear your hand,
    give cards to others,
    and add cards to your hand
    my_hand.give(my_hand.cards[0], your_hand)
    my_hand.add(deck.pop())
    my_hand.clear()
    """

    def __init__(self):
        self.cards=[]

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card)+" "
        else:
            rep = "<empty>"
        return rep

    def clear(self):
        self.cards = []

    def add(self,card):
        self.cards.append(card)

    def give(self,card,other_hand):
        self.cards.remove(card)
        other_hand.add(card)

class Deck(Hand):
    """a deck to stache cards and to pull them from.
    allows you to shuffle,
    populate a deck,
    and to deal the deck
    deck.populate()
    deck.shuffle()
    deck.deal(hands,5)
    """

    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self,hands,per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Can't continue to deal. Out of cards!")

if __name__ == "__main__":
    print("You ran this module directly (and didnt import it).")
    input("\n\nPress the enter key to exit.")

