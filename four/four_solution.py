# part one
zone_pairs = []
counter = 0

with open('four_input') as file:
    for line in file:
        zone_pairs.append(line.strip('\n').split(','))


ws = []
for pair in zone_pairs:
    for section_range in pair:
        x = section_range.replace('-', ' ')
        x = x.split()
        ws.append(x[0])
        ws.append(x[1])
    if int(ws[0]) >= int(ws[2]) and int(ws[1]) <= int(ws[3]):
        counter += 1
        print(ws[0], ws[1], ws[2], ws[3], "cond 1")
    elif int(ws[0]) <= int(ws[2]) and int(ws[1]) >= int(ws[3]):
        counter += 1
        print(ws[0], ws[1], ws[2], ws[3], "cond 2")
    ws = []

print(counter)



# part two
