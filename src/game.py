

class Game:
    def __init__(self):
        self.win_conditions = [
            [(0,0), (0,1), (0,2)],
            [(1,0), (1,1), (1,2)],
            [(2,0), (2,1), (2,2)],
            [(0,0), (1,0), (2,0)],
            [(0,1), (1,1), (2,1)],
            [(0,2), (1,2), (2,2)],
            [(0,0), (1,1), (2,2)],
            [(0,2), (1,1), (2,0)],

        ]

    def check_for_win(self, board):
        for wc in self.win_conditions:
            (r1, c1), (r2, c2), (r3, c3) = wc
            if board[r1][c1] == board[r2][c2] == board[r3][c3] != " ":
                return board[r1][c1]
        return None

    def check_for_tie(self, board):
        for row in board:
            if " " in row:
                return False
        return True





