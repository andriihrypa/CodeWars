# https://www.codewars.com/kata/alien-accent/train/python


def convert(st):
    st = st.replace("o", "u")
    st = st.replace("a", "o")
    return st


print(convert("codewars"))