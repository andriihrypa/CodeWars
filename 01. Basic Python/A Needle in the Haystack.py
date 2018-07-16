# https://www.codewars.com/kata/56676e8fabd2d1ff3000000c


def find_needle(haystack):
    index = 0
    for i in haystack:
        if i == "needle":
            break
        index += 1
    return "found the needle at position {0}".format(index)


print(find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk']))