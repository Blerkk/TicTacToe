from setuptools import setup, find_packages

setup(
    name="TicTacToe",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "dearpygui>=1.8.0",
    ],
    author="Bagdi Máté Olivér",
    author_email="bagdimate@gmail.com",
    description="A simple Tic-Tac-Toe game with GUI",
    keywords="game, tic-tac-toe, gui",
    url="https://github.com/Blerkk/TicTacToe",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'TicTacToe=TicTacToe.main:main',
        ],
    },
    tests_require=[
        'pytest',
    ],
    setup_requires=[
        'pytest-runner',
    ],
)