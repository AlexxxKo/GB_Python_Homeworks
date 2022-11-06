# Вычислить число pi c заданной точностью d

def get_number():
    is_num = False
    while not is_num:
        try:
            num = int(input(
                'Введите точность числа pi (количество знаков после запятой). Максимум 14: '))
            if num and 0 < num < 15:
                is_num = True
        except ValueError:
            print('Нужно ввести целое положительное число\n')
    return num


def set_pi():
    # алгоритм Брента — Саламина
    a0 = 1
    b0 = 1 / (2 ** .5)
    t0 = 1 / 4
    p0 = 1
    for i in range(1000):
        a1 = (a0 + b0) / 2
        b1 = (a0 * b0) ** .5
        t1 = t0 - p0 * ((a0 - a1) ** 2)
        p1 = 2 * p0
        a0 = a1
        b0 = b1
        t0 = t1
        p0 = p1
    return (a0 + b0) ** 2 / (4 * t0)


print(f'{set_pi(): .{get_number()}f}')
