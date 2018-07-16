# https://www.codewars.com/kata/5b043e3886d0752685000009

def pizza(cost):
    if cost <= 5:
        mike = round(cost, 2)
    elif cost > 5:
        kate = cost/3
        if kate <= 10:
            mike = round(cost - kate, 2)
        else:
            mike = round(cost - 10, 2)

    return mike


print(pizza(6))