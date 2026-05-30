# Maze Path Finder

A terminal-based shortest path visualizer that solves a maze using the **Breadth-First Search (BFS)** algorithm, with a step-by-step animated display powered by Python's `curses` library.

## Demo

```
# O # # # # # # #
#               #
#   # #   # #   #
#   #       #   #
#   #   #   #   #
#   #   #   #   #
#   #   #   # # #
#               #
# # # # # # # X #
```

The algorithm finds the shortest path from `O` (start) to `X` (end), highlighting the visited path in real time.

## Features

- **BFS algorithm** — guarantees the shortest path
- **Live terminal animation** — watch the search unfold step by step
- **Color-coded display** — path shown in red, maze walls and spaces in blue

## Requirements

- Python 3.x
- Unix/Linux/macOS terminal (or Windows with `windows-curses`)

> **Windows users:** Install the `windows-curses` package:
> ```bash
> pip install windows-curses
> ```

## Usage

```bash
python path_finder.py
```

The maze will render in your terminal and animate the BFS search. Press any key to exit once the path is found.

## How It Works

1. The maze is defined as a 2D list of characters:
   - `#` — wall
   - ` ` — open path
   - `O` — start position
   - `X` — end position

2. BFS explores neighbors (up, down, left, right) level by level, tracking the path taken to reach each cell.

3. When `X` is reached, the shortest path is returned and highlighted in the terminal.

## File Structure

```
path_finder.py   # Main script — maze definition, BFS logic, and curses rendering
```

## Customization

You can modify the `maze` list in `path_finder.py` to create your own maze. Just make sure:
- The maze is a rectangular 2D list
- There is exactly one `O` (start) and one `X` (end)
- The maze is surrounded by `#` walls

## Algorithm Overview

```
BFS(start):
  queue ← [(start, [start])]
  visited ← {start}

  while queue is not empty:
    current, path ← dequeue
    if current == end: return path

    for each neighbor of current:
      if neighbor not visited and not a wall:
        enqueue (neighbor, path + [neighbor])
        mark neighbor as visited
```

BFS guarantees the **shortest path** because it explores all positions at distance `n` before any at distance `n+1`.
