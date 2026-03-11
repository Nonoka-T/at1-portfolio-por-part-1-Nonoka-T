'''A monolithic and poorly written tic-tac-toe for you to refactor.'''
from board import Board
from game import Game


# Game state
p1 = "X"
p2 = "O"

board = Board()
game = Game()

# Game loop
while True:
    # Print board
    board.display()

    # Check for win - Game.py

    for wc in win_conditions:
        if board[wc[0]] == board[wc[1]] == board[wc[2]] != empty:
            print("Player", board[wc[0]], "wins!")
            exit(0)

    # Check for tie - game.py
    if empty not in board:
        print("It's a tie!")
        exit(0)

    # Get next move
    while True:
        player = p1 if board.count(empty) % 2 == 1 else p2
        move = input("Next move for player " + player + " (0-8): ")
        if move.isdigit() and 0 <= int(move) <= 8 and board[int(move)] == empty:
            board[int(move)] = player
            break
        else:
            print("Invalid move, try again.")

