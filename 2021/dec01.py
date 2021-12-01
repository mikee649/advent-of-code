input_file = open('input01.txt', 'r')
depths = list(map(lambda x: int(x), input_file.readlines()))

print('--- Part One ---')

prev = depths[0]
count = 0

for depth in depths[1:]:
    if depth > prev:
        count += 1
    prev = depth

print(count)

print('--- Part Two ---')

windowA = depths[0:3]
windowB = depths[1:4]

count = 1 if sum(windowA) < sum(windowB) else 0

for depth in depths[4:]:
    windowA.pop(0)
    windowA.append(windowB[2])

    windowB.pop(0)
    windowB.append(depth)

    if sum(windowA) < sum(windowB):
        count += 1

print(count)
