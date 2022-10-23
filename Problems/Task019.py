# Напишите программу, в которой пользователь будет задавать две строки, а программа -
# определять количество вхождений одной строки в другую.
# «qwe» «qwertyqwe» -> 2

def find_str_in_str(strBig: str, strSmall: str):
    countSubString = 0
    for i in range(len(strBig) - len(strSmall) + 1):
        if strBig[i:i+len(strSmall)] == strSmall:
            countSubString += 1
    return countSubString


strBig = input('Введите полную строку: ')
strSmall = input('Введите строку, которую нужно найти: ')

print(
    f'Строка "{strSmall}" входит в строку "{strBig}" {find_str_in_str(strBig, strSmall)} раза')
