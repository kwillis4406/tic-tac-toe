# Tic-Tac-Toe

![Ex](https://github.com/kwillis4406/tic-tac-toe/blob/main/example_image.PNG?raw=true)

## About

A text-based version of [Tic-Tac-Toe](https://en.wikipedia.org/wiki/Tic-tac-toe). Programmed using Python, users can play the game using text inputs in the console.

The game is run from the main file, relevant dictionaries are located in the data file.

___

## How It Works

+ Upon running the script, the welcome message is printed which includes a board filled with numbers representing the corresponding values of the grid.

+ Underneath the welcome message, the game is initiated with an empty board and prompts player 1 (X) to make a move.

+ Players make their moves by entering a number (0-9), indicating which space they would like to play.
  - If the player enters an invalid move, the error type is printed and the player is again prompted to make a move.

  - Once a valid move is entered, the board is updated and player 2 (O) is prompted to make their move.

+ Players rotate making their moves until a player has won, or all spaces are filled with no winner, resulting in a draw.

+ When a game ending condition occurs, the final board and result are printed, and the user is prompted if they would like to play a new game.
  - Entering 'y' for yes, the board clears and a new game starts with player 1 (X).
  - Entering 'n' for no (or any other character) terminates the script.