import prompt

from .cli import welcome_user


def run_game(get_data, DESCRIPTION):
    user_name = welcome_user()
    print(DESCRIPTION)

    ROUNDS = 3

    for _ in range(ROUNDS):
        (question, right_answer) = get_data()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == right_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f"Correct answer was '{right_answer}'.")
            print(f"Let's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')
