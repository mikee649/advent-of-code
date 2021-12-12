input_file = open('input12.txt', 'r')
lines = input_file.readlines()

connections = {}
bigCaves = set()

visited = set()

for line in lines:
    caves = line.rstrip().split('-')

    connections[caves[0]] = connections.get(caves[0], set())
    connections[caves[1]] = connections.get(caves[1], set())

    if(caves[1]) != 'start':
        connections[caves[0]].add(caves[1])
    if(caves[0]) != 'start':
        connections[caves[1]].add(caves[0])

    if caves[0][0] < 'a':
        bigCaves.add(caves[0])
    if caves[1][0] < 'a':
        bigCaves.add(caves[1])


def search_paths(cave, doubled_cave):
    if cave == 'end':
        return 1

    if cave not in bigCaves:
        visited.add(cave)

    count = 0
    for neighbor in connections[cave]:
        if neighbor not in visited or neighbor in bigCaves:
            count += search_paths(neighbor, doubled_cave)
        elif doubled_cave is None:
            count += search_paths(neighbor, neighbor)

    if cave not in bigCaves and doubled_cave != cave:
        visited.remove(cave)

    return count


print('--- Part One ---')
print(search_paths('start', "don't double visit any caves"))
print('--- Part Two ---')
print(search_paths('start', None))
