# Организуйте последовательный ввод чисел до тех пор, пока не будет введён 0.
# Подсчитайте среди введённых чисел те, которые кратны трём.

count = 0
user_number = None

while user_number != 0:
    user_number = int(input('Введите число: '))
    if user_number % 3 == 0 and user_number != 0:
        count += 1

print(count)
