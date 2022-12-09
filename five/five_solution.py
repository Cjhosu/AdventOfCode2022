# part one
opening_list = []
stack_pos = []

with open('five_sample') as file:
    for line in file:
        if not line.startswith("move"):
            line = list(line)
            try:
                if line[1] == '1':
                    stack_pos = line
            except:
                pass

print(stack_pos)
number_of_stacks = int(stack_pos[len(stack_pos) - 3])

print(number_of_stacks)
with open('five_sample') as file:
    for line in file:
        if not line.startswith("move"):
            line = list(line)
            for i in range(1, len(line)):
                if line[i] != ' ' :
                    print(i, line[i])
