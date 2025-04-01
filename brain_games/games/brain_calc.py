from random import randint

DESCRIPTION = 'What is the result of the expression?'


def computing(num1, num2, operator):
    match operator:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case _:
            raise ValueError(f'Operator: {operator} is wrong!')


def get_data():
    number1 = randint(0, 25)
    number2 = randint(0, 25)
    operators = ['+', '-', '*']
    operator = operators[randint(0, 2)]

    question = f'{number1} {operator} {number2}'
    right_answer = str(computing(number1, number2, operator))

    return (question, right_answer)
