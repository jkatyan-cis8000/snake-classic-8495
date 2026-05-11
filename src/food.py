import random


class Food:
    def __init__(self, board_width: int = 20, board_height: int = 20):
        self.board_width = board_width
        self.board_height = board_height
        self.position = (0, 0)
        self.respawn([])

    def get_position(self) -> tuple[int, int]:
        return self.position

    def respawn(self, snake_positions: list[tuple[int, int]]) -> None:
        while True:
            x = random.randint(0, self.board_width - 1)
            y = random.randint(0, self.board_height - 1)
            position = (x, y)
            if position not in snake_positions:
                self.position = position
                break

    def check_collision(self, head_position: tuple[int, int]) -> bool:
        return head_position == self.position


if __name__ == "__main__":
    food = Food()
    print(f"Food position: {food.get_position()}")
