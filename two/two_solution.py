# part one
match_list = []
score_sheet = {"AX" : 4, "AY": 8, "AZ": 3, "BX": 1, "BY" : 5, "BZ" : 9, "CX" : 7, "CY": 2, "CZ": 6}
score = 0

with open('two_input') as file:
    for line in file:
        match_list.append(line.strip('\n'))

match_list = [ i.replace(' ','') for i in match_list]

for i in match_list:
    score += score_sheet[i]

print(score)

# part two

altered_score_sheet = {"AX" : 3, "AY": 4, "AZ": 8, "BX": 1, "BY" : 5, "BZ" : 9, "CX" : 2, "CY": 6, "CZ": 7}
score = 0

for i in match_list:
    score += altered_score_sheet[i]

print(score)
