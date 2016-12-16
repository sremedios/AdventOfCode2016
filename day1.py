with open("day1_input.txt") as f:
    directions = f.read().split(", ")

path = {'N':0,'E':0,'S':0,'W':0}
state = 'N'

for i in directions:
    if i[0] == 'R':
        if state == 'N': state = 'E'
        elif state == 'E': state = 'S'
        elif state == 'S': state = 'W'
        elif state == 'W': state = 'N'
    else:
        if state == 'N': state = 'W'
        elif state == 'W': state = 'S'
        elif state == 'S': state = 'E'
        elif state == 'E': state = 'N'
    path[state] += int(i[1:])

print(abs(path['N']-path['S'])+abs(path['E']-path['W']))
