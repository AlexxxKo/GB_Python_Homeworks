# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

from random import randint


def get_number(text: str) -> int:
    is_num = False
    while not is_num:
        try:
            num = int(
                input(f'Введите натуральную степень {text} многочлена: '))
            if num:
                if num > 0:
                    is_num = True
                else:
                    print('Нужно ввести целое положительное число\n')
        except ValueError:
            print('Нужно ввести целое положительное число\n')
    return num


def get_random_list(num: int) -> list:
    rand_list = [randint(0, 101) for i in range(num + 1)]
    return rand_list


def get_str(num: int) -> str:
    b = ''
    rand_list = get_random_list(num)
    for i in range(num + 1):
        if rand_list[i] != 0:
            if i == 0:
                b = str(rand_list[i])
            elif i == 1:
                b = f'{rand_list[i]}x + {b}'
            else:
                b = f'{rand_list[i]}x^{i} + {b}'
    b += ' = 0'
    return b


def write_file(st: str, file_name: str):
    with open(file_name, 'w') as data:
        data.write(st)


def read_file(file_name: str) -> str:
    with open(file_name, 'r') as data:
        st = data.readline()
    return st


def set_terms_degrees(st: str) -> list:
    st_list = st.replace(' ', '').split('=')
    st_list = st_list[0].split('+')
    for i in range(len(st_list)):
        st_list[i] = st_list[i].split('x^')
        if len(st_list[i]) == 1:
            if (st_list[i][0][-1] == 'x'):
                st_list[i][0] = st_list[i][0][:-1]
                st_list[i].append('1')
            else:
                st_list[i].append('0')
    return st_list


def sum_terms(lst1: list, lst2: list) -> dict:
    lst1_max_degree = int(lst1[0][1])
    lst2_max_degree = (int(lst2[0][1]))
    if lst1_max_degree >= lst2_max_degree:
        max_degree = lst1_max_degree
    else:
        max_degree = lst2_max_degree

    dict_final = {}
    for i in range(max_degree, -1, -1):
        s = 0
        for j in lst1:
            if int(j[1]) == i:
                s += int(j[0])
                lst1.remove(j)
        for k in lst2:
            if int(k[1]) == i:
                s += int(k[0])
                lst2.remove(k)
        dict_final[i] = s
    return dict_final


def set_final_poly(dict_final: dict) -> str:
    st_poly = ''
    for i in range(len(dict_final)):
        if (i == 0 and dict_final[i]):
            st_poly = f'{dict_final[i]}'
        elif (i == 1 and dict_final[i]):
            st_poly = f'{dict_final[i]}x + ' + st_poly
        else:
            if (dict_final[i]):
                st_poly = f'{dict_final[i]}x^{i} + ' + st_poly
    st_poly += ' = 0'
    return st_poly


poly1 = get_str(get_number('первого'))
poly2 = get_str(get_number('второго'))
write_file(poly1, './Homework04_Task05_01.txt')
write_file(poly2, './Homework04_Task05_02.txt')
print(poly1)
print(poly2)

lst1 = set_terms_degrees(read_file('./Homework04_Task05_01.txt'))
lst2 = set_terms_degrees(read_file('./Homework04_Task05_02.txt'))

final_poly = set_final_poly(sum_terms(lst1, lst2))
write_file(final_poly, './Homework04_Task05_final.txt')
print(final_poly)
