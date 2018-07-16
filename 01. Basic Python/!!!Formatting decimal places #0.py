# https://www.codewars.com/kata/formatting-decimal-places-number-0/train/python

from decimal import Decimal
def two_decimal_places(n):
    n = Decimal(n)
    return round(n, 2)


print(two_decimal_places(2.6750))