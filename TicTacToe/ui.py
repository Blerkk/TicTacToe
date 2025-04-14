"""
UI module for the Tic-Tac-Toe game.
Contains the TicTacToeUI class which handles the graphical user interface.
"""

import os
import time
import dearpygui.dearpygui as dpg

from .game import TicTacToeGame
from .themes import setup_themes

class TicTacToeUI:
    def __init__(self):
        self.game = TicTacToeGame()
        self.setup_dpg()
        
    def setup_dpg(self):
        dpg.create_context()
        dpg.create_viewport(title="Tic-Tac-Toe Game", width=500, height=675)
        dpg.set_viewport_resizable(False)
        dpg.setup_dearpygui()
        self.themes = setup_themes()
        
        # Itt kezdodik a UI...
        with dpg.window(tag="main_window", label="Tic-Tac-Toe", no_resize=True, no_close=True):
            # "Beallitasok vagy mifene"
            with dpg.collapsing_header(label="Game Settings", default_open=True):
                with dpg.group(horizontal=True):
                    dpg.add_text("Game Mode: ")
                    dpg.add_radio_button(
                        items=["Against AI", "Two Players"], 
                        default_value="Against AI",
                        callback=lambda s, a, u: self.set_jatekMod(a),
                        horizontal=True
                    )
                
                # Nehezseg kivalaszto, csak Ai elleni meccsben lathato!
                with dpg.group(horizontal=True, tag="nehezseg_group"):
                    dpg.add_text("AI nehezseg: ")
                    dpg.add_radio_button(
                        items=["Easy", "Medium", "Hard"], 
                        default_value="Easy",
                        callback=lambda s, a, u: self.set_nehezseg(a),
                        horizontal=True
                    )

            dpg.add_separator()
            dpg.add_spacer(height=10)  # Added more vertical spacing
            
            # Cimsor - Better centering with calculated spacing
            with dpg.group(horizontal=True):
                dpg.add_spacer(width=170)
                dpg.add_text("TIC-TAC-TOE GAME", color=[255, 255, 255])
            
            dpg.add_separator()
            dpg.add_spacer(height=10)  # Added more vertical spacing
            
            # Jatek statusz - Center alignment improved
            with dpg.group(horizontal=True):
                dpg.add_spacer(width=190)
                dpg.add_text("Next Player: X", tag="game_status", color=[220, 220, 220])
            
            dpg.add_spacer(height=5)  # Added spacing
            
            # Jatek mezo
            with dpg.group(horizontal=True):
                dpg.add_spacer(width=75)
                
                with dpg.group():
                    # 3x3-as gomb grid
                    for row in range(3):
                        with dpg.group(horizontal=True):
                            for col in range(3):
                                pos = row * 3 + col
                                button = dpg.add_button(
                                    label="  ",
                                    tag=f"button_{pos}",
                                    width=100,
                                    height=100,
                                    callback=lambda s, a, u: self.handle_button_click(u),
                                    user_data=pos
                                )
                                dpg.bind_item_theme(button, "button_theme")
            
            dpg.add_separator()
            dpg.add_spacer(height=10)  # Added more vertical spacing
            
            # Eredmenyek - Better centering
            with dpg.group(horizontal=True):
                dpg.add_spacer(width=130)
                dpg.add_text("X: 0 wins   |   O: 0 wins   |   0 ties", 
                             tag="pontszam_text", color=[200, 200, 200])
            
            dpg.add_spacer(height=5)  # Added spacing
            
            # Uj jatek gomb
            with dpg.group(horizontal=True):
                dpg.add_spacer(width=155)
                reset_button = dpg.add_button(
                    label="New Game",
                    callback=lambda: self.handle_reset_game(),
                    width=150
                )
                dpg.bind_item_theme(reset_button, "reset_button_theme")
            
            dpg.add_spacer(height=10)  # Added more vertical spacing
            
            # Tutorial
            with dpg.collapsing_header(label="How to Play", default_open=False):
                dpg.add_text("1. Click on an empty space to place an X", color=[130, 130, 130])
                dpg.add_text("2. The computer will automatically place an O", color=[130, 130, 130])
                dpg.add_text("3. First to get 3 in a row, column, or diagonal wins", color=[130, 130, 130])

        
        # Font setup for better typography
        with dpg.font_registry():
            # Try to find appropriate fonts based on OS
            possible_fonts = [
                # Windows fonts
                "C:/Windows/Fonts/ariblk.ttf",  # Arial Black
                "C:/Windows/Fonts/calibrib.ttf",  # Calibri Bold
                "C:/Windows/Fonts/segoeui.ttf",  # Segoe UI
                # Mac fonts
                "/Library/Fonts/Arial Bold.ttf",
                "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
                # Linux fonts
                "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
                "/usr/share/fonts/TTF/DejaVuSans-Bold.ttf",
                "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
            ]
            
            # Try each font until one works
            for font_path in possible_fonts:
                if os.path.exists(font_path):
                    try:
                        # Use larger font size for better visibility (THICC FONT)
                        default_font = dpg.add_font(font_path, 16)
                        dpg.bind_font(default_font)
                        break
                    except Exception:
                        continue
        
        # Center the window content
        dpg.set_primary_window("main_window", True)
        
        # Loop inditasa
        dpg.set_viewport_resize_callback(self.on_resize)
    
    def handle_button_click(self, position):
        """Handle click on game button."""
        self.game.make_move(position)
        self.update_ui()

    def handle_reset_game(self):
        """Handle click on reset button."""
        self.game.reset_game()
        
        # Win eseten resetelni kell a zold feedback szineket
        for i in range(9):
            dpg.bind_item_theme(f"button_{i}", "button_theme")
            
        self.update_ui()
        
    def set_jatekMod(self, value):
        if value == "Against AI":
            self.game.jatekMod = "ai"
            dpg.configure_item("nehezseg_group", show=True)
        else:
            self.game.jatekMod = "two_player"
            dpg.configure_item("nehezseg_group", show=False)
        self.game.reset_game()

    def set_nehezseg(self, value):
        self.game.nehezseg = value.lower()
    
    def on_resize(self):
        dpg.set_primary_window("main_window", True)
    
    def update_ui(self):
        """Update the UI to reflect current game state."""
        # Eredmenyjelzo update, meg minden UI text with color feedback
        if self.game.gameOver:
            if self.game.nyertes == 'Tie':
                status = "It's a Draw!"
                status_color = [255, 165, 0]  # Orange for tie
            else:
                status = f"Winner: {self.game.jatekosokJelolese[self.game.nyertes]}"
                status_color = [0, 200, 0]    # Green for winner
        else:
            status = f"Next Player: {self.game.jatekosokJelolese[self.game.jelenlegiJatekos]}"
            status_color = [220, 220, 220]    # Default color

        dpg.set_value("game_status", status)
        dpg.configure_item("game_status", color=status_color)

        # Eredmeny update
        dpg.set_value("pontszam_text", 
                    f"X: {self.game.pontszam['X']} wins   |   O: {self.game.pontszam['O']} wins   |   {self.game.pontszam['Tie']} ties")
        
        # Gombok frissitese
        for i in range(9):
            button_text = "  " if self.game.tabla[i] == ' ' else self.game.jatekosokJelolese[self.game.tabla[i]]
            dpg.set_item_label(f"button_{i}", button_text)
            
            # Color feedback jatekosonkent
            if self.game.tabla[i] == 'X':
                dpg.bind_item_theme(f"button_{i}", "x_button_theme")
            elif self.game.tabla[i] == 'O':
                dpg.bind_item_theme(f"button_{i}", "o_button_theme")
            
        # Winning combination gets special highlighting
        if self.game.gameOver and self.game.nyertes != 'Tie':
            for pos in self.game.winningCombo:
                dpg.bind_item_theme(f"button_{pos}", "nyertes_button_theme")
    
    def run(self):
        dpg.show_viewport()
        
        # Jatek loopolasa
        while dpg.is_dearpygui_running():
            # Ai kovetkezik vagy jatekos?
            if (not self.game.gameActive and self.game.animActive and 
                time.time() - self.game.lastMoveTime > 0.7):  # Kis delay mintha az AI "gondolkozna" xD
                self.game.ai_move()
                self.update_ui()
            
            dpg.render_dearpygui_frame()
        
        dpg.destroy_context()