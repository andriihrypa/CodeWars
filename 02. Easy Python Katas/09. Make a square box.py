# https://www.codewars.com/kata/make-a-square-box/train/python


def box(n):
    box = []
    box.append("-"*n)
    i = 0
    while i < (n -2):
        box.append("-" + " "*(n-2) + "-")
        i += 1
    box.append("-" * n)
    return box


print(box(5))