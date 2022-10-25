# Задайте список из n чисел последовательности (1+1/n)^n
# и выведите на экран их сумму.

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


def get_list(n):
    list = []
    for i in range(1, n + 1):
        x = (1 + 1/i) ** i
        list.append(round(x, 10))
    return list


def sum_list(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    return round(sum, 10)


list = get_list(get_number())
print(list)
print(sum_list(list))
