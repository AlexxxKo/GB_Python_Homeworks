# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

def sum_fraction_part(lst):
    if len(lst) > 0:
        min = abs(lst[0]) % 1
        max = abs(lst[0]) % 1
        for i in range(1, len(lst)):
            fraction = abs(lst[i]) % 1
            if fraction < min:
                min = fraction
            if fraction > max:
                max = fraction
        return (max - min) * 100 // 1 / 100
    else:
        return 'List is null'


lst = [1.1, -1.2, 3.1, 5, 10.01]
print(sum_fraction_part(lst))
