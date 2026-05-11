import curses

from .snake_game import SnakeGame, DIFFICULTIES


def run_game(difficulty: str = "medium") -> int:
    game = SnakeGame(difficulty)
    game.start()
    return game.get_score()


def main(screen) -> int:
    return run_game("medium")


if __name__ == "__main__":
    score = curses.wrapper(main)
    print(f"Final score: {score}")
