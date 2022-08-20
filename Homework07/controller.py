from import_data import import_data
from export_data import export_data
from print_data import print_data
from search_data import search_data


def choice_todo():
    print('Что желаете сделать?\n\
      1 - импорт;\n\
      2 - экспорт;\n\
      3 - поиск контакта')
    is_corr_num = False
    while not is_corr_num:
        ch = input('Введите цифру: ')
        if ch == '1':
            is_corr_num = True
            sep = choice_sep()
            import_data(input_data(), sep)
        elif ch == '2':
            is_corr_num = True
            data = export_data()
            print_data(data)
        elif ch == '3':
            is_corr_num = True
            word = input('Введите данные для поиска: ')
            data = export_data()
            items = search_data(word, data)
            print_data(items, True)  # как вариант


def input_data():
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')

    is_num = False
    while not is_num:
        try:
            phone_number = input('Введите телефон (только цифры): ')
            if int(phone_number):
                is_num = True
        except ValueError:
            print('Неправильный ввод!')
    note = input('Введите примечание: ')
    return [last_name, first_name, phone_number, note]


def choice_sep():
    is_sep = False
    while not is_sep:
        sep = input('Введите разделитель (; или enter - пустая строка): ')
        if sep == '':
            sep = None
            is_sep = True
        elif sep == ';':
            is_sep = True
    return sep
