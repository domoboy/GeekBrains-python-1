# lesson6-1, easy

import math


class Triangle:
    def __init__(self, a, b, c):
        '''
        Длины сторон треугольника
        '''
        try:
            self.AB = round(math.sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2), 2)
            self.BC = round(math.sqrt((c[0]-b[0])**2 + (c[1]-b[1])**2), 2)
            self.CA = round(math.sqrt((a[0]-c[0])**2 + (a[1]-c[1])**2), 2)
        except TypeError:
            print('Неверные параметры!')


    def perimetr(self):
        return round(self.AB + self.BC + self.CA, 2)


    def area(self):
        pp = self.perimetr() / 2
        S = math.sqrt(pp*(pp-self.AB)*(pp-self.BC)*(pp-self.CA))
        return round(S, 2)


    @property
    def getAB(self):
        return self.AB
    @property
    def getBC(self):
        return self.BC
    @property
    def getCA(self):
        return self.CA
    @property
    def getH(self):
        return 2*self.area() / self.CA
        

tri = Triangle((2, -5), (-6, 1), (6, -2))
print('В треугольнике со сторонами:\n' \
      'AB {}cm,\nBC {}cm,\nCA {}cm'.format(tri.getAB, tri.getBC, tri.getCA))
print('Периметр: {} cm'.format(tri.perimetr()))
print('Площадь: {} кв.cm'.format(tri.area()))
print('Высота: {} cm'.format(tri.getH))




    
