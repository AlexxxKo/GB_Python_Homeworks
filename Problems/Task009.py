# Дано число, обозначающее день недели. Вывести его название и указать, является ли он выходным

def get_number():
    is_num = False
    while not is_num:
        try:
            num = int(input('Введите номер дня недели: '))
            if num:
                is_num = True
        except ValueError:
            print('Нужно ввести целое число\n')
    return num


days = []
day = get_number()

if day == 1:
    print('Понедельник - будни')
if day == 2:
    print('Вторник - будни')
if day == 3:
    print('Среда - будни')
if day == 4:
    print('Четверг - будни')
if day == 5:
    print('Пятница - будни')
if day == 6:
    print('Суббота - выходной')
if day == 7:
    print('Воскресенье - выходной')
else:
    print('В неделе 7 дней')
