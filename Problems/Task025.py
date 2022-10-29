# Написать программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
# N = 4 -> [ 1, 2, 6, 24 ]

def get_number():
    is_num = False
    while not is_num:
        try:
            num = int(input('Введите целое положительное число: '))
            if num & num > 0:
                is_num = True
            else:
                print('Число не положительное\n')
        except ValueError:
            print('Не целое число\n')
    return num


def fill_fact_list(n):
    lst = []
    for i in range(1, n + 1):
        lst.append(more_fact(i))

    return lst


def more_fact(num):
    if num == 1:
        return 1
    else:
        return num * more_fact(num - 1)


print(fill_fact_list(get_number()))
