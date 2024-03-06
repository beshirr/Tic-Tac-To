# Program: Tic-Tac-Toe Game
# Author: Youssef Ahmed Beshir 20230476
# Version: 2.0
# Date: March 1, 2024


def game_status(game_board):

    #  Prints the current state of the game board.
    for i in range(3):
        for j in range(3):
            print(board[i][j], end="   ")
        print()


def empty(index, game_board, index_dic):
    # Checks if a specific index on the board is empty (not filled by a player).
    if game_board[index_dic[index][0]][index_dic[index][1]] == index:
        return True
    return False


def player_turn(game_board, player, available_numbers, index_dic):

    # Handles the turn for a specific player, allowing them to choose a number and an index on the board.
    # It validates the input and removes the chosen number from the available options.
    game_status(board)

    if player == 1:
        while True:
            try:
                value = int(input(f"Player-{player}, pick an odd number {available_numbers}: "))
                break
            except ValueError:
                value = int(input(f"Pick valid numbers only {available_numbers}: "))
            break

        while value not in available_numbers:
            try:
                value = int(input(f"Pick available numbers only {available_numbers}: "))
                break
            except ValueError:
                value = int(input(f"Pick valid numbers only {available_numbers}: "))
            break

        available_numbers.remove(value)

        index = input("Choose an index: ").upper()

        while index not in indexes or not empty(index, board, indexes_dic):
            index = input(f"{index} is not available, choose a valid index {indexes}: ").upper()

        indexes.remove(index)
        game_board[index_dic[index][0]][index_dic[index][1]] = value

    if player == 2:
        while True:
            try:
                value = int(input(f"Player-{player}, pick an even number {available_numbers}: "))
                break
            except ValueError:
                value = int(input(f"Pick valid numbers only {available_numbers}: "))
            break

        while value not in available_numbers:
            try:
                value = int(input(f"Pick available numbers only {available_numbers}: "))
                break
            except ValueError:
                value = int(input(f"Pick valid numbers only {available_numbers}: "))
            break

        available_numbers.remove(value)

        index = input("Choose an index: ").upper()

        while index not in indexes or not empty(index, board, indexes_dic):
            index = input(f"{index} is not available, choose a valid index {indexes}: ").upper()

        indexes.remove(index)
        game_board[index_dic[index][0]][index_dic[index][1]] = value

    return game_board


def check_winner(game_board):
    # Checks if the current board state satisfies the win condition
    try:
        for i in range(3):
            if game_board[i][0] + game_board[i][1] + game_board[i][2] >= 15:
                return True
    except TypeError:
        pass

    try:
        for i in range(3):
            if game_board[0][i] + game_board[1][i] + game_board[2][i] >= 15:
                return True
    except TypeError:
        pass

    try:
        if game_board[0][0] + game_board[1][1] + game_board[2][2] >= 15:
            return True
    except TypeError:
        pass

    try:
        if game_board[0][2] + game_board[1][1] + game_board[2][0] >= 15:
            return True
    except TypeError:
        pass

    return False


def full(game_board, index_dic):
    # Checks if all positions on the board are filled (no empty cells).
    for i in range(3):
        for j in range(3):
            if game_board[i][j] in index_dic:
                return False
    return True


# game data
evenPlayer = [0, 2, 4, 6, 8]
oddPlayer = [1, 3, 5, 7, 9]

board = [["A", "B", "C"],
         ["D", "E", "F"],
         ["G", "H", "I"]]

indexes_dic = {"A": [0, 0], "B": [0, 1], "C": [0, 2],
               "D": [1, 0], "E": [1, 1], "F": [1, 2],
               "G": [2, 0], "H": [2, 1], "I": [2, 2]}

indexes = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
# The main loop runs the game until either a player wins or the board is full (resulting in a tie).
# It alternates between players, calling the player_turn function for each and checking for a win after each turn.

while True:
    if full(board, indexes_dic) and not check_winner(board):
        print("Tie!")
        break

    player_turn(board, 1, oddPlayer, indexes_dic)
    if check_winner(board):
        print("Player-1 Wins")
        break

    player_turn(board, 2, evenPlayer, indexes_dic)
    if check_winner(board):
        print("Player-2 Wins")
        break
