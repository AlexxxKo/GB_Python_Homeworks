# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def rle_encode(data):
    encoding = ''
    prev_ch = ''
    count = 1

    if not data:
        return ''

    for ch in data:
        if ch != prev_ch:
            if prev_ch:
                encoding += str(count) + prev_ch
            count = 1
            prev_ch = ch
        else:
            count += 1
    else:
        encoding += str(count) + prev_ch
        return encoding


def rle_decode(data):
    decode = ''
    count = ''
    for ch in data:
        if ch.isdigit():
            count += ch
        else:
            decode += ch * int(count)
            count = ''
    return decode


def read_file(url):
    with open(url, encoding='utf-8') as file:
        return file.readline()


def write_file(url, st):
    with open(url, 'w', encoding='utf-8') as file:
        file.write(st)


write_file('Homework05_Task04_encode.txt', rle_encode(
    read_file('Homework05_Task04_start.txt')))

write_file('Homework05_Task04_decode.txt', rle_decode(
    read_file('Homework05_Task04_encode.txt')))
