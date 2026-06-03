# Pong Game

A classic Pong game built with Python's `turtle` graphics module. Play in **single-player mode against an AI opponent** or **two-player mode on the same keyboard**!

## Features

- **Two game modes**: Single-player vs AI or two-player multiplayer
- **AI opponent**: Intelligent computer player with adjustable difficulty
- **Score tracking**: Real-time score display at the top of the screen
- **Win condition**: First player to reach 10 points wins!
- **Ball physics**: Ball bounces off walls and paddles with increasing speed
- **Sound effects**: Audio feedback on paddle and wall collisions
- **Simple controls**: Easy keyboard controls for smooth gameplay

## Requirements

- Python 3.x
- Windows OS (for sound support)
- Turtle graphics module (included with Python)
- Sound file: `sounds/bounce.wav`

## Installation & Setup

1. Ensure all files are in the correct directory structure:
   ```
   pong-game/
   ├── pong-game.py
   └── sounds/
       └── bounce.wav
   ```

2. Run the game:
   ```bash
   python pong-game.py
   ```

## Game Mode Selection

When you start the game, you'll see a prompt to select your game mode:

- **Press `1`** for **Single Player** (you vs AI)
- **Press `2`** for **Two Player** (local multiplayer)

## Controls

| Player | Move Up | Move Down |
|--------|---------|-----------|
| **Player A** (Green, Left Paddle) | `W` | `S` |
| **Player B** (Blue, Right Paddle) | `↑` (Up Arrow) | `↓` (Down Arrow) |

*In single-player mode, the AI automatically controls Player B (blue paddle).*

## How to Play

1. **Objective**: Keep the ball in play by hitting it with your paddle. The ball bounces off the top and bottom walls automatically.
2. **Scoring**: Each time your opponent fails to hit the ball and it passes their paddle, you score 1 point.
3. **Ball Physics**: The ball starts at the center and moves diagonally. Each successful paddle hit increases the ball's speed by 2%.
4. **Winning**: The **first player to reach 10 points wins** the game. A "Game Over" message displays the winner.
5. **Replay**: Press `1` or `2` after the game ends to start a new game with fresh scores.

## Single-Player Mode (vs AI)

- **Difficulty**: The AI has ~65% accuracy, making it challenging but beatable
- **AI Behavior**: The AI only moves when the ball is heading towards it
- **Strategy**: The AI has slight imperfections—look for patterns to exploit!

## Gameplay Tips

- **React quickly** when the ball approaches your paddle
- **Position your paddle in the middle** to maximize hit opportunities
- **The ball accelerates** with each paddle collision, so the game gets faster
- **In single-player**: Watch the AI's movement patterns—it's beatable!
- **In two-player**: Communicate and coordinate with your opponent

## Technical Details

- **Game Window**: 800×600 pixels with black background
- **Ball Speed**: Starts at 0.08 units per frame, increases by 2% (×1.02) on each paddle hit
- **Paddle Dimensions**: 20 pixels wide, 100 pixels tall
- **Win Score**: 10 points (editable in code)
- **AI Accuracy**: 65% (adjustable for difficulty)
- **Sound**: Uses Windows `winsound` module for audio playback

## Project Structure

```
pong-game/
├── pong-game.py          # Main game script
├── readme.md             # This file
└── sounds/
    └── bounce.wav        # Bounce sound effect
```

## Troubleshooting

**Sound not playing?**
- Ensure `sounds/bounce.wav` exists in the `pong-game/` directory
- Check that your speakers/audio is enabled on your system
- The script auto-detects the sound file path, so verify it exists

**Game mode won't start?**
- Make sure to press `1` or `2` to select a game mode before playing
- The game will wait for your selection before starting

**Game runs slowly?**
- Close other applications to free up CPU resources
- The `turtle` module can be resource-intensive on some systems

**Not working on Mac/Linux?**
- The `winsound` module is Windows-only
- Comment out or replace the `winsound.PlaySound()` lines to run on other systems

## Customization

To modify the game, edit these values in `pong-game.py`:

| Setting | Variable | Default | Effect |
|---------|----------|---------|--------|
| **Win Score** | `WIN_SCORE` | `10` | Points needed to win |
| **AI Accuracy** | `random.random() < 0.65` | `0.65` | Change to `0.9` for harder AI, `0.5` for easier |
| **Ball Speed** | `ball.dx` / `ball.dy` | `0.08` | Increase for faster gameplay |
| **Speed Increase on Hit** | `ball.dx *= -1.02` | `1.02` | Increase to `1.05` for faster acceleration |
| **Screen Size** | `wn.setup(width=800, height=600)` | `800x600` | Adjust dimensions |
| **Colors** | `paddle_a.color()`, `paddle_b.color()` | Green/Blue | Customize paddle colors |

## License

Free to use and modify for personal projects.
