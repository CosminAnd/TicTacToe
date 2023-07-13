import random


def print_board(board):
    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[0], board[1], board[2]))
    print("_____|_____|_____")
    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[3], board[4], board[5]))
    print("_____|_____|_____")
    print("     |     |")
    print("  {}  |  {}  |  {}".format(board[6], board[7], board[8]))
    print("     |     |")


def get_player_move(board):
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit() and int(move) in range(1, 10) and board[int(move) - 1] == " ":
            return int(move) - 1
        else:
            print("Invalid move. Please try again.")


def get_computer_move(board, level):
    if level == "easy":
        return random.choice([i for i in range(9) if board[i] == " "])
    elif level == "medium":
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                if check_win(board, "O"):
                    board[i] = " "
                    return i
                board[i] = " "
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                if check_win(board, "X"):
                    board[i] = " "
                    return i
                board[i] = " "
        return random.choice([i for i in range(9) if board[i] == " "])
    else:
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                if check_win(board, "O"):
                    board[i] = " "
                    return i
                board[i] = " "
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                if check_win(board, "X"):
                    board[i] = " "
                    return i
                board[i] = " "
        if board[4] == " ":
            return 4
        corners = [0, 2, 6, 8]
        empty_corners = [i for i in corners if board[i] == " "]
        if empty_corners:
            return random.choice(empty_corners)
        sides = [1, 3, 5, 7]
        empty_sides = [i for i in sides if board[i] == " "]
        if empty_sides:
            return random.choice(empty_sides)
        return random.choice([i for i in range(9) if board[i] == " "])


def check_win(board, player):
    if (board[0] == player and board[1] == player and board[2] == player) or \
            (board[3] == player and board[4] == player and board[5] == player) or \
            (board[6] == player and board[7] == player and board[8] == player) or \
            (board[0] == player and board[3] == player and board[6] == player) or \
            (board[1] == player and board[4] == player and board[7] == player) or \
            (board[2] == player and board[5] == player and board[8] == player) or \
            (board[0] == player and board[4] == player and board[8] == player) or \
            (board[2] == player and board[4] == player and board[6] == player):
        return True
    else:
        return False


def check_tie(board):
    if " " not in board:
        return True
    else:
        return False


def tic_tac_toe():
    board = [" "] * 9
    print_board(board)
    player = "X"
    level = ""
    while level not in ["easy", "medium", "hard", "pvp", "exit"]:
        level = input("Select a level (easy, medium, hard, pvp, exit): ")
    while True:
        if level == "exit":
            return 0
        if level in ["easy", "medium", "hard"]:
            if player == "X":
                move = get_player_move(board)
            else:
                print("Computer's turn ({}):".format(level))
                move = get_computer_move(board, level)
            board[move] = player
            print_board(board)
            if check_win(board, player):
                print("{} wins!".format(player))
                break
            if check_tie(board):
                print("It's a tie!")
                break
            player = "O" if player == "X" else "X"
        else:
            move = get_player_move(board)
            board[move] = player
            print_board(board)
            if check_win(board, player):
                print("{} wins".format(player))
                break
            if check_tie(board):
                print("It's a tie!")
                break
            player = "O" if player == "X" else "X"
    level = input("If you restart game type 'restart'! For end game type 'exit'!")
    if level == "exit":
        return 0
    if level == "restart":
        tic_tac_toe()


tic_tac_toe()
