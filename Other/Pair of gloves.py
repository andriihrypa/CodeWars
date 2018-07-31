def number_of_pairs(gloves):
	unique_glove_color = set(gloves)
	pairs = 0
	for color in unique_glove_color:
		if gloves.count(color) > 1:
			pairs += gloves.count(color) // 2
	return pairs


print(number_of_pairs(["red", "green", "red", "blue", "blue"]))
