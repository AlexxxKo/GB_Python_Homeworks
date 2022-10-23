# Напишите программу, которая принимает на вход число (N),
# а на выходе показывает все чётные числа от 1 до N.
# 5 -> 2, 4
# 8 -> 2, 4, 6, 8

def get_number():
    is_num = False
    while not is_num:
        try:
            num = int(input('Введите целое положительное число: '))
            if num and num > 0:
                is_num = True
        except ValueError:
            print('Нужно ввести целое число\n')
    return num


number = get_number()

for i in range(1, number + 1):
    if i % 2 == 0:
        print(i, end=' ')
