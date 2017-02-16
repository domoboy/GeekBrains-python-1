#lesson 3, normal
'''
#1---------------------------

def fibonacci(n, m):
    
    возвращает ряд фибоначчи
    от n до m включительно
    
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
    
    возвращает отсортированный список
    по увеличению
    
    def min_num(li):
        
        возвращает минимальноое число
        из списка
        
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
'''
#3---------------------------

def alt_filter(func, itererable):
    itr = itererable
    for elem in itr:
        if not func(elem):
            itr.remove(elem)
    print(itr)
    print(itererable)
    return itr

alt_filter(lambda x: x > 5, [2, 10, -10, 8, 2, 0, 14])





























