import random
import math
import copy


def printBoard(board):
    print("---------")
    print("|" + " " + board[0] + " " + board[1] + " " + board[2] + " " + "|")
    print("|" + " " + board[3] + " " + board[4] + " " + board[5] + " " + "|")
    print("|" + " " + board[6] + " " + board[7] + " " + board[8] + " " + "|")
    print("---------")


def getState(board):
    state = ""
    Xwin, Owin = False, False
    Xcount, Ocount = 0, 0

    for i in board:
        if i == "X":
            Xcount += 1
        if i == "O":
            Ocount += 1

    if board[0] == board[1] == board[2] == "X" or \
            board[3] == board[4] == board[5] == "X" or \
            board[6] == board[7] == board[8] == "X" or \
            board[0] == board[3] == board[6] == "X" or \
            board[1] == board[4] == board[7] == "X" or \
            board[2] == board[5] == board[8] == "X" or \
            board[0] == board[4] == board[8] == "X" or \
            board[2] == board[4] == board[6] == "X":
        Xwin = True

    if board[0] == board[1] == board[2] == "O" or \
            board[3] == board[4] == board[5] == "O" or \
            board[6] == board[7] == board[8] == "O" or \
            board[0] == board[3] == board[6] == "O" or \
            board[1] == board[4] == board[7] == "O" or \
            board[2] == board[5] == board[8] == "O" or \
            board[0] == board[4] == board[8] == "O" or \
            board[2] == board[4] == board[6] == "O":
        Owin = True

    if not Xwin and not Owin and Xcount + Ocount < 9:
        state = "Game not finished"

    elif Xwin:
        state = "X wins"

    elif Owin:
        state = "O wins"

    else:
        state = "Draw"

    return state


def menu():
    command = input("Input command: ").split()
    commands = ["user", "easy", "medium", "hard"]

    while True:
        if len(command) == 2:
            if command[0] not in commands or command[1] not in commands:
                print("Bad parameters")
                command = input("Input command: ").split()
            else:
                break
        elif command[0] == "exit":
            #exit()
            return
        else:
            print("Bad parameters!")
            command = input("Input command: ").split()

    return command


def human(board):
    while True:
        move = int(input("Enter the move: "))
        if not type(move) == int:
            print("You should enter numbers!")
        elif move not in range(9):
            print("Coordinates should be from 0 to 8!")
        elif not board[move] == " ":
            print("This cell is occupied! Choose another one!")
        else:
            break

    return move


def easyAI(moves):
    print('Making move level "easy"')
    move = random.choice(moves)
    return move


def mediumAI(board, moves):
    print('Making move level "medium"')
    symbols = 'XO'

    if board[0] == board[1] and board[0] in symbols and 2 in moves:
        move = 2
    elif board[0] == board[2] and board[0] in symbols and 1 in moves:
        move = 1
    elif board[1] == board[2] and board[1] in symbols and 0 in moves:
        move = 0

    elif board[3] == board[4] and board[3] in symbols and 5 in moves:
        move = 5
    elif board[3] == board[5] and board[3] in symbols and 4 in moves:
        move = 4
    elif board[4] == board[5] and board[4] in symbols and 3 in moves:
        move = 3

    elif board[6] == board[7] and board[6] in symbols and 8 in moves:
        move = 8
    elif board[6] == board[8] and board[6] in symbols and 7 in moves:
        move = 7
    elif board[7] == board[8] and board[7] in symbols and 6 in moves:
        move = 6

    elif board[0] == board[3] and board[0] in symbols and 6 in moves:
        move = 6
    elif board[0] == board[6] and board[0] in symbols and 3 in moves:
        move = 3
    elif board[3] == board[6] and board[3] in symbols and 0 in moves:
        move = 0

    elif board[1] == board[4] and board[1] in symbols and 7 in moves:
        move = 7
    elif board[1] == board[7] and board[1] in symbols and 4 in moves:
        move = 4
    elif board[4] == board[7] and board[4] in symbols and 1 in moves:
        move = 1

    elif board[2] == board[5] and board[2] in symbols and 8 in moves:
        move = 8
    elif board[2] == board[8] and board[2] in symbols and 5 in moves:
        move = 5
    elif board[5] == board[8] and board[5] in symbols and 2 in moves:
        move = 2

    elif board[0] == board[4] and board[0] in symbols and 8 in moves:
        move = 8
    elif board[0] == board[8] and board[0] in symbols and 4 in moves:
        move = 4
    elif board[4] == board[8] and board[4] in symbols and 0 in moves:
        move = 0

    elif board[2] == board[4] and board[2] in symbols and 6 in moves:
        move = 6
    elif board[2] == board[6] and board[2] in symbols and 4 in moves:
        move = 4
    elif board[4] == board[6] and board[4] in symbols and 2 in moves:
        move = 2
    else:
        move = random.choice(moves)

    return move


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 if game is a tie.
    """
    if getState(board) == "X wins":
        return 1
    elif getState(board) == "O wins":
        return -1
    else:
        return 0


def moves(board):
    available = set()
    for i in range(len(board)):
        if board[i] == " ":
            available.add(i)

    return available


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    print('Making move level "hard"')
    turn = getTurn(board)

    if turn == "X":
        bestVal = -math.inf

        for move in moves(board):
            res = minValue(result(board, move))
            if res > bestVal:
                bestVal = res
                bestMove = move

    else:
        bestVal = math.inf

        for move in moves(board):
            res = maxValue(result(board, move))
            if res < bestVal:
                bestVal = res
                bestMove = move

    return bestMove


def maxValue(board):
    if getState(board) != "Game not finished":
        return utility(board)
    v = -math.inf
    for move in moves(board):
        v = max(v, minValue(result(board, move)))

    return v


def minValue(board):
    if getState(board) != "Game not finished":
        return utility(board)
    v = math.inf
    for move in moves(board):
        v = min(v, maxValue(result(board, move)))

    return v


def result(board, move):
    turn = getTurn(board)
    resultBoard = copy.deepcopy(board)
    resultBoard = list(resultBoard)
    resultBoard[move] = turn
    return resultBoard


def getTurn(board):
    count = 0
    for i in board:
        if i != " ":
            count += 1
    if count % 2 == 0:
        return "X"
    else:
        return "O"


def main():
    command = ""
    while command != "exit":
        command = menu()
        if not command:
            return

        board = "         "
        printBoard(board)
        turn = "X"
        state = ""
        movesAvail = [0, 1, 2,
                      3, 4, 5,
                      6, 7, 8]

        while state != "X wins" and state != "O wins" and state != "Draw":
            if turn == "X":
                if command[0] == "user":
                    move = human(board)
                elif command[0] == "easy":
                    move = easyAI(movesAvail)
                elif command[0] == "medium":
                    move = mediumAI(board, movesAvail)
                elif command[0] == "hard":
                    move = minimax(board)
            else:
                if command[1] == "user":
                    move = human(board)
                elif command[1] == "easy":
                    move = easyAI(movesAvail)
                elif command[1] == "medium":
                    move = mediumAI(board, movesAvail)
                elif command[1] == "hard":
                    move = minimax(board)

            board = list(board)

            board[move] = turn

            if turn == "X":
                turn = "O"
            else:
                turn = "X"

            movesAvail.remove(move)

            printBoard(board)

            state = getState(board)
            if state == "X wins" or state == "O wins" or state == "Draw":
                print(state)
            print()


main()

