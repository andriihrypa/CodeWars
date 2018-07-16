# https://www.codewars.com/kata/554b4ac871d6813a03000035


def high_and_low(numbers):
    numbers_list = numbers.split(" ")

    low = int(numbers_list[0])
    high = int(numbers_list[0])

    index = 0
    for i in numbers_list:
        if int(numbers_list[index]) <= low:
            low = int(numbers_list[index])
        elif int(numbers_list[index]) > high:
            high = int(numbers_list[index])
        index += 1

    numbers = str(high) + " " + str(low)
    return numbers


print(high_and_low("1 9 3 4 -5"))