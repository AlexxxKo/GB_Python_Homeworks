# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k

from random import randint


def get_number():
    is_num = False
    while not is_num:
        try:
            num = int(input('Введите натуральную степень k: '))
            if num:
                if num > 0:
                    is_num = True
                else:
                    print('Нужно ввести целое положительное число\n')
        except ValueError:
            print('Нужно ввести целое положительное число\n')
    return num


def get_random_list(num: int) -> list:
    rand_list = [randint(0, 101) for i in range(num + 1)]
    return rand_list


def get_str(num: int) -> str:
    b = ''
    rand_list = get_random_list(num)
    for i in range(num + 1):
        if rand_list[i] != 0:
            if i == 0:
                b = str(rand_list[i])
            elif i == 1:
                b = f'{rand_list[i]}x + {b}'
            else:
                b = f'{rand_list[i]}x^{i} + {b}'
    b += ' = 0'
    return b


def write_file(st: str):
    with open('./Homework04_Task04.txt', 'w') as data:
        data.write(st)


st = get_str(get_number())
write_file(st)
print(st)
