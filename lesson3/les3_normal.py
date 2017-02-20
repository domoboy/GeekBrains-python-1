#lesson 3, normal

#1---------------------------

def fibonacci(n, m):
    '''
    возвращает ряд фибоначчи
    от n до m включительно
    '''
    fib = []
    a, b = 0, 1
    for num in range(m):
        fib.append(b)
        a, b = b, a+b
    n -= 1
    res = [fib[i] for i in range(n, m)]
    del fib
    print(res)
    return res

fibonacci(5, 10)

#2---------------------------

def sort_to_max(unsort_list):
    '''
    возвращает отсортированный список
    по увеличению
    '''
    def min_num(li):
        '''
        возвращает минимальноое число
        из списка
        '''
        min_elem = float('inf')
        for elem in li:
            if elem < min_elem:
                min_elem = elem
        return min_elem
    work_list = [x for x in unsort_list]
    sorted_list = []
    while len(work_list):
        for elem in work_list:
            if elem == min_num(work_list):
                sorted_list.append(elem)
                work_list.remove(elem)
    print('Список %s преобразован:\n%s'%(unsort_list, sorted_list))
    del work_list
    return sorted_list

sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

#3---------------------------

def alt_filter(func, itr):
    '''
    реализация функции filter
    '''
    new_itr = [elem for elem in itr if func(elem)]
    if type(itr) is tuple:
        new_itr = tuple(new_itr)
    if type(itr) is set:
        new_itr = set(new_itr)
    if type(itr) is str:
        new_itr = ''.join(new_itr)
    print(new_itr)
    return new_itr

alt_filter(lambda x: x > 5, {2, 10, -12, 2.5, 20, -11, 4, 4, 0})

#4---------------------------

import math

A1, A2, A3, A4 = (2, 3), (0, 2), (4, 1), (6, 2)

def isparall(a, b, c, d):
    '''
    Проверка признаков параллелограмма
    '''
    p1 = False
    p2 = False
    
   #Противополжные стороны параллельны и равны
    ab = math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
    cb = math.sqrt((b[0] - c[0])**2 + (b[1] - c[1])**2)
    cd = math.sqrt((d[0] - c[0])**2 + (d[1] - c[1])**2)
    ad = math.sqrt((d[0] - a[0])**2 + (d[1] - a[1])**2)
    if ab == cd and cb == ad:
        print('Равенство сторон: верно')
        p1 = True
    else:
        print('Противоположные стороны НЕ равны')
    
   #Диагонали O1 и O2 в точках пересечения делятся пополам и равны
    hO1 = ((a[0] + c[0])/2, (a[1] + c[1])/2)
    hO2 = ((b[0] + d[0])/2, (b[1] + d[1])/2)
    if hO1 == hO2:
        print('Равенство половин диагоналей: верно')
        p2 = True
    else:
        print('Половины диагоналей НЕ равны')

    if p1 and p2:
        print('Вершины A1%s, A2%s, A3%s, A4%s\nобразуют параллелограмм'%
          (a, b, c, d))
    else:
        print('Вершины не образуют параллелограмм')

isparall(A1, A2, A3, A4)




























