# -*- coding: utf-8 -*-

import os
import sys
import shutil


def dir_list():
    '''
    Функция для вывода списка файлов в текущей директории
    '''
    cur_path = os.getcwd()
    list_dir = os.listdir(cur_path)
    print(list_dir)


def change_dir():
    '''
    Функция смены директории
    '''
    target = input('Введите название папки или символ "*"\n' \
                   'если хотите перейти в родительский каталог: ')
    if target == '*':
        to_dir = (os.getcwd().split('\\') if os.name == 'nt' else
                   os.getcwd().split('/'))
        to_dir.pop()
        to_dir = ('\\'.join(to_dir) if os.name == 'nt' else
                   '/'.join(to_dir))        
    else:
        to_dir = os.path.join(os.getcwd(), target)
    try:
        os.chdir(to_dir)
        print('Переход выполнен успешно')
    except WindowsError:
        print('Переход не возможен!')
    

def make_dir():
    '''
    Функция для создания директории
    '''
    name_dir = input('Введите название новой папки:\n')
    cur_path = os.path.join(os.getcwd(), name_dir)
    try:
        os.mkdir(cur_path)
        print('Директория {} успешно создана'.format(name_dir))
    except WindowsError:
        print('Папка с таким именем уже существует')


def del_dir():
    '''
    Функция для удаления директории
    '''
    name_dir = input('Введите название папки для удаления:\n')
    cur_path = os.path.join(os.getcwd(), name_dir)
    try:
        os.rmdir(cur_path)
        print('Директория {} успешно удалена'.format(name_dir))
    except WindowsError:
        print('Не удаётся найти путь')


def copy_file():
    '''
    Функция для копирования текущего файла
    '''
    file_name = sys.argv[0]
    while file_name in os.listdir(os.getcwd()):
        file_name = file_name.split('.py').pop(0) + '_copy.py'
    cur_file = os.path.join(os.getcwd(), sys.argv[0])
    new_file = os.path.join(os.getcwd(), file_name)
    try:
        shutil.copy(cur_file, new_file)
    except:
        print('Ошибка!')
