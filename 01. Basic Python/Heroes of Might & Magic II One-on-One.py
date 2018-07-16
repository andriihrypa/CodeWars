# https://www.codewars.com/kata/5b114e854de8651b6b000123


# Solution #1: Working but not valid for Code Wars due to Execution Timed Out ERROR
# _________________________________________________________________________________________


# def who_would_win(mon1, mon2):
#
#     hp1 = mon1["hitpoints"]
#     hp2 = mon2["hitpoints"]
#
#     def mon1_turn(mon1, mon2):
#         current_hp = mon2["hitpoints"]
#         damage = mon1["number"]*mon1["damage"]
#         total_hp = hp2 * (mon2["number"] -1) + current_hp
#         total_hp -= damage
#         if total_hp > 0:
#             if total_hp % hp2 == 0:
#                 mon2["number"] = int(total_hp/hp2)
#                 current_hp = hp2
#             else:
#                 mon2["number"] = total_hp//hp2 + 1
#                 current_hp = total_hp - total_hp//hp2 * hp2
#             mon2["hitpoints"] = current_hp
#         else:
#             mon2["number"] = 0
#         return mon2
#
#     def mon2_turn(mon1, mon2):
#         current_hp = mon1["hitpoints"]
#         damage = mon2["number"] * mon2["damage"]
#         total_hp = hp1 * (mon1["number"] - 1) + current_hp
#         total_hp -= damage
#         if total_hp > 0:
#             if total_hp % hp1 == 0:
#                 mon2["number"] = int(total_hp/hp1)
#                 current_hp = hp1
#             else:
#                 mon1["number"] = total_hp//hp1 + 1
#                 current_hp = total_hp - total_hp//hp1 * hp1
#             mon1["hitpoints"] = current_hp
#         else:
#             mon1["number"] = 0
#         return mon1
#
#     while True:
#         mon1_turn(mon1, mon2)
#         mon2_turn(mon1, mon2)
#         if mon1["number"] <= 0:
#             msg = str(mon2["number"]) + " " + mon2["type"] + "(s) won"
#             break
#         if mon2["number"] <= 0:
#             msg = str(mon1["number"]) + " " + mon1["type"] + "(s) won"
#             break
#
#     return msg


# Solution #2: Working and valid for Code Wars
# _________________________________________________________________________________________


def who_would_win(mon1, mon2):
    hp1 = mon1["hitpoints"] * mon1["number"]  # mo1 current total health
    hp2 = mon2["hitpoints"] * mon2["number"]  # mon2 current total health

    damage1 = mon1["number"] * mon1["damage"]  # mon1 current total damage
    damage2 = mon2["number"] * mon2["damage"]  # mon2 current total damage

    while hp1 > 0 and hp2 > 0:  # while loop until sombody wins

        # mon1 turn
        hp2 -= damage1
        if hp2 <= 0:
            mon2["number"] = 0
            mon1["number"] = int(hp1 / mon1["hitpoints"])
            if hp1 % mon1["hitpoints"] > 0:
                mon1["number"] += 1
            break
        damage2 = hp2 // mon2["hitpoints"] * mon2["damage"]
        if hp2 % mon2["hitpoints"] > 0:
            damage2 += mon2["damage"]

        # mon2 turn
        hp1 -= damage2
        if hp1 <= 0:
            mon1["number"] = 0
            mon2["number"] = int(hp2 / mon2["hitpoints"])
            if hp2 % mon2["hitpoints"] > 0:
                mon2["number"] += 1
            break
        damage1 = hp1 // mon1["hitpoints"] * mon1["damage"]
        if hp1 % mon1["hitpoints"] > 0:
            damage1 += mon1["damage"]

    if mon1["number"] > mon2["number"]:
        msg = str(mon1["number"]) + " " + mon1["type"] + "(s) won"
    else:
        msg = str(mon2["number"]) + " " + mon2["type"] + "(s) won"

    return msg



mon1 = {"type": "Paladin", "hitpoints": 50, "number": 8, "damage": 20}
mon2 = {"type": "Skeleton", "hitpoints": 4, "number": 100, "damage": 3}

# mon1 = {"type": "Titan", "hitpoints": 300, "number": 1, "damage": 50}
# mon2 = {"type": "Battle Dwarf", "hitpoints": 20, "number": 25, "damage": 4}
print(who_would_win(mon1, mon2))