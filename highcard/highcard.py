import games, cards

deck = cards.Deck()
deck.populate()
deck.shuffle()

print("welcome to the world's simplest game high card!\n")
again = None

while again != "n":
    players = []
    num = games.ask_num("How many players? (2-10):", 2, 10)

    for i in range(num):
        name = input("Player name: ")
        player = games.Player(name)
        players.append(player)

    hands = []

    for player in players:
        hand = player.hand
        hands.append(hand)

    deck.deal(hands,1)
    print("\nHere are the game results:")

    for player in players:
        print(player)

    flip = games.ask_yes_no("\nDo you want to flip the cards? (y/n)")

    if flip == "y":
        for player in players:

            print(card)

    again = games.ask_yes_no("\nDo you want to play again? (y/n):")

input("\n\nPress the enter key to exit.")
