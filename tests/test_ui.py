"""
Tests for the UI of the Tic-Tac-Toe game.
Note: UI testing often requires mocking the Dear PyGui library
and checking if the right functions are called with the right parameters.
"""
import unittest
from unittest.mock import patch, MagicMock
from TicTacToe.ui import TicTacToeUI
from TicTacToe.game import TicTacToeGame

class TestTicTacToeUI(unittest.TestCase):
    @patch('TicTacToe.ui.dpg')
    @patch('TicTacToe.ui.setup_themes')
    def setUp(self, mock_setup_themes, mock_dpg):
        """Set up UI instance with mocked dependencies."""
        # Mock the themes dict returned by setup_themes
        mock_setup_themes.return_value = {
            "global_theme": "global_theme",
            "button_theme": "button_theme",
            "x_button_theme": "x_button_theme",
            "o_button_theme": "o_button_theme",
            "nyertes_button_theme": "nyertes_button_theme",
            "reset_button_theme": "reset_button_theme"
        }
        
        # Create UI with mocked DPG
        self.ui = TicTacToeUI()
        self.mock_dpg = mock_dpg
        
        # Replace the real game with a mock for more isolated testing
        self.ui.game = MagicMock(spec=TicTacToeGame)
        self.ui.game.tabla = [' ' for _ in range(9)]
        self.ui.game.jelenlegiJatekos = 'X'
        self.ui.game.gameOver = False
        self.ui.game.nyertes = None
        self.ui.game.pontszam = {'X': 0, 'O': 0, 'Tie': 0}
        self.ui.game.jatekMod = "ai"
        self.ui.game.nehezseg = "easy"
        self.ui.game.jatekosokJelolese = {'X': 'X', 'O': 'O'}
        self.ui.game.winningCombo = []
    
    def test_handle_button_click(self):
        """Test button click handler."""
        # Call the handler
        self.ui.handle_button_click(4)  # Click center position
        
        # Check if game's make_move was called with right position
        self.ui.game.make_move.assert_called_once_with(4)
        
        # Check if UI was updated
        self.ui.game.update_ui = MagicMock()
        self.ui.update_ui()
        self.assertTrue(self.ui.game.update_ui.called)
    
    def test_handle_reset_game(self):
        """Test reset button handler."""
        # Call the handler
        self.ui.handle_reset_game()
        
        # Check if game reset was called
        self.ui.game.reset_game.assert_called_once()
        
        # Since we're mocking dpg, we need to check if bind_item_theme would be called
        # for each button to reset their themes
        expected_calls = [
            unittest.mock.call(f"button_{i}", "button_theme") for i in range(9)
        ]
        self.mock_dpg.bind_item_theme.assert_has_calls(expected_calls, any_order=True)
    
    def test_set_jatek_mod_ai(self):
        """Test setting game mode to AI."""
        self.ui.set_jatekMod("Against AI")
        self.assertEqual(self.ui.game.jatekMod, "ai")
        self.mock_dpg.configure_item.assert_called_once_with("nehezseg_group", show=True)
        self.ui.game.reset_game.assert_called_once()
    
    def test_set_jatek_mod_two_player(self):
        """Test setting game mode to two player."""
        self.ui.set_jatekMod("Two Players")
        self.assertEqual(self.ui.game.jatekMod, "two_player")
        self.mock_dpg.configure_item.assert_called_once_with("nehezseg_group", show=False)
        self.ui.game.reset_game.assert_called_once()
    
    def test_set_nehezseg(self):
        """Test setting difficulty level."""
        self.ui.set_nehezseg("Hard")
        self.assertEqual(self.ui.game.nehezseg, "hard")
    
    def test_update_ui_in_progress(self):
        """Test UI update when game is in progress."""
        # Set up game state
        self.ui.game.gameOver = False
        self.ui.game.jelenlegiJatekos = 'X'
        self.ui.game.jatekosokJelolese = {'X': 'X', 'O': 'O'}
        
        # Call update
        self.ui.update_ui()
        
        # Check if status was updated
        self.mock_dpg.set_value.assert_any_call("game_status", "Next Player: X")
        self.mock_dpg.configure_item.assert_any_call("game_status", color=[220, 220, 220])
    
    def test_update_ui_winner(self):
        """Test UI update when there's a winner."""
        # Set up game state with winner
        self.ui.game.gameOver = True
        self.ui.game.nyertes = 'X'
        self.ui.game.winningCombo = [0, 1, 2]
        self.ui.game.jatekosokJelolese = {'X': 'X', 'O': 'O'}
        
        # Call update
        self.ui.update_ui()
        
        # Check if winner status was updated
        self.mock_dpg.set_value.assert_any_call("game_status", "Winner: X")
        self.mock_dpg.configure_item.assert_any_call("game_status", color=[0, 200, 0])
        
        # Check if winning buttons got special theme
        for pos in [0, 1, 2]:
            self.mock_dpg.bind_item_theme.assert_any_call(f"button_{pos}", "nyertes_button_theme")
    
    def test_update_ui_tie(self):
        """Test UI update when game ends in a tie."""
        # Set up game state with tie
        self.ui.game.gameOver = True
        self.ui.game.nyertes = 'Tie'
        
        # Call update
        self.ui.update_ui()
        
        # Check if tie status was updated
        self.mock_dpg.set_value.assert_any_call("game_status", "It's a Draw!")
        self.mock_dpg.configure_item.assert_any_call("game_status", color=[255, 165, 0])

if __name__ == '__main__':
    unittest.main()