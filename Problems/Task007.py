# Найти наибольшее и наименьшее число из списка значений.

my_list = [1, 4, -1, 0, 8, -6, 3]

min = my_list[0]
max = my_list[0]

for i in my_list:
    if i > max:
        max = i
    elif i < min:
        min = i

print(f'В списке {my_list} минимальное число - {min}')
print(f'В списке {my_list} максимальное число - {max}')
