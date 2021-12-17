input_file = open('input17.txt', 'r')
line = input_file.readlines()[0]

xRange = tuple(map(lambda x: int(x), line.split('x=')
               [1].split(',')[0].split('..')))
yRange = tuple(map(lambda x: int(x), line.split('y=')[1].split('..')))

print('--- Part One ---')
print((abs(yRange[0]) - 1) * abs(yRange[0]) // 2)

minXVelocity = 1
while True:
    finalPoint = (minXVelocity) * (1 + minXVelocity) // 2
    if finalPoint >= xRange[0]:
        break
    minXVelocity += 1

xInRangeAt = {}
xStoppedInRangeAt = {}

for initialVelocity in range(minXVelocity, xRange[1] + 1):
    vel = initialVelocity
    pos = 0
    step = 0
    while vel >= 0:
        pos += vel
        step += 1
        if pos >= xRange[0] and pos <= xRange[1]:
            if step not in xInRangeAt:
                xInRangeAt[step] = []
            xInRangeAt[step].append(initialVelocity)

        vel -= 1

        if vel == 0 and pos >= xRange[0] and pos <= xRange[1]:
            if step not in xStoppedInRangeAt:
                xStoppedInRangeAt[step] = []
            xStoppedInRangeAt[step].append(initialVelocity)

velComboCount = 0
for initialVelocity in range(yRange[0], -yRange[0]):
    vel = initialVelocity
    pos = 0
    step = 0
    matchedXVels = set()
    while pos >= yRange[0]:
        step += 1
        pos += vel
        if pos >= yRange[0] and pos <= yRange[1]:
            if step in xInRangeAt:
                for xVel in xInRangeAt[step]:
                    matchedXVels.add(xVel)
            for stoppedStep in xStoppedInRangeAt.keys():
                if stoppedStep <= step:
                    for xStoppedVel in xStoppedInRangeAt[stoppedStep]:
                        matchedXVels.add(xStoppedVel)
        vel -= 1

    velComboCount += len(matchedXVels)

print('--- Part Two ---')
print(velComboCount)
