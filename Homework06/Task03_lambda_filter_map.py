# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.

def get_number():
    is_num = False
    while not is_num:
        try:
            num = float(input('Введите число: '))
            if num:
                is_num = True
        except ValueError:
            print('Нужно ввести число\n')
    return str(abs(num))


x = get_number()
sum_numbers = sum(map(int, filter(lambda i: i != '.', x)))
print(f'Сумма цифр числа {x} равна {sum_numbers}')
