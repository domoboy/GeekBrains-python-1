# lesson6-2, easy

import math


class Trapeze:
    def __init__(self, a, b, c, d):
        '''
        Стороны трапеции
        '''
        try:
            self.AB = round(math.sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2), 2)
            self.BC = round(math.sqrt((c[0]-b[0])**2 + (c[1]-b[1])**2), 2)
            self.CD = round(math.sqrt((d[0]-c[0])**2 + (d[1]-c[1])**2), 2)
            self.DA = round(math.sqrt((a[0]-d[0])**2 + (a[1]-d[1])**2), 2)
        except TypeError:
            print('Параметры заданы неправильно')

    def isosceles(self):
        return self.AB == self.CD

    def perimeter(self):
        return round(self.AB + self.BC + self.CD + self.DA, 2)

    def area(self):
        if self.isosceles():
            h = math.sqrt(self.AB**2 - ((self.DA - self.BC)**2) / 4)
            return round(1/2 * (self.BC + self.DA) * h, 2)
        else:
            p = self.perimeter() / 2
            return round((self.BC + self.DA)/abs(self.DA - self.BC) *
                         math.sqrt((p-self.DA)*(p-self.BC)*(p-self.DA-self.AB)*
                                   (p-self.DA-self.CD)), 2)


trap = Trapeze((-4, 1), (-2, 3), (3, 3), (5, 2))

print('Трапеция с основаниями DA и BC\nявляется равнобокой: {0}\n' \
      'с Площадью {1} кв.см и Периметром {2} ' \
      'см'.format(trap.isosceles(), trap.area(), trap.perimeter()))

            
        
