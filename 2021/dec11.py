input_file = open('input11.txt', 'r')
lines = input_file.readlines()


def get_neighbors(x, y):
    neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1),
                 (x - 1, y - 1), (x + 1, y + 1), (x - 1, y + 1), (x + 1, y - 1)]
    filteredNeighbors = []

    for n in neighbors:
        if n[0] >= 0 and n[0] < len(
                lines[0]) - 1 and n[1] >= 0 and n[1] < len(lines):
            filteredNeighbors.append(n)

    return filteredNeighbors


states = []
for line in lines:
    rows = []
    for char in line.rstrip():
        rows.append(int(char))
    states.append(rows)

numFlashes = 0
roundNum = 0
while True:
    roundNum += 1
    willFlash = set()
    hasFlashed = set()

    for y in range(0, len(states)):
        for x in range(0, len(states[0])):
            states[y][x] += 1
            if states[y][x] > 9:
                willFlash.add((x, y))

    while len(willFlash) > 0:
        x, y = willFlash.pop()
        hasFlashed.add((x, y))

        for n in get_neighbors(x, y):
            states[n[1]][n[0]] += 1
            if states[n[1]][n[0]] > 9 and n not in hasFlashed:
                willFlash.add(n)

    if len(hasFlashed) == len(states) * len(states[0]):
        print('--- Part Two ---')
        print(roundNum)
        break

    numFlashes += len(hasFlashed)

    for n in hasFlashed:
        states[n[1]][n[0]] = 0

    if roundNum == 100:
        print('--- Part One ---')
        print(numFlashes)
