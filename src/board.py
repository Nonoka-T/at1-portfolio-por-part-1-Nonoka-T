class Board:

#initialise board
    def __init__(self):
        #三つのリストが入ったリスト2Dで列012の3行3列のボード
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

#display 3row
    def display(self):
        for row in self.board:
            print(row[0], row[1], row[2])
            print("--")

#player xo input
    def update(self, row, col, player):
        self.board[row][col] = player

#check if the row is emply
    def is_empty(self, row, col):
        return self.board[row][col] == " "