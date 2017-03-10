# Скрипт для удаления директории

import os

def del_dir(name_dir):
    cur_path = os.path.join(os.getcwd(), name_dir)
    try:
        os.rmdir(cur_path)
        print('Директория {} успешно удалена'.format(name_dir))
    except WindowsError:
        print('Не удаётся найти путь')
