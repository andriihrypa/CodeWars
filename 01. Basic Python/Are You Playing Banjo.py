# https://www.codewars.com/kata/53af2b8861023f1d88000832

def areYouPlayingBanjo(name):
    if name[0] == "R" or name[0] == "r":
        name += " plays banjo"
    else:
        name += " does not play banjo"
    return name


john = "John"
rick = "Rick"
print(areYouPlayingBanjo(john))
