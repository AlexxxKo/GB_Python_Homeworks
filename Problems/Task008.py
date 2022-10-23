# Дано число. Проверить, кратно ли оно 5 и 10 или 15, но не 30

def get_number():
    is_num = False
    while not is_num:
        try:
            num = int(input('Введите целое число: '))
            if num:
                is_num = True
        except ValueError:
            print('Нужно ввести целое число\n')
    return num

n = get_number()

if n % 10 == 0 or (n % 15 == 0 and n % 30 != 0):
    print(f'Число {n} кратно 5 и 10 или кратно 15, но не кратно 30')
else:
    print(f'Число {n} не удовлетворяет условиям')