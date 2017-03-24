# Игра Лото
import loto_classes as loto

def game():
    '''
    Определяет основные переменные программы
    : player_card : Объект карты игрока
    : cpu_card : Объект карты компьютера
    : barrel : Генератор бочонков
    : player_count : Счётчик зачеркиваний карты игрока
    : cpu_count : Счётчик зачёркиваний карты компьютера
    '''
    player_card = loto.Card('Ваша карточка')
    cpu_card = loto.Card('Карточка компьютера')
    barrel = loto.BarrelGenerator()

    player_count = 0
    cpu_count = 0

    def print_field():
        '''
        Печать игрового поля
        '''
        nonlocal player_count, cpu_count, player_card, cpu_card, barrel
        if player_count == 15 and cpu_count == 15:
            print('Ничья!')
        if player_count == 15:
            print('Вы выиграли!')
        if cpu_count == 15:
            print('Вы проиграли!\nКомпьютер зачеркнул все цифры на своей карте')
        if player_count == 15 or cpu_count == 15:
            print('{0}\n{1}'.format(player_card, cpu_card))
            start(input('Ещё партию? (y/n) '))
            return

        try:
            field  = '\nНовый бочонок {0} (осталось {1})\n' \
                     '{2}\n{3}'.format(next(barrel), barrel.length,
                                       player_card, cpu_card)
            print(field)
        except TypeError:
            print('Не удаётся отобразить игровое поле')
            return
        except AttributeError:
            print('Ошибка при создании генератора бочонков')
            return
        

        def do_step():
            '''
            Обработка хода игрока и компьютера
            '''
            nonlocal player_count, cpu_count, player_card, cpu_card, barrel 

            user_answer = input('- Зачеркнуть цифру? (y/n) ')

            if cpu_card.is_include(barrel.current_number):
                cpu_card.cross_out(barrel.current_number)
                cpu_count += 1

            try:
                if user_answer is 'y':
                    if player_card.is_include(barrel.current_number):
                        player_card.cross_out(barrel.current_number)
                        player_count += 1
                        print_field()
                    else:
                        print('Вы проиграли! На Вашей карте нет числа '
                              '{}'.format(barrel.current_number))
                        start(input('Хотите начать заново? (y/n) '))
                        return
                elif user_answer is 'n':
                    if not player_card.is_include(barrel.current_number):
                        print_field()
                    else:
                        print('Вы проиграли! '
                              'Пропущено число ' \
                              '{}'.format(barrel.current_number))
                        start(input('Хотите начать заново? (y/n) '))
                        return
                else:
                    raise TypeError

            except TypeError:
                print('Введена неизвестная команда "{}"'.format(user_answer))
                user_answer = input('Для продолжения введите "y" ')
                if user_answer == 'y':
                    do_step()
                else:
                    return
        
        do_step()    
    
    print_field()

def start(user_answer='y'):
    '''
    Запускает основной код программы
    в зависимости от ответа игрока
    '''
    if user_answer == 'y':
        game()
    else:
        return

start(input('Добро пожаловать в "Лото"!\n- Начать игру? (y/n) '))
