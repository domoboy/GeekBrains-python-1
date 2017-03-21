# lesson6-1, easy

from math import sqrt


class Side:
    @staticmethod
    def width(A, B):
        return round(sqrt(sum(tuple(map(lambda a, b: (b - a)**2,
                                             A, B)))), 2)


class Triangle(Side):
    def __init__(self, A, B, C):
        self._A = A
        self._B = B
        self._C = C

    def sides(self):
        return {'AB': self.width(self._A, self._B),
                'BC': self.width(self._B, self._C),
                'CA': self.width(self._C, self._A)
                }

    def perimeter(self):
        return round(self.sides()['AB'] +
                     self.sides()['BC'] +
                     self.sides()['CA'], 2)

    def area(self):
        return round((lambda pp, x, y, z:
                      sqrt(pp*(pp - x)*(pp - y)*(pp - z)))
                      (self.perimeter() / 2,
                       self.sides()['AB'],
                       self.sides()['BC'],
                       self.sides()['CA']), 2)

A1, A2, A3 = (2, -5),(-6, 2), (6, -2)

ABC = Triangle(A1, A2, A3)

print('В треугольнике со сторонами:')
print('см\n'.join([str(side) for side in ABC.sides().values()]) + 'cм')
print('Площадь: {}кв.см'.format(ABC.area()))
print('Периметр: {}см'.format(ABC.perimeter()))
