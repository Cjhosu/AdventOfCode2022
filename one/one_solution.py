# part one
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

# part two

cal_list = []
max_cals = 0
second_most_cals = 0
third_most_cals = 0

with open('one_inputt ') as file:
    for line in file:
        if line  != '\n':
            cal_list.append(int(line.strip()))
            new_cals = sum(cal_list)
        else:
            cal_list = []
            if new_cals > max_cals:
                third_most_cals = second_most_cals
                second_most_cals = max_cals
                max_cals = new_cals
                print(max_cals)
                print(max_cals, second_most_cals, third_most_cals)
            elif new_cals > second_most_cals:
                third_most_cals = second_most_cals
                second_most_cals = new_cals
                print(second_most_cals)
                print(max_cals, second_most_cals, third_most_cals)
            elif new_cals > third_most_cals:
                third_most_cals = new_cals
                print(third_most_cals)
                print(max_cals, second_most_cals, third_most_cals)
            else:
                pass
            cal_list = []
if new_cals > max_cals:
    third_most_cals = second_most_cals
    second_most_cals = max_cals
    max_cals = new_cals
    print(max_cals)
    print(max_cals, second_most_cals, third_most_cals)
elif new_cals > second_most_cals:
    third_most_cals = second_most_cals
    second_most_cals = new_cals
    print(second_most_cals)
    print(max_cals, second_most_cals, third_most_cals)
elif new_cals > third_most_cals:
    third_most_cals = new_cals
    print(third_most_cals)
    print(max_cals, second_most_cals, third_most_cals)
else:
    pass

big_cals_list = [max_cals, second_most_cals, third_most_cals]

print(big_cals_list)

print(sum(big_cals_list))
