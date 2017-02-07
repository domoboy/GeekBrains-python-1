#lesson2, hard

#1
import re

# y = kx - b
equation = 'y = -12x + 67'
x = 2.5

equation = equation.replace(' ', '')

k = (re.compile('[+-]*\d*x+').findall(equation))[0][:-1]
if not len(k): k = 1
elif k == '-': k = -1
else: k = int(k)

b = (re.compile('[+-]?\d*[^x]').findall(equation))
'''
y = k * x - b

print('{}\nпри x = {}\ny = {}'.format(equation, x, y))
'''
print(b)
