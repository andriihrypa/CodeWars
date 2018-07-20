# https://www.codewars.com/kata/find-the-middle-element


def gimme(input_array):
	sorted_list = sorted(input_array)[1]
	return input_array.index(sorted_list)


print(gimme([2, 3, 1]))