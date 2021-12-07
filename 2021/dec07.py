input_file = open('input07.txt', 'r')
positions = list(map(lambda x: int(x),input_file.readlines()[0].split(',')))

dist1 = {}
dist2 = {}

sum

for pos1 in range(min(positions), max(positions)+1):
    if pos1 in dist1:
        continue
    for pos2 in positions:
        dist1[pos1] = dist1.get(pos1, 0) + abs(pos1-pos2)
        dist2[pos1] = dist2.get(pos1, 0) + int(abs(pos1-pos2)/2 * (1+abs(pos1-pos2)))

print('--- Part One ---')
print(min(dist1.values()))

print('--- Part Two ---')
print(min(dist2.values()))
