import random
board = [
    "-","-","-",
    "-","-","-",
    "-","-","-",
]
currentPlayer = "X"
winner = None
gameRunning = True

#game board
def printBoard(board):
    print(board[0] + " | ", board[1] + " | ", board[2])
    print("-----------")
    print(board[3] + " | ", board[4] + " | ", board[5])
    print("------------")
    print(board[6] + " | ", board[7] + " | ", board[8])


#player input
def playerInput(board):
    inp = int(input("Enter a number from 1 - 9: "))
    if inp >= 1 and inp <= 9 and board[inp -1] == "-":
        board[inp -1] = currentPlayer
    else:
        print("Spot Already Taken!!!")

#check for win, tie or loss
##Horizontal win
def checkHorizontalWin(board):
    global winner
    if board[0] == board[1] ==board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] ==board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] ==board[8] and board[6] != "-":
        winner = board[6]
        return True
    
##Vartical win
def checkVerticalWin(board):
    global winner
    if board[0] == board[3] ==board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] ==board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] ==board[8] and board[2] != "-":
        winner = board[2]
        return True
    
##Diagonal win
def checkDiagonalWin(board):
    global winner
    if board[0] == board[4] ==board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] ==board[6] and board[2] != "-":
        winner = board[2]
        return True

##Tie
def checkTie(board):
    if "-" not in board:
        printBoard(board)
        print("YUP!! its a TIE")
        gameRunning = False

# Change Player
def changePlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

# Win Check
def checkWin():
    if  checkHorizontalWin(board) or checkDiagonalWin(board) or checkVerticalWin(board):
        print(f"The Winner is {winner}")

#Bot
def bot(board):
    while currentPlayer == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            changePlayer()

#Main
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    changePlayer()
    bot(board)
    checkWin()
    checkTie(board)