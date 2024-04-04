# Eight8Puzzle
# 8 Puzzle Game and Solver

## Description
This Python program includes both a simple 8 puzzle game and a solver that finds the optimal solution path using a search algorithm. The game allows players to interactively solve the puzzle, while the solver automatically finds the solution from any given start state to the goal state.

## Installation
Ensure you have Python 3.x and Pygame installed. Run the game using `python 8_puzzle_game.py` and the solver using `python 8_puzzle_solver.py`.

## Game Controls
- Click on a tile adjacent to the empty space to move it.
- Try to solve the puzzle in the fewest moves possible.

## Files
1. `8_puzzle_game.py`: Contains the main game logic and graphical interface using Pygame.
2. `8_puzzle_solver.py`: Contains the puzzle solving logic using a search algorithm.
3. `icon.png`: Icon file for the game window.
4. `move_sound.wav`: Sound effect for tile movements.
5. `solved_sound.wav`: Sound effect for solving the puzzle.

---

### 8_puzzle_game.py

#### Functions
1. `is_movable(row, col)`
   - **Input:** `row` and `col` indices of a tile
   - **Output:** Boolean indicating if the tile can be moved into the empty space
   - **Purpose:** Checks if a tile at a given position can be moved into the empty space.

2. `is_solved()`
   - **Output:** Boolean indicating if the puzzle is solved
   - **Purpose:** Checks if the current board state matches the solved state.

3. Game Loop
   - **Purpose:** Handles game events, updates the display, and checks for a solved puzzle.
   - **Events:** Handles mouse clicks for moving tiles.
   - **Display:** Draws the board, tiles, move counter, and the "Solved!" message if the puzzle is solved.

---

### 8_puzzle_solver.py

#### Functions
1. `StackFrontier`, `QueueFrontier` (inheritance from `StackFrontier`)
   - **Purpose:** Manage the order of accessing nodes in the search algorithm.
   - **`add(node)`:** Adds a node to the frontier.
   - **`contains_state(state)`:** Checks if a state is in the frontier.
   - **`empty()`:** Checks if the frontier is empty.
   - **`remove()`:** Removes and returns a node from the frontier.

2. `Puzzle` Class
   - **Purpose:** Represents the 8 puzzle problem and implements the search algorithm.
   - **`neighbors(state)`:** Returns a list of neighboring states for a given state.
   - **`print()`:** Prints the start state, goal state, number of explored states, and the solution path.
   - **`does_not_contain_state(state)`:** Checks if a state is not already explored.
   - **`solve()`:** Solves the puzzle using a search algorithm (BFS) and sets the solution path.

3. `Node` Class
   - **Purpose:** Represents a node in the search tree.
   - **`__init__(state, parent, action)`:** Initializes a node with a state, parent node, and action taken.

4. Main Block
   - **Purpose:** Creates a puzzle instance with a start state, goal state, and solves it.
   - **`start` and `goal`**: Initial and goal states of the puzzle.
   - **`startIndex` and `goalIndex`**: Indices of the empty tile in the start and goal states.
   - **`p.solve()`**: Solves the puzzle and stores the solution path.
   - **`p.print()`**: Prints the solution path and other details of the puzzle.
   - **`time.sleep(60*1000)`**: Keeps the program running for a long time to allow viewing the output.

