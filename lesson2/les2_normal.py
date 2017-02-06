#lessson2, normal


#1
import math

example_list = [2, -5, 8, 9, -25, 25, 4]
new_list = []

for i in example_list:
    if i>0 and (math.sqrt(i) - int(math.sqrt(i))) == 0:
            new_list.append(int(math.sqrt(i)))

print(new_list)


#2
event_date = '03.11.1986'

days = [
    'первое',
    'второе',
    'третье',
    'четвертое',
    'пятое',
    'шестое',
    'седьмое',
    'восьмое',
    'девятое',
    'десятое',
    'одиннадцатое',
    'двенадцатое',
    'тринадцатое',
    'четырнадцатое',
    'пятнадцатое',
    'шестнадцатое',
    'семнадцатое',
    'восемнадцатое',
    'девятнадцотое',
    'двадцатое',
    'двадцать первое',
    'двадцать второе',
    'двадцать третье',
    'двадцать четвертое',
    'двадцать пятое',
    'двадцать шестое',
    'двадцать седьмое',
    'двадцать восьмое',
    'двадцать девятое',
    'тридцатое',
    'тридцать первое'
]
months = [
    'января',
    'февраля',
    'марта',
    'апреля',
    'мая',
    'июня',
    'июля',
    'августа',
    'сентября',
    'октября',
    'ноября',
    'декабря'
]

date_list = event_date.split('.')
day = days[int(date_list[0])-1]
month = months[int(date_list[1])-1]
year = int(date_list[2])

print('Формат даты: {} - изменён\nРезультат форматирования: {} {} {} года'.format(event_date, day, month, year))


#3
import random

n_elem = int(input('Введите количество элементов в списке:\n'))

list = []
while len(list) < n_elem:
    list.append(random.randint(-100, 100))

print(list)


#4
uniq = []

for i in list:
    if list.count(i) == 1:
        uniq.append(i)

print(uniq)
