# https://www.codewars.com/kata/list-filtering/train/python


def filter_list(l):
    ints = []
    for i in l:
        if type(i) is int:
            ints.append(i)
    return ints


print(filter_list([1,2,'a','b']))