# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def dif(lst: list):
    return (lst[1] - lst[0]) ** 2


coord1 = input('Введите координаты (x, y) первой точки через запятую: ')
coord2 = input('Введите координаты (x, y) второй точки через запятую: ')

lst_coord1 = list(map(float, coord1.split(',')))
lst_coord2 = list(map(float, coord2.split(',')))

list_x, list_y = list(zip(lst_coord1, lst_coord2))

print(round((dif(list_x) + dif(list_y)) ** .5, 2))
