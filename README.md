# 🎮 Tic-Tac-Toe Game 🎲

A modern Tic-Tac-Toe game with a polished graphical user interface built using DearPyGui. ✨

![Game Screenshot](https://raw.githubusercontent.com/Blerkk/TicTacToe/refs/heads/main/screenshot.png)

## ✅ Features

- **Multiple Game Modes** 🔄:
  - Play against AI with three difficulty levels (Easy, Medium, Hard) 🤖
  - Two-player mode for playing with a friend 👫
  
- **Smart AI Opponent** 🧠:
  - Implemented with minimax algorithm 🔍
  - Varying difficulty levels to match your skill 📊
  
- **Modern UI** 🖌️:
  - Clean and intuitive interface 🎨
  - Visual feedback with color-coded moves 🌈
  - Winning combinations are highlighted ✨
  
- **Score Tracking** 📝:
  - Keep track of wins and ties 🏆
  - Statistics persist during your gaming session 📊

## 📥 Installation

### Option 1: Using pip 🛠️

```bash
pip install git+https://github.com/Blerkk/TicTacToe.git
```

After installation, you can run the game with: 🚀

```bash
TicTacToe
```

### Option 2: From source 💻

```bash
# Clone the repository
git clone https://github.com/Blerkk/TicTacToe.git
cd TicTacToe

# Set up virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the game
python main.py
```

## 🎯 How to Play

1. Select game mode (Against AI or Two Players) 🤖👫
2. If playing against AI, choose the difficulty level 🔢
3. Click on an empty square to place your mark (X goes first) ❌⭕
4. The first player to get three marks in a row (horizontally, vertically, or diagonally) wins 🏆
5. If all squares are filled with no winner, the game ends in a tie 🤝

## 👨‍💻 Development

### Project Structure 📁

```
TicTacToe/
├── TicTacToe/
│   ├── __init__.py
│   ├── game.py      # Game logic
│   ├── themes.py    # UI styling
│   └── ui.py        # User interface
├── tests/
│   ├── __init__.py
│   ├── test_game.py # Game logic tests
│   └── test_ui.py   # UI tests
├── main.py          # Entry point
├── setup.py
├── requirements.txt
└── README.md
```

### Running Tests 🧪

```bash
python -m pytest
```

## 📋 Requirements

- Python 3.6+ 🐍
- DearPyGui 1.8.0+ 🖼️

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details. ⚖️

## 🙏 Acknowledgments

- [DearPyGui](https://github.com/hoffstadt/DearPyGui) - The amazing immediate mode GUI library for Python ✨
