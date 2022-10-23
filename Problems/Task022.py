# Для натурального n создать словарь индекс-значение,
# состоящий из элементов последовательности 3n + 1
# n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

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


def set_dict(num):
    dic = {}
    for i in range(1, num + 1):
        dic[i] = 3 * i + 1
    return dic


print(set_dict(get_number()))
