import prompt
from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
ROUNDS = 3


def main():
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(DESCRIPTION)

    for _ in range(ROUNDS):
        number = randint(1, 100)
        print(f'Question: {number}')

        right_answer = 'yes' if number % 2 == 0 else 'no'
        user_answer = prompt.string('Your answer: ')

        if user_answer == right_answer:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{right_answer}'.")
            print(f"Let's try again, {user_name}!")
            return
    
    print(f'Congratulations, {user_name}!')


if __name__ == "__main__":
    main()
