input_file = open('input09.txt', 'r')
lines = list(map(lambda line: line.rstrip(), input_file.readlines()))

def get_neighbors(x, y):
    neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    filteredNeighbors = []

    for n in neighbors:
        if n[0] >= 0 and n[0] < len(lines[0]) and n[1] >= 0 and n[1] < len(lines):
            filteredNeighbors.append(n)
        
    return filteredNeighbors

basins = {}
totalRisk = 0

for y in range(0, len(lines)):
    for x in range(0, len(lines[0])):
        neighbors = get_neighbors(x, y)

        isLow = True
        for n in neighbors:
            if lines[n[1]][n[0]] <= lines[y][x]:
                isLow = False
                break
        
        if isLow:
            totalRisk += int(lines[y][x]) + 1
            basins[(x,y)] = set()

print('--- Part One ---')
print(totalRisk)

def expand_basin(root, point):
    if point in basins[root] or lines[point[1]][point[0]] == '9':
        return
    
    basins[root].add(point)

    for n in get_neighbors(point[0], point[1]):
        if lines[n[1]][n[0]] >= lines[point[1]][point[0]]:
            expand_basin(root, n)

for point in basins.keys():
    expand_basin(point, point)

for x in range(0, len(lines[0])):
    for y in range(0, len(lines)):
        occursIn = []
        for basin in basins.keys():
            if (x,y) in basins[basin]:
                occursIn.append(basin)
        
        if len(occursIn) > 1:
            for basin in occursIn:
                basins[basin].remove((x,y))


sizes = list(map(lambda x: len(x), basins.values()))
sizes.sort()

print('--- Part Two ---')
print(sizes[-1]*sizes[-2]*sizes[-3])
