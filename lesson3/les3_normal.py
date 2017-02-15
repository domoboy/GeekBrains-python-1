#lesson 3, normal

#1
def fibonacci(n, m):
    n -= 1
    fib = [1, 1]
    for i in range(m):
        fib.append(fib[len(fib)-1] + fib[len(fib)-2])
    res = [fib[i] for i in range(n, m)]
    del fib
    print(res)

fibonacci(3, 5)
        
