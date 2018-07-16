# https://www.codewars.com/kata/will-you-make-it/train/python


def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump > fuel_left * mpg:
        return False

    return True


print(zero_fuel(50, 25, 1))