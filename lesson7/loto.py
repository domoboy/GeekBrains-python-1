# les7-1, Лото
import random

# N, line, n, empty, char
class Card_Generator:
    '''Генератор карточек -> массив из строк'''
    def __init__(self, **kwargs):
        '''
        <N> всего цифр (по кол-ву бочёнков)
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
                line = list(map(lambda x: x.replace(rand_num, self.char), line))
            self.line -= 1
            return line
        else:
            raise StopIteration


class Barrel_Generator:
    '''Генератор для бочёнков'''
    def __init__(self, N):
        '''
        <N> количество бочёнков
        '''
        self.N = [_ for _ in range(1, N+1)]
        self.barrel = None

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
        self._card = list(map(lambda x: x, Card_Generator(N=90, line=3, n=9, empty=4, char='  ')))

    def __str__(self):
        return '{:-^26}\n{}\n{:-^26}' \
               ''.format(self._title, '\n'.join(list(map(lambda x: ' '.join(x),
                                                         self._card))), '-')

    def is_include(self, num):
        '''
        Проверка на совпадение номера
        '''
        return not len([line for line in self._card if str(num) in line]) is 0

    def cross_out(self, num):
        '''
        Вычёркинвание совпавшего номера
        Возвращает новый объект
        '''
        self._card = [list(map(lambda x: x.replace(str(num), ' -'), line)) for
                      line in self._card[:]]
        return self


gamer_card = Card(' Ваша карточка ')
cpu_card = Card(' Карточка компьютера ')
barrel = Barrel_Generator(90)

print(gamer_card)

print('\nНовый бочонок: {} (осталось {})\n'.format(next(barrel), barrel.length))
if gamer_card.is_include(barrel.current_number):
    gamer_card.cross_out(barrel.current_number)

print(gamer_card)

print('\nНовый бочонок: {} (осталось {})\n'.format(next(barrel), barrel.length))
if gamer_card.is_include(barrel.current_number):
    gamer_card.cross_out(barrel.current_number)

print(gamer_card)

print('\nНовый бочонок: {} (осталось {})\n'.format(next(barrel), barrel.length))
if gamer_card.is_include(barrel.current_number):
    gamer_card.cross_out(barrel.current_number)

print(gamer_card)

print('\nНовый бочонок: {} (осталось {})\n'.format(next(barrel), barrel.length))
if gamer_card.is_include(barrel.current_number):
    gamer_card.cross_out(barrel.current_number)

print(gamer_card)

