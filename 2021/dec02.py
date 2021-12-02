input_file = open('input02.txt', 'r')
directions = input_file.readlines()

print('--- Part One ---')

pos = [0,0]

for direction in directions:
    direction = direction.split(' ')

    if direction[0] == "forward":
        pos[0] += int(direction[1])
    elif direction[0] == "down":
        pos[1] += int(direction[1])
    elif direction[0] == "up":
        pos[1] -= int(direction[1])

print(pos[0]*pos[1])

print('--- Part Two ---')

pos = [0,0]
aim = 0

for direction in directions:
    direction = direction.split(' ')

    if direction[0] == "forward":
        pos[0] += int(direction[1])
        pos[1] += int(direction[1])*aim
    elif direction[0] == "down":
        aim += int(direction[1])
    elif direction[0] == "up":
        aim -= int(direction[1])

print(pos[0]*pos[1])
