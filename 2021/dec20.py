input_file = open('input20.txt', 'r')
lines = input_file.readlines()

enhanceAlg = lines[0].rstrip()

litSet = set()

for i, line in enumerate(lines[2:]):
    for j in range(len(line)):
        if line[j] == '#':
            litSet.add((j, i))


def is_lit(x, y, litSet, rectangle, iteration):
    binary = ''

    for yInc in range(-1, 2):
        for xInc in range(-1, 2):
            if x + xInc <= rectangle[0] or x + xInc >= rectangle[2] or y + \
                    yInc <= rectangle[1] or y + yInc >= rectangle[3]:
                binary += '0' if iteration % 2 == 0 else '1'
            elif (x + xInc, y + yInc) in litSet:
                binary += '1'
            else:
                binary += '0'

    return enhanceAlg[int(binary, 2)] == '#'


rectangle = (-1, -1, 100, 100)
for i in range(50):
    newLitSet = set()

    for y in range(rectangle[1], rectangle[3] + 1):
        for x in range(rectangle[0], rectangle[2] + 1):
            if is_lit(x, y, litSet, rectangle, i):
                newLitSet.add((x, y))

    litSet = newLitSet
    rectangle = (
        rectangle[0] - 1,
        rectangle[1] - 1,
        rectangle[2] + 1,
        rectangle[3] + 1)

    if i == 1:
        print('--- Part One ---')
        print(len(litSet))

print('--- Part Two ---')
print(len(litSet))
