# RPG Character Display

>  **Active Development** — Displaying animated RPG character stats with visual bars.

A Pygame-based RPG character display featuring animated stat visualization with level bars and a live character sprite.

## Features

- **Animated Character Sprite** - Smooth bobbing and arm swing animations
- **Visual Stat Bars** - Progress bars for all character attributes
- **Core Stats**:
  - Strength (STR) - Red bar
  - Intelligence (INT) - Blue bar
  - Charisma (CHA) - Magenta bar
- **Resource Bars**:
  - Health - Green bar
  - Mana - Cyan bar
  - Experience - Orange bar
- **Real-time Display** - 60 FPS animation

## Usage

Run the script:

```bash
python RGP_Character.py
```

The application will display a window showing:
- **Left side**: Character stats with visual progress bars
- **Right side**: Animated character sprite with smooth movement

### Character Details

The default character "Hero" displays:
- Level: 5
- Strength: 15/20
- Intelligence: 12/20
- Charisma: 14/20
- Health: 85/100
- Mana: 60/75
- Experience: 65/100

## Customization

Edit the `main()` function to change:
- Character name
- Stat values
- Max values for health, mana, and experience
- Character color (change the `color` parameter in `draw_character_sprite`)

### Color Customization

Modify the color tuple (R, G, B) in the sprite drawing call:
```python
draw_character_sprite(screen, 420, 200, frame, color=(100, 200, 255))  # Blue
```

## Requirements

- Python 3.6+
- Pygame

