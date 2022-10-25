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
    return abs(num)


def set_int(number):
    number = str(number)
    num = ''
    for i in number:
        if i != '.':
            num += i
    return int(num)


def sum_digit(number):
    sum = 0
    while number != 0:
        sum += number % 10
        number //= 10
    return sum


x = get_number()
print(f'{x} - число')
sum = sum_digit(set_int(x))
print(f'{sum} - сумма цифр')
