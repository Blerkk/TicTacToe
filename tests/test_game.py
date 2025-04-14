"""
Tests for the game logic of the Tic-Tac-Toe game.
"""
import unittest
from TicTacToe.game import TicTacToeGame

class TestTicTacToeGame(unittest.TestCase):
    def setUp(self):
        """Set up a new game instance before each test."""
        self.game = TicTacToeGame()
    
    def test_init(self):
        """Test the initialization of the game."""
        self.assertEqual(self.game.tabla, [' ' for _ in range(9)])
        self.assertEqual(self.game.jelenlegiJatekos, 'X')
        self.assertFalse(self.game.gameOver)
        self.assertIsNone(self.game.nyertes)
        self.assertEqual(self.game.pontszam, {'X': 0, 'O': 0, 'Tie': 0})
        self.assertTrue(self.game.gameActive)
        self.assertEqual(self.game.nehezseg, "easy")
        self.assertEqual(self.game.jatekMod, "ai")
    
    def test_make_move(self):
        """Test making a valid move."""
        self.game.make_move(0)
        self.assertEqual(self.game.tabla[0], 'X')
        self.assertEqual(self.game.jelenlegiJatekos, 'O')
    
    def test_make_move_invalid(self):
        """Test making an invalid move (occupied space)."""
        self.game.tabla[0] = 'X'  # Pre-occupy a space
        self.game.jelenlegiJatekos = 'O'
        self.game.make_move(0)  # Try to move on occupied space
        # Move should be ignored, state should remain unchanged
        self.assertEqual(self.game.tabla[0], 'X')
        self.assertEqual(self.game.jelenlegiJatekos, 'O')
    
    def test_check_nyertes_row(self):
        """Test win detection for a row."""
        self.game.tabla = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertTrue(self.game.check_nyertes())
        self.assertEqual(self.game.nyertes, 'X')
        self.assertTrue(self.game.gameOver)
        self.assertEqual(self.game.winningCombo, [0, 1, 2])
    
    def test_check_nyertes_column(self):
        """Test win detection for a column."""
        self.game.tabla = ['O', ' ', ' ', 'O', ' ', ' ', 'O', ' ', ' ']
        self.assertTrue(self.game.check_nyertes())
        self.assertEqual(self.game.nyertes, 'O')
        self.assertTrue(self.game.gameOver)
        self.assertEqual(self.game.winningCombo, [0, 3, 6])
    
    def test_check_nyertes_diagonal(self):
        """Test win detection for a diagonal."""
        self.game.tabla = ['X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X']
        self.assertTrue(self.game.check_nyertes())
        self.assertEqual(self.game.nyertes, 'X')
        self.assertTrue(self.game.gameOver)
        self.assertEqual(self.game.winningCombo, [0, 4, 8])
    
    def test_check_tie(self):
        """Test draw/tie detection."""
        self.game.tabla = ['X', 'O', 'X', 'X', 'O', 'X', 'O', 'X', 'O']
        self.assertTrue(self.game.check_nyertes())
        self.assertEqual(self.game.nyertes, 'Tie')
        self.assertTrue(self.game.gameOver)
    
    def test_reset_game(self):
        """Test game reset functionality."""
        # Set up a game in progress
        self.game.tabla = ['X', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.game.jelenlegiJatekos = 'X'
        self.game.gameOver = True
        self.game.nyertes = 'X'
        self.game.winningCombo = [0, 1, 2]
        
        # Reset the game
        self.game.reset_game()
        
        # Check if game state is properly reset
        self.assertEqual(self.game.tabla, [' ' for _ in range(9)])
        self.assertEqual(self.game.jelenlegiJatekos, 'X')
        self.assertFalse(self.game.gameOver)
        self.assertIsNone(self.game.nyertes)
        self.assertEqual(self.game.winningCombo, [])
    
    def test_random_move(self):
        """Test the random move generation."""
        # Set up a board with only one empty space
        self.game.tabla = ['X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', ' ']
        move = self.game.random_move()
        self.assertEqual(move, 8)  # Only position 8 is available
    
    def test_best_move_blocking(self):
        """Test AI's blocking move."""
        # Set up a board where X is about to win
        self.game.tabla = ['X', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.game.jelenlegiJatekos = 'O'
        
        # AI should block X's win
        move = self.game.best_move()
        self.assertEqual(move, 2)
    
    def test_best_move_winning(self):
        """Test AI's winning move."""
        # Set up a board where O is about to win
        self.game.tabla = ['O', 'O', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.game.jelenlegiJatekos = 'O'
        
        # AI should take the winning move
        move = self.game.best_move()
        self.assertEqual(move, 2)

if __name__ == '__main__':
    unittest.main()