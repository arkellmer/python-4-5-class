##word = input("enter a word")
##print("\nHere's each letter in your word:")
##for letter in word:
##    print(letter)
##print(len(word))
##
##message = input ("Enter a message")
##new_message =""
##VOWELS = "aeiouy"
##
##for letter in message:
##    if letter.lower() not in VOWELS:
##        new_message += letter
##        print("A new string has been created:", new_message)
##
##print("\nYour message without vowels", new_message)


print("counting:")
for i in range(10):
    print(i, end=" ")

print("\n\nCounting by fives:")
for i in range(0,50,5):
    print(i, end=" ")

print("\n\nCounting backwards:")
for i in range(10,0,-1):
    print(i, end=" ")