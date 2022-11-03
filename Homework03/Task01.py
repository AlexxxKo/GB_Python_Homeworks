# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

def sum_list(lst):
    sum = 0
    for i in range(len(lst)):
        if i % 2:
            sum += lst[i]
    return sum


lst = [1, 2, 9, 15, 28, 17, 98]
print(sum_list(list))
