from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    
    return True


def get_data():
    question = randint(1, 30)
    right_answer = 'yes' if is_prime(question) else 'no'

    return (question, right_answer)
