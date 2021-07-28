from data import grid_layout, board, win_conditions


# Variables #
player_1 = "X"
player_2 = "O"
current_player = player_1
game_over = False


# Functions #
def print_board(grid_dict):
    """Prints the game board with data from the input dictionary."""
    print(f"{grid_dict['1']} | {grid_dict['2']} | {grid_dict['3']}")
    print("---------")
    print(f"{grid_dict['4']} | {grid_dict['5']} | {grid_dict['6']}")
    print("---------")
    print(f"{grid_dict['7']} | {grid_dict['8']} | {grid_dict['9']}")


def check_win_condition():
    """Checks if a player has won by looping through the list of possible win configurations, comparing current board
    state. If the game has been won, returns True, otherwise returns False."""
    for condition in win_conditions:
        # Each win condition is a list of 3 spaces, if the 3 spaces are not empty and are the same, the game is won
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != " ":
            return True
    return False


def check_draw_condition():
    """Checks if there are any empty spaces on the board. If there are NOT -- result is a draw and returns True,
    otherwise returns False."""
    for space in board:
        if board[space] == " ":
            return False
    return True


def switch_players(player):
    """Switches players, returns the opponent of the input player."""
    if player == player_1:
        return player_2
    else:
        return player_1


def play_again():
    """Asks the player if they would like to play again. For 'y', clears the board inserting ' 's into the spaces and
    returns True. Otherwise, returns False."""
    option = input("Would you like to play again? (y, n)")
    if option == "y":
        for space in board:
            board[space] = " "
        return True
    else:
        return False


# Initial Message #
# Prints welcome message and example grid for the board
print("Let's Play Tic-Tac-Toe!\nSpaces are defined as:")
print_board(grid_layout)
print("\nGo!\n")


# Game Loop #
while not game_over:

    print_board(board)
    # Asks for the current player to make a move and stores the string in {player_move}
    player_move = str(input(f"Player {current_player}, select your next move:\n"))
    # Checks if the player move is a valid choice, and not yet played. If true, updates board dictionary with the
    # player's move, otherwise tells the player the error and continues the while loop
    if player_move in board:
        if board[player_move] == " ":
            board[player_move] = current_player
        elif board[player_move] == "X" or board[player_move] == "O":
            print(f"Space '{player_move}' has already been played, choose an empty space.")
            continue
    else:
        print(f"'{player_move}' is invalid, select an empty space '0-9'.")
        continue

    if check_win_condition():
        print_board(board)
        print(f"Player {current_player} wins!")
        if play_again():
            current_player = player_1
            continue
        else:
            game_over = True

    if check_draw_condition():
        print_board(board)
        print(f"Draw!")
        if play_again():
            current_player = player_1
            continue
        else:
            game_over = True

    current_player = switch_players(current_player)
