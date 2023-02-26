
# display game board
def displayBoard(board):
    print()
    print(' ', board[0][0], " | ", board[0][1], " | ", board[0][2])
    print("-----------------")
    print(' ', board[1][0], " | ", board[1][1], " | ", board[1][2])
    print("-----------------")
    print(' ', board[2][0], " | ", board[2][1], " | ", board[2][2])

# player input
def playerInput(player, board):
    option = [int(x) for x in input(f"It's {player} turn. Choose an position on the board (line, column): ").split()]
    if 1 <= option[0] <= 3 and 1 <= option[1] <= 3:
        if board[option[0] - 1][option[1] - 1] == "-":
            board[option[0] - 1][option[1] - 1] = player
        else:
            print("Oops, this position is already occupied.")
            playerInput(player)
    else:
        print("Oops, you entered an invalid position.")
        playerInput(player)
    return board

# check if there is any winner
def checkWin(board):
    for i in range(0,2):
        # check horizontally
        if board[i][0] == board[i][1] == board[i][2] != "-":
            winner = board[i][0]
            return winner
        # check vertically
        if board[0][i] == board[1][i] == board[2][i] != "-":
            winner = board[0][i]
            return winner
    # check diags
    if board[0][0] == board[1][1] == board[2][2] != "-":
        winner = board[0][0]
        return winner
    if board[2][0] == board[1][1] == board[0][2] != "-":
        winner = board[1][1]
        return winner
    return None

def checkTie(board):
    if "-" not in board[0] and "-" not in board[1] and "-" not in board[2]:
        return True
    return False

# switch the player
def switchPlayer(player):
    if player == "X":
        return "O"
    else:
        return "X"

board = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]
currentPlayer = "X"
winner = None
gameRunning = True

while gameRunning:
    displayBoard(board)
    board = playerInput(currentPlayer, board)
    winner = checkWin(board)
    if winner != None:
        gameRunning = False
        displayBoard(board)
        print(winner, " is the WINNER!")
    if checkTie(board):
        gameRunning = False
        displayBoard(board)
        print("It's a tie! ")
    currentPlayer = switchPlayer(currentPlayer)