def solve(arr):
	list_of_sets = ["".join(set(i)) for i in arr]
	set_of_sets = set(list_of_sets)
	list_of_index_sum = []
	for i in set_of_sets:
		if list_of_sets.count(i) > 1:
			list_of_index_sum.append(sum([j for j in range(len(list_of_sets)) if list_of_sets[j] == i]))
	return sorted(list_of_index_sum)


print(solve(["abc", "abbc", "ab", "xyz", "xy", "zzyx"]))
