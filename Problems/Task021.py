# Найдите все положительные числа до 10000, у которых количество делителей равно 10.

def count_div(x):
    count = 0
    for i in range(1, x + 1):
        if x % i == 0:
            count += 1
    return count


def find_max_div():
    lst = []
    for i in range(1, 10001):
        if count_div(i) == 10:
            lst.append(i)
    return lst


print(find_max_div())
