"""
UI themes module for the Tic-Tac-Toe game.
Contains functions to set up the visual appearance of the game.
"""

import dearpygui.dearpygui as dpg

def setup_themes():
    """
    Set up all UI themes for the game.
    Returns a dictionary containing all theme tags.
    """
    # Main theme (dark iOS-inspired)
    with dpg.theme() as global_theme:
        with dpg.theme_component(dpg.mvAll):
            # Dark background
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, [30, 30, 35])
            dpg.add_theme_color(dpg.mvThemeCol_Text, [220, 220, 220])
            # Round corners
            dpg.add_theme_style(dpg.mvStyleVar_WindowRounding, 8)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 8)
            dpg.add_theme_style(dpg.mvStyleVar_GrabRounding, 8)
            
    # Default button theme
    with dpg.theme(tag="button_theme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, [60, 60, 70])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [80, 80, 90])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [90, 90, 100])
            dpg.add_theme_color(dpg.mvThemeCol_Text, [220, 220, 220])
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 12)
            # Make text bigger for better visibility
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 14, 14)
            
    # Player X button theme (Light Blue)
    with dpg.theme(tag="x_button_theme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, [30, 120, 180])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [40, 130, 190])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [50, 140, 200])
            dpg.add_theme_color(dpg.mvThemeCol_Text, [240, 240, 240])
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 12)
            # Make text bigger for better visibility (THICC FONT)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 14, 14)
            
    # Player O button theme (Light Red)
    with dpg.theme(tag="o_button_theme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, [180, 60, 60])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [190, 70, 70])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [200, 80, 80])
            dpg.add_theme_color(dpg.mvThemeCol_Text, [240, 240, 240])
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 12)
            # Make text bigger for better visibility (THICC FONT)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 14, 14)
            
    # nyertes button theme
    with dpg.theme(tag="nyertes_button_theme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, [0, 150, 70])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [0, 170, 90])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [0, 190, 110])
            dpg.add_theme_color(dpg.mvThemeCol_Text, [255, 255, 255])
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 12)
            # Make text bigger for better visibility (THICC FONT)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 14, 14)
            
    # Reset button theme
    with dpg.theme(tag="reset_button_theme"):
        with dpg.theme_component(dpg.mvButton):
            dpg.add_theme_color(dpg.mvThemeCol_Button, [70, 100, 200])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, [90, 120, 220])
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, [110, 140, 240])
            dpg.add_theme_color(dpg.mvThemeCol_Text, [240, 240, 240])
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 12)
    
    dpg.bind_theme(global_theme)
    
    return {
        "global_theme": global_theme,
        "button_theme": "button_theme",
        "x_button_theme": "x_button_theme",
        "o_button_theme": "o_button_theme",
        "nyertes_button_theme": "nyertes_button_theme",
        "reset_button_theme": "reset_button_theme"
    }