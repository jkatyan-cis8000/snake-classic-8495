class Board:
    def __init__(self, width: int = 20, height: int = 20):
        self.width = width
        self.height = height

    def is_inside_bounds(self, position: tuple[int, int]) -> bool:
        x, y = position
        return 0 <= x < self.width and 0 <= y < self.height

    def get_dimensions(self) -> tuple[int, int]:
        return (self.width, self.height)


if __name__ == "__main__":
    board = Board()
    print(f"Board dimensions: {board.get_dimensions()}")
    print(f"Is (10, 10) inside bounds: {board.is_inside_bounds((10, 10))}")
    print(f"Is (-1, 10) inside bounds: {board.is_inside_bounds((-1, 10))}")
