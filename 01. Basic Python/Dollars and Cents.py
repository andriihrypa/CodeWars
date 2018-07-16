# https://www.codewars.com/kata/dollars-and-cents/train/python


def format_money(amount):
    return "${:.2f}".format(amount)


print(format_money(3))