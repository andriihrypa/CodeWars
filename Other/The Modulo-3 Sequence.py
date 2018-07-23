def sequence(n):
	a = 0
	b = 1
	for i in range(2, n):
		b, a = (a+b)%3,



print(sequence(1))