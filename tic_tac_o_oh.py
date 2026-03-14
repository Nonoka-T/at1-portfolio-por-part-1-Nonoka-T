'''A monolithic and poorly written tic-tac-toe for you to refactor.'''
from src.board import Board
from src.game import Game


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
    winner = game.check_for_win(board.board)
    if winner is not None:
        print("Player", winner, "win!")
        break

    # Check for tie - game.py
    if game.check_for_tie(board.board):
        print("Tie!")
        break


    # Get next move


