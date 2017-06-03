import os
import glob


def get_first_list():
    migrations = 'Migrations'
    files = glob.glob(os.path.join(migrations, '*.sql'))
    return files


def file_searching():
    files = get_first_list()
    while True:
        print('Введите фрагмент строки из файла для поиска (для выхода из программы введите - ё):')
        string_fragm = input()
        if string_fragm == 'ё':
            break
        file_listing = list()
        for file_name in files:
            with open(file_name) as f:
                search_string = f.read()
            if string_fragm in search_string:
                print(file_name)
                file_listing.append(file_name)
        files = file_listing
        print('Всего файлов: {0:d}'.format(len(files)))


file_searching()