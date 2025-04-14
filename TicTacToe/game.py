"""
Game logic module for the Tic-Tac-Toe game.
Contains the TicTacToeGame class which handles the game state and rules.
"""

import random
import time

class TicTacToeGame:
    def __init__(self):
        self.tabla = [' ' for _ in range(9)]
        self.jelenlegiJatekos = 'X' 
        self.gameOver = False
        self.nyertes = None
        self.pontszam = {'X': 0, 'O': 0, 'Tie': 0}
        self.gameActive = True
        self.lastMoveTime = 0
        self.animActive = False
        self.winningCombo = []
        self.nehezseg = "easy"    # Default nehezseg deklaralasa
        self.jatekMod = "ai"     # Default jatek mod deklaralasa
        self.jatekosokJelolese = {'X': 'X', 'O': 'O'}

    def get_ai_move(self):
        if self.nehezseg == "easy":
            return self.random_move()
        elif self.nehezseg == "medium":
            # 70% intelligens, 30% random
            return self.best_move() if random.random() < 0.7 else self.random_move()
        else:
            return self.best_move()

    def random_move(self):
        uresHelyek = [i for i, spot in enumerate(self.tabla) if spot == ' ']
        return random.choice(uresHelyek) if uresHelyek else None

    def best_move(self):
        legjobbPontszam = float('-inf')
        move = None
        uresHelyek = [i for i, spot in enumerate(self.tabla) if spot == ' ']
        
        for spot in uresHelyek:
            # hely kiprobalasa
            self.tabla[spot] = 'O'
            pontszam = self.minimax(0, False)
            # visszavonas
            self.tabla[spot] = ' '
            
            if pontszam > legjobbPontszam:
                legjobbPontszam = pontszam
                move = spot
        
        return move

    def minimax(self, depth, is_maximizing):
        if self.check_nyertes_silent('O'):
            return 10 - depth
        elif self.check_nyertes_silent('X'):
            return depth - 10
        elif ' ' not in self.tabla:  # Dontetlen
            return 0
        
        if is_maximizing:
            legjobbPontszam = float('-inf')
            for i in range(9):
                if self.tabla[i] == ' ':
                    self.tabla[i] = 'O'
                    pontszam = self.minimax(depth + 1, False)
                    self.tabla[i] = ' '
                    legjobbPontszam = max(legjobbPontszam, pontszam)
            return legjobbPontszam
        else:
            legjobbPontszam = float('inf')
            for i in range(9):
                if self.tabla[i] == ' ':
                    self.tabla[i] = 'X'
                    pontszam = self.minimax(depth + 1, True)
                    self.tabla[i] = ' '
                    legjobbPontszam = min(legjobbPontszam, pontszam)
            return legjobbPontszam

    def check_nyertes_silent(self, player):
        # Nyero patternek (vizszintes, fuggoleges, atlos)
        patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # sorok
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # oszlopok
            [0, 4, 8], [2, 4, 6]              # atlok
        ]
        
        for pattern in patterns:
            if (self.tabla[pattern[0]] == player and
                self.tabla[pattern[0]] == self.tabla[pattern[1]] == self.tabla[pattern[2]]):
                return True
        
        return False
    
    def reset_game(self):
        self.tabla = [' ' for _ in range(9)]
        self.gameOver = False
        self.nyertes = None
        self.gameActive = True
        self.winningCombo = []
        self.jelenlegiJatekos = 'X'

    def check_nyertes(self):
        # Nyero patternek (vizszintes, fuggoleges, atlos)
        patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # sorok
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # oszlopok
            [0, 4, 8], [2, 4, 6]              # atlok
        ]
        
        for pattern in patterns:
            if (self.tabla[pattern[0]] != ' ' and
                self.tabla[pattern[0]] == self.tabla[pattern[1]] == self.tabla[pattern[2]]):
                self.nyertes = self.tabla[pattern[0]]
                self.gameOver = True
                self.winningCombo = pattern
                return True
        
        # Dontetlen-e?
        if ' ' not in self.tabla:
            self.gameOver = True
            self.nyertes = 'Tie'
            return True
        
        return False
    
    def make_move(self, position):
        if self.tabla[position] == ' ' and not self.gameOver and self.gameActive:
            self.tabla[position] = self.jelenlegiJatekos
            
            if self.check_nyertes():
                if self.nyertes != 'Tie':
                    self.pontszam[self.nyertes] += 1
                else:
                    self.pontszam['Tie'] += 1
            else:
                # Switch player
                self.jelenlegiJatekos = 'O' if self.jelenlegiJatekos == 'X' else 'X'
                
                # If next player is AI (O) and game isn't over and game mode is AI
                if self.jelenlegiJatekos == 'O' and not self.gameOver and self.jatekMod == "ai":
                    self.gameActive = False
                    self.lastMoveTime = time.time()
                    self.animActive = True

    def ai_move(self):
        if not self.gameOver:
            move = self.get_ai_move()
            if move is not None:
                self.tabla[move] = self.jelenlegiJatekos
                
                if self.check_nyertes():
                    if self.nyertes != 'Tie':
                        self.pontszam[self.nyertes] += 1
                    else:
                        self.pontszam['Tie'] += 1
                else:
                    # Csere vissza az elozo playerre
                    self.jelenlegiJatekos = 'X'
            
            self.gameActive = True
            self.animActive = False