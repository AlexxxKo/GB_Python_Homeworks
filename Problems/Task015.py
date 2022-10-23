# Найти факториал числа.

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


fact = 1
number = get_number()
for i in range(1, number + 1):
    fact *= i

print(f'{number}! = {fact}')
