import time

from .snake import Snake
from .food import Food
from .board import Board
from .ui import render_board, get_user_input, display_game_over


DIFFICULTIES = {
    "easy": 0.2,
    "medium": 0.1,
    "hard": 0.05,
}


class SnakeGame:
    def __init__(self, difficulty: str = "medium"):
        self.board = Board()
        self.snake = Snake()
        self.food = Food(*self.board.get_dimensions())
        self.score = 0
        self.game_over = False
        self.speed = DIFFICULTIES.get(difficulty, DIFFICULTIES["medium"])

    def start(self) -> None:
        while not self.game_over:
            self.update()

    def is_over(self) -> bool:
        return self.game_over

    def get_score(self) -> int:
        return self.score

    def update(self) -> bool:
        direction = get_user_input()
        if direction:
            self.snake.move(direction)
        else:
            self.snake.move(self.snake.get_direction())

        head = self.snake.get_head_position()

        if not self.board.is_inside_bounds(head):
            self.game_over = True
            return False

        if self.snake.check_self_collision():
            self.game_over = True
            return False

        if self.food.check_collision(head):
            self.score += 1
            self.snake.grow()
            self.food.respawn(self.snake.get_all_positions())

        render_board(self.snake, self.food, self.board, self.score, self.game_over)
        time.sleep(self.speed)
        return not self.game_over


if __name__ == "__main__":
    game = SnakeGame("medium")
    game.start()
