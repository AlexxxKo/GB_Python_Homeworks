# Задать список из N элементов, заполненных числами из промежутка [-N, N].
# Сдвинуть все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]

def fill_list(num):
    lst = []
    for i in range(-num, num + 1):
        lst.append(i)
    return lst


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


def shift_numbers_in_list(lst):
    last_index = len(lst) - 1
    i = 0
    while i < 2:
        num = lst[last_index]
        lst.pop(last_index)
        lst.insert(0, num)
        i = i + 1
    return lst


print(shift_numbers_in_list(fill_list(get_number())))
