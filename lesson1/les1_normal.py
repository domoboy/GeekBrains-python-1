# lesson1, normal

#1
n = int(0)
num = str(input('Введите целое число: '))
for i in num:
  if (int(i))>n:
    n=int(i)
print(n)

#2
a = input('Введите a: ')
b = input('Введите b: ')
print('a = {0}, b = {1}'.format(b, a))

#3
import math
print('Дано квадратное уравнение:\nax**2 + bx + c')
a = float(input('Введите a: '))
b = float(input('Введите b: '))
c = float(input('Введите c: '))
D = b**2-4*a*c
if D>0:
    x1 = (-b + math.sqrt(D))/a*2
    x2 = (-b - math.sqrt(D))/a*2
    print('Корни уравнения:\n','x1 = ', x1, '\n x2 = ', x2)
elif D==0:
    print('Корень уравнения: ', x1)
else:
    print('Нет корней')
