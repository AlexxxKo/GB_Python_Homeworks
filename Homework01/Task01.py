# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.

day_of_week = int(input('Введите номер дня недели: '))

if day_of_week in range(1, 6):
    print('Будний день')
elif day_of_week in range(6, 8):
    print('Выходной')
else:
    print('В неделе 7 дней')
