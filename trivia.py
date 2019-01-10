#andrew kellmer trivia project
import sys

def open_file(file_name, mode):
    #open a file
    
    try:
        the_file = open(file_name, mode)
        
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n",e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
        
    else:
        return the_file

def next_line(the_file):
    #read a line to a variable
    
    line = the_file.readline()
    line = line.replace("/","\n")
    
    return line

def next_block(the_file):
    #sets up the catagory, question, and answers
    
    category = next_line(the_file)
    question = next_line(the_file)
    answer_list = []
    
    for i in range(4):
        answer = next_line(the_file)
        answer_list.append(answer)

    correct_answer = next_line(the_file)
    
    if correct_answer:
        correct = correct_answer[0]
    else:
        correct = ""
        
    explanation = next_line(the_file)
    
    return category, question, answer_list, correct, explanation

def welcome(title):
    #welcome and prints title
    print("\t\tWelcome to Trivia Challenge!\n")
    print("\t\t", title,"\n")

def main():
    #the main of the function
    
    the_file = open_file("trivia.txt","r")
    title = next_line(the_file)
    welcome(title)
    score = 0
    category, question, answer_list, correct, explanation = next_block(the_file)

    while category:
        print(category)
        print(question)
        
        for i in range(4):
            print(answer_list[i])

        answer_input = input("enter a number 1-4 to answer the question")

        if answer_input == correct:
            print("\nwell done you have guessed correctly.")
            score += 1

        else:
            print("\nyou guessed wrong")

        print(explanation)
        input("press enter to continue")
        category, question, answer_list, correct, explanation = next_block(the_file)

    the_file.close()
    print("\nwell done. you have earned a score of:")
    print(score,"/ 10")
    input("press enter three times to end the test")
    input("press enter two times to end the test")
    input("press enter one time to end the test")

main()
