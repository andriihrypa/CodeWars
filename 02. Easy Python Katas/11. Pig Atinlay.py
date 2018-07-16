# https://www.codewars.com/kata/pig-atinlay/train/python


def pig_latin(word):
    if len(word) > 3:
        return word[1:] + word[0] + "ay"
    return word


print(pig_latin("hello"))