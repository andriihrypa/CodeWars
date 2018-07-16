# https://www.codewars.com/kata/reversing-words-in-a-string


def reverse(st):
    st = st.split(" ")
    st = reversed(st)
    st = " ".join(st)
    return st


print(reverse("Python Core"))