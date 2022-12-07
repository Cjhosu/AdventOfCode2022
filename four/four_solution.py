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
    elif int(ws[0]) <= int(ws[2]) and int(ws[1]) >= int(ws[3]):
        counter += 1
    ws = []

print(counter)



# part two

ws = []
counter = 0
for pair in zone_pairs:
    for section_range in pair:
        x = section_range.replace('-', ' ')
        x = x.split()
        ws.append(x[0])
        ws.append(x[1])
    if int(ws[0]) in range(int(ws[2]), int(ws[3]) +1) or int(ws[1]) in range(int(ws[2]),int(ws[3])+1):
        counter += 1
    elif int(ws[2]) in range(int(ws[0]), int(ws[1]) +1) or int(ws[3]) in range(int(ws[0]),int(ws[1])+1):
        counter += 1
    ws = []

print(counter)
