import os
import shutil


def dir_list():
    '''
    Скрипт для вывода списка файлов в текущей директории
    '''
    cur_path = os.getcwd()
    list_dir = os.listdir(cur_path)
    return list_dir


def make_dir(name_dir):
    '''
    Скрипт для создания директории
    '''
    cur_path = os.path.join(os.getcwd(), name_dir)
    try:
        os.mkdir(cur_path)
        print('Директория {} успешно создана'.format(name_dir))
    except WindowsError:
        print('Папка с таким именем уже существует')


def del_dir(name_dir):
    '''
    Скрипт для удаления директории
    '''
    cur_path = os.path.join(os.getcwd(), name_dir)
    try:
        os.rmdir(cur_path)
        print('Директория {} успешно удалена'.format(name_dir))
    except WindowsError:
        print('Не удаётся найти путь')

def copy_curfile(file_name):
    '''
    Скрипт для копирования текущего файла
    '''
    file_name_copy = file_name.split('.py').pop(0) + '_copy.py'
    cur_path_file = os.path.join(os.getcwd(), file_name)
    shutil.copy(cur_path_file, file_name_copy)

print(copy_curfile('dir_commands.py'))
