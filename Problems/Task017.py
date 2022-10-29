# Дано число N. Найти все его делители.
# Для каждого делителя указать, чётный он или нечётный.
# 10 -> 10 (чётный), 5(нечётный), 2 (чётный), 1(нечётный)

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


def findDividers(x):
    result = []
    for i in range(x, 0, -1):
        if x % i == 0:
            result.append(i)
    return result


def checkEvenNumber(x):
    if x % 2 == 0:
        even = f'(чётный){addComma(x)}'
        return (even)
    else:
        even = f'(нечётный){addComma(x)}'
        return (even)


def addComma(x):
    if x != 1:
        return ','
    else:
        return ''


dividers = findDividers(get_number())

for i in dividers:
    print(i, checkEvenNumber(i), end=' ')
