def factorsRange(n, m):
    factors = {}
    temp = []
    for i in range(n, m+1):
        for j in range(2, i):
            if i % j == 0:
                temp.append(j)
        if not temp:
            temp = ["None"]
        factors[i] = temp
        temp = []
    return factors


print(factorsRange(2, 6))