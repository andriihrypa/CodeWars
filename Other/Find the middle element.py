# https://www.codewars.com/kata/find-the-middle-element


def gimme(input_array):
	s = sorted(input_array)
	return input_array.index(s[1])


print(gimme([2, 3, 1]))