# Solution using Loop


# def filter_list(l):
#     ints = []
#     for i in l:
#         if type(i) is int:
#             ints.append(i)
#     return ints

# Solution using List comprehension


def filter_list(l):
	return [i for i in l if type(i) is int]


print(filter_list([1,2,'a','b']))