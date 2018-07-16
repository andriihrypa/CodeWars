# https://www.codewars.com/kata/a-function-within-a-function/train/python


def always(n=0):

    def return_n(n):
        print(n)

    return return_n(n)


three = always(5)
print(three)