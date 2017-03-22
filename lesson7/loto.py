# les7-1, Лото
import random


class Card_Generator:
    '''Генератор карточек -> массив из строк'''
    def __init__(self, N, line, n, empty, char):
        '''
        <N> всего цифр (по кол-ву бочёнков)
        <line> количество строк в карточке
        <n> количество цифр в строке
        <empty> количество пустых клеток в строке
        <char> символ пустой клетки
        '''
        self.N = [str(x) for x in range(1, N+1)]
        self.line = line
        self.n = n
        self.empty = empty
        self.char = char

        random.shuffle(self.N)

    def __iter__(self):
        return self

    def __next__(self):
        if self.line:
            line = []
            while len(set(line)) != self.n:
                line = [random.choice(self.N) for _ in range(self.n)]
            self.N = list(set(self.N) - set(line))
            lines = list(map(lambda x: ' ' + x if len(x) == 1 else x, line[:]))
            lines += [self.char] * self.empty
            random.shuffle(lines)
            self.line -= 1
            return lines
        else:
            raise StopIteration


class Card:
    '''Карточка игрока'''
    def __init__(self, title):
        self._title = title
        self._card = list(map(lambda x: x, Card_Generator(90, 3, 5, 4, '  ')))

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

print(gamer_card)
print(cpu_card)
