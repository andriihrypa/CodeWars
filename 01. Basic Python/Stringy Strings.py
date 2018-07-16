# https://www.codewars.com/kata/stringy-strings/train/python


def stringy(size):
    num = 1
    while len(str(num)) < size:
        num *= 10
        if len(str(num)) == size:
            return str(num)
        num = num*10 + 1
        if len(str(num)) == size:
            return str(num)
    return str(num)


print(stringy(1))