# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def get_number():
    is_num = False
    while not is_num:
        try:
            num = int(input('Введите целое положительное число: '))
            if num > 0:
                is_num = True
            else:
                print('Число не положительное\n')
        except ValueError:
            print('Не целое число\n')
    return num


def negafib_fib(num):
    lst = []
    a, b = 1, 1
    for i in range(num):
        lst.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range(num + 1):
        lst.insert(0, a)
        a, b = b, a - b
    return lst


number = get_number()
print(number)
print(negafib_fib(number))
