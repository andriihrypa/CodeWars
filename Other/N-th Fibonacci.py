def nth_fib(n):
    fib1 = 0
    fib2 = 1
    if n < 3:
        return n-1
    for i in range(3, n + 1):
        fib2, fib1 = fib1 + fib2, fib2
    return fib2


print(nth_fib(8))