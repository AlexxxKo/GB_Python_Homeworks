# Задать список из N элементов, заполненный числами из промежутка [-N, N].
# Найти произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint

with open('Homework02_Task04.txt', 'w') as data:
    data.write('0\n')
    data.write('2\n')
    data.write('3\n')
    data.write('5\n')
    data.write('2\n')


def get_data_from_file():
    with open('Homework02_Task04.txt', 'r') as data:
        filelist = [int(line.strip()) for line in data]
    return filelist


def get_mult(lst, positionlist):
    mult = 1
    for i in positionlist:
        mult *= lst[i]
    return mult


def get_number():
    is_num = False
    while not is_num:
        try:
            num = int(input('Введите целое число: '))
            if num:
                is_num = True
        except ValueError:
            print('Не целое число\n')
    return abs(num)


def set_list(num):
    lst = []
    for i in range(-num, num + 1):
        lst.append(randint(-num, num))
    return lst


num = get_number()
lst = set_list(num)
filelist = get_data_from_file()

print(num)
print(lst)
print(f'positions: {filelist}')
print('multiplication:', get_mult(list, filelist))
