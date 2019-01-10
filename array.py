game_list = ["Overwatch",
             "Destiny 1",
             "Rainbow Six Siege",
             "Destiny 2",
             "LOZ: Twilight Princess",
             "Black Ops 2",
             "Minecraft",
             "Wii Sports",
             "Superhot",
             "Star Wars Battlefront 2"]
print(len(game_list))
num5game = game_list[4]
print(num5game)
middle5 = game_list[3:7]
print(middle5)
last4 = game_list[6:9]
print(last4)
evens = game_list[::2]
print(evens)
backward = game_list[::-1]
print(backward)
for i in game_list:
    print(i)
print(game_list)
game_list += ("11", 12, 13.0, 14, "15")
print(game_list)

game_list[0] = "Destiny 1"
game_list[1] = "Overwatch"
print(game_list)
