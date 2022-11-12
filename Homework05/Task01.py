# Напишите программу, удаляющую из текста все слова, содержащие "абв".

def read_file() -> list:
    with open('Homework05_Task01_start.txt', encoding='utf-8') as file:
        return file.readlines()


def find_substr(lst: list, letters: str) -> str:
    my_list = []
    for _ in lst:
        words = _.split()
        my_list.append(' '.join([i for i in words if letters not in i]))
    return '\n'.join(my_list)


def write_file(st: str):
    with open('Homework05_Task01_final.txt', 'w', encoding='utf-8') as file:
        file.writelines(st)


txt = 'лабва абав бва оабв\nкрабвь абвабва крыж'
print(txt, '\n')
txt_final = find_substr(txt.split('\n'), 'абв')
write_file(txt_final)
print(txt_final)


# Отрывок из "Война и мир". Ищем слова, не содержащие "на".

# write_file(find_substr(read_file(), 'на'))
