# Loto game for lesson7
import loto_classes


def get_obj_classes():
    '''
    Возвращает словарь из объектов
    '''
    gamer_card = loto_classes.CardGenerator('Ваша карта')
    cpu_card = loto_classes.CardGenerator('Карта компьютера')
    barrel = loto_classes.BarrelGenerator()
    return {
        'gamer': gamer_card,
        'cpu': cpu_card,
        'barrel': barrel
    }


def have_win(obj):
    '''
    Проверка на поедителя

    obj -- словарь содержащий карты игрока и компьтера,
           а также мешок с бочонками
    '''
    win = True

    if obj['gamer'].is_win() and obj['cpu'].is_win():
        print('\nНИЧЬЯ!')
    elif obj['gamer'].is_win() and not obj['cpu'].is_win():
        print('\nПОЗДРАВЛЯЕМ!\nВЫ ПОБЕДИЛИ!!!')
    elif obj['cpu'].is_win() and not obj['gamer'].is_win():
        print('\nВЫ ПРОИГРАЛИ!\nКомпьютер зачеркнул все цифры на своей карте')
    else:
        win = False

    return win


def print_step(obj):
    '''
    Печать игрового поля
    '''
    print('\nНовый бочонок {0} (осталось {1})\n'
          '{2}\n{3}'.format(obj['barrel'], obj['barrel'].length-1,
                            obj['gamer'], obj['cpu']))
    return obj


def control_step(obj):
    '''
    Проверка хода игрока
    '''
    try:
        gamer_answer = input('Зачеркнуть цифру? ')

        if obj['cpu'].is_include(obj['barrel'].current_number):
            obj['cpu'].cross_out(obj['barrel'].current_number)

        if gamer_answer == 'y':
            if obj['gamer'].is_include(obj['barrel'].current_number):
                obj['gamer'].cross_out(obj['barrel'].current_number)
                return True
            else:
                print('\nВЫ ПРОИГРАЛИ!\nЦифры '
                      '{} нет на Вашей карте'
                      ''.format(obj['barrel'].current_number))
                return False
        elif gamer_answer == 'n':
            if not obj['gamer'].is_include(obj['barrel'].current_number):
                return True
            else:
                print('\nВЫ ПРОИГРАЛИ!\nПропущена цифра '
                      '{}'.format(obj['barrel'].current_number))
                return False
        else:
            raise ValueError
    except ValueError:
        print('Введена неизвестная команда')
        gamer_answer = input('\nДля продолжения введите "y": ')
        if gamer_answer == 'y':
            return control_step(obj)
        else:
            print('Игра завершена...')
            return False


def do_step(obj):
    '''
    Организует структуру хода
    '''
    if have_win(obj):
        return False

    print_step(obj)

    if control_step(obj):
        return True


def start_game():
    '''
    Контролирует запуск игры, с нужным параметром obj
    '''
    obj = get_obj_classes()
    while True:
        if not do_step(obj) is True:
            user_answer = input('\nВведите "y", чтобы начать новую игру: ')
            if user_answer == 'y':
                obj = get_obj_classes()
            else:
                print('Выход из программы')
                break
            


def game_regulations():
    '''
    Печать справки из файла loto.txt 
    '''
    with open('loto.txt', encoding='UTF-8') as file:
        print('\n'.join([x.strip() for x in file]))
    user_answer = input('Введите "y" чтобы начать игру: ')
    if user_answer == 'y':
        start_game()
    else:
        print('Выход из программы')
        return


def menu():
    '''
    Меню программы
    Запускает выбранный пользователем пункт
    '''
    user_answer = input('Добро пожаловать в игру "ЛОТО"!\n'
                        '   1. Начать играть\n'
                        '   2. Напомнить правила\n'
                        'Введите "1" или "2" чтобы выбрать пункт: ')
    menu = {
        '1': start_game,
        '2': game_regulations
        }

    for key in menu:
        if user_answer == key:
            menu[key]()


menu()
