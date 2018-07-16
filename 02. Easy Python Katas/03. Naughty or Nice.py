def what_list_am_i_on(actions):
    naughty = 0
    nice = 0
    for i in actions:
        if i[0] == "b" or i[0] == "f" or i[0] == "k":
            naughty += 1
        elif i[0] == "g" or i[0] == "s" or i[0] == "n":
            nice += 1

    if nice > naughty:
        return "nice"
    else:
        return "naughty"


print(what_list_am_i_on(['broke a vending machine', 'never got into a fight', 'tied someone\'s shoes']))