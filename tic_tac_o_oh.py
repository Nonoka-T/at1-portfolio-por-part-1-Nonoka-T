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
    while True:
        empty_count = 0
        for row in board.board:
            for cell in row:
                if cell == " ":
                    empty_count += 1

        player = p1 if empty_count % 2 == 0 else p2
        move = input("Enter your move: " + player + "(0-8): ")

        if move.isdigit() and 0 <= int(move) <= 8:
            row = int(move) // 3
            col = int(move) % 3

            if board.is_empty(row, col):
                board.update(row, col, player)
                break
            else:
                print("Invalid move!")

        else:
            print("Invalid move!")


