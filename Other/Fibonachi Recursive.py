def nth_fib(n):
	if n < 3:
		return n-1
	else:
		return nth_fib(n - 1) + nth_fib(n - 2)


print(nth_fib(8))