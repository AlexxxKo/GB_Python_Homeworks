# Вывести таблицу истинности для выражения ¬X ∨ Y.

def injunction():
    for x in 0, 1:
        for y in 0, 1:
            print(x, y, f'   {int(not x or y)}  ')


print('x', 'y', '¬X ∨ Y')
injunction()
