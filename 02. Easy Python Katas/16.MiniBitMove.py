# https://www.codewars.com/kata/esolang-minibitmove/train/python


def interpreter(tape, array):
    def flip(param):
        if param == "1":
            param = "0"
        else:
            param = "1"
        return param

    bits_new, y = list(array), 0
    while True:
        for i in tape:
            if i == "1":
                bits_new[y] = flip(bits_new[y])
            else:
                y += 1
                if y == len(array):
                    return "".join(bits_new)



print(interpreter('100', '1111111111'))