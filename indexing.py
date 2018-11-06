#andrew kellmer 11/6/19
import random
name = input("enter a name")
print(name[0])
length = len(name)
print(length)
index_pos = random.randrange(0,length)
if index_pos<=length:
    char = name[index_pos]
    print(char)
else:
    print("thats out of the range.")
