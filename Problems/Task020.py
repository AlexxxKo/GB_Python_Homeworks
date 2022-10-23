# Дано число N. Заполните список длиной N  элементами 1, -3, 9, -27, 81, -243...
# N = 5 -> [1, -3, 9, -27, 81]

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


def fill_lst(n):
    lst = [0]*n
    for i in range(n):
        lst[i] = (-3)**i
    return lst


print(fill_lst(get_number()))
