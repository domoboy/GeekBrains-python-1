#lesson5-1, hard

import os
import sys
import shutil
print('sys.argv = ', sys.argv)


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("cp <file_name> - создание копии файла")
    print("rm <file_name> - удаление файла")
    print("cd <full_path or relative_path> - изменеие директории")
    print("ls - отображение полного пути")
    print("ping - тестовый ключ")


def make_dir():
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def cp():
    if not dir_name:
        print("Необходимо указать имя копируемого файла вторым параметром")
        return
    c_file = dir_name
    count = 1
    while True:
        c_file = c_file.split('.py').pop(0) + '_copy' + str(count) + '.py'
        if c_file not in os.listdir(os.getcwd()):
            break
    cur_path_file = os.path.join(os.getcwd(), dir_name)
    copy_path_file = os.path.join(os.getcwd(), c_file)
    try:
        shutil.copy(cur_path_file, copy_path_file)
        print('файл {} успешно скопирован'.format(sys.argv[2]))
    except WindowsError:
        print('копирование невозможно!')


def ping():
    print("pong")

do = {
    "help": print_help,
    "mkdir": make_dir,
    "cp": cp,
    "ping": ping
}

try:
    dir_name = sys.argv[2]
except IndexError:
    dir_name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None


if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
