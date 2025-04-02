from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_greatest_divider(num1, num2):
    if num1 == num2:
        return num1
    
    first_number = num1
    second_number = num2

    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number %= second_number
        else:
            second_number %= first_number
    
    return first_number + second_number


def get_data():
    number1 = randint(1, 20)
    number2 = randint(1, 20)
    question = f'{number1} {number2}'
    right_answer = str(get_greatest_divider(number1, number2))

    return (question, right_answer)
