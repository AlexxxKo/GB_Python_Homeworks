# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности

lst = [3, 17, -13, 0, 17, 134, 97, -13, 0, 17, 153, 134]
new_lst = []
[new_lst.append(i) for i in lst if i not in new_lst]
print(f'Начальный список: {lst}\nПросеянный список: {new_lst}')