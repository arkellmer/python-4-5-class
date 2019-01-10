#deck andrew kellmer 12/6/18

import random


deck = []
player1_hand = []
player2_hand =[]

def makedeck(deck):
    """ populate the deck of cards """
    SUITS = ["Hearts","Diamonds","Clubs","Spades"]
    VALUES = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    for e in SUITS:
        for i in VALUES:
            card = i+" of "+e
            deck.append(card)

def shuffledeck(deck):
    for i in range(len(deck)):
        j = random.randrange(len(deck))
        temp = deck[i]
        deck[i] = deck[j]
        deck[j] = temp

def dealcard(deck,player1_hand,player2_hand):
    for i in range(5):
        card = deck.pop()
        player1_hand.append(card)
        card = deck.pop()
        player2_hand.append(card)


        
        

makedeck(deck)

print(deck)
print()
print()
print()
print(len(deck))
print()
print()
print()
shuffledeck(deck)
print(deck)
print()
print()
print()
dealcard(deck,player1_hand,player2_hand)
print(player1_hand)
print()
print(player2_hand)
