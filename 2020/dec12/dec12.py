input_file = open('input.txt', 'r')
lines = input_file.readlines()

print('--- Part One ---')
directions = [[1, 0], [0, -1], [-1, 0], [0, 1]]
cur_dir = 0

pos = [0, 0]

for line in lines:
    val = int(line[1:])

    if line[0] == 'F':
        velocity = [i * val for i in directions[cur_dir]]
        pos = [pos[0] + velocity[0], pos[1] + velocity[1]]
    elif line[0] == 'R':
        cur_dir = (cur_dir + int(val/90)) % 4
    elif line[0] == 'L':
        cur_dir = (cur_dir - int(val/90)) % 4
    elif line[0] == 'N':
        pos[1] += val
    elif line[0] == 'E':
        pos[0] += val
    elif line[0] == 'S':
        pos[1] -= val
    elif line[0] == 'W':
        pos[0] -= val

print(abs(pos[0]) + abs(pos[1]))

print('--- Part Two ---')
waypoint = [10, 1]
pos = [0, 0]

for line in lines:
    val = int(line[1:])

    if line[0] == 'F':
        pos = [pos[0] + waypoint[0]*val, pos[1] + waypoint[1]*val]
    elif line[0] == 'R':
        for i in range(0, int(val/90)):
            waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]
    elif line[0] == 'L':
        for i in range(0, int(val/90)):
            waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]
    elif line[0] == 'N':
        waypoint[1] += val
    elif line[0] == 'E':
        waypoint[0] += val
    elif line[0] == 'S':
        waypoint[1] -= val
    elif line[0] == 'W':
        waypoint[0] -= val

print(abs(pos[0]) + abs(pos[1]))
