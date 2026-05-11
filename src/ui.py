import curses


def render_board(snake, food, board, score: int, game_over: bool) -> None:
    screen = curses.initscr()
    screen.clear()

    board_width, board_height = board.get_dimensions()

    for y in range(board_height):
        for x in range(board_width):
            position = (x, y)
            if position == food.get_position():
                screen.addch(y, x, "F")
            elif position in snake.get_all_positions():
                screen.addch(y, x, "O")
            else:
                screen.addch(y, x, " ")

    screen.addstr(board_height + 1, 0, f"Score: {score}")

    if game_over:
        screen.addstr(board_height + 2, 0, "GAME OVER")

    screen.refresh()


def get_user_input() -> str | None:
    screen = curses.initscr()
    screen.nodelay(True)
    key = screen.getch()
    screen.nodelay(False)

    if key == curses.KEY_UP:
        return "UP"
    elif key == curses.KEY_DOWN:
        return "DOWN"
    elif key == curses.KEY_LEFT:
        return "LEFT"
    elif key == curses.KEY_RIGHT:
        return "RIGHT"
    return None


def display_score(score: int) -> None:
    screen = curses.initscr()
    screen.clear()
    screen.addstr(0, 0, f"Score: {score}")
    screen.refresh()
    screen = curses.initscr()
    screen.addstr(0, 0, f"Score: {score}")
    screen.refresh()


def display_game_over(score: int) -> None:
    screen = curses.initscr()
    screen.clear()
    height, width = screen.getmaxyx()
    game_over_msg = "GAME OVER"
    final_score_msg = f"Final Score: {score}"

    screen.addstr(height // 2 - 1, (width - len(game_over_msg)) // 2, game_over_msg)
    screen.addstr(height // 2 + 1, (width - len(final_score_msg)) // 2, final_score_msg)
    screen.refresh()


if __name__ == "__main__":
    import curses
    import time

    class MockSnake:
        def __init__(self):
            pass

        def get_all_positions(self):
            return [(10, 10)]

        def get_head_position(self):
            return (10, 10)

    class MockFood:
        def get_position(self):
            return (5, 5)

    class Board:
        def get_dimensions(self):
            return (20, 20)

    def main(screen):
        curses.curs_set(0)
        snake = MockSnake()
        food = MockFood()
        board = Board()
        render_board(snake, food, board, 0, False)
        time.sleep(2)

    curses.wrapper(main)
