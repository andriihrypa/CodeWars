def sequence(n):
	num1 = 0
	num2 = 1
	if n < 3:
		return n - 1
	n = (n - 2) % 8
	for num in range(n):
		num2, num1 = (num1 + num2) % 3, num2
	return num2


print(sequence(4))