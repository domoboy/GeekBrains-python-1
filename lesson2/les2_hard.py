#lesson2, hard

#1
equation = 'y = -12x + 11111140.2121'
x = 2.5

eq = equation.replace('x', '*{}'.format(x))
#res = eq(eq.find('='))

print(eq[eq.find('=')+2:])
