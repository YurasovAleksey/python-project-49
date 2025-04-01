from brain_games.games.brain_calc import DESCRIPTION, get_data
from brain_games.index import run_game


def start_calc_game():
    run_game(get_data, DESCRIPTION)


def main():
    start_calc_game()


if __name__ == "__main__":
    main()