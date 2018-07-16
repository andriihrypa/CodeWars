# https://www.codewars.com/kata/how-much-will-you-spend


def getTotal(costs, items, tax):
    value = 0
    j = 0
    for i in items:
        if i in costs:
            value += costs[i]
    value = value + value*tax
    value = round(value, 2)
    return value



costs = {'socks':5, 'shoes':60, 'sweater':30}
print(getTotal(costs, ['socks', 'shoes', 'shirt'], 0.09))