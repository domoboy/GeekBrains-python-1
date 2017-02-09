#lesson2, hard


#1------------------------------
import re

equation = 'y = -12x + 11111140.2121'
x = 2.5

eq = equation.replace(' ', '')

foo = (re.compile('[+-]?\d*[.]?\d*x').findall(eq))[0][:-1]
if not len(foo):
    k = 1.0
elif foo == '-':
    k = -1.0
else:
    k = float(foo)

bar = (re.compile('[^y=]\d*[.]?\d*x?').findall(eq))
for value in bar:
    if value.find('x') == -1:
        b = float(value)

y = k * x + b

print('Прямая задана уравнением:\n{}\nпри x = {}\ny = {}'.format(equation, x, y))


#2------------------------------

#date = 'dd.mm.yyyy'

date = input('Введите дату в формате: dd.mm.yyyy\n')

days = {i+1 for i in range(31)}
months = {i+1 for i in range(12)}
years = {i+1 for i in range(9999)}

ERROR_FLAG = 0
ERROR_MSG_1 = 'Ошибка! Формат даты некорректен'
ERROR_MSG_2 = 'Ошибка! В {} \'{}\' неправильный ввод'
ERROR_MSG_3 = 'Ошибка! Такой даты не бывает'
ERROR_MSG_4 = 'Ошибка! В этом месяце нет 31-ого числа'
REQUIRES_MSG = '\nТребуемый формат: dd.mm.yyyy\nДень(01-31).Месяц(01-12).Год(0001-9999)'
CORRECTLY_MSG = 'Дата верна:'

d = date.split('.')
if len(d) == 3:
    d = {'day': d[0], 'month': d[1], 'year': d[2]}
    if (not len(d['day']) == 2 or
        not len(d['month']) == 2 or
        not len(d['year']) == 4):
            print('{}{}'.format(ERROR_MSG_1, REQUIRES_MSG))
            ERROR_FLAG = 1
else:
    print('{}{}'.format(ERROR_MSG_1, REQUIRES_MSG))
    ERROR_FLAG = 1

if isinstance(d, dict):
    for key, value in d.items():
        if not value.isdigit():
            ERROR_FLAG = 1
            print(ERROR_MSG_2.format(key, value), REQUIRES_MSG)
    if not ERROR_FLAG:
        day = int(d['day'])
        month = int(d['month'])
        year = int(d['year'])
        
        if not (day in days and
                month in months and
                year in years):
            print(ERROR_MSG_3, REQUIRES_MSG)
        elif (day == 31 and
              month in (2,4,6,9,11)):
            print(ERROR_MSG_4)
        else:
            print(CORRECTLY_MSG)

print(date)
days.clear()
months.clear()
years.clear()


#3------------------------------
