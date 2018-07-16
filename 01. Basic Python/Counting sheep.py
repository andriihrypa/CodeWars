# https://www.codewars.com/kata/54edbc7200b811e956000556


def count_sheeps(arrayOfSheeps):
    return arrayOfSheeps.count(True)


lst = [True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]

print(count_sheeps(lst))