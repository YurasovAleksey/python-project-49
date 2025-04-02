from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def get_progression_array(first_item, step, length):
    progression_array = []

    for i in range(length):
        progression_array.append(str(first_item + step * i))

    return progression_array


def get_data():
    first_item = randint(1, 10)
    step = randint(1, 10)
    length = randint(5, 10)
    progression = get_progression_array(first_item, step, length)
    index_of_invis_num = randint(0, length - 1)

    right_answer = str(progression[index_of_invis_num])
    progression[index_of_invis_num] = '..'
    question = str.join(" ", progression)

    return (question, right_answer)
