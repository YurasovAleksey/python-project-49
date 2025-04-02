from brain_games.games.brain_progression import DESCRIPTION, get_data
from brain_games.index import run_game


def start_progression_game():
    run_game(get_data, DESCRIPTION)


def main():
    start_progression_game()


if __name__ == "__main__":
    main()
