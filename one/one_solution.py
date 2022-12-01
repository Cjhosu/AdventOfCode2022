cal_list = []
max_cals = 0

with open('one_input') as file:
    for line in file:
        if line  != '\n':
            cal_list.append(int(line.strip()))
        else:
            cal_list = []
        new_cals = sum(cal_list)
        if new_cals > max_cals:
            max_cals = new_cals

print(max_cals)


