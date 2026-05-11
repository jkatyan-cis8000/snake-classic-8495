# ARCHITECTURE.md

Written by team-lead before spawning teammates. This is the shared blueprint —
teammates read it to understand what they are building and how their module fits.
Update it when the structure changes; do not let it drift from the actual code.

## Module Structure

- src/snake_game.py: Main game engine - manages game state, loop, scoring, difficulty levels
- src/snake.py: Snake entity - position tracking, movement, growth, collision detection with self
- src/food.py: Food entity - spawn location, position tracking
- src/board.py: Game board - boundary management, grid representation, collision with walls
- src/ui.py: User interface - terminal rendering, input handling, score display
- src/game_runner.py: Game orchestration - creates and coordinates all components, runs main loop

## Interfaces

### snake_game.py
- `SnakeGame(difficulty: str = "medium")`: Constructor accepts difficulty level
- `start(): None`: Initialize and start the game loop
- `is_over(): bool`: Check if game has ended
- `get_score(): int`: Return current score
- `update(): bool`: Process one game tick, returns True if game continues

### snake.py
- `Snake(initial_position: tuple[int, int] = (10, 10), initial_direction: str = "RIGHT")`: Initialize snake
- `move(direction: str): None`: Update direction and move forward
- `grow(): None`: Add new segment to tail
- `get_head_position() -> tuple[int, int]`: Get head coordinates
- `get_all_positions() -> list[tuple[int, int]]`: Get all body segment positions
- `check_self_collision() -> bool`: Detect if head touches body segment

### food.py
- `Food(board_width: int = 20, board_height: int = 20)`: Spawn food on board
- `get_position() -> tuple[int, int]`: Get current food position
- `respawn(snake_positions: list[tuple[int, int]]) -> None`: Move to new random position not on snake
- `check_collision(head_position: tuple[int, int]) -> bool`: Detect if snake head eats food

### board.py
- `Board(width: int = 20, height: int = 20)`: Initialize grid dimensions
- `is_inside_bounds(position: tuple[int, int]) -> bool`: Check if position is within boundaries
- `get_dimensions() -> tuple[int, int]`: Get board width and height

### ui.py
- `render_board(snake: Snake, food: Food, score: int, game_over: bool) -> None`: Draw game state to terminal
- `get_user_input() -> str | None`: Return direction key ("UP", "DOWN", "LEFT", "RIGHT") or None
- `display_score(score: int) -> None`: Show current score
- `display_game_over(score: int) -> None`: Show final score and game over message

### game_runner.py
- `run_game(difficulty: str = "medium") -> int`: Create components, run game, return final score
- `DIFFICULTIES: dict[str, float]`: Mapping of difficulty to speed (lower = faster)

## Shared Data Structures

### Direction constants
- `"UP"`, `"DOWN"`, `"LEFT"`, `"RIGHT"` - string-based cardinal directions

### Position format
- `tuple[int, int]`: (x, y) coordinates where (0, 0) is top-left

### Difficulty levels
- `"easy"`: 200ms per frame
- `"medium"`: 100ms per frame
- `"hard"`: 50ms per frame

### Game state
- `score`: int - count of food items eaten
- `game_over`: bool - True when snake hits wall or itself

## External Dependencies

- `curses` (Python standard library): Terminal UI for rendering and input handling
- No external packages required - uses Python 3 standard library only
