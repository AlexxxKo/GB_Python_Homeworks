# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# - [2, 3, 4, 5, 6] => [12, 15, 16]
# - [2, 3, 5, 6] => [12, 15]

# === var 1, For ===
# def sum_pair(lst: list) -> list:
#     sum_list = []
#     if len(lst) > 1:
#         last_index = len(lst) - 1
#         for i in range(len(lst) // 2 + 1):
#             if last_index - i > i:
#                 sum_list.append(lst[i] * lst[last_index - i])
#             elif last_index - i == i:
#                 sum_list.append(lst[i] ** 2)
#     else:
#         sum_list.append('List length < 2')

#     return sum_list

# === var 2. While ===
def sum_pair(lst: list) -> list:
    sum_list = []
    if len(lst) > 1:
        i = 0
        last_index = len(lst) - 1
        while last_index >= i:
            if last_index > i:
                sum_list.append(lst[i] * lst[last_index])
            elif last_index == i:
                sum_list.append(lst[i] ** 2)

            i += 1
            last_index -= 1
    else:
        sum_list.append('List length < 2')

    return sum_list


lst1 = [2, 3, 4, 5, 6]
lst2 = [2, 3, 5, 6]

print(sum_pair(lst1))
print(sum_pair(lst2))
