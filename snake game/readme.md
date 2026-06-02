#Snake Game

A classic Snake game built with Python and Pygame.

## Overview

Guide the snake around the grid to eat snacks and grow longer. Avoid colliding with yourself — the snake wraps around the edges of the board, so there are no walls to worry about.

## Features

- Smooth grid-based movement with keyboard controls
- Snake wraps around screen edges
- Score display on game over
- Snack spawns randomly, never on the snake's body
- Snake head rendered with eyes for a fun visual touch

## Requirements

- Python 3.x
- `pygame`
- `tkinter` (included in most standard Python installations)

## Installation

1. Clone or download this repository.
2. Install the required dependency:

```bash
pip install pygame
```

## Running the Game

```bash
python snake-game.py
```

## How to Play

| Key | Action |
|-----|--------|
| ← Arrow | Move Left |
| → Arrow | Move Right |
| ↑ Arrow | Move Up |
| ↓ Arrow | Move Down |

- Eat the **green snack** to grow longer and increase your score.
- The game ends if the snake **runs into itself**.
- Your score equals the **length of the snake** at the time of collision.
- After game over, the snake resets and you can play again.

## Project Structure

```
snake-game.py
├── class cube       # Represents a single grid cell (snake segment or snack)
├── class snake      # Manages the snake's body, movement, and growth
├── drawGrid()       # Renders the background grid
├── redrawWindow()   # Redraws the full game window each frame
├── randomSnack()    # Generates a snack at a random unoccupied position
├── message_box()    # Displays the game over popup using tkinter
└── main()           # Game loop and initialisation
```

## Configuration

Two constants at the top of `main()` control the board:

| Variable | Default | Description |
|----------|---------|-------------|
| `width` | `500` | Window size in pixels |
| `rows` | `20` | Number of grid rows/columns |

Adjust these to change the board size and cell density.
