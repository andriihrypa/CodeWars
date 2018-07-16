# https://www.codewars.com/kata/sum-arrays/train/python


def sum_array(a):
    if len(a) > 0:
        return sum(a)
    return 0

print(sum_array([1, 7, 8, 45, 96]))