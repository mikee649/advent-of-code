input_file = open('input05.txt', 'r')
lines = input_file.readlines()

p1Counts = {}
p2Counts = {}

for line in lines:
    line = line.split(' -> ')
    line[0] = (int(line[0].split(',')[0]), int(line[0].split(',')[1]))
    line[1] = (int(line[1].split(',')[0]), int(line[1].split(',')[1]))

    if line[0][1] == line[1][1]:    # Horizontal
        startX = min(line[0][0], line[1][0])
        endX = max(line[0][0], line[1][0])
        for x in range(startX, endX+1):
            p1Counts[(x,line[0][1])] = p1Counts.get((x,line[0][1]), 0) + 1 
            p2Counts[(x,line[0][1])] = p2Counts.get((x,line[0][1]), 0) + 1 
    elif line[0][0] == line[1][0]:  # Vertical 
        startY = min(line[0][1], line[1][1])
        endY = max(line[0][1], line[1][1])
        for y in range(startY, endY+1):
            p1Counts[(line[0][0],y)] = p1Counts.get((line[0][0],y), 0) + 1
            p2Counts[(line[0][0],y)] = p2Counts.get((line[0][0],y), 0) + 1
    else:
        startX = min(line[0][0], line[1][0])
        endX = max(line[0][0], line[1][0])

        if startX == line[0][0]:
            y = line[0][1]
            incY = 1 if line[0][1] < line[1][1] else -1
        else:
            y = line[1][1]
            incY = 1 if line[1][1] < line[0][1] else -1

        for x in range(startX, endX+1):
            p2Counts[(x,y)] = p2Counts.get((x,y), 0) + 1 
            y += incY

print('--- Part One ---')
print(len(list(filter(lambda x: x > 1, p1Counts.values()))))

print('--- Part Two ---')
print(len(list(filter(lambda x: x > 1, p2Counts.values()))))
