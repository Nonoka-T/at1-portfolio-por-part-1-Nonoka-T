class Board:
    """manage the game board state and display"""

    def __init__(self):
        """initialize the board 3x3 2D list with empty cells"""
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


    def display(self):
        """display current board state """
        print(self.board[0][0], "|", self.board[0][1], "|", self.board[0][2])
        print("------------")
        print(self.board[1][0], "|", self.board[1][1], "|", self.board[1][2])
        print("------------")
        print(self.board[2][0], "|", self.board[2][1], "|", self.board[2][2])
        print()


    def update(self, row, col, player):
        """update cell with player's symbol, X and O."""
        self.board[row][col] = player


    def is_empty(self, row, col):
        """check if cell is empty or not"""
        return self.board[row][col] == " "