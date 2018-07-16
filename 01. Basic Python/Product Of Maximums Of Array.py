# https://www.codewars.com/kata/5a63948acadebff56f000018

def maxProduct(list, k):
    # sorting list of integers
    list.sort(reverse=True)

    # product of k greatest elements of the list
    product = 1
    for i in range(k):
        product *= list[i]

    return product


list = [2, 4, 9, 0, -4, 24, -1]
k = 3
print(maxProduct(list, k))