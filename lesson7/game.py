# game
import loto_classes


def get_obj_classes():
    gamer_card = loto_classes.CardGenerator('Ваша карта')
    cpu_card = loto_classes.CardGenerator('Карта компьютера')
    barrel = loto_classes.BarrelGenerator()
    return {
        'gamer': gamer_card,
        'cpu': cpu_card,
        'barrel': barrel
    }


def have_win(obj):
    win = False

    if obj['gamer'].is_win() and obj['cpu'].is_win():
        print('НИЧЬЯ!')
        return True
    if obj['gamer'].is_win() and not obj['cpu'].is_win():
        print('ВЫ ПОБЕДИЛИ!')
        return True
    if obj['cpu'].is_win() and not obj['gamer'].is_win():
        print('ВЫ ПРОИГРАЛИ!\n Компьютер зачеркнул все цифры на своей карте')
        return True

    return win


def print_step(obj):
    print('\nНовый бочонок {0} (осталось {1})\n'
          '{2}\n{3}'.format(obj['barrel'], obj['barrel'].length-1,
                            obj['gamer'], obj['cpu']))
    return obj


def control_step(obj):
    try:
        gamer_unswer = input('Зачеркнуть цифру? ')

        if obj['cpu'].is_include(obj['barrel'].current_number):
            obj['cpu'].cross_out(obj['barrel'].current_number)

        if gamer_unswer == 'y':
            if obj['gamer'].is_include(obj['barrel'].current_number):
                obj['gamer'].cross_out(obj['barrel'].current_number)
                return True
            else:
                print('ВЫ ПРОИГРАЛИ!\nЦифры '
                      '{} нет на Вашей карте'
                      ''.format(obj['barrel'].current_number))
                return False
        elif gamer_unswer == 'n':
            if not obj['gamer'].is_include(obj['barrel'].current_number):
                return True
            else:
                print('ВЫ ПРОИГРАЛИ!\nПропущена цифра '
                      '{}'.format(obj['barrel'].current_number))
                return False
        else:
            raise ValueError
    except ValueError:
        print('Введена неизвестная команда')
        gamer_unswer = input('Для продолжения введите "y" ')
        if gamer_unswer == 'y':
            return control_step(obj)
        else:
            return False


def do_step(obj=get_obj_classes()):

    if have_win(obj):
        return

    print_step(obj)

    if control_step(obj):
        return True


def start_game():
    while True:
        if not do_step() is True:
            break

start_game()
