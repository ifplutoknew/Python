# Pong Game

A two-player Pong game built with Python's `turtle` graphics module.

## Requirements

- Python 3.x
- Windows OS (required for sound via `winsound`)
- Sound files (`.wav`) for bounce effects

## Setup

1. Clone or download the project files.
2. Place your sound files in the following directory (or update the paths in the code):
   ```
   C:pong-game\sounds\bounce.wav
   ```
3. Run the game:
   ```bash
   python pong-game.py
   ```

## Controls

| Player | Move Up | Move Down |
|--------|---------|-----------|
| Player A (Left, Green) | `W` | `S` |
| Player B (Right, Blue) | `↑` Up Arrow | `↓` Down Arrow |

## How to Play

- Each player controls a paddle on their side of the screen.
- The ball bounces off the top and bottom walls.
- If the ball passes your opponent's paddle, **you score a point**.
- The current score is displayed at the top of the screen.
- The game runs indefinitely — play to any score you like!

## Project Structure

```
pong-game/
├── pong-game.py
└── sounds/
    └── bounce.wav
```

## Notes

- Sound playback uses the `winsound` module, which is **Windows-only**. On macOS or Linux, remove or replace the `winsound.PlaySound(...)` calls.
- Ball speed is set to `0.08` units per frame. You can increase `ball.dx` and `ball.dy` in the code to make the game faster.
