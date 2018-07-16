# https://www.codewars.com/kata/will-there-be-enough-space/train/python


def enough(cap, on, wait):
    if (cap - on - wait) >= 0:
        return 0
    return -1 * (cap - on - wait)


print(enough(40, 20, 23))