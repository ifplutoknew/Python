# Connect Four

A two-player Connect Four game built with Python and Pygame.

## Overview

This is a classic Connect Four implementation where two players take turns dropping coloured pieces into a 7-column, 6-row grid. The first player to connect four of their pieces horizontally, vertically, or diagonally wins.

## Requirements

- Python 3.x
- [NumPy](https://numpy.org/)
- [Pygame](https://www.pygame.org/)

Install dependencies with:

```bash
pip install numpy pygame
```

## How to Run

```bash
python connect_game.py
```

## How to Play

- **Player 1** — Red pieces
- **Player 2** — Yellow pieces

1. Move your mouse left and right over the board to aim at a column. A preview piece will follow your cursor.
2. Click to drop your piece into that column. It falls to the lowest available row.
3. Players alternate turns until one player connects four pieces in a row (horizontally, vertically, or diagonally).
4. The winner's name is displayed on screen and the game closes automatically after 3 seconds.

## Game Rules

- Pieces fall to the lowest empty row in the selected column.
- You cannot place a piece in a full column.
- Win conditions: four consecutive pieces in a **row**, **column**, or **diagonal**.

## Project Structure

```
connect_game.py
├── create_board()         # Initialises a 6×7 board of zeros
├── drop_piece()           # Places a piece at the given row/column
├── is_valid_location()    # Checks if a column has space remaining
├── get_next_open_row()    # Finds the lowest empty row in a column
├── print_board()          # Prints the board to the console (flipped upright)
├── winning_move()         # Checks all win conditions for a given piece
└── draw_board()           # Renders the board and pieces using Pygame
```

## Controls

| Action | Input |
|---|---|
| Aim | Move mouse left/right |
| Drop piece | Left mouse click |
| Quit | Close the window |
