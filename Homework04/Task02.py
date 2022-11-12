# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N

def get_number():
    is_num = False
    while not is_num:
        try:
            num = int(input('Введите целое положительное число: '))
            if num:
                if num > 0:
                    is_num = True
                else:
                    print('Нужно ввести положительное число\n')
        except ValueError:
            print('Нужно ввести целое число\n')
    return num


def prime_numbers(num):
    first = 2
    lst = []
    while first <= num:
        if num % first == 0:
            lst.append(first)
            num //= first
            first = 2
        else:
            first += 1
    lst = lst if lst else None
    return lst


number = get_number()
print(f'Простые множители числа {number} - {prime_numbers(number)}')
