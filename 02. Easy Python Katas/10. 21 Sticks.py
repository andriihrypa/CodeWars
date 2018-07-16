# https://www.codewars.com/kata/21-sticks/train/python


def makeMove(sticks):
    if sticks < 4:
        return sticks
    else:
        if sticks % 4 == 0:
            return 1
        return sticks % 4


print(makeMove(21))