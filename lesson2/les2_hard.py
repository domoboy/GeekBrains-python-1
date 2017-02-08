#lesson2, hard

#1
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
