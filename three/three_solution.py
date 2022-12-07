# part one
packs = []
priorities = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f" : 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26 , "A": 27, "B": 28, "C": 29, "D": 30, "E": 31, "F" : 32, "G": 33, "H": 34, "I": 35, "J": 36, "K": 37, "L": 38, "M": 39, "N": 40, "O": 41, "P": 42, "Q": 43, "R": 44, "S":45, "T": 46, "U": 47, "V": 48, "W": 49, "X": 50, "Y": 51, "Z": 52}

priority_total = 0

with open('three_input') as file:
    for line in file:
        packs.append(line.strip('\n'))

for pack in packs:
    number_of_items = len(pack)
    first_comp = pack[:number_of_items//2]
    second_comp = pack[number_of_items//2:]
    common_item = set(first_comp) & set(second_comp)
    for i in common_item:
        priority_total += priorities[i]


print(priority_total)

# part two
priority_total = 0

for pack in range(0, len(packs), 3):
    elf_group = packs[pack:pack + 3]
    pack_one = elf_group[0]
    pack_two = elf_group[1]
    pack_three = elf_group[2]
    common_item = set(pack_one) & set(pack_two) & set(pack_three)
    for i in common_item:
        priority_total += priorities[i]

print(priority_total)

