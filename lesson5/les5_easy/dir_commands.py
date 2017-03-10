import os

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
