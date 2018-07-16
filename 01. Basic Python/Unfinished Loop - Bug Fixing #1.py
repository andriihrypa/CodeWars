# https://www.codewars.com/kata/unfinished-loop-bug-fixing-number-1/train/python


def create_array(n):
    res = []
    i = 1
    while i <= n:
        res += [i]
        i += 1
    return res


print(create_array(5))