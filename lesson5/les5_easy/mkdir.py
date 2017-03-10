# Скрипт для создания директории

import os

def make_dir(name_dir):
    cur_path = os.path.join(os.getcwd(), name_dir)
    try:
        os.mkdir(cur_path)
        print('Директория {} успешно создана'.format(name_dir))
    except WindowsError:
        print('Папка с таким именем уже существует')
