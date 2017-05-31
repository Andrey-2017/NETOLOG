import os
import glob


def get_first_list():
    migrations = 'Migrations'
    files = glob.glob(os.path.join(migrations, '*.sql'))
    return files


def file_searching():
    files = get_first_list()
    while True:
        print('Введите фрагмент названия файла для поиска (для выхода из программы введите - ё):')
        name_fragm = input()
        if name_fragm == 'ё':
            break
        else:
            file_listing = list()
            for file in files:
                if name_fragm in file:
                    print(file)
                    file_listing.append(file)
            files = file_listing
            print('Всего файлов:', len(files))


file_searching()