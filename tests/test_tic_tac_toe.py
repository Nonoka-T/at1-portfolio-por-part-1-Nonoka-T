import unittest

from board import Board
from src.game import Game

class TestTicTacToe(unittest.TestCase):
    def test_check_win(self):
        game = Game()

        board = [["X", "X", "X"], [" ", " ", " "], [" ", " ", " "] ]

        self.assertEqual(game.check_for_win(board), "X")

if __name__ == '__main__':
    unittest.main()