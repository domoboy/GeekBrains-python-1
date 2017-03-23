# Игра Лото
import loto_classes as loto


def start_game():
    player_card = loto.Card('Ваша карточка')
    cpu_card = loto.Card('Карточка компьютера')
    barrel = loto.BarrelGenerator(90)

    def print_step():
        print('\nНовый бочонок {} (осталось {})\n'
              ''.format(next(barrel), barrel.length))
        print(player_card)
        print(cpu_card)
        print('Зачеркнуть цифру? (y/n)')

        user_answer = input()

        if user_answer is 'y':
            if player_card.is_include(barrel.current_number):
                cpu_card.cross_out(barrel.current_number)
                player_card.cross_out(barrel.current_number)
                print_step()
            else:
                print('Вы проиграли!')
                return
        elif user_answer is 'n':
            if not player_card.is_include(barrel.current_number):
                cpu_card.cross_out(barrel.current_number)
                print_step()
            else:
                print('Вы проиграли!')
                return

    print_step()


def menu():
    print('Добро пожаловать в игру Лото!\n'
          '1. Играть\n2. Выход')
    user_answer = int(input())
    if user_answer == 1:
        start_game()
    elif user_answer == 2:
        return

menu()
