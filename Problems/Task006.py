# Написать программу, которая принимает на вход дробь
# и показывает первую цифру дробной части числа.
# 6,78 -> 7, 5 -> нет, 0,34 -> 3

def get_number():
    is_num = False
    while not is_num:
        try:
            num = float(input('Введите число: '))
            if num:
                is_num = True
        except ValueError:
            print('Нужно ввести число\n')
    return abs(num)


n = get_number()

if n % 1 > 0:
    print(f'Первая цифра дробной части числа {n} равна {int(n * 10 % 10)}')
else:
    print('Число целое')
