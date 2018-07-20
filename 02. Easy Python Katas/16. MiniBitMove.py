def interpreter(tape, array):
    
    def flip(bit):
        return "0" if bit == "1" else "1"

    bits, index = list(array), 0
    while True:
        for i in tape:
            if i == "1":
                bits[index] = flip(bits[index])
            else:
                index += 1
                if index == len(array):
                    return "".join(bits)


print(interpreter('100', '1111111111'))