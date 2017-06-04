import os
import subprocess


def get_treatment():
    first_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Source')
    os.mkdir(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Result'))
    final_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Result')
    input_list = [os.path.join(os.path.abspath(os.path.dirname(__file__)), 'convert.exe'), '', '-resize', '200', '']
    for name in os.listdir(first_dir):
        input_list[1] = os.path.join(first_dir, name)
        input_list[-1] = os.path.join(final_dir, name)
        subprocess.run(input_list)
    print('Файлы обработаны! Программа закончила работу.')


def del_directory():
    name_directory = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Result')
    for file_name in os.listdir(name_directory):
        os.remove(os.path.join(name_directory, file_name))
    os.rmdir(name_directory)


def pic_work():
    if os.path.exists(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Result')):
        del_directory()
    get_treatment()


pic_work()