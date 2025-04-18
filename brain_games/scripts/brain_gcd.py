from brain_games.games.brain_gcd import DESCRIPTION, get_data
from brain_games.index import run_game


def start_gcd_game():
    run_game(get_data, DESCRIPTION)


def main():
    start_gcd_game()


if __name__ == "__main__":
    main()
