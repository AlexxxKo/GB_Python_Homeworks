# Написать программу, которая принимает на вход число N
# и выдаёт последовательность из N членов

from random import randint


def get_number():
    is_num = False
    while not is_num:
        try:
            num = int(input('Введите целое положительное число: '))
            if num and num > 0:
                is_num = True
        except ValueError:
            print('Нужно ввести целое положительное число\n')
    return num


def set_sequence(n):
    sequence = []
    for i in range(n):
        sequence.append(randint(1, 100))
    return sequence


print(set_sequence(get_number()))
