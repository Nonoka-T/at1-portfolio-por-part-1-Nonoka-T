class Board:

#initialise board
    def __init__(self):
        #三つのリストが入ったリスト2Dで列012の3行3列のボード
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

#display 3row
    def display(self):
        print(self.board[0], self.board[1], self.board[2])
        print("------------")
        print(self.board[3], self.board[4], self.board[5])
        print("------------")
        print(self.board[6], self.board[7], self.board[8])
        print()

#player xo input
    def update(self, row, col, player):
        self.board[row][col] = player

#check if the row is empty
    def is_empty(self, row, col):
        return self.board[row][col] == " "