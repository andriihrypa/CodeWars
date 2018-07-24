def factorsRange(n, m):
    factors = {}
    for i in range(n, m+1):
        current_list_of_factors = []
        for j in range(2, i):
            if i % j == 0:
                current_list_of_factors.append(j)
        if not current_list_of_factors:
            current_list_of_factors = ["None"]
        factors[i] = current_list_of_factors
    return factors


print(factorsRange(2, 6))