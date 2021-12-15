from sortedcontainers import SortedList, SortedSet, SortedDict

input_file = open('input15.txt', 'r')
lines = list(map(lambda line: line.rstrip(), input_file.readlines()))


def get_neighbors(x, y, mapMultiplyer):
    neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    filteredNeighbors = []

    for n in neighbors:
        if n[0] >= 0 and n[0] < len(
                lines[0]) * mapMultiplyer and n[1] >= 0 and n[1] < len(lines) * mapMultiplyer:
            filteredNeighbors.append(n)

    return filteredNeighbors


def value_at(x, y):
    val = (int(lines[y % len(lines)][x % len(lines[0])]) +
           y // len(lines) + x // len(lines[0]))

    if val >= 10:
        val = val % 10 + 1

    return val if val < 10 else 1


def run_dijkstra(mapMultiplyer):
    visited = set()
    distanceFromStart = {}
    upNext = SortedDict({0: [(0, 0)]})

    for y in range(len(lines) * mapMultiplyer):
        for x in range(len(lines[0]) * mapMultiplyer):
            distanceFromStart[(x, y)] = float("inf")

    distanceFromStart[(0, 0)] = 0

    while (len(lines[0]) * mapMultiplyer - 1,
           len(lines) * mapMultiplyer - 1) not in visited:
        node = upNext[upNext.keys()[0]].pop()
        if upNext[upNext.keys()[0]] == []:
            upNext.pop(upNext.keys()[0])

        for neighbor in get_neighbors(node[0], node[1], mapMultiplyer):
            if value_at(node[0], node[1]) + \
                    distanceFromStart[node] < distanceFromStart[neighbor]:
                if distanceFromStart[neighbor] in upNext:
                    upNext[distanceFromStart[neighbor]].remove(neighbor)
                    if upNext[distanceFromStart[neighbor]] == []:
                        upNext.pop(distanceFromStart[neighbor])

                newDistance = value_at(
                    node[0], node[1]) + distanceFromStart[node]
                upNext[newDistance] = upNext.get(newDistance, []) + [neighbor]
                distanceFromStart[neighbor] = newDistance

        visited.add(node)

    return distanceFromStart[(
        len(lines[0]) * mapMultiplyer - 1, len(lines) * mapMultiplyer - 1)]


print('--- Part One ---')
print(run_dijkstra(1) - value_at(0, 0) +
      value_at(len(lines[0]) - 1, len(lines) - 1))
print('--- Part Two ---')
print(run_dijkstra(5) - value_at(0, 0) +
      value_at(len(lines[0]) * 5 - 1, len(lines) * 5 - 1))
