input_file = open('input21.txt', 'r')
lines = input_file.readlines()

scores = [0, 0]
positions = [int(lines[0].split(': ')[1]) - 1,
             int(lines[1].split(': ')[1]) - 1]

nextDieRoll = 1
rolls = 0

while max(scores) < 1000:
    for i in range(3):
        positions[rolls // 3 %
                  2] = (positions[rolls // 3 % 2] + nextDieRoll) % 10
        nextDieRoll = nextDieRoll % 100 + 1
        rolls += 1
    scores[(rolls // 3 - 1) % 2] += positions[(rolls // 3 - 1) % 2] + 1

print('--- Part One ---')
print(rolls * min(scores))
