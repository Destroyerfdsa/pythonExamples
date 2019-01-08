##Nicholaus Whites
##12/14/18
##Tic Tac Toe


#global
BOARD = """
       |   |   
    ===|===|===
       |   |   
    ===|===|===
       |   |
"""
BOARD2 = """
    \\ /  | /-\\ |
     \\   ||   ||
    / \\  | \\_/ |   
   ======|=====|======
         | \\ / | /-\\
         |  \\  ||   |
         | / \\ | \\_/
   ======|=====|======
         |     | \\ / 
         |     |  \\
         |     | / \\
"""

#=====================================================================================================================

X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9


#functions
#=====================================================================================================================
def instructions():
    """Display Instructions"""
    print("Tic-Tac-Toe")
    print("Win by getting 3 in a row of an X, or an O")
    print("""
     0 | 1 | 2 
    ===|===|===
     3 | 4 | 5 
    ===|===|===
     6 | 7 | 8
""")
    print("Prepare to be destroyed.")
#=====================================================================================================================
def ask_y_n(question):
    """Ask a yes or no question"""
    responce = None
    while responce not in ("y","n"):
        responce = input(question+"y/n: ").lower()
    return responce

#=====================================================================================================================
def ask_num(question, low, high):
    responce = "8888"
    while True:
        if responce.isdigit():
            if int(responce) in range(low,high):
                break
            else:
                responce = input(question)
        else:
            print("digits only")
            responce = input(question)
    return int(responce)
#=====================================================================================================================
def pieces():
    """does the computer or the player go first."""
    go_first = ask_y_n("Do you go first? Y/N: ")
    if go_first == "y":
        print("Does not matter what you choose, for I will always win!")
        human = X
        computer = O
    else:
        print("Too scared to go first? Against me, I would be too!")
        human = O
        computer = X
    return computer,human
#=====================================================================================================================
def new_board():
    """Create a new board"""
    board = []
    for squares in range(NUM_SQUARES):
        board.append(EMPTY)
    return board
#=====================================================================================================================
def display_board(board):
    """Display game board on screen"""
    print("\n\t ",board[0],"|",board[1],"|", board[2])
    print("\t","===|===|===")
    print("\t ",board[3],"|",board[4],"|", board[5])
    print("\t","===|===|===")
    print("\t ",board[6],"|",board[7],"|", board[8], "\n")
#=====================================================================================================================
def legal_moves(board):
    """Create list of legal moves"""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves
#=====================================================================================================================

def winner(board):
    """Determine the game winner"""
    WAYS_TO_WIN = ((0,1,2),
            (3,4,5),
            (6,7,8),
            (0,3,6),
            (1,4,7),
            (2,5,8),
            (0,4,8),
            (2,4,6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE
                   
    return None
#=====================================================================================================================

def human_move(board):
    """Get Human Move."""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_num("Where do you want to move? (0-8): ",0,NUM_SQUARES)
        if move not in legal:
            print("\nYou seem to be going crazy; Because you can't go there!\n")
    print("Fine..")
    return move
#=====================================================================================================================
def next_turn(turn):
    """Switch turns."""
    if turn == X:
        return O
    else:
        return X
#=====================================================================================================================

def congrat_winner(winner,computer,human):
    if winner != TIE:
        print(winner,"won!\n")
    else:
        print("It's a tie!\n")
    if winner == computer:
        print("You have been defeated by me, but of course, it was no mystery who would win.")
    if winner == human:
        print("Impossible! How can you, a mere human, beat me, the computer?! You will never be this lucky again!")
    if winner == TIE:
        print("Somehow you have managed to tie against me, however that will be the best you can acheive.")
#=====================================================================================================================


def computer_move(board,computer,human):
    #make board copy
    board = board[:]
    #best moves
    BEST_MOVES = (4,0,2,6,8,1,3,5,7)
    print("I shall take square number ",end="")

    #if computer can win, do it.
    for move in legal_moves(board):
        board[move]=computer
        if winner(board) == computer:
            print(move)
            return move
        # done checking this move, undo it
        board[move] = EMPTY

    for move in legal_moves(board):
        board[move]=human
        if winner(board) == human:
            print(move)
            return move
        # done checking this move, undo it
        board[move] = EMPTY

    #since no one can win on next move, pick best open sqaure
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move

#=====================================================================================================================
def main():
    instructions()

    computer,human = pieces()
    turn = X
    
    board = new_board()
    
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board)
            board[move] = turn
            display_board(board)
            next_turn(turn)
        elif turn == computer:
            move = computer_move(board,computer,human)
            board[move] = turn
            display_board(board)
            next_turn(turn)
    winner(board)
    congrat_winner(winner,computer,human)



main()






























