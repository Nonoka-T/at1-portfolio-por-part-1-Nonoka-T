import unittest
from src.board import Board
from src.game import Game


class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_row_win(self):
        """Test horizontal win is detected or not"""
        board = [
            ["X", "X", "X"],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        self.assertEqual(self.game.check_for_win(board), "X")

    def test_column_win(self):
        """Test vertical win is detected or not"""
        board = [
            ["O", " ", " "],
            ["O", " ", " "],
            ["O", " ", " "]
        ]
        self.assertEqual(self.game.check_for_win(board), "O")

    def test_diagonal_win_top_right(self):
        """Test top right diagonal win"""
        board = [
            [" ", " ", "O"],
            [" ", "O", " "],
            ["O", " ", " "]
        ]
        self.assertEqual(self.game.check_for_win(board), "O")

    def test_diagonal_win_top_left(self):
        """Test top left diagonal win"""
        board = [
            ["X", " ", " "],
            [" ", "X", " "],
            [" ", " ", "X"]
        ]
        self.assertEqual(self.game.check_for_win(board), "X")


if __name__ == '__main__':
    unittest.main()