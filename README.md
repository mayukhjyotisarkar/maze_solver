# Maze Solver

A simple Python maze solver using the A* search algorithm.

## Project Structure

- `main.py` - entry point. Loads the maze, finds start and goal, runs A*, and prints the result.
- `astar.py` - A* implementation with Manhattan distance heuristic and grid neighbor handling.
- `maze.py` - maze definition and helper to locate start (`S`) and goal (`G`) positions.
- `visualize.py` - functions for printing the maze and drawing the path.

## How to Run

1. Install Python 3.8+ if you do not already have it.
2. Open a terminal in the project directory.
3. Run:

```bash
python main.py
```

## Maze Format

- `S` = start
- `G` = goal
- `#` = wall
- `.` = open space
- `*` = path marker added after solving

## Notes

- The current maze is hard-coded in `maze.py`.
- The solver uses 4-directional movement (up, down, left, right).
- If the maze has no valid path, the program prints `No path found!`.
