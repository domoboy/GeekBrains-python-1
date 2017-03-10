# lesson5-1, easy
import os

def make_dir(name_dir):
    cur_path = os.path.join(os.getcwd(), name_dir)
    try:
        os.mkdir(cur_path)
        print('Директория {} успешно создана'.format(name_dir))
    except WindowsError:
        print('Папка с таким именем уже существует')

def del_dir(name_dir):
    cur_path = os.path.join(os.getcwd(), name_dir)
    try:
        os.rmdir(cur_path)
        print('Директория {} успешно удалена'.format(name_dir))
    except WindowsError:
        print('Не удаётся найти путь')

dirs = ['dir_' + str(n) for n in range(1, 10)]

for cur_dir in dirs:
     make_dir(cur_dir)

for cur_dir in dirs:
    del_dir(cur_dir)
