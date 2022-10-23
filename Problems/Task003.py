# Найти максимальное из пяти чисел

def get_number(i):
    is_num = False
    while not is_num:
        try:
            num = float(input(f'Введите число a{i}: '))
            if num:
                is_num = True
        except ValueError:
            print('Вы ввели не число\n')
    return num


for i in range(1, 6):
    a = get_number(i)
    if i == 1:
        max_number = a
    elif max_number < a:
        max_number = a
print(f'Максимальное число {max_number}')
