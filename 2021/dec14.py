input_file = open('input14.txt', 'r')
lines = input_file.readlines()

polymer = lines[0].rstrip()

pairSwaps = {}

for line in lines[2:]:
    entry = line.rstrip().split(' -> ')
    pairSwaps[entry[0]] = entry[1]

pairsCount = {}
singlesCount = {polymer[-1]: 1}
for i in range(len(polymer) - 1):
    key = polymer[i] + polymer[i + 1]
    pairsCount[key] = pairsCount.get(key, 0) + 1
    singlesCount[polymer[i]] = singlesCount.get(polymer[i], 0) + 1

for i in range(40):
    pairsCountNew = pairsCount.copy()
    for pair, value in pairSwaps.items():
        pairsCountNew[pair] = pairsCountNew.get(
            pair, 0) - pairsCount.get(pair, 0)
        singlesCount[value] = singlesCount.get(
            value, 0) + pairsCount.get(pair, 0)
        pairsCountNew[pair[0] + value] = pairsCountNew.get(
            pair[0] + value, 0) + pairsCount.get(pair, 0)
        pairsCountNew[value + pair[1]
                      ] = pairsCountNew.get(value + pair[1], 0) + pairsCount.get(pair, 0)
    pairsCount = pairsCountNew

    if i == 9:
        print('--- Part One ---')
        print(max(singlesCount.values()) - min(singlesCount.values()))

print('--- Part Two ---')
print(max(singlesCount.values()) - min(singlesCount.values()))
