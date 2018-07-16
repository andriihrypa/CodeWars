# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9


def find_short(s):
    list = s.split(" ")

    l = len(list[0])

    for i in list:
        if len(i) < l:
            l = len(i)

        i = + 1

    return l


print(find_short("Python is cool"))