# Лото-классы
import random
import config


class CardGenerator:
    '''Генератор карточек -> массив из строк'''
    def __init__(self, **kwargs):
        '''
        <N> всего цифр (по кол-ву бочонков)
        <line> количество строк в карточке
        <n> количество клеток в строке
        <empty> количество пустых клеток в строке
        <char> символ пустой клетки
        '''
        self.N = [_ for _ in range(1, kwargs['N']+1)]
        self.line = kwargs['line']
        self.n = kwargs['n']
        self.empty = kwargs['empty']
        self.char = kwargs['char']

    def __iter__(self):
        return self

    def __next__(self):
        if self.line:
            line = []
            while len(set(line)) != self.n:
                line = list(map(lambda x: ' ' + str(x) if len(str(x)) == 1 else
                                str(x), sorted([random.choice(self.N) for
                                                _ in range(self.n)])))
            self.N = list(set(self.N) - set([int(x) for x in line]))
            while line.count(self.char) != self.empty:
                rand_num = random.choice(line)
                line = list(map(lambda x: x.replace(rand_num, self.char),
                            line))
            self.line -= 1
            return line
        else:
            raise StopIteration


class BarrelGenerator:
    '''Генератор для бочонков'''
    def __init__(self, N=config.N):
        '''
        <N> количество бочонков
        '''
        try:
            self.N = [_ for _ in range(1, N+1)]
            self.barrel = None
        except TypeError:
            print('Не удаётся определить число бочонков в мешке')

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.N):
            self.barrel = random.choice(self.N)
            self.N = list(filter(lambda x: x != self.barrel, self.N))
            return self.barrel
        else:
            raise StopIteration
                    
        @property
        def length(self):
            return len(self.N)

        @property
        def current_number(self):
            return self.barrel

            
class Card:
    '''Карточка игрока'''
    def __init__(self, title):
        self._title = title
        try:
            self._card = list(map(lambda x: x,
                                  CardGenerator(N=config.N, line=config.line,
                                                n=config.n, empty=config.empty,
                                                char=config.char)))
        except TypeError:
            print('Ошибка в параметрах при создании "{}"'.format(self._title))

    def __str__(self):
        try:
            return '{:-^26}\n{}\n{:-^26}' \
                   ''.format(self._title, '\n' \
                             ''.join(list(map(lambda x: ' '.join(x),
                                                            self._card))), '-')
        except AttributeError:
            print('Cоздание карты невозможно!')

    def is_include(self, num):
        '''
        Проверка на совпадение номера
        '''
        return not len([line for line in self._card if
                       (lambda x: ' ' + str(x)
                        if len(str(x)) == 1 else str(x))(num) in line]) is 0

    def cross_out(self, num):
        '''
        Вычёркинвание совпавшего номера
        Возвращает объект
        '''
        self._card = [list(map(lambda x: x.replace(
                      (lambda x: ' ' + str(x) if len(str(x)) == 1 else
                       str(x))(num), ' -'), line)) for line in self._card[:]]
        return self
