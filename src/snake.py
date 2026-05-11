import random


class Snake:
    def __init__(
        self,
        initial_position: tuple[int, int] = (10, 10),
        initial_direction: str = "RIGHT",
    ):
        self._body = [initial_position]
        self._direction = initial_direction
        self._growth_pending = 0

    def move(self, direction: str) -> None:
        self._direction = direction
        head = self._body[0]
        new_head = self._get_new_position(head, direction)

        if self._growth_pending > 0:
            self._body.insert(0, new_head)
            self._growth_pending -= 1
        else:
            self._body.insert(0, new_head)
            self._body.pop()

    def grow(self) -> None:
        self._growth_pending += 1

    def get_head_position(self) -> tuple[int, int]:
        return self._body[0]

    def get_direction(self) -> str:
        return self._direction

    def get_all_positions(self) -> list[tuple[int, int]]:
        return list(self._body)

    def check_self_collision(self) -> bool:
        head = self._body[0]
        return head in self._body[1:]

    def _get_new_position(
        self, position: tuple[int, int], direction: str
    ) -> tuple[int, int]:
        x, y = position
        if direction == "UP":
            return (x, y - 1)
        elif direction == "DOWN":
            return (x, y + 1)
        elif direction == "LEFT":
            return (x - 1, y)
        elif direction == "RIGHT":
            return (x + 1, y)
        return position
