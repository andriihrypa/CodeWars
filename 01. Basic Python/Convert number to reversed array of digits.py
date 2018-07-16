# https://www.codewars.com/kata/5583090cbe83f4fd8c000051


def digitize(n):
    lst = list(str(n))
    lst = list(reversed(lst))
    lst = list(map(int, lst))

    return lst


print(digitize(348597))