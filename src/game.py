class Game:
    """Handle the game logic for win and tie condition"""

    def __init__(self):
        """Initialize the game logic"""
        self.win_conditions = [
            [(0,0), (0,1), (0,2)], #top row
            [(1,0), (1,1), (1,2)], #middle row
            [(2,0), (2,1), (2,2)], #bottom row
            [(0,0), (1,0), (2,0)], #left column
            [(0,1), (1,1), (2,1)], #middle column
            [(0,2), (1,2), (2,2)], #right column
            [(0,0), (1,1), (2,2)], #diagonal top left
            [(0,2), (1,1), (2,0)], #diagonal top right
        ]

    def check_for_win(self, board):
        """Check if any player won the game."""

        for wc in self.win_conditions:
            (r1, c1), (r2, c2), (r3, c3) = wc
            if board[r1][c1] == board[r2][c2] == board[r3][c3] != " ":
                return board[r1][c1]
        return None

    def check_for_tie(self, board):
        """check if the game is tied"""
        for row in board:
            if " " in row:
                return False
        return True





