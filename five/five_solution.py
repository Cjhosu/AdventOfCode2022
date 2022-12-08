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

with open('five_sample') as file:
    for line in file:
