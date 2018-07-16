# https://www.codewars.com/kata/5412509bd436bd33920011bc


def maskify(cc):
    if cc == "" or len(cc) < 5:
        return cc
    else:
        mask = list(cc)
        for i in range(len(mask)-4):
            mask[i] = "#"
    cc = "".join(mask)
    return cc


print(maskify("4556364607935616"))