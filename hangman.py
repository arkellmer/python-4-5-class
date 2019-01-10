#hangman game
#andrew kellmer
#11/26/18

import random
import time

hangman = (
"""
________
|        |
|
|
|
|
|
|
|______
""",
"""
________
|        |
|       O
|
|
|
|
|
|______
""",
"""
________
|        |
|       O
|        |
|        |
|
|
|
|______
""",
"""
________
|        |
|       O
|     ---|
|        |
|
|
|
|______
""",
"""
________
|        |
|       O
|     ---|---
|        |
|
|
|
|______
""",
"""
________
|        |
|       O
|     ---|---
|        |
|       / 
|      /
|
|______
""",
"""
________
|        | 
|       O 
|     ---|--- 
|        | 
|       / \ 
|      /   \ 
|           
|______
""",)

max_wrong = len(hangman)-1
words = ("overused","clam","guam","taffeta","python")
word = random.choice(words) #the word to be guessed
so_far = "_"*len(word) #one dash for each letter
wrong = 0 #number of wrong guesses
used = [] #letters already guessed

def guess():
    global max_wrong
    global words
    global word
    global so_far
    global wrong
    global used
    while wrong < max_wrong and so_far != word:
       
        
        print(hangman[wrong])
        print("\nYou've used the following letters:\n", used)
        print("\nSo far, the word is:\n",so_far)

        guess = input("\n\nEnter your guess: ")
        guess = guess.lower()


        while guess in used:
            print("You've already used that letter")
            guess = input("Enter your guess: ")
            guess = guess.lower()

        used.append(guess)

        if guess in word:
            print("\nYes!", guess, "is in the word!")

            #create a new so_far to include guess
            new = ""
            for i in range(len(word)):
                if guess == word[i]:
                    new += guess
                else:
                    new += so_far[i]

            so_far = new

        else:
            print("\nSorry,", guess,"isnt in the word")
            wrong +=1
    

    if wrong == max_wrong:
        dead()

    else:
        win()
        
def dead():
    global wrong
    print(hangman[wrong])
    print("\nYou've been hanged")
    print("\nThe word was",word)
    input("\n\nPress the enter key to exit.")

def win():
    print("\nYou guessed it!")
    print("\nThe word was",word)
    input("\n\nPress the enter key to exit.")

guess()


                
                
    
        
    
