from brain_games.games.brain_even import DESCRIPTION, get_data
from brain_games.index import run_game


def start_even_game():
    run_game(get_data, DESCRIPTION)


def main():
    start_even_game()


if __name__ == "__main__":
    main()
