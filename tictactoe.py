#andrew kellmer
#12/10/18
#tic tac toe vs ai

#global constants
x = "X"
o = "O"
empty = " "
tie = "tie"
num_squares = 9

#functions
#########################################
def display_instructions():
    print("Welcome to the game of Tic-Tac-Toe")
    print("When prompted, enter a location for your mark. Win by having 3 marks lined in a row.")
    print("locations on the board are listed below.")
    print("""
0 | 1 | 2
-----------
3 | 4 | 5
-----------
6 | 7 | 8
""")
    print("Computer: Ha...Ha...Ha... Your foolish brain cannot handle my power. Try and best me if you can.")

####################################################
def ask_yes_no(question):
    #y/n question asker
    response = None
    while response != "y" and response != "n":
        response = input(question+" y or n:").lower()
    return response

#######################################################
def ask_num(question, low, high):
    #number guess
    response = "9999"
    while True:
        if response.isdigit():
            if int(response) in range(low, high):
                break
            else:
                response = input(question)
        else:
            print("you must enter a number")
            response = input(question)
    return int(response)

#########################################################
def pieces():
    #chooses who goes first
    go_first = ask_yes_no("Do you want to go first?")
    if go_first == "y":
        print("You will not win even with the advantage of first pick! Ha...Ha...Ha...")
        human = x
        computer = o

    elif go_first == "n":
        print("Ha...Ha...Ha... Time to crush you in glorious combat!")
        human = o
        computer = x
        
    return human, computer

#####################################################
def new_board():
    #creates a new board
    board = []

    for square in range(num_squares):
        board.append(empty)

    return board

######################################################
def display_board(board):
    #prints the current board
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "-----------")
    print("\n\t", board[3], "|", board[4], "|", board[5])
    print("\t", "-----------")
    print("\n\t", board[6], "|", board[7], "|", board[8], "\n")

#########################################################
def legal_moves(board):
    #creates list of legal moves
    
    moves = []
    for square in range(num_squares):
        if board[square] == empty:
            moves.append(square)

    return moves

###########################################################
def winner(board):
    #determines winner
    ways_to_win = (
        (0,1,2),
        (3,4,5),
        (6,7,8),
        (0,3,6),
        (1,4,7),
        (2,5,8),
        (0,4,8),
        (2,4,6)
        )
    for row in ways_to_win:
        if board[row[0]] == board[row[1]] == board[row[2]] != empty:
            winner = board[row[0]]
            return winner

    if empty not in board:
        return tie

    return None

###################################################################################

def human_move(board):
    #gets human move
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_num("Which box do you want to mark? 0-8 ", 0, num_squares)
        if move not in legal:
            print("Ha...Ha...Ha... You cannot place a marker there. You are so dumb. Ha...Ha...Ha...")
    return move

##################################################################################

def next_turn(turn):
    #switches turns
    if turn == x:
        return o
    else:
        return x

##############################################################################

def congrat_winner(the_winner, computer, human):
    if the_winner == tie:
        print("It is a tie.")
    else:
        print(the_winner,"won!")

    if the_winner == computer:
        print("Ha...Ha...Ha... You have been bested.")
    elif the_winner == human:
        print("I admit defeat. ha...ha...ha...")
    elif the_winner == tie:
        print("You have failed to win human, and that is a loss! Ha...Ha...Ha...")
              
##############################################################################

def computer_move(board, human, computer):
    #computer moves
    #make a copy of board to work with
    board = board[:]
    #decent positions to use, not unbeatable
    best_moves = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("Ha...Ha...Ha... I shall take square number", end=" ")

    #if computer can win, take the move
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        #done checking move, undo it
        board[move] = empty

    #check if human can win
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        #done checking move, undo it
        board[move] = empty

    #since no one can win in next move, pick best open square
    for move in best_moves:
        if move in legal_moves(board):
            print(move)
            return move

############################################################################

#the main run of the program
def main():
    display_instructions()
    human, computer = pieces()
    turn = x
    board = new_board()
    display_board(board)
    
    while not winner(board):
        
        if turn == human:
            move = human_move(board)
            board[move] = human
            
        elif turn == computer:
            move = computer_move(board, human, computer)
            board[move] = computer

        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)

#run main
main()
