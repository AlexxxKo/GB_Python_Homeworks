# Реализуйте алгоритм перемешивания списка

from random import randint

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('list', str(lst))

for i in range(len(lst)-1, 0, -1):
    j = randint(0, i + 1)
    lst[i], lst[j] = lst[j], lst[i]

print(str(lst))
