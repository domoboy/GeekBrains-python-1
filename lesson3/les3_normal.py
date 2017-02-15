#lesson 3, normal

#1---------------------------
'''
def fibonacci(n, m):
    n -= 1
    fib = [1, 1]
    for i in range(m):
        fib.append(fib[len(fib)-1] + fib[len(fib)-2])
    res = [fib[i] for i in range(n, m)]
    del fib
    print(res)

fibonacci(2, 10)
'''
#2---------------------------

def sort_to_max(li):
    min_elem = float('inf')
    sort_list = []
        for i in li:
            if i < min_elem:
                min_elem = i
                sort_list.append(i)
                li.remove(i)
    print(sort_list)
    
sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])
