# https://www.codewars.com/kata/noob-debug-1-fix-the-string-sum/train/python


def add(s1, s2):
    s1 = s1.encode()
    s2 = s2.encode()
    s1 = sum(s1)
    s2 = sum(s2) # here was a mistake. Instead of s2 there was s1
    return s1+s2


print(add("a", "b"))